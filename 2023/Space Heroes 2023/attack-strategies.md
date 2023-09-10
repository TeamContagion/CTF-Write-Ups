# Attack-strategies
**Category:** Web

**Points:** 116

**Solved By:** Apicius

## Challenge
>The StarCraft III Interplanetary Newbie Championship is almost live and I was assigned to take care of teaching everyone in the Newbie-84 planet how to play. I made a blog so each individual can choose their favorite races and strategies to learn before the tournament. I will secretly participate and to give them a change, I hid my go to strategy somewhere on the website. Wanna try finding it?
>
>*Author: Bal*

## Solution

When we go to the site, we're prompted with a selection screen where we can chose a folder and select a file within that folder. If we check out the Javascript for the challenge we can see how it works.

![image](https://user-images.githubusercontent.com/17153535/233863549-3ec5fead-e639-4a40-95c7-01ab0d997b13.png)

```js
document.getElementById('folder_select').addEventListener('change', function() {
	var folderSelect = document.getElementById('folder_select');
	var fileSelect = document.getElementById('file_select');
	var submitBtn = document.querySelector('input[type="submit"]');
	var folder = folderSelect.value;
	if (folder) {
		fetch('/files/' + folder)
			.then(response => response.json())
			.then(data => {
				fileSelect.innerHTML = '';
				for (var i = 0; i < data.length; i++) {
					var option = document.createElement('option');
					option.value = data[i];
					option.text = data[i];
					fileSelect.appendChild(option);
				}
				fileSelect.disabled = false;
				submitBtn.disabled = false;
			});
	} else {
		fileSelect.innerHTML = '<option value="" selected>Select a file...</option>';
		fileSelect.disabled = true;
		submitBtn.disabled = true;
	}
});
```

This script selects files/folders from the current folder that it's in, and then displays them to the 'Select a folder' selector. Suspiciously, if we check our cookies we can see a "show_hidden" cookie. Setting this to true shows us a `flag.txt` under folders.

![image](https://user-images.githubusercontent.com/17153535/233863465-3e9e8ddf-451f-44b4-900e-b62b66717a95.png)

![image](https://user-images.githubusercontent.com/17153535/233863476-fa3a52e8-acad-4d94-b030-24129126b303.png)

Of course it forbids us from selecting it, though. I had an idea, however. What happens if I put a `../` in the request? What if I requested `folder_select=Protoss&file_select=../Terrans/Double+Proxy+Rax`?

Well, doing that shows us that our suspicion is correct.

![image](https://user-images.githubusercontent.com/17153535/233863530-737203e3-25ac-4515-bdba-5a4b08f801dd.png)

From here, all I needed to do was request the flag.

![image](https://user-images.githubusercontent.com/17153535/233863519-b0738cdc-5ea9-450c-b38a-358a57acb866.png)

**Flag**: `shctf{get_zerg_rushed_nb}`