const fs = require('fs');
const readline = require('readline');

// Define the file paths
const inputFilePath = './dump.sql';
const outputFilePath = './output_dump.sql';

// Create read and write streams
const readStream = fs.createReadStream(inputFilePath, 'utf8');
const writeStream = fs.createWriteStream(outputFilePath, 'utf8');

// Create a readline interface
const rl = readline.createInterface({
    input: readStream,
    output: writeStream,
    terminal: false
});

let inCreateStatement = false;

rl.on('line', (line) => {
    // Trim any leading/trailing whitespace for more accurate matching
    const trimmedLine = line.trim();

    // Skip PRAGMA foreign_keys=OFF; line
    if (trimmedLine.match(/^PRAGMA\s+foreign_keys\s*=\s*OFF\s*;/i)) {
        return;
    }

    // Skip BEGIN TRANSACTION; and COMMIT; lines
    if (trimmedLine.match(/^BEGIN\s+TRANSACTION\s*;/i) || trimmedLine.match(/^COMMIT\s*;/i)) {
        return;
    }

    // Detect start of CREATE TABLE or CREATE INDEX statements
    if (trimmedLine.match(/^CREATE\s+(TABLE|INDEX)/i)) {
        inCreateStatement = true;
    }

    // Detect the end of a CREATE TABLE or CREATE INDEX statement
    if (inCreateStatement && trimmedLine.match(/;\s*$/)) {
        inCreateStatement = false;
        return; // Skip the final line of the CREATE statement
    }

    // If not in a CREATE statement, process the line
    if (!inCreateStatement) {
        // Replace 'NA' with 0
        line = line.replace(/'NA'/g, '0');
        writeStream.write(line + '\n');
    }
});

rl.on('close', () => {
    console.log(`Filtered dump saved to ${outputFilePath}`);
    writeStream.end();
});
