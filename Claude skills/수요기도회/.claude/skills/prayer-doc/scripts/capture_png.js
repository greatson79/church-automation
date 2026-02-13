#!/usr/bin/env node
/**
 * 디딤수요기도회 기도제목 HTML → PNG 캡처
 * Puppeteer를 사용하여 A4 사이즈 HTML을 PNG로 캡처한다.
 * 
 * Usage: node capture_png.js <input.html> <output.png> [--high-res]
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function captureHtmlToPng(inputHtml, outputPng, highRes = false) {
    const htmlPath = path.resolve(inputHtml);
    const pngPath = path.resolve(outputPng);
    
    if (!fs.existsSync(htmlPath)) {
        console.error(`HTML 파일을 찾을 수 없습니다: ${htmlPath}`);
        process.exit(1);
    }
    
    // A4 사이즈 (mm → px)
    // 96 DPI: 210mm = 794px, 297mm = 1123px
    // 192 DPI (고해상도): 1587px × 2245px
    const scale = highRes ? 2 : 1;
    const width = 794;
    const height = 1123;
    
    const browser = await puppeteer.launch({
        headless: 'new',
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--font-render-hinting=none',
        ],
    });
    
    try {
        const page = await browser.newPage();
        
        await page.setViewport({
            width: width,
            height: height,
            deviceScaleFactor: scale,
        });
        
        // HTML 파일 로드
        const fileUrl = `file://${htmlPath}`;
        await page.goto(fileUrl, { 
            waitUntil: 'networkidle0',
            timeout: 30000 
        });
        
        // 폰트 로딩 대기
        await page.evaluate(() => document.fonts.ready);
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // 스크린샷 캡처
        await page.screenshot({
            path: pngPath,
            type: 'png',
            clip: {
                x: 0,
                y: 0,
                width: width,
                height: height,
            },
        });
        
        console.log(`PNG 캡처 완료: ${pngPath}`);
        console.log(`해상도: ${width * scale} × ${height * scale}px`);
        
    } finally {
        await browser.close();
    }
}

// CLI
const args = process.argv.slice(2);
if (args.length < 2) {
    console.log('Usage: node capture_png.js <input.html> <output.png> [--high-res]');
    process.exit(1);
}

const inputHtml = args[0];
const outputPng = args[1];
const highRes = args.includes('--high-res');

captureHtmlToPng(inputHtml, outputPng, highRes).catch(err => {
    console.error('캡처 실패:', err.message);
    process.exit(1);
});
