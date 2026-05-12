const { exec } = require('child_process');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const input = path.join(rootDir, 'BOOK.md');
const output = path.join(rootDir, 'book.epub');
const css = path.join(rootDir, 'epub.css');
const cover = path.join(rootDir, 'cover_text.png');

console.log('開始編譯 EPUB...');

const command = `pandoc "${input}" -o "${output}" --css "${css}" --toc --toc-depth=2 --metadata title="AI Coding 入門" --metadata author="Happy eBook" --metadata lang="zh-Hant" --epub-cover-image="${cover}"`;

exec(command, { cwd: rootDir }, (error, stdout, stderr) => {
  if (error) {
    console.error(`執行 Pandoc 失敗，請確認是否已安裝 Pandoc。錯誤訊息: ${error.message}`);
    return;
  }
  if (stderr) {
    console.warn(`Pandoc 輸出提示: ${stderr}`);
  }
  console.log(`✅ EPUB 編譯成功！檔案位於: ${output}`);
});
