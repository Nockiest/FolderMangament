const fs = require('fs');
const path = require('path');

const folderPath = 'C:/Users/ondra/Desktop/Peřinka/perinka'; // Replace with the actual path to your folder
const sourceExtension = '.tsx'; // Replace with the source file extension
const targetExtension = '.js'; // Replace with the target file extension

const ignoreFolders = ['node_modules', '.next'];

const renameFilesInFolder = (folderPath) => {
  const files = fs.readdirSync(folderPath);

  files.forEach((file) => {
    const filePath = path.join(folderPath, file);

    if (fs.statSync(filePath).isDirectory()) {
      // If it's a directory, recursively call the function
      if (!ignoreFolders.includes(file)) {
        renameFilesInFolder(filePath);
      }
    } else if (file.endsWith(sourceExtension) && !file.includes('config')) {
      // Ignore files with "config" in their names
      const newFile = file.replace(new RegExp(`${sourceExtension}$`), targetExtension);
      const newFilePath = path.join(folderPath, newFile);

      fs.renameSync(filePath, newFilePath);
      console.log(`Renamed ${file} to ${newFile}`);
    }
  });
};

renameFilesInFolder(folderPath);
