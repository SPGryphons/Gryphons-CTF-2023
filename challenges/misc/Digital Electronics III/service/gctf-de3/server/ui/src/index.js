import {EditorState} from "@codemirror/state"
import {EditorView, keymap} from "@codemirror/view"
import {defaultKeymap} from "@codemirror/commands"
import * as CodeMirror from 'codemirror';
import {cpp} from "@codemirror/lang-cpp"

console.log("Hello World!")

const heightFixedTheme = EditorView.theme({
  "&": {height: "100%"},
  ".cm-scroller": {overflow: "auto"}
})


async function init() {
  const response = await (await fetch("template.cc")).text()
  console.log("resp", response)


  let state = EditorState.create({
    doc: response,
    extensions: [CodeMirror.basicSetup, heightFixedTheme, keymap.of(defaultKeymap), cpp()],
  
  })
  
  
  let editorParent = document.getElementById("editor-component")
  let editor = new EditorView({
    state: state,
    parent: editorParent ?? document.body,
  })

  document.getElementById("submit-code").onclick = async () => {
    // AJAX, send a post request to "/play"
    console.log("submit")
    const code = editor.state.doc.toString()
    document.getElementById("loading-text").style.display = ""
    const response = await fetch("/play", {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
      body: JSON.stringify({code: code})}
        )
    
    if (!response.ok) {
      alert("Request failed")
    } else {
      const data = await response.json()
      if (data.error) {
        // error
        const error = `Error!
${data.error ?? ""}
${data.msg ?? ""}`
        alert(error)
      }
      else if (data.success) {
        alert(`Success! Flag: ${data.flag}`)
      }
    }

    document.getElementById("loading-text").style.display = "none"

  }
  

}
void init()




window.onbeforeunload =  () => {return "You have attempted to leave this page. Are you sure?"; };
