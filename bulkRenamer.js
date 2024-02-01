const fs = require('fs');
const path = require('path');

async function renameFiles(name, folderPath) {
  try {
    const files = await fs.promises.readdir(folderPath);

    for (let i = 0; i < files.length; i++) {
      const oldFilePath = path.join(folderPath, files[i]);
      const newFileName = `${name}-${i + 1}`;
      const newFilePath = path.join(folderPath, `${newFileName}${path.extname(oldFilePath)}`);

      await fs.promises.rename(oldFilePath, newFilePath);
      console.log(`Renamed: ${files[i]} to ${newFileName}`);
    }

    console.log('Renaming complete.');
  } catch (error) {
    console.error('Error renaming files:', error);
  }
}

// Example usage:
const folderPath = 'C:/Users/ondra/Desktop/Peřinka/perinka/public/RedakcePics';
const newName = 'img';
renameFiles(newName, folderPath);
