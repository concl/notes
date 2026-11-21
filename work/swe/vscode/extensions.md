## Contributions

The features that a VSCode extension "contributes" is specified in the `package.json`. 

Example:
```json
// package.json
{
  "name": "vertices",
  "displayName": "vertices",
  "description": "Tools for competitive programming",
  ...
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "vertices.helloWorld",
        "title": "Hello World"
      }
    ],
    "viewsContainers": {
      "activitybar": [
        {
          "id": "vertices",
          "title": "Vertices",
          "icon": "assets/vertices.svg"
        }
      ]
    },
    "views": {
	
    }
  },
  ...
}
```



### Contribution Points

`views`: A GUI element
`viewsContainers`: A "container" for views, for which we can add to the activity bar (and represent with an icon). The `id` field specifies which view to take.