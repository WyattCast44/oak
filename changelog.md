# Changelog/Maker's Log

## 15-Feb-2021

- So i determined the issue with the default providers, by calling them in the application class it lead to module import issues. But by importing the providers passed in via the config dict which makes you import the app root.
- Changed the order of operation on application constructor, now have the commands and options registrars init'd before the providers are registered and booted.