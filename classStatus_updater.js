// This code opens https://usfweb.usf.edu/DSS/StaffScheduleSearch, selects a course number,semester, and outputs the state of the class.
// Uses puppeteer v. 16.1 chromium 104.05112.81
//Code by NandhuShankar

// initializes puppeteer. We use async functions to wait for website.
const puppeteer = require('puppeteer')
async function start() {
    const browser = await puppeteer.launch()
    var [page] = await browser.pages();
    await page.goto("https://usfweb.usf.edu/DSS/StaffScheduleSearch")

    // Enters semester and CRN
    await page.select('#P_SEMESTER', "202208")
    await page.type("#P_REF", "81151")

    // Submits data, then switches to new page
    const [newPage] = await Promise.all([
        new Promise(resolve => page.once('popup', resolve)),
        page.click("button[value='Search']"),
    ]);
    await page.close()

    // Gets content of the status
    const textContent = await newPage.evaluate(() => document.querySelector('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(11)').textContent);
    console.log(textContent)
    await browser.close()
}   
start()
