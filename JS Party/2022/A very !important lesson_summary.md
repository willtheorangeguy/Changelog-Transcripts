• Estelle Weyl co-authored "The Definitive CSS Guide" and is working on its fifth edition
• The book aims to help developers understand the specifications of CSS without having to read them directly
• Estelle has three jobs: co-authoring the book, writing "Learn HTML" for web.dev, and working at Open Web Docs maintaining Mozilla Developer Network (MDN)
• She discusses the process of getting changes into the MDN docs, which involves community contributions and code reviews
• The conversation turns to the management of CSS and HTML through working groups similar to ECMA (for JavaScript)
• Estelle explains how the WHATWG was formed as a result of the division between W3C's focus on XHTML and the more forgiving HTML syntax used by browsers
• Changing default search engine to MDN in Edge browser
• Setting up MDN as a custom search engine
• Firefox and Brave browsers discussed for security features
• WHATWG (HTML standards body) vs. CSS Working Group (CSS standards body)
• Explanation of HTML and CSS living standards, not versioned like HTML 5 or CSS 3
• New color functions in CSS Color module level 4
• Complexity of CSS and HTML specs
• Handling languages such as Mongolian and Japanese text in web development
• Use of language attributes in HTML and their impact on CSS rendering
• Ordered lists and unordered lists, including issues with bullet points and numbering
• Standards bodies and the complexity of considering every use case for the web
• History of abandoned specs, including HTML imports and App Cache
• Browsers now support cascade layers and can be imported using @import
• Interoperability (Interop 2022) is a key initiative to ensure web features work consistently across browsers
• Web Platform Tests (WPT) helps browsers run tests and ensures features like CSS list views and viewport units work correctly
• The latest Interop ratings show significant progress, with some features at 100% interoperability
• Interoperability has driven new CSS features and improved support for existing ones across browsers
• Examples of new CSS features include the dialog element and :has() selector, which allows styling based on conditions other than parents.
• nth last of type selectors
• :has() parent selector and its capabilities
• Forgiving selector lists vs normal selector lists
• Use cases for :has() in practical applications (focus within, styling based on ancestor or child elements)
• Cascade layers as an alternative to using !important
• Understanding the CSS cascade order: user agent, user, developer, and browser styles
• How !important works in relation to the cascade order
• Using cascade layers to control specificity wars between different stylesheets or third-party libraries
• The mechanics of declaring a cascade layer and its impact on styling priorities
• Discussion on using @import inside a style and its relationship to cascade layers
• Control over cascade layer order through declaration before other styles
• Ability to put cascade declarations within media queries for dynamic styling
• Immutable nature of cascade layers and inability to change order at runtime
• Demonstration of "styling the style" by making CSS editable with content editable attribute
• Explanation of content editable attribute as an enumerated value, not a boolean
• Content editable is an enumerated attribute with values of true, false, and possibly a new value called plain text only
• The default value of content editable depends on whether it's present, empty, or invalid
• Inherit is not a valid value for content editable, but can be the result of an invalid value
• Hidden is an enumerated attribute with a new value called until found
• Until found means the element takes up space on the page, but its content is not visible until it's focused and matches a certain condition
• Browsers currently supporting hidden until found are Edge, Chrome, and possibly Safari soon
• Comparison between JavaScript and HTML/CSS syntax
• Discussion on type standardization in HTML parsing
• Explanation of enumerated and boolean attributes in HTML
• Accessibility features in HTML and importance of proper usage
• Specific examples of accessible HTML practices (e.g. radio buttons, SVG images)
• Importance of learning HTML for developers to achieve accessibility goals
• The speaker discusses creating accessible web components, including carousels
• Estelle Weyl mentions that she contracts with Google Chrome to work on web.dev content
• Open Web Docs is funded by corporations and individuals, specifically Edge and Google
• Mozilla does not donate to Open Web Docs but has their own staff working on related projects
• The speaker discusses common misconceptions about HTML and CSS, including the use of semantic elements and interactive labels
• The topic of accessible radio buttons and labels is discussed in detail
• Issues with website usability and design due to poorly designed clickable areas
• CSS specificity and selector knowledge being underutilized or misunderstood by developers
• Importance of learning selectors and specificity for efficient styling
• The need for extensible and scalable coding practices
• Common mistakes in using radio buttons and checkboxes
• Container queries and their potential applications
• The range of capabilities in CSS, from basics to complex effects
• Mastering the basics of HTML and CSS is essential for developers
• The importance of accessibility in web development
• Where to find Estelle Weyl online (social media platforms)
• Available resources for learning CSS, HTML, and accessibility (MDN, Open Web Docs, Web.dev/html/learn)
• Recommended experts in accessibility (Marcy Sutton, Melanie Sumner)
• Estelle Weyl's areas of expertise and availability for teaching/training
• Her preferred contact method and desire to avoid spam