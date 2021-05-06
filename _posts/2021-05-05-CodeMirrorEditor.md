---
title: CodeMirrorEditor
date: 2021-05-05 19:57:26 
categories: Dev
tags: [WebDev]
---

Try to Use the [CodeMirror](https://codemirror.net/) module for web code text editor. Preparing for the future webGL practice.

{% include codemirror.html %}

<div id="editor"></div>
<button id="sendDisplay"> Send Code to display </button>
<div id="display"></div>

<script>
var container = document.getElementById("editor");
var button = document.getElementById("sendDisplay");
var display = document.getElementById("display");
var defaultText = 
`#include "stdio.h"

int main(int argv, const char ** argv)
{
    printf("Hello World!!");
    return 0;
}
`;

var myCodeMirror = CodeMirror(container, {
  value: defaultText,
  mode:  "c++",
  lineNumbers: true
});

function Send()
{
    display.textContent = myCodeMirror.getValue();
}
button.onclick = Send;
</script>


