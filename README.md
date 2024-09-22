# shared-letters
Letters that the players have decided to share with everyone for inspiration.

All the shared letters are compiled and published at https://mindwarriorgame.org/shared-letters to inspire other players.

# Contributions

Thank you very much for your contribution! Sharing what works for you could be a great help to other players to achieve their own goals and aspirations 🙌.

## Requirements to Letters

To have your Letter accepted, it must comply with the following requirements:

1. The content must be respectful and constructive, free from hate speech, personal attacks, or discriminatory language.
1. The Letter should not include any inappropriate content, such as sexual material, violent threats, or anything that violates the law.
1. Spamming, advertising, or promoting unrelated products/services is not allowed.
1. Avoid excessive profanity or offensive language.
1. All Letters should be written in a clear and readable manner.
1. At the moment of publishing:
  - your difficulty level must be at least "Normal" (3/5)
  - your active game counter must be at least 5 days
  - your game scores must be positive

## How to share your Letter

To share your Letter, please folow these steps:

- Step 1: oubtain your `shared_key_uuid`. There are several ways how to do that:
  - Option 1: send `/data` message to [MindWarriorGame bot](https://t.me/MindWarriorGame_bot), find and copy `shared_key_uuid` value
    - <img width="470" alt="image" src="https://github.com/user-attachments/assets/d4a67c10-2e25-4ad0-9ac4-03d6dea9ac54">
  - Option 2: send `/letter` command to [MindWarriorGame bot](https://t.me/MindWarriorGame_bot), press `Share` button and copy `shared_key_uuid` value 

- Step 2: create a new [Issue](https://github.com/mindwarriorgame/shared-letters/issues) here with the following information:
    - your `shared_key_uuid`
    - your Letter
    - clearly express your intent to share your Letter on our website
      - please make sure you clearly understand that you are contributing your Letter under MIT license (the license of "MindWarrior" project), to avoid any misunderstandings in the future.
 
## Translations

By default, all shared Letters are translated to the missing languages using ChatGPT. If you'd like, please feel free to submit your own translation (add it 

## How to modify a Letter

If you have spotted a typo, or wanted to modify your own Letter, please feel free to submit another PR (or an Issue) with the change.

If the modification is major, please make sure 
- you are using the same GitHub account that you were using for the first time submission of the Letter 
- please provide `shared_key_uuid` (if it was regenerated) somewhere in the description of your change
- please make sure the change complies with all the "Requirements to Letters".

## Privacy considerations


### `shared_key_uuid`

Since we have asked for your `shared_key_uuid` , even though it doesn't contain any sensitive information about yourself (a random string), this might raise a Privacy concern. To address that, you could always regenerate `shared_key_uuid` for your playing account by sending `regenerate_shared_key_uuid` command to the bot. This will remove the logical link between the shared Letter and your playing account.

We ask you to do that only after your Letter has been merged to the codebase of the repository, because otherwise we won't be able to check the requirements for Letter about the difficulty, scores and the active game counter.

### Repository history

Please note that GitHub contribution model saves the history of all modifications of the repository. In regards to sharing your Letter, that would make a permanent link between your Git and GitHub information and the Letter. While there are possible strategies how to mitigate that (e.g. using anonymizers, like, https://www.gitmask.com/ or temp accounts), all them are subject to their own privacy considerations. (And if we cannot identify you as the original author, you won't be able to submit a major upate for your Letter in the future.) Please be mindful about this.

## License

All content of this repository is under [MIT license](https://en.wikipedia.org/wiki/MIT_License). Your Letter will also become an essential part of this public, open source project. According to the license, you give everyone permission to use, copy, modify, merge, publish, distribute, sublicense, sell copies etc. of your Letter. Please make sure you understand it before contributing!
