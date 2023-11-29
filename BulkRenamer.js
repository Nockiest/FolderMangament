const fs = require('fs');
const path = require('path');

function renameFilesWithSuffix(folderPath, oldSuffix, newSuffix) {
    // Read the contents of the folder
    const files = fs.readdirSync(folderPath);

    // Iterate over each file
    files.forEach(file => {
        const filePath = path.join(folderPath, file);

        // Check if the file is a directory
        if (fs.statSync(filePath).isDirectory()) {
            // Recursively rename files in subdirectories
            renameFilesWithSuffix(filePath, oldSuffix, newSuffix);
        } else {
            // Check if the file has the specified old suffix
            if (file.endsWith(oldSuffix)) {
                const newFileName = file.replace(new RegExp(`${oldSuffix}$`), newSuffix);
                const newFilePath = path.join(folderPath, newFileName);

                // Rename the file
                fs.renameSync(filePath, newFilePath);

                console.log(`Renamed: ${file} => ${newFileName}`);
            }
        }
    });
}

// Example usage:
const folderPath = 'C:/Users/ondrej.lukes/Desktop/restful_šachy/online--achy-websocket-25.10/server';
const oldSuffix = '.js';
const newSuffix = '.ts';

renameFilesWithSuffix(folderPath, oldSuffix, newSuffix);