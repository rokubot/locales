# RokuBot Locales Repository

This repository hosts the i18n (internationalization) translation files used for the RokuBot project ([rokubot on GitHub](https://github.com/rokubot)). Its purpose is to enable and manage translation and localization for all supported languages in RokuBot, a multipurpose Discord bot.

## Key Features

### 🌍 Centralized Locale Files
Contains all translation resources (e.g., `en_US`, `bg_BG`, `es_ES`, etc.) required by RokuBot.

### 🤝 Crowdsourced Collaboration
Open for contributions from translators and the wider community—submit pull requests to add new languages or improve existing translations.

### 🔗 Seamless Integration
Used as a submodule in the main (private) RokuBot repository, ensuring up-to-date translations without exposing the entire codebase.

### ⚙️ Structured for Automation
Designed for compatibility with standard i18n tools and workflows (such as JSON, YAML, or other resource file formats).

## Repository Structure

```
├── bg_BG/          # Bulgarian translations
├── en_US/          # English (US) translations
├── es_ES/          # Spanish (Spain) translations
└── ...             # Other language folders
```

## Who Should Use This Repository?

### 🎯 Translators
Those interested in contributing to RokuBot's localization can work directly on this repository.

### 🔧 RokuBot Maintainers
Maintainers pull the latest translations via submodule, ensuring the main bot always has fresh, community-driven language updates.

### 👥 End Users
All language and localization enhancements for RokuBot come from this public repo, improving accessibility for global Discord communities.

## Contribution Guidelines

### Getting Started
1. **Fork** the repository
2. **Add or improve** translations in the appropriate language folder
3. **Submit a pull request** with your changes

### Translation Standards
- Follow any format and linting conventions described in this README
- Maintain consistency with existing translation patterns
- Ensure proper encoding (UTF-8) for special characters
- Test your translations for accuracy and context

### Important Notes
- **All contributions should focus on language files only**—no bot code is present here
- Keep translations concise and natural for the target language
- Consider cultural context and regional variations
- Maintain the same structure across all language folders

## Supported Languages

Currently supported languages include:
- 🇺🇸 English (US) - `en_US`
- 🇧🇬 Bulgarian - `bg_BG`
- 🇪🇸 Spanish (Spain) - `es_ES`

*More languages are welcome! See the contribution guidelines above.*

## License

This project is licensed under the same terms as the main RokuBot project. Please refer to the [LICENSE](LICENSE) file for details.

## Summary

This is the official community-driven translation repository powering all internationalization for the RokuBot Discord bot. By keeping it public and standalone, it welcomes contributions from anyone wishing to expand or improve RokuBot's language support, while ensuring the core project remains secure and private.

---

**Ready to contribute?** 🚀 Start by forking this repository and adding your language expertise to help make RokuBot accessible to Discord communities worldwide!
