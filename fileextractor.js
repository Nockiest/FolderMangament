const fs = require('fs/promises');
const path = require('path');

async function moveFilesFromSubfolders(sourceFolder, destinationFolder) {
  try {
    // Read the contents of the source folder
    const subfolders = await fs.readdir(sourceFolder);

    // Iterate through each subfolder
    for (const subfolder of subfolders) {
      const subfolderPath = path.join(sourceFolder, subfolder);

      // Check if it's a directory
      const isDirectory = (await fs.stat(subfolderPath)).isDirectory();

      if (isDirectory) {
        // Read the files in the subfolder
        const files = await fs.readdir(subfolderPath);

        // Move each file to the destination folder
        for (const file of files) {
          const sourceFilePath = path.join(subfolderPath, file);
          const destinationFilePath = path.join(destinationFolder, file);

          // Move the file
          await fs.rename(sourceFilePath, destinationFilePath);

          console.log(`Moved: ${file} from ${subfolderPath} to ${destinationFolder}`);
        }
      }
    }

    console.log('Files moved successfully!');
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Example usage:
const sourceFolder = 'C:/Users/ondra/Documents/iLovePDF_Output';
const destinationFolder = './result';

moveFilesFromSubfolders(sourceFolder, destinationFolder);
