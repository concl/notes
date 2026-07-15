Related: [[HTTP]], [[JavaScript]], [[CSS]]

HTML is the basic markup language used to *structure* web pages on the internet. It consists of tags that form a hierarchical structure where larger elements group together child elements. For instance, a page often has a few main components: the navigation bar, the main body of content, and "the header". Each of these components may have subcomponents which can be represented in HTML.

## Webpages

When visiting a website, the browser executes an HTTP GET request to the address from the resolved URL. The server with this address then returns the HTML file for the queried webpage.

Elements of the webpage may require resources that are not present in the HTML file (including JS code, images, CSS). For instance:
```
<img src="foo.png"/>
```
defines an image that requires another resource. The browser fetches this resource by executing another GET request to the server.

The URL the browser fetches from depends on the type of path; `./foo` (or with the `./` omitted) represents a relative path while `/foo` represents an absolute path.

Furthermore, the URL may point to other websites as well; instead of requesting the current server, the browser will fetch the resource from the given URL.

## Links

Links are represented with the `a` tag, and the target is specified through the `href` attribute, which stores a URL. A URL can point to a specific fragment of a document, by using the `#` syntax.

For instance, if a heading has an `id`, then we can create a link to it like the following:

```
<h2 id="content">Information</h2>

<a href="#content">Link to info</a>
```

## Structuring Content

Creating layouts is mainly done through [[CSS]].
## Types of Elements

### Text

There are 6 headings and there is the `<p>` tag, which represents a paragraph.

### Tables


### Lists


