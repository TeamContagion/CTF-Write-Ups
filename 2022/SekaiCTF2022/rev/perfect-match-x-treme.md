# Perfect Match X-treme
**Category:** Reverse Engineering

**Points:** 100

**Solved By:** Apicius

## Challenge
>Can you qualify Fall Guy’s _Perfect Match_ and get the flag?
>
>*Author: sahuang & enscribe*

Files: `Perfect_Match_X-treme.zip`

## Solution

This problem required you beat a game of 'Fall Guys' icon matching in a Unity made game. However, by a cruel twist of fate, in the third round all of the platforms disappear. How unfair.

<img width="1014" alt="image" src="https://user-images.githubusercontent.com/17153535/193478932-1f3e762a-193d-4ab8-bb48-b63afc278e76.png">

Because this is a Unity game and we have the whole Build folder, I thought I'd take a look at the code. The unity build folder contains dll files that are the compiled C# code that the game author writes within unity. These handle many of the scripted functionality of the game such as how the game grid functions, or how the UI displays.

I loaded up `Build/PerfectMatch_Data/Managed/Assembly-CSharp.dll` in dnSpy and took a look at it. Within the UI class we can see where the win condition is checked for and where the flag is displayed. 

```csharp
using System;
using TMPro;
using UnityEngine;

// Token: 0x02000010 RID: 16
public partial class UI : MonoBehaviour
{
    // Token: 0x06000086 RID: 134 RVA: 0x00004604 File Offset: 0x00002804
    public void SetGameState(bool isWon)
    {
        this.gameStateUI.SetActive(true);
        this.gameStateText.gameObject.SetActive(true);
        if (isWon)
        {
            this.SetGameStateText("Qualified! Have your flag :)");
            this.text1.gameObject.SetActive(true);
            this.text2.gameObject.SetActive(true);
            this.text3.gameObject.SetActive(true);
        }
        else
        {
            this.SetGameStateText("Eliminated! No flag :(");
        }
        Time.timeScale = 0f;
    }
}
```

This code snippet is what's executed when the game is over (either losing or winning). If the game is won, game objects that store the flag text will be popped into existence and shown to the player. In order to get the flag, I simply edited the decompiled method to set the game text to the flag when you lose.

```csharp
this.SetGameStateText(this.text1.text+this.text2.text+this.text3.text);
```

I recompiled the code and reran the game. Now all I need to do is lose! I accomplished this by jumping off the edge as soon as the round started. The flag is then printed straight to the screen.

**Flag:**  `SEKAI{F4LL_GUY5_H3CK_15_1LL3G4L}`
 

<img width="758" alt="image" src="https://user-images.githubusercontent.com/17153535/193478958-f439ace9-097b-43af-ab02-1c3727fd832b.png">
