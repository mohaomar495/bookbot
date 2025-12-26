# BookBot 🤖

BookBot is a simple but powerful Python command-line tool designed to analyze text files (books). It can count the total number of words in a document and perform a frequency analysis of the characters used, sorting them by occurrence.

## 🚀 Features

-   **Word Count**: fast and accurate calculation of the total number of words in a text file.
-   **Character Frequency Analysis**: counts every alphabetic character and reports their frequency.
-   **Sorted Reporting**: outputs character counts sorted from most frequent to least frequent for easy analysis.
-   **Command Line Interface**: easy to use directly from your terminal.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your machine:

-   [Python 3](https://www.python.org/downloads/) (version 3.6 or higher recommended)

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/mohaomar495/bookbot.git
    ```

2.  **Navigate to the project directory**:
    ```bash
    cd bookbot
    ```

## 📖 Usage

To use BookBot, run the `main.py` script from your terminal, providing the path to the text file you want to analyze as an argument.

### Syntax
```bash
python3 main.py <path_to_book>
```

### Example
Analyze the provided *Frankenstein* text:

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output
When you run the command above, you will see an output similar to this:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count -----------
Found 77986 total words
--------- Character Count ---------
e: 46043
t: 30365
a: 26743
o: 25225
...
============= END =============
```

## 📂 Project Structure

-   `main.py`: The entry point of the application. It handles argument parsing and orchestrates the analysis.
-   `stats.py`: Contains the logic for text analysis (counting words and characters).
-   `books/`: A directory containing sample text files for testing (e.g., `frankenstein.txt`).

## 📄 License

This project is licensed under the [MIT License](LICENSE).
