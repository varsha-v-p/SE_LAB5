1. Which issues were the easiest to fix, and which were the hardest? Why?
->The easiest issues to fix were style and documentation-related, such as adding missing docstrings, formatting lines within 100 characters, and specifying the encoding argument in file operations. These changes were straightforward and didn’t affect program logic.
->The hardest issue was the broad except: block, as it required identifying which exceptions could realistically occur and narrowing them down to (KeyError, TypeError). This needed a proper understanding of the code flow to avoid accidentally breaking error handling.

2. Did the static analysis tools report any false positives? If so, describe one example.
-> Yes, Pylint flagged a “missing logging configuration” warning even though logging was properly set up at the top of the file. This was a minor false positive because the configuration used (basicConfig) already ensured correct logging behavior.
->Additionally, Bandit sometimes flags open() usage even when used safely within a context manager, which can be misleading.

3. How would you integrate static analysis tools into your actual software development workflow?
-> I would integrate Pylint, Flake8, and Bandit into a Continuous Integration (CI) pipeline so that every code commit automatically triggers static analysis checks.
-> Locally, I would configure these tools to run automatically on file save (e.g., through a VS Code extension or pre-commit hook) to catch issues early.
-> This helps maintain consistent code quality across the team and prevents security or style issues from reaching production.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
-> After applying the fixes, the code became cleaner, safer, and more maintainable.
-> Using proper exception handling and type validation improved robustness against runtime errors.
-> Adding docstrings and consistent formatting made the code much more readable and easier to understand.
->  Security and reliability improved by removing unsafe functions (eval) and adding file handling best practices.

Overall, the project achieved a Pylint score of 9.84/10, with zero Bandit or Flake8 issues, showing measurable improvement in quality.