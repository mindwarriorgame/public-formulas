# shared-letters
Letters that the players have decided to share with everyone for inspiration.

All shared letters are compiled and published at https://mindwarriorgame.org/shared-letters to help other players.

# Contributions

Thank you very much for your contribution! Sharing what works for you might inspire and help other players to achieve their own goals and aspirations 🙌.

## Requirements to Letters

To have your Letter accepted, it must comply with the following requirements:

1. The content must be respectful and constructive, free from hate speech, personal attacks, or discriminatory language.
1. The Letter should not include any inappropriate content, such as sexual material, violent threats, or anything that violates the law.
1. Spamming, advertising, or promoting unrelated products/services is not allowed.
1. Avoid excessive profanity or offensive language.
1. All Letters should be written in a clear and readable manner.
1. At the moment of publishing, your active game counter must be at least 5 days and you must score postively.

## How to share your Letter

To share a Letter, you need to follow the following steps:

- Send `/data` message to [MindWarriorGame bot](https://t.me/MindWarriorGame_bot)
  - copy your `shared_key_uuid` , which is required for the following steps
    - <img width="470" alt="image" src="https://github.com/user-attachments/assets/d4a67c10-2e25-4ad0-9ac4-03d6dea9ac54">

- If you are familiar with GitHub contribution model:
  - raise a Pull Request with the content of your Letter and translations
    - `letters/your-shared-key-uuid.md`
- If you are NOT familiar with GitHub:
    - just raise a new [Issue](https://github.com/mindwarriorgame/shared-letters/issues) here
    - in the issue, please provide your `shared_key_uuid`, your Letter and the translations (if any)
 
## Translations

By default, all letters are translated with ChatGPT. If you want, please feel free to submit your own translations. For that insert the language code before `.md` extension (e.g. `my-uuid.ru.md`)

## How to modify a Letter

If you have spotted a typo, or wanted to modify your own Letter, please feel free to submit another PR (or an Issue explaining the change).

## Privacy considerations

Since we have asked for your `shared_key_uuid` , even though it doesn't contain any sensitive information about yourself (a random string), this might raise a Privacy concern. To address that, you could always regenerate `shared_key_uuid` for your playing account by sending `regenerate_shared_key_uuid` command to the bot. 

We ask you to do that only after your Letter has been merged to the codebase of the repository, because otherwise we won't be able to check the requirements for Letter about the positive scores and the active game length.

## License

All content of this repository is under [MIT license](https://en.wikipedia.org/wiki/MIT_License). Your Letter will also become an essential part of this public, open source project. According to the license, you give everyone permission to use, copy, modify, merge, publish, distribute, sublicense, sell copies etc. of your Letter. Please make sure you understand it before contributing!
