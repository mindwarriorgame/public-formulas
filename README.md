# MindWarrior game: Shared Letters

Letters that the players have decided to share with everyone to inspire them.

All the shared letters are compiled and published at https://mindwarriorgame.org/shared-letters to inspire other players.

# Contributions

Thank you very much for your contribution! Sharing what works for you could be a great help to other players to achieve their own goals and aspirations 🙌.

## Requirements to Letters

To have your Letter accepted, it must comply with the following requirements:

1. The content must be respectful and constructive, free from hate speech, personal attacks, or discriminatory language.
1. The Letter should not include any inappropriate content, such as sexual material, violent threats, or anything that violates the law.
1. Spamming, advertising, or promoting other products/services is not allowed.
1. Avoid excessive profanity or offensive language.
1. All Letters should be written in a clear and readable manner.
1. At the moment of publishing:
  - your difficulty level must be at least "Normal" (3/5)
  - your active game counter must be at least 5 days
  - your game scores must be positive

## How to share your Letter

To share your Letter, please folow these steps:

### Step 1: oubtain your `shared_key_uuid`.

There are several ways how to do that, use whichever is more convenient:

- Option 1: send `/data` message to [MindWarriorGame bot](https://t.me/MindWarriorGame_bot), find and copy `shared_key_uuid` value
  <img width="553" alt="image" src="https://github.com/user-attachments/assets/15bb09c5-ffc7-4169-b9f5-27f3812beced">

- Option 2: send `/letter` command to [MindWarriorGame bot](https://t.me/MindWarriorGame_bot), press `Share` button and copy `shared_key_uuid` value
    <img width="401" alt="image" src="https://github.com/user-attachments/assets/fb68451c-d766-4a47-a5bb-e504b8a5d420">

   

### Step 2: post your letter as a GitHub issue

Create a new [Issue](https://github.com/mindwarriorgame/shared-letters/issues) for this repository and provide the following information:

  - your `shared_key_uuid`
  - your Letter
  - clearly express your intent to share your Letter on our website
    - please make sure you understand that you are sharing your Letter under [MIT license](LICENSE) (the license of this repository) and all the implications
     
## Translations

By default, all shared Letters are translated to missing languages using ChatGPT. If you'd like, please feel free to submit your own translations (add it to the Issue) 

## How to modify a Letter

If you have spotted a typo, or wanted to modify your own Letter, please feel free to open another Issue and explain what you'd like to change.

If the modification is major, please
- make sure you are using the same GitHub account that you were using for the first time submission of the Letter 
- provide your `shared_key_uuid` again
- make sure the change complies with all the "Requirements to Letters".

## Privacy considerations


### `shared_key_uuid`

Since we have asked for your `shared_key_uuid` , even though it doesn't contain any sensitive information about yourself (a random string), this might raise a Privacy concern. To address that, you could always regenerate `shared_key_uuid` for your playing account by sending `regenerate_shared_key_uuid` command to the bot. This will remove the logical link between the shared Letter and your playing account.

<img width="710" alt="image" src="https://github.com/user-attachments/assets/c07c9888-2e63-4f9c-827e-4d4445133629">

We ask you to do that only after your Letter has been merged to the codebase of the repository, because otherwise we won't be able to check the requirements for Letter about the difficulty, scores and the active game counter.

### Repository history

Please note that GitHub contribution model saves the history of all modifications of the repository. In regards to sharing your Letter, that would make a permanent link between your Git and GitHub information and the Letter. While there are possible strategies how to mitigate that (e.g. using anonymizers, like, https://www.gitmask.com/ or temp accounts), all them are subject to their own privacy considerations. (And if we cannot identify you as the original author, you won't be able to submit a major upate for your Letter in the future.) Please be mindful about this.

## License

All content of this repository is under [MIT license](https://en.wikipedia.org/wiki/MIT_License). Whatever you write in the Issue or in PR, including your Letter, becomes an essential part (content, documentation) of this public, open source project. According to the license, you give everyone permission to use, copy, modify, merge, publish, distribute, sublicense, sell copies etc. of your Letter. Please make sure you understand it before contributing!
