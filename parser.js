const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = {};
  }

  async readFile() {
    try {
      const content = await fs.promises.readFile(this.filePath, 'utf8');
      return content;
    } catch (error) {
      throw new Error(`Error reading file: ${error.message}`);
    }
  }

  parseData(content) {
    try {
      this.data = JSON.parse(content);
      return this.data;
    } catch (error) {
      throw new Error(`Error parsing data: ${error.message}`);
    }
  }

  async parseFile() {
    const content = await this.readFile();
    return this.parseData(content);
  }

  getData() {
    return this.data;
  }
}

module.exports = Parser;