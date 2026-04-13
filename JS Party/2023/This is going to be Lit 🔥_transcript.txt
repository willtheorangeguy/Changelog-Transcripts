[0.00 --> 11.48]  This is JS Party, a weekly celebration of JavaScript and the web.
[12.02 --> 13.98]  Connect with us in our community Slack.
[14.18 --> 15.16]  It's totally free.
[15.54 --> 19.64]  Head to jsparty.fm slash community and sign up today.
[20.32 --> 24.72]  Thank you to our partners for helping us bring you world-class developer pods each and every week.
[24.72 --> 28.90]  Shout out to Fastly.com, Fly.io, and Typesense.org.
[28.90 --> 31.50]  Okay. Hey, it's party time, y'all.
[39.70 --> 41.52]  Hello, JS Party listeners.
[42.16 --> 47.20]  We're so excited to be back with another amazing special show today.
[47.42 --> 49.94]  We have a very special guest on.
[49.94 --> 56.48]  And before I introduce them, I'd like to welcome my co-panelist, co-writer for the day.
[56.72 --> 57.80]  Hello, K-Ball. Welcome.
[58.24 --> 58.88]  Hello, hello.
[58.90 --> 60.72]  I'm excited. This is going to be lit.
[61.04 --> 66.62]  Yeah. Like, that's like, if anybody's counting puns, that's like one on the pun meter so far.
[66.76 --> 71.26]  And spoiler alert, our special guest today is Justin Fagnani.
[71.80 --> 72.70]  Welcome, Justin.
[73.34 --> 75.40]  Thanks. Glad to be here. Thanks for having me.
[75.66 --> 75.84]  Yeah.
[76.02 --> 76.22]  Yeah.
[76.32 --> 80.90]  I know. So the last time Justin and I were on a podcast together was in March of 2018.
[80.90 --> 85.30]  He was on my OG podcast called the Web Platform Podcast.
[85.76 --> 92.84]  And we were actually just kind of welcoming lit into the world in some form of its like current iteration.
[92.84 --> 96.48]  I think that there's a lot has changed in the library since 2018.
[96.48 --> 104.82]  But it's just so great to kind of like be full circle, you know, back with you today in the far, far future, kind of talking about lit.
[104.82 --> 109.98]  And so before we get into lit, just, you know, can you tell us a little bit about yourself, Justin?
[110.94 --> 115.72]  Yeah. So I've been working in the web space for a while now.
[115.80 --> 117.28]  I'm an engineer at Google.
[117.46 --> 121.72]  Been at Google for almost 15 years, which is, I find kind of unbelievable.
[121.96 --> 122.96]  Never really planned on that.
[122.96 --> 127.86]  Yeah. And before that, I had been, you know, doing small business consulting stuff.
[128.44 --> 133.68]  So I kind of came into Google and fell into developer tooling work there.
[133.92 --> 137.48]  I built a low code application building tool called App Maker there.
[137.60 --> 139.10]  And then I went on the Dart team.
[139.24 --> 146.04]  And then I kind of finally found my like, you know, true spiritual home on the Web Components team and Polymer team at the time.
[146.38 --> 150.34]  Worked on tooling there and then somewhat accidentally created lit.
[150.34 --> 154.16]  And I've been, you know, working on that ever since.
[154.70 --> 161.16]  Yeah. And so for those who are unfamiliar, could you tell us what is lit besides having an awesome name?
[161.96 --> 169.34]  Besides, lit is a little library that's part of where its name came from that helps you build web components.
[169.94 --> 176.22]  And so it's, you can think of it as a little bit similar to a framework, but not exactly like a framework.
[176.54 --> 177.56]  A little framework?
[177.56 --> 180.78]  A little framework. That's where the name originally came from.
[181.24 --> 184.26]  It started with a templating system, not even a component system.
[184.78 --> 188.14]  And we needed to name it for NPM.
[188.38 --> 193.74]  And it's just like literals. It uses template literals. It's little. It was like 1K at the time.
[194.16 --> 195.92]  So like n number of pens.
[196.10 --> 199.22]  It's like pun. There's like puns on puns on puns.
[199.32 --> 201.04]  It's like, wow.
[201.04 --> 205.44]  I never thought it would stick. Honestly, this is kind of a temporary name. Like, you know, you're like, I just need a name.
[205.78 --> 211.24]  You got 10 minutes to think of one. And then, you know, for better or worse, it sticks around for the rest of eternity.
[211.54 --> 213.46]  I mean, developers are great at naming things, right?
[213.52 --> 213.80]  Yeah.
[214.62 --> 215.52]  My best skill.
[216.06 --> 217.72]  Yeah. Lit helps you build web components.
[217.98 --> 224.96]  You know, I think one of the big things about it that's not apparent at first is that how important lit helping you build web components is.
[224.96 --> 229.96]  Like, lit wouldn't exist if it wasn't for web components. We wouldn't have made just another framework.
[230.54 --> 234.64]  So really lit and web components are like kind of so tight at the hip.
[234.82 --> 237.70]  They're, you know, you can't talk about lit without web components at all.
[238.02 --> 240.10]  Yeah. Yeah. No, thanks for that great summary.
[240.28 --> 250.02]  And it's really, it's really interesting to hear you speak about this because, you know, as I've known you for many years, just I've, you know, seen the kind of community pains and some of the adoptions, like friction to adoption
[250.02 --> 265.16]  because of the kind of, you know, how hard web components were to work with, you know, on the developer side, just the DX around working with web components and building and like working at scale was a little painful and rocky, like many, many years ago.
[265.16 --> 275.62]  And, you know, it's really great to hear that, you know, one of like lit's core missions is to kind of like smooth over like that process and being able to kind of leverage this really powerful primitive.
[275.62 --> 280.40]  And so you, you talked about web components being at the core.
[280.62 --> 282.96]  Can you kind of just walk us through the evolution of lit?
[283.02 --> 291.56]  Because, you know, you, for those who may be familiar with you, you were also like very involved with Polymer, another project that kind of was aiming to do some of this.
[291.84 --> 294.80]  But, you know, the standards world was in a different place at that point.
[294.92 --> 297.50]  So can you just tell us about the evolution of this project?
[297.78 --> 300.54]  Yeah. So, I mean, Polymer and lit are very closely related.
[300.54 --> 303.44]  You know, one way to think about lit is Polymer version four.
[303.44 --> 311.50]  And, you know, Polymer came around at a little bit different time when a couple of standards and browser support features were a little bit different.
[311.78 --> 320.68]  Like in particular, like ES2015 or ES6, as some people like to call it, like wasn't quite there yet in terms of browser support.
[320.92 --> 323.90]  Modules, JavaScript modules especially, were not there yet.
[324.20 --> 332.60]  And as part of the web component specs at the time, we had things like the template element, custom elements, shadow DOM, and HTML imports.
[332.60 --> 339.40]  Which gave you a way to import kind of HTML libraries into the main HTML page or other HTML libraries.
[339.90 --> 345.54]  So before we had a native browser supported JavaScript module system, Chrome actually had HTML imports.
[345.84 --> 347.98]  So Polymer was, it's a lot like Vue in some ways.
[348.04 --> 350.20]  I think Vue kind of took a lot of ideas from Polymer.
[350.62 --> 354.04]  It's like an HTML centric library for helping you make web components.
[354.54 --> 357.00]  The goals are very, very much the same as lit.
[357.00 --> 368.22]  But as we evolved Polymer to keep up with the specs and HTML imports was not going to be adopted by other browsers, we started putting Polymer into JavaScript modules.
[368.86 --> 371.96]  And its HTML centric nature didn't quite fit anymore, right?
[371.96 --> 375.84]  Because you had like a JavaScript file with HTML embedded into it.
[375.84 --> 384.72]  And then inside of that HTML, you had Polymer's kind of custom expression and control flow language, which looked a little bit like JavaScript, but wasn't JavaScript.
[385.22 --> 390.82]  So that motivated us to work on lit, which is basically like, yes, you're going to have HTML strings inside your JavaScript.
[390.82 --> 397.84]  But when you need to do logic inside of that template, let's just use the JavaScript that's already available in that context.
[398.00 --> 399.52]  And so that's kind of the biggest difference with lit.
[399.52 --> 408.30]  And because of that, we were able to shave a bunch of like code and weight and concepts off of Polymer and make things a lot smaller and a lot faster.
[408.58 --> 411.26]  And because it was such a big change, we changed the name.
[411.40 --> 414.74]  But more or less, like lit is a direct successor to Polymer there.
[415.26 --> 418.06]  So in some ways, it sounds like you inverted Polymer.
[418.06 --> 427.80]  You put JavaScript Polymer with sort of HTML as the structure and control flow or JavaScript or what have you as like the meat and pudding inside.
[427.80 --> 432.92]  And then for lit, you have a JavaScript container and you happen to have the HTML in the middle.
[433.30 --> 433.52]  Yeah.
[433.62 --> 435.04]  And there's multiple layers, right?
[435.08 --> 440.46]  Because like when you have HTML, I mean, probably a lot of your readers are familiar with JSX, right?
[440.48 --> 441.70]  And they say it's just JavaScript.
[441.70 --> 447.88]  And usually what they mean by that is not the tag part of the JSX, but it's the expressions and the logic, right?
[447.98 --> 451.90]  Your turn areas and conditionals and, you know, mapping over an array.
[452.06 --> 452.68]  That's all JavaScript.
[453.22 --> 454.16]  Lit is the same as that.
[454.26 --> 456.10]  So you have JavaScript container, like you said.
[456.10 --> 458.80]  Then you have an HTML-ish looking template.
[459.58 --> 463.36]  And then inside of that template, you have expressions and conditionals and whatnot.
[463.54 --> 464.90]  And that's all just plain JavaScript.
[465.60 --> 474.06]  So yeah, in both, you know, Polymer was HTML and then logic inside of that, potentially some JavaScript and lit is JavaScript on the outside and HTML.
[474.70 --> 481.88]  And you did something very clever with the HTML, which, you know, was that it's leveraging JavaScript template literals.
[482.12 --> 483.18]  Sorry, JavaScript literals.
[483.18 --> 486.02]  JavaScript tagged template literals.
[486.18 --> 486.40]  Yes.
[486.52 --> 487.14]  There we go.
[487.46 --> 494.14]  Yeah, this is probably the biggest, you know, kind of innovation there is that lit doesn't use a VDOM and it doesn't have a compiler.
[494.50 --> 499.48]  This makes it relatively unique amongst the framework and framework like library world.
[499.48 --> 500.92]  Yet it's really fast.
[500.92 --> 504.26]  It's faster than most of the popular frameworks out there on the benchmarks.
[504.64 --> 509.84]  And it's due to this, like, magic quality of tag template literals that not a lot of people know about.
[510.48 --> 517.74]  But it basically, you know, if you don't know what a tag template literal is, if you look at lit code, you'll see the templates are like a string, but they're using backticks.
[517.74 --> 520.74]  And they have this little HTML tag in front of them.
[520.86 --> 525.54]  And if you're using a good IDE or a plugin, you'll get HTML syntax highlighting there, which is nice.
[525.54 --> 531.84]  But the really cool thing that happens is that in JavaScript, you get this reference to those strings that are part of your template.
[531.84 --> 533.30]  And it's like a stable reference.
[533.30 --> 545.98]  So every time you execute a function that contains the same HTML backticks, that HTML tag is a function that gets the same exact, like, strings array passed to it for that template every single time.
[546.62 --> 548.86]  And so what we do is we do some prep work.
[549.02 --> 552.46]  We create an HTML template element out of the template you write in JavaScript.
[552.64 --> 555.38]  But we only have to do that the very first time we ever see a template.
[556.00 --> 560.78]  After that, we can do things like clone a template if you're rendering that template to a new spot.
[560.78 --> 572.06]  Or actually just skip all cloning and not even looking at or touching the DOM for the static parts of the template, but just go directly to the values and update them if necessary.
[572.36 --> 575.34]  So we get kind of like a VDOM-like behavior.
[575.98 --> 579.82]  Like, we only make the minimal DOM updates, but it's actually way more efficient than VDOM.
[580.20 --> 583.22]  Because we're not holding on to an old VDOM and a new VDOM.
[583.32 --> 584.20]  We're not doing a diff.
[584.60 --> 587.62]  And we're not walking the DOM that's in the page.
[587.62 --> 590.68]  We're just jumping right to where the expressions are in your template.
[591.46 --> 597.86]  So it's a little bit like the benefit you get from signals in some way, although we have to kind of update all the expressions in the template at once.
[598.16 --> 601.14]  But without a compiler with a very simple syntax.
[601.74 --> 603.12]  Can I ask a question there?
[603.34 --> 606.56]  So how is the actual update flowing into the DOM?
[606.76 --> 609.08]  Like, where does that, what is doing that?
[609.08 --> 618.88]  So the main entry point to at least the template system, which is called lit HTML, is a render function that looks a lot like React's render.
[619.18 --> 624.46]  And you give it like a template expression, and then you give it a container to render into.
[624.46 --> 626.56]  So there's a couple of different phases here.
[626.68 --> 637.42]  The very first time you render a template, we're going to create an HTML template element, populate it with the strings from your template, kind of walk through it and remember where the dynamic expressions are.
[637.42 --> 643.48]  And then the very first time it's rendered, we're going to clone that template and append it into the container you render it to.
[643.78 --> 647.00]  And then we jump to where all the expressions are, and we fill it in with data.
[647.54 --> 655.20]  When you update, we actually leave a little marker in the DOM, a little property that says, this DOM here was rendered by lit with this template.
[655.20 --> 660.84]  So next time you come to render and update, we go, are you rendering the same template that was already rendered here?
[661.36 --> 663.86]  And if so, we don't do anything with the DOM.
[664.20 --> 666.98]  We just skip to where the data is and update the data.
[667.58 --> 671.70]  And at each data point, we remember what the old data was and only update that data if it changed.
[672.42 --> 677.70]  So yeah, there's the initial pass is you do like three steps, and the update pass is you just jump right to the last step.
[677.70 --> 687.26]  Got it. And so how are you tracking where that data is living in the actual HTML so that you can jump in and do those edits in place?
[687.52 --> 688.48]  Ah, that's a fun question.
[688.74 --> 698.92]  So what we do on the first pass is we walk the DOM, and we have like a little counter, like a node index about where we expect to find those expressions.
[699.14 --> 704.14]  And in the HTML template, we actually place like comments where the bindings would be.
[704.14 --> 714.42]  So after the initial clone, before we put the initial data in, we walk the DOM and we go, we expect to find a comment at like, you know, depth first node index 12.
[714.92 --> 719.82]  So we'll do a tree walker and walk down, we get to 12 and we go, okay, here's our comment that says where the data is going to be.
[720.36 --> 723.68]  Once we find all those comments, we make a data structure we call parts.
[724.16 --> 726.72]  And that just kind of lives with the template instance.
[726.86 --> 729.64]  And it says, okay, first binding, here's the part for it.
[729.74 --> 731.98]  And it's a child part where you might put text or whatever.
[731.98 --> 734.20]  Second binding is an attribute part.
[734.72 --> 736.66]  It's at this node index with this attribute name.
[737.18 --> 738.78]  So we have just a couple of part classes.
[738.96 --> 742.34]  And so they maintain direct JavaScript references into the DOM.
[742.62 --> 744.42]  So you don't have to do any walking after that.
[744.80 --> 746.76]  And they remember their old value.
[747.22 --> 752.90]  And the cool thing about this technique is it's very, very fast to update with a little bit of memory overhead just to remember where these things are.
[752.90 --> 764.64]  But we've been working with Apple and Chrome and whatnot on a couple of proposals called template instantiation or DOM parts to actually bring a very, very similar technique into the browser.
[765.18 --> 774.20]  So that, you know, hopefully with very minimal code, anybody or any library will be able to kind of use this technique of clone some DOM and then get these references back into it to do fast updates.
[774.20 --> 774.52]  Okay.
[774.52 --> 774.92]  Okay.
[775.12 --> 779.24]  So to make sure I understand properly, I'm going to rephrase what I think I heard you say.
[779.38 --> 789.22]  So each template that you have in lit, you are maintaining what is essentially a lookup table where you say, okay, here are the sets of bindings within this template.
[789.42 --> 791.54]  A lookup table and a last value, essentially.
[791.68 --> 792.60]  Here's a set of bindings.
[792.94 --> 794.14]  Here's what their last value was.
[794.16 --> 798.86]  And here's a pointer to where this lives in the DOM so I can update it as fast as humanly possible.
[798.86 --> 803.74]  And then when an update comes through, you go for each one of those and you say, did this change?
[803.82 --> 805.08]  If no change, no worries.
[805.22 --> 808.50]  If so, follow that pointer, plop it into that location in the DOM.
[808.84 --> 809.04]  Yep.
[809.60 --> 812.32]  How does that work with subtemplates and things like that?
[812.58 --> 814.26]  So a subtemplate is just a value.
[814.26 --> 821.22]  This is another thing that's very similar to JSX and VDOM is that a template expression returns an actual JavaScript object.
[821.90 --> 825.18]  So the subtemplate will be an object that gets rendered into a binding.
[825.18 --> 829.22]  And at that point, we just recursively repeat the whole process.
[829.50 --> 832.46]  We go, have we rendered this here yet?
[832.54 --> 836.24]  If not, we do the prepare the templates and clone it and whatnot.
[836.66 --> 842.72]  And if we have, you know, that template instance also has that data structure of that lookup table and we jump into that.
[843.36 --> 848.72]  And having this identity of templates from the JavaScript tag template literal, the template strings,
[849.36 --> 854.02]  it lets us pretty trivially handle the case where you have like a subtemplate, but it's a conditional.
[854.02 --> 858.00]  And you're swapping between two subtemplates because we go, have we rendered this template here?
[858.16 --> 858.86]  Yes, do it.
[858.96 --> 862.56]  If the condition switches and you render a new one, we're like, have we rendered this template here?
[862.60 --> 863.28]  The answer is no.
[863.82 --> 866.32]  Clear that and start the process over again.
[866.70 --> 871.30]  So composition, array.map, all that kind of stuff kind of just falls out from that.
[872.04 --> 872.24]  Yeah.
[872.34 --> 877.46]  Thank you for walking us through the underbelly of your rendering business logic.
[877.56 --> 878.20]  That was very cool.
[878.20 --> 882.94]  I was curious, are you using symbols or just hashes or what are you using to kind of manage
[882.94 --> 883.60]  your references?
[884.12 --> 885.10]  It's actually an array.
[885.44 --> 890.52]  So if you look at a tag template literal, the way that's given to a tag function is you get
[890.52 --> 892.70]  an array of the strings and you get an array of the values.
[893.44 --> 897.88]  And to put everything together, you would kind of zip it where the values would sit in between
[897.88 --> 898.76]  the strings you got.
[899.60 --> 901.80]  So for, and the length of that is always the same, right?
[901.80 --> 906.08]  Like you can't dynamically add an expression inside of a template literal.
[906.70 --> 910.12]  Like if your template literal has five expressions, it will always have five expressions.
[910.72 --> 912.86]  So we have, we don't even really keep a reference.
[912.94 --> 916.26]  We just keep an array of like, every time we get new values, we're going to get an array
[916.26 --> 916.72]  of five.
[916.72 --> 919.84]  And we have this array of five kind of pointers into the DOM.
[919.94 --> 921.18]  So we just run through the array.
[921.72 --> 923.58]  Keeps it very simple and fast.
[924.40 --> 924.42]  Interesting.
[924.42 --> 929.02]  And so how would you manage kind of dynamic HTML, right?
[929.02 --> 934.12]  Or what feels like dynamic like content, if the references are, if you're kind of always
[934.12 --> 936.64]  relying on the references to, to be the same.
[936.74 --> 940.72]  Because in theory, I could just pass a JavaScript template into a JavaScript template into a
[940.72 --> 941.76]  JavaScript template, right?
[941.90 --> 942.08]  So.
[942.64 --> 947.28]  So yeah, it turns out that there's a lot less dynamicism in templates than you might think,
[947.30 --> 949.82]  or that a lot of systems are kind of built to expect, right?
[949.82 --> 954.44]  Like if you look at a template in a component or something, a lot of it is static, even in JSX,
[954.52 --> 954.72]  right?
[955.34 --> 957.96]  And then you have limited number of, of, of bindings there.
[957.96 --> 962.34]  And so where you do have dynamicism, like looping and conditionals and whatnot, that
[962.34 --> 965.02]  is happening kind of bounded inside of an expression, right?
[965.04 --> 969.64]  So you have this like static outside, then you have an expression and that expression
[969.64 --> 974.32]  might have some dynamicism, but it will oftentimes produce another template, which itself is,
[974.40 --> 977.60]  you know, a lot of static and then expressions in it.
[978.04 --> 978.56]  That makes sense.
[978.86 --> 981.82]  So 99% of the cases are handled by that, right?
[981.90 --> 984.94]  Just like template composition and conditional there handles all that.
[984.94 --> 989.30]  There are some cases where things get very dynamic and you might want to accept HTML as
[989.30 --> 995.34]  a string and put it in a spot, or you might want to do some things that like we kind of
[995.34 --> 999.70]  don't support because we're, we're doing like template cloning, which is like, you might want to have a
[999.70 --> 1001.44]  dynamic tag name, right?
[1001.52 --> 1005.48]  And that kind of is not a kind of thing you can like put into an HTML template element
[1005.48 --> 1008.42]  and clone because in the DOM, you can't change the tag name of an element.
[1008.42 --> 1011.90]  So we kind of have two ways of handling that stuff, which is very, very dynamic.
[1012.02 --> 1013.18]  It actually ends up being unsafe.
[1013.68 --> 1018.28]  Like one nice thing about lit is that because we're doing this template prep template cloning
[1018.28 --> 1021.48]  thing, it's very resistant to cross-site scripting attacks.
[1021.92 --> 1024.92]  You can almost think about this as like SQL prepared statements.
[1025.18 --> 1025.26]  Yeah.
[1025.30 --> 1029.18]  You're also enforcing like people to not do use anti-patterns, right?
[1029.20 --> 1035.32]  And also just like react, their whole like unsafe, you know, dangerously set inner HTML,
[1035.32 --> 1038.04]  you know, like I have a fun song about that.
[1038.04 --> 1041.50]  Every time I see that, every time I see that method, I think of you singing that.
[1042.08 --> 1045.68]  It's like, I don't think we have it in the soundboard, but yeah, we should add it to the
[1045.68 --> 1045.90]  soundboard.
[1045.90 --> 1050.34]  Your voice in my head, dangerously set inner HTML.
[1051.94 --> 1055.64]  What's so dangerous about HTML's inner parts?
[1055.64 --> 1059.02]  What's so dangerous about HTML's inner parts?
[1059.02 --> 1059.82]  Inner parts.
[1060.26 --> 1060.70]  Anyway.
[1061.22 --> 1066.50]  Your head, your voice is, that documents that react function for me now, by the way.
[1066.52 --> 1067.74]  Oh my God, that's hilarious.
[1068.04 --> 1069.88]  Song as a service.
[1070.84 --> 1071.16]  But yeah.
[1071.54 --> 1072.70]  No, so, so, so yeah.
[1072.84 --> 1076.44]  React's dangerously set inner HTML is like an example of that.
[1076.70 --> 1076.94]  Yeah.
[1077.10 --> 1078.78]  We have a similar thing.
[1079.08 --> 1082.34]  We, we probably should have named it longer and more obtuse.
[1082.50 --> 1084.00]  We could, we just call it unsafe HTML.
[1084.70 --> 1086.72]  And we recommend not using it.
[1086.94 --> 1091.06]  I mean, we call it, you could rename it like, you know, don't use this API or your B fire.
[1091.06 --> 1095.94]  At Google, we actually don't even import it into our repo.
[1096.18 --> 1096.98]  It's just not available.
[1097.22 --> 1097.30]  Wow.
[1097.38 --> 1100.24]  Because in Google, there's like a whole HTML sanitizer thing you're supposed to use.
[1100.28 --> 1101.76]  So we force you to use that.
[1102.02 --> 1105.00]  It's like strict mode for lit, you know, that's, that's, I think it's a good thing.
[1105.00 --> 1109.78]  And so I guess just kind of like jumping up a few layers on the stack here, you know, so
[1109.78 --> 1113.84]  there's some core principles that, you know, lit is really centered around.
[1114.10 --> 1116.26]  I'd love to kind of chat with you about that.
[1116.26 --> 1121.90]  So, you know, you know, I'd say the maybe umbrella principle is like just what you need
[1121.90 --> 1122.74]  and nothing more.
[1122.74 --> 1125.00]  So could you kind of speak to that, Justin?
[1125.64 --> 1130.94]  Yeah, I think maybe like the overriding principle is based around web components interoperability,
[1131.10 --> 1131.28]  right?
[1131.62 --> 1137.94]  And so the biggest thing is that lit and polymer before it are implementation details of your
[1137.94 --> 1138.28]  component.
[1138.60 --> 1144.36]  Like if you're using a lit based web component and you're not using lit yourself, you shouldn't
[1144.36 --> 1146.62]  really be aware that the thing is made with lit.
[1147.14 --> 1151.56]  Web components give you like a strong interface and a defined life cycle and the browser takes
[1151.56 --> 1154.86]  care of that and what you see using the thing is just an HTML element.
[1155.36 --> 1157.14]  And you're like, wow, this is a cool HTML element.
[1157.24 --> 1160.72]  I wish HTML had it, but now install it from NPM, right?
[1160.92 --> 1167.94]  So that kind of implementation detail and kind of transparency there is like the P0 of principles
[1167.94 --> 1168.34]  there.
[1168.74 --> 1170.96]  After that, we try to be minimal.
[1171.72 --> 1175.78]  So we basically try to give you just the things that you want in order to make writing web
[1175.78 --> 1179.42]  components easy and that you get fast and lightweight components.
[1179.42 --> 1182.64]  So we give you declarative templating, which we've talked about.
[1182.76 --> 1184.72]  We give you declarative reactive properties.
[1185.56 --> 1190.94]  So using decorators or like another form without decorators, you can declare properties of your
[1190.94 --> 1192.84]  element that will cause it to re-render when they change.
[1193.42 --> 1196.00]  We also give you a very easy way to write styles in line.
[1196.12 --> 1198.64]  So we get single file components, but they're in JavaScript.
[1198.90 --> 1202.70]  So you'll have CSS backticks for your styles and HTML backticks for your templates.
[1203.06 --> 1205.14]  And we'll attach those styles to the shadow root.
[1205.24 --> 1205.72]  They're scoped.
[1205.72 --> 1210.26]  We always support all the most modern CSS because we don't do anything with the CSS except for,
[1210.50 --> 1211.80]  you know, attach it to the DOM.
[1212.46 --> 1216.70]  So yeah, reactive properties, easy way to write styles, declarative templates.
[1217.32 --> 1218.58]  That's really most of it.
[1218.64 --> 1223.28]  We give like a lifecycle that's a little more fine-grained than the web component lifecycle.
[1223.58 --> 1228.66]  So we give like things like update, which will in turn call render, which is where you write
[1228.66 --> 1232.54]  your template and we'll get like updated, which goes after your element has updated.
[1232.54 --> 1234.00]  So just a little helpers.
[1234.08 --> 1238.00]  And we've heard from people that they want to write like no library web components.
[1238.00 --> 1239.74]  So they start writing their own base class.
[1240.44 --> 1245.88]  And then they realize that after they do everything they want to, to have a nice base class to use,
[1245.92 --> 1247.14]  they're basically reinventing lit.
[1247.48 --> 1252.28]  So we like to think that it's like unopinionated enough that basically everybody would eventually
[1252.28 --> 1255.38]  discover the same things that we give to developers.
[1256.16 --> 1258.90]  So lit is the base class for writing web components?
[1259.42 --> 1259.58]  Yeah.
[1259.78 --> 1260.20]  Lit element.
[1260.20 --> 1260.64]  Yeah.
[1260.86 --> 1266.86]  And I hope that one day, you know, most or all of what lit element gives you is actually
[1266.86 --> 1271.58]  standardized into some higher level, more featureful base class in the browser.
[1272.02 --> 1272.26]  Yeah.
[1272.78 --> 1273.88]  That's really great to hear.
[1273.98 --> 1277.22]  And I know we'll chat about standards at some point in this show.
[1277.30 --> 1281.50]  And I'd love to kind of dig into how much of this kind of shifting left that, you know,
[1281.52 --> 1284.70]  is going to continue to happen, I think, as the platform continues to evolve.
[1284.70 --> 1287.62]  But I think so one of your claims is simple, right?
[1287.70 --> 1289.94]  That lit is simple and that it's also fast.
[1290.18 --> 1294.82]  And I, you know, for anyone who hasn't seen what a lit element looks like, highly encourage
[1294.82 --> 1296.18]  you to go to lit.dev.
[1296.44 --> 1301.30]  And it's like you spend like 10 minutes reading the docs and you're pretty much ready to go
[1301.30 --> 1302.40]  and start creating elements.
[1302.40 --> 1304.54]  Like it's super intuitive, super straightforward.
[1304.54 --> 1310.84]  I would say you should add simple AF to your claim of being simple because it like it's
[1310.84 --> 1311.38]  pretty simple.
[1311.54 --> 1315.90]  And so how did you, you know, what was that like for you kind of trying to, I mean, it
[1315.90 --> 1319.22]  takes a lot of constraints to design an API that feels simple and intuitive.
[1319.22 --> 1321.04]  It's much harder than it looks.
[1321.22 --> 1324.46]  So I'm just curious if you could kind of share some insights onto that.
[1324.82 --> 1327.92]  I think it helped a little bit that we went slowly.
[1327.92 --> 1334.66]  So, you know, at the event where I introduced lit.html, the template library, we were also
[1334.66 --> 1339.64]  introducing Polymer 3, which was the version of Polymer that put your components into JavaScript
[1339.64 --> 1340.06]  modules.
[1340.54 --> 1343.84]  And I had like made the first version of lit like two weeks prior to that.
[1344.10 --> 1347.86]  You know, I was leading the tools team and like doing an automatic conversion of Polymer
[1347.86 --> 1350.54]  from HTML mod imports to JavaScript modules.
[1351.08 --> 1355.16]  So it was kind of like this little side project that some people were like, whoa, this is really
[1355.16 --> 1355.34]  cool.
[1355.38 --> 1356.30]  You need to talk about this.
[1356.30 --> 1361.24]  But, you know, we were very aware and very cautious that we were like throwing churn onto
[1361.24 --> 1362.04]  our audience.
[1362.34 --> 1364.74]  And we were like releasing Polymer 3 on the same day.
[1365.26 --> 1368.46]  So we didn't go all in on lit for like a little while.
[1368.82 --> 1370.16]  And we only had the template system.
[1370.24 --> 1371.82]  We didn't have a base class that called it yet.
[1372.60 --> 1379.54]  So we wrote by hand multiple times when we needed to do examples, like a base class that
[1379.54 --> 1380.16]  used templates.
[1380.36 --> 1384.04]  And that base class at the time was something around like less than a dozen lines.
[1384.04 --> 1388.46]  And the way it worked is like when a property changed and you would write a getter and setter
[1388.46 --> 1389.32]  instead of a decorator.
[1389.52 --> 1392.08]  And the setter would say like re-render the element.
[1392.32 --> 1396.82]  And the re-render the element call would, you know, basically go like, am I already re-rendering
[1396.82 --> 1397.60]  if not return?
[1398.48 --> 1403.36]  And I mean, if so return, and if not a way to promise that way you could batch up a bunch
[1403.36 --> 1403.80]  of things.
[1403.80 --> 1408.26]  And then after that promise is awaited, call the render method and render it into the shadow
[1408.26 --> 1408.48]  root.
[1409.02 --> 1412.42]  And it was really like, like I said, 10 lines, 12 lines.
[1412.70 --> 1414.40]  We wrote this over and over and over again.
[1414.44 --> 1415.20]  And it was so small.
[1415.30 --> 1416.68]  We were like, does it really need a base class?
[1416.70 --> 1418.70]  Or can we just tell people this pattern?
[1419.06 --> 1422.64]  So I think like we resisted even having lit element for a little while.
[1423.04 --> 1427.10]  And I think that kind of led to like, well, if we're going to have it, we should at least
[1427.10 --> 1428.50]  keep it as small as possible.
[1428.50 --> 1433.72]  And we kind of only added the things we absolutely needed to get elements done.
[1434.50 --> 1438.56]  What are some of the other things that you have added beyond lit element?
[1438.92 --> 1442.62]  I'm looking at the API docs, and there's a few other things listed.
[1442.94 --> 1445.20]  What has proved to be absolutely necessary?
[1445.68 --> 1446.08]  Let's see.
[1446.18 --> 1447.60]  So we've added some decorators.
[1447.82 --> 1453.66]  I'm very excited, by the way, that decorators are landing now in TypeScript and Babel.
[1453.76 --> 1457.32]  And I've heard rumors of implementation starting to be done in V8.
[1457.32 --> 1461.52]  So these decorators help you do, you know, we have at property to declare a property.
[1461.80 --> 1464.20]  At state kind of gives you internal reactive state.
[1464.54 --> 1469.04]  There's a few things with, you know, adding event options to event listener methods or
[1469.04 --> 1470.46]  querying the shadow root.
[1471.04 --> 1474.40]  The nice thing about those is they're kind of, we try to structure our libraries so everything
[1474.40 --> 1474.96]  is opt-in.
[1475.50 --> 1478.32]  So if you want the query decorator, you got to import that from another module.
[1478.76 --> 1482.10]  And even if you're not using a bundler, that means you get kind of tree shaking for free,
[1482.16 --> 1482.32]  right?
[1482.34 --> 1484.08]  Like if you don't import it, it doesn't load.
[1484.08 --> 1489.10]  Let's see some other stuff that people aren't too aware of often when they start building
[1489.10 --> 1489.60]  their own class.
[1489.88 --> 1491.10]  So attribute reflection.
[1491.64 --> 1496.74]  Like if you use certain elements in the DOM and you set a property on them, like you set
[1496.74 --> 1500.02]  ID or title, it'll reflect to the attribute and vice versa.
[1500.70 --> 1504.66]  So we will keep attributes and properties in sync and let you kind of specify the attribute
[1504.66 --> 1505.46]  name for a property.
[1506.12 --> 1511.48]  We'll also do things like custom elements can kind of upgrade late, meaning you can load their
[1511.48 --> 1513.56]  definition after you already have the element in the DOM.
[1514.12 --> 1517.58]  And that means you could have set properties on this thing that the element cares about.
[1518.14 --> 1522.24]  So when we upgrade, we'll go look for those properties and kind of pull them off and put
[1522.24 --> 1524.94]  them into the reactive property system.
[1525.42 --> 1526.44]  Bookkeeping and stuff like that.
[1526.52 --> 1531.48]  So there are a lot of things that you wouldn't know you needed until you hit the need for it.
[1531.78 --> 1536.24]  And so one way of thinking about like lit element is just a collection of those lessons that
[1536.24 --> 1540.26]  we've learned, you know, the hard way as people have hit these needs and we added it in.
[1540.26 --> 1543.64]  And then another fun thing that I like, actually probably two things here.
[1543.72 --> 1546.76]  One, we have a base class that actually sits under lit element.
[1547.22 --> 1548.26]  It's called reactive element.
[1548.72 --> 1553.56]  And it contains all of the reactivity, but not the built-in lit template system.
[1553.94 --> 1558.82]  And we've actually built React and Preact base classes where you can use React to render
[1558.82 --> 1559.48]  your web component.
[1559.96 --> 1562.62]  And building those is just a few lines of code.
[1562.82 --> 1565.42]  You just call React render in your update method.
[1565.80 --> 1569.98]  And then another thing we added with lit 2 that came out two years ago, I think, is this
[1569.98 --> 1571.06]  thing called reactive controllers.
[1571.44 --> 1577.16]  And you can think of them as like custom React hooks in a way, but without the hook magic
[1577.16 --> 1578.84]  and laws of hooks and stuff like that.
[1578.90 --> 1583.76]  And so they're just simple objects that you can hook up to a class and they hook the lifecycle.
[1584.54 --> 1585.70]  And that's basically where we're at.
[1585.78 --> 1589.42]  Everything else we've added since then has kind of been in separate modules, like new controllers,
[1589.58 --> 1591.34]  new decorators, things like that.
[1591.98 --> 1597.02]  You alluded to interactability with frameworks like React and things like that.
[1597.02 --> 1600.76]  And it leads to a question that I've had sort of stewing, right?
[1600.84 --> 1608.88]  So much of the front end ecosystem has drifted towards these more comprehensive application
[1608.88 --> 1609.42]  frameworks.
[1610.22 --> 1616.50]  And both we've seen that kind of happening at the base level where, you know, Vue and React
[1616.50 --> 1620.84]  and other things are like absorbing more and more pieces of what you might need to create
[1620.84 --> 1621.34]  an application.
[1621.34 --> 1625.30]  But also we've seen a lot of innovation at that meta framework level of, okay, now we
[1625.30 --> 1628.12]  have Next.js or Next.js or what have you.
[1628.46 --> 1633.14]  That's really about a lot of the different pieces that go into structuring an application.
[1633.66 --> 1640.58]  It seems that Lit is really going after that very fine grained, build me a component, build
[1640.58 --> 1641.36]  another component.
[1641.36 --> 1649.06]  Are there application frameworks that have been built on top of Lit that people end up
[1649.06 --> 1649.56]  using?
[1649.96 --> 1655.66]  Do they end up, like if I were to try to build a whole web application using Lit, is there
[1655.66 --> 1659.50]  an ecosystem around it that provides some of that default structure or am I building it
[1659.50 --> 1659.98]  all myself?
[1660.26 --> 1665.28]  I think it's still a little bit nascent on the like complete out of the box application
[1665.28 --> 1666.50]  framework kind of thing.
[1666.50 --> 1672.10]  We see most of our users kind of picking and choosing libraries to put together with Lit
[1672.10 --> 1673.12]  to build their application of.
[1673.34 --> 1680.14]  And the two most common things are, you know, a router, if they're doing a single page app
[1680.14 --> 1682.52]  routing and a state management system.
[1682.88 --> 1690.36]  So we see like out there, people have built Lit adapters for Redux and MobX and Apollo,
[1690.76 --> 1691.36]  things like that.
[1691.48 --> 1693.78]  And there are, you can use any router you want.
[1693.78 --> 1698.74]  We also have a router in our lab system that's a little tailored to Lit.
[1699.14 --> 1704.16]  And yeah, so I think we've kind of self-selected for a crowd that likes to pick and choose their
[1704.16 --> 1705.02]  libraries that way.
[1706.02 --> 1711.40]  Internally at Google, we've, you know, had a lot of experience with like helping teams
[1711.40 --> 1716.94]  and kind of collecting what, you know, we hope will form an application framework that
[1716.94 --> 1720.54]  I jokingly call Lit AF, but will probably not be called that.
[1721.40 --> 1722.92]  Lit application framework.
[1722.92 --> 1723.48]  Why not?
[1723.78 --> 1727.40]  You just name it that and let other people interpret, oh, it's Lit AF.
[1727.66 --> 1727.82]  Yeah.
[1727.84 --> 1729.16]  Why did your mind go there?
[1729.28 --> 1730.64]  My mind didn't go there.
[1730.78 --> 1732.96]  Just call it Laugh, you know?
[1733.08 --> 1733.26]  Yeah.
[1733.66 --> 1735.64]  Can you still get the .af domain name?
[1735.98 --> 1736.96]  I don't know if that's...
[1736.96 --> 1737.00]  No.
[1738.48 --> 1738.84]  Yeah.
[1738.84 --> 1739.24]  Where was I going?
[1739.34 --> 1739.50]  Yeah.
[1739.60 --> 1743.92]  So, you know, we have a lot of experience with internal frameworks at Google that do like
[1743.92 --> 1744.52]  incremental.
[1744.94 --> 1746.08]  They do SSR.
[1746.42 --> 1750.32]  They'll help do dynamic bundling by tracking what components are actually used in any request.
[1750.32 --> 1756.42]  They'll do incremental on-demand hydration, data fetching based on what components and
[1756.42 --> 1760.44]  what data actually got used, routing and a whole bunch of stuff like that.
[1760.72 --> 1764.14]  And we have some prototypes of those types of things we'd like to get out there.
[1764.52 --> 1765.60]  That's one approach, right?
[1765.64 --> 1769.10]  That's for the people who might want to choose Lit for both components and the whole app and
[1769.10 --> 1769.74]  do everything there.
[1769.74 --> 1774.16]  But at the same time, like, you know, web components, their main goal is to be interoperable.
[1774.68 --> 1779.66]  And so we want people to be able to use web components and Lit inside of React and Vue
[1779.66 --> 1781.56]  and Angular and inside of these other meta frameworks.
[1781.96 --> 1785.12]  So we have been working on that integration as well.
[1785.24 --> 1787.00]  So we have SSR for Lit.
[1787.70 --> 1792.86]  And currently a third party has built Vue integration for Nuxt.
[1793.08 --> 1795.04]  And we have been working on Next integration.
[1795.04 --> 1800.58]  So you basically can use your web components inside of your JSX templates.
[1800.90 --> 1807.26]  If you add a config plugin to Next, we will like SSR those and then hydrate them when the
[1807.26 --> 1808.30]  rest hydrates on the client.
[1808.72 --> 1812.58]  So I think like rather than forcing everybody to go into a full stack Lit framework, we want
[1812.58 --> 1816.08]  to have that option, but we want to let a lot of people, you know, especially because
[1816.08 --> 1821.64]  one of the biggest areas of success we have with Lit is in design systems for teams that
[1821.64 --> 1822.18]  need to vended.
[1822.24 --> 1822.98]  No, that makes sense.
[1822.98 --> 1826.00]  Yeah, they need a vended design system to their Vue team and the React team and whatever.
[1826.12 --> 1827.76]  And those teams are using Next and Nuxt.
[1827.94 --> 1829.80]  And we want to make all that work.
[1830.36 --> 1830.46]  Yeah.
[1830.54 --> 1836.54]  Having a truly cross framework design system sounds phenomenal for a larger company that's
[1836.54 --> 1840.36]  not only doing that, but maybe they have, you know, their WordPress site doing something
[1840.36 --> 1843.84]  else and other places like they've got lots of different front end frameworks.
[1844.28 --> 1848.84]  Yeah, it's like it's actually a pretty bold assumption to even make when, you know, you think,
[1848.84 --> 1850.18]  hey, you're working at the same company.
[1850.18 --> 1853.58]  Maybe this company should be using everyone should be on Angular.
[1853.82 --> 1854.72]  Everyone should be on React.
[1854.82 --> 1859.28]  And it's like, no, actually, there's like four or five different like front end stacks
[1859.28 --> 1860.78]  depending on what part of the company.
[1861.10 --> 1865.32]  And so, you know, and that's a big challenge that design system teams have often is like,
[1865.36 --> 1869.02]  you know, like there's sometimes there's the new design system and then there's like,
[1869.02 --> 1872.90]  oh, we have to kind of we can't serve every customer with like React.
[1873.06 --> 1873.20]  Right.
[1873.24 --> 1875.92]  But, you know, that's for me what web components were.
[1876.30 --> 1877.38]  That was kind of the goal.
[1877.44 --> 1878.04]  That was the dream.
[1878.12 --> 1879.32]  That was like, yeah, that's the dream.
[1879.50 --> 1880.00]  Why they were created.
[1880.16 --> 1880.42]  Right.
[1880.48 --> 1884.62]  So to be able to kind of really be that baseline because it's just leveraging the platform.
[1885.38 --> 1889.60]  And so it's really great to hear Lit is, you know, just kind of enabling that use
[1889.60 --> 1890.78]  case more at scale.
[1890.98 --> 1894.20]  And so can we talk a little bit about like who's using this?
[1894.28 --> 1899.60]  And for me, like I was amazed to see the number of like big companies that have like adopted
[1899.60 --> 1899.98]  Lit.
[1900.14 --> 1903.50]  Just seeing some really big names on your on your website, including a company that I
[1903.50 --> 1903.86]  work for.
[1903.94 --> 1907.54]  And I didn't even know that we use Lit because it's being used on another side of the company.
[1907.54 --> 1911.58]  But for like the design system that's supposed to be the future design system, supposedly,
[1911.82 --> 1913.52]  you know, so just great.
[1914.20 --> 1914.32]  Yeah.
[1914.38 --> 1919.10]  So who's who's using you talk about the adoption and who's using it and how it's helped teams?
[1919.76 --> 1919.92]  Yeah.
[1919.92 --> 1923.72]  Um, so a couple of things here on the design system front, we're really trying to kind
[1923.72 --> 1925.72]  of lean into that area of success there.
[1925.76 --> 1929.58]  And we've created these framework wrappers, which like even though web components are naturally
[1929.58 --> 1933.72]  interoperable, a lot of times tooling and type checkers and linters and stuff, you know,
[1933.72 --> 1935.34]  don't have to do with web components.
[1935.34 --> 1938.98]  So we've created a react and view and working on angular wrappers.
[1939.30 --> 1943.42]  That way it plugs into their type system type checker template type checker stuff.
[1943.70 --> 1947.44]  And so, yeah, a lot of our customers are using Lit for design systems.
[1947.44 --> 1957.74]  So Adobe, Alaska Airlines, IBM, Cisco, ING is a huge one, Red Hat, SAP, shoelace components.
[1957.74 --> 1960.82]  If people have heard of that one, it's like a modern bootstrap, but web components.
[1962.14 --> 1964.44]  VMware, the Internet Archive.
[1964.90 --> 1968.96]  There's just a ton of these that have Reddit and Just Eat Takeaway.
[1968.96 --> 1972.96]  I can't even recall them all that have built design systems that way.
[1973.64 --> 1973.78]  Yeah.
[1973.80 --> 1977.14]  And we've also seen, you know, very interesting kind of application uses here too.
[1977.32 --> 1982.12]  Like Chrome, the parts of the settings UI and dev tools is built with Lit.
[1982.46 --> 1987.58]  Firefox migrated their UI from Zool to web components a while back.
[1987.64 --> 1990.92]  And I noticed recently that they're now starting to port some of their web components to Lit.
[1991.34 --> 1993.28]  So desktop applications there.
[1993.56 --> 1995.98]  Chrome OS, like a lot of their built-in apps are built with Lit.
[1995.98 --> 2000.32]  But in complex apps, like Photoshop for the web is built with Lit.
[2000.54 --> 2000.72]  Yeah.
[2000.80 --> 2001.72]  And that's huge.
[2001.90 --> 2007.76]  And for everyone who's a listener on the show, I have a kind of a backlog item to get the Adobe team on here.
[2007.96 --> 2011.56]  So stay tuned, fingers crossed, on that show soon.
[2012.16 --> 2015.78]  But, you know, for me, like there's two elements here which are fascinating.
[2016.12 --> 2020.90]  One is, you know, this kind of investment and just like big companies taking bets on the platform
[2020.90 --> 2026.92]  and also wanting to kind of get the tailwind of leveraging the platform and the stabilization factor
[2026.92 --> 2029.10]  and like the cost factor, right?
[2029.14 --> 2029.98]  Like let's be realistic.
[2030.18 --> 2035.54]  Like at the end of the day, these are corporations and like it is just cheaper to build it once and distribute it.
[2035.54 --> 2039.10]  And so for me, like web components are like the sleeper hit.
[2039.32 --> 2041.32]  I was chatting with Alex about this.
[2041.86 --> 2042.98]  Alex Russell, to be specific.
[2043.32 --> 2053.30]  And he mentioned to me the last time we spoke about web components that 17% of traffic that they are Google bots report back, like 17% of...
[2053.30 --> 2054.10]  Page views on Chrome.
[2054.24 --> 2054.40]  Yeah.
[2054.46 --> 2061.36]  So page views on 17% of page views on Chrome contain web components, which I mean, that's a humongous part of the Internet.
[2061.36 --> 2069.54]  And so considering how large of a surface that is and how little we hear about web component usage in the JavaScript community,
[2069.62 --> 2075.98]  I mean, those are just like it's like the reality disconnect that like is JavaScript, you know?
[2076.46 --> 2079.60]  And so, yeah, I'm very excited by those numbers.
[2079.78 --> 2083.60]  And I think that's like healthy for the web to have that level of stabilization.
[2083.60 --> 2087.00]  Can I ask a question about that?
[2087.18 --> 2093.14]  And it gets into, so how is Lit as a project governed and run?
[2093.30 --> 2102.14]  Because it makes me anxious to have something that is becoming a big part of web infrastructure owned by a corporation,
[2102.74 --> 2107.60]  particularly one that has a little bit of a reputation for shutting down projects,
[2108.28 --> 2110.70]  even when they're used by millions of happy users.
[2110.70 --> 2113.38]  So how is that being handled with Lit?
[2113.58 --> 2119.28]  That's actually a very interesting question because, you know, I think that consumers and tech reporters and stuff
[2119.28 --> 2122.24]  are not the only ones kind of concerned about these topics, right?
[2122.32 --> 2126.32]  You know, to be frank, as an employee, you wonder about these things too.
[2126.78 --> 2130.70]  And we do have some, you know, very, very large companies making huge bets, right?
[2130.74 --> 2133.46]  Like Photoshop isn't the only app that Adobe is building with Lit.
[2133.90 --> 2136.98]  So we take that concern seriously on our team.
[2136.98 --> 2141.14]  And there's a couple things that we're trying to do to kind of mitigate that.
[2141.44 --> 2143.98]  One of them is just keeping Lit simple, right?
[2144.04 --> 2148.94]  Like the template system is a single 1400 line file that has tons of comments.
[2149.32 --> 2156.52]  And we just started making a big like how it works kind of after the fact design doc so that people can kind of come up to speed on it.
[2156.52 --> 2160.94]  And then reactive elements, other 600 lines or something, again, heavily commented.
[2161.48 --> 2164.22]  We want people, we want Lit to have low lock-in.
[2164.58 --> 2170.30]  If the Lit team were to disappear one day, we want either the community to be able to very easily jump in and maintain it
[2170.30 --> 2176.90]  or for, you know, any almost like single person to be able to fork the project and keep their fork going.
[2177.46 --> 2181.42]  This is also why we keep Lit as an implementation detail of the components, right?
[2181.44 --> 2183.84]  We don't want Lit to be viral within your app.
[2183.84 --> 2188.06]  You know, because we want to be able to migrate component by component to or from Lit.
[2188.50 --> 2193.04]  And so hopefully that's a big mitigation, like risk mitigation factor here is that, you know,
[2193.08 --> 2195.70]  we want it to be easy to adopt Lit and to move away from it.
[2196.04 --> 2200.20]  Like we think that's the morally correct way to build libraries like this.
[2200.80 --> 2204.84]  And the other thing that we're looking into is how to do more open governance.
[2204.84 --> 2214.48]  So this year, and especially since the layoffs that did hit our team a little bit, we have been putting like a much bigger and bigger emphasis on open development practices.
[2214.82 --> 2220.18]  So open engineering meetings, you know, doing our developing developer chat and discord, you know,
[2220.18 --> 2229.08]  basically trying to make it so that any person who wants to can be as much to on the same level as our actually Google employed core team as possible.
[2229.46 --> 2236.46]  And then going further than that, we're looking into what it would look like to put Lit into actual open governance.
[2236.46 --> 2239.08]  I haven't seen a ton of projects like do this yet.
[2239.12 --> 2241.46]  So we're kind of like asking around for a lot of advice and help.
[2241.60 --> 2247.84]  And, you know, we're trying to talk to our big customers like, you know, do they want to have a seat at the table with a technical steering committee?
[2247.84 --> 2252.66]  And can we put, you know, the keys to all the resources and copyrights and stuff like that?
[2253.00 --> 2255.70]  So I don't know how long that thing might take.
[2255.70 --> 2261.66]  And we have had like people from the OpenJS Foundation come to us in years past and be like, do you want to do this?
[2261.72 --> 2265.50]  And we've been like, yeah, theoretically, yes, but it sounds like a lot of work.
[2265.50 --> 2278.16]  And I think we're more motivated to do this now to give like everybody, like our team, Google, the customers, like individual developers, everybody, like, you know, more stake, more say and better peace of mind.
[2278.70 --> 2281.22]  Yeah, I mean, I think that's that's super cool.
[2281.38 --> 2285.54]  And I think like the output for me is like our web components.
[2285.80 --> 2288.36]  And yes, there is a library, but it's really tiny.
[2288.60 --> 2295.24]  And I'm hoping that from everything you've said that like as Lit continues to evolve, that library just gets smaller and smaller.
[2295.24 --> 2296.26]  Or smarter and smarter.
[2296.26 --> 2296.66]  Right.
[2296.78 --> 2308.28]  And so I think teams are not going to be dealing with like compatibility issues and that kind of, you know, the cost of maintaining framework code, really, you know, because like there's a real cost there.
[2308.28 --> 2311.70]  And so very excited to hear those goals.
[2312.20 --> 2320.42]  And, you know, just getting back to the web component discussion, because like that is really important, like 70% of page views on Chrome, like that's a lot of adoption.
[2320.42 --> 2334.48]  And so what do you think is kind of behind, like there's the community, like mindshare, right, the like thought leadership and, you know, and what are some obstacles towards like getting developers to really think about web component first?
[2334.62 --> 2337.98]  And if web components don't meet my use case, then I'll go on to something else.
[2337.98 --> 2338.20]  Right.
[2338.20 --> 2339.84]  So like, how do we flip that?
[2340.58 --> 2344.92]  How do we flip the script so that like we're thinking about building for the platform first?
[2345.04 --> 2346.50]  Like very curious to hear your thoughts.
[2347.06 --> 2347.22]  Yeah.
[2347.36 --> 2349.88]  The ecosystem question here is very tricky.
[2349.98 --> 2355.46]  Like I think if you look at raw numbers, there are a lot of numbers that indicate that web components are successful in different ways.
[2355.52 --> 2359.52]  So there's the Chrome user metrics that show it's on a ton of page views.
[2359.52 --> 2366.36]  There's also like NPM, you know, we're, we're doing more than a million downloads a week now, which puts us a little bit behind Preact.
[2366.60 --> 2378.96]  So it's like React, Vue, Angular, Preact, us, I think, you know, these numbers objectively, like, you know, depending on how much you think these are good numbers or whatever, you know, put you kind of above other frameworks that have a lot more hype.
[2379.14 --> 2381.54]  So there's a question, like, are these bad numbers to be looking at?
[2381.60 --> 2383.34]  Like, what are the numbers we should be looking at?
[2383.38 --> 2388.18]  We also have a lot of GitHub stars or whatever, but you don't see the buzz on, you know, Twitter or whatever.
[2388.18 --> 2394.14]  I think some of this is because like we're a little bit split in terms of marketing and identity.
[2394.90 --> 2398.48]  Like, should we be leading with web components or should we be leading with lit?
[2398.70 --> 2400.18]  There's like pros and cons each way.
[2400.26 --> 2409.84]  If you lead with web components and people go to like MDN and look at the low level web components that APIs, they're like, well, how do I build a full app out of this or even a full component?
[2409.98 --> 2411.66]  This is, it's going to take too much boilerplate.
[2411.66 --> 2417.56]  If you lead with lit, sometimes people lose the fact that lit's there to help you make web components.
[2418.18 --> 2420.92]  And then they only just compare lit one to one with a framework like React.
[2421.38 --> 2435.64]  And so there is like this really tricky threading the needle kind of marketing point where you want to market, you know, the good DX ways of doing these things and potentially other, you know, friendly frameworks out there like Stencil.js and Fast and whatnot.
[2436.14 --> 2436.36]  Right.
[2436.36 --> 2440.92]  But you also want to market web components as like a low level functionality.
[2440.92 --> 2445.78]  And I think like figuring that out is going to be the thing that unlocks the next kind of level of growth.
[2446.30 --> 2451.52]  I feel like you just have such a good line with lit there and puns and marketing to developers, right?
[2451.54 --> 2457.86]  Like I'm just imagining this set of short form videos where you're like doing this, you know, rapid web component development.
[2458.00 --> 2460.62]  Wait, it's just this code and it's just a web component?
[2460.74 --> 2461.30]  That's lit.
[2461.30 --> 2469.58]  Like, you know, you could have this like whole branded that's lit kind of feel around it that would give it this energy.
[2469.76 --> 2472.20]  But then you show, oh, but it's just a web component.
[2472.42 --> 2473.68]  Oh, but it can do that.
[2473.96 --> 2476.04]  Oh, it's only five kilobytes.
[2476.20 --> 2480.24]  Oh, like all the different selling points of how cool this thing is.
[2480.62 --> 2481.16]  I don't know.
[2481.24 --> 2484.64]  Like there's not like a slant to web components.
[2484.76 --> 2485.70]  They're not sexy.
[2485.70 --> 2491.76]  They're low level and boring and great because they can go everywhere and it's just the platform.
[2491.88 --> 2492.92]  But like, I don't know.
[2493.04 --> 2495.78]  I feel like you've got a much better story if you lean into lit.
[2496.36 --> 2496.72]  Certainly.
[2496.94 --> 2499.74]  I mean, this is one reason why we made the lit brand.
[2500.04 --> 2504.38]  So it used to be that we just had lit.html as a template library and lit.element was the base class.
[2504.48 --> 2506.18]  And they were kind of, they even had separate websites.
[2506.64 --> 2507.84]  I think that was very confusing.
[2508.46 --> 2513.10]  But it kind of spoke to us kind of saying, these are low level pieces you can put together as you want.
[2513.10 --> 2516.94]  But we heard from a lot of potential customers and consultants and stuff.
[2517.18 --> 2522.22]  Like you need one website that puts everything together, that has one pitch that like, you know,
[2522.22 --> 2528.72]  some enterprise IT department can compare in a way they understand against frameworks like React and Angular.
[2529.28 --> 2531.40]  So we went through like this branding exercise.
[2531.54 --> 2534.28]  We were going to try to come up with a new name because I was like, we can't just call it lit.
[2534.40 --> 2536.54]  And they came back and they were like, everybody always just calls it lit.
[2536.60 --> 2537.26]  You have to call it lit.
[2538.10 --> 2539.56]  That's a wonderful name.
[2541.02 --> 2542.84]  It's such an accident name.
[2543.10 --> 2547.00]  So like, yeah, that only just happened kind of like during the pandemic.
[2547.00 --> 2554.26]  So we actually are only relatively fresh out of the gate with like a unified brand and a unified messaging on that.
[2554.66 --> 2557.44]  So I think there's still a lot to do in utilizing that.
[2557.54 --> 2558.52]  You need some DevRel people.
[2558.88 --> 2560.00]  Like this has potential.
[2560.62 --> 2560.76]  Yeah.
[2561.44 --> 2562.12]  Well, yeah.
[2562.22 --> 2566.18]  I mean, I love the little flame, the like blue, the little flame that you made.
[2566.44 --> 2569.76]  I just noticed that that was a flame after just like staring at it.
[2569.76 --> 2571.10]  So it's like, whoa, wait a second.
[2571.24 --> 2571.86]  That's a flame.
[2571.98 --> 2572.34]  It's lit.
[2572.78 --> 2582.66]  So, I mean, you know, getting back to the, you know, feature list and web components and, you know, there's, there's, you know, way too much to kind of, I think, cover with the remaining time we have in this podcast.
[2582.66 --> 2600.00]  But one thing I did want to like call out was that, you know, there's scoped styles, you know, within lit and that scoping of styles is leveraging shadow DOM, you know, which allows for, you know, like great for design system teams that just like want something to look and work the same everywhere.
[2600.00 --> 2605.74]  And being, being able to kind of like reliably say, yes, we're, we're, we're confident we can ship this, you know?
[2605.96 --> 2620.26]  And so can you talk to us a little bit about, you know, what it's been like to incorporate shadow DOM and like also just, I haven't looked recently around browser support, but you know, there, there was a lot of like naysaying back in the day on this.
[2620.26 --> 2623.64]  And so where are we now with being able to leverage shadow DOM everywhere?
[2624.42 --> 2625.74]  Yeah, browser support is excellent.
[2626.06 --> 2631.00]  Like all browsers have supported custom elements and shadow DOM, the basic layers for years now.
[2631.24 --> 2636.40]  I mean, that happened when Edge switched over from whatever their Trident system was over to Blink.
[2636.78 --> 2641.48]  Yeah, it was like, yeah, Edge, Edge HTML, I think was the engine that they created.
[2641.74 --> 2642.94]  Yeah, Trident was the one before that.
[2643.04 --> 2644.90]  So now it's Blink, I think, was that 2020?
[2645.42 --> 2646.40]  Can't remember exactly when that was.
[2646.40 --> 2649.34]  It was, it was definitely like 2019, 2018, I think.
[2649.34 --> 2651.52]  Like early 2019, maybe.
[2652.02 --> 2653.52]  So browser support is very good.
[2653.82 --> 2653.96]  Yeah.
[2654.06 --> 2662.34]  And then in terms of like lit and style scoping and slots, which is what you use for composition, like that'd be like React Children, the kind of analog.
[2662.88 --> 2664.12]  Lit actually doesn't do anything there.
[2664.48 --> 2668.84]  This actually trips some people up where they're like, I want lit to do this with my styles.
[2668.86 --> 2670.56]  And we're like, we don't do anything with styles.
[2670.58 --> 2674.86]  It's the browser behavior, you know, look it up on MDN, it's right there.
[2675.16 --> 2679.02]  So lit really like, it puts the styles into the shadow root.
[2679.02 --> 2679.42]  That's it.
[2679.98 --> 2682.26]  So it's like, will it support CSS nesting?
[2682.52 --> 2683.36]  Like it already does.
[2683.70 --> 2685.22]  Will it support some new selector?
[2685.40 --> 2685.76]  Absolutely.
[2686.06 --> 2686.62]  Already does.
[2686.78 --> 2687.64]  Like has and not.
[2688.04 --> 2690.06]  You know, it's just, it's impossible for it not to support it.
[2690.74 --> 2690.94]  Yeah.
[2690.96 --> 2694.50]  But Shadow DOM has been, you know, a little bit harsh for some people, right?
[2694.50 --> 2701.48]  Because it enforces this encapsulation where people are used to being able to reach into a component and style something inside that component any way they want.
[2702.22 --> 2706.30]  So it's a little bit of a double-edged sword because some teams are like, yes, nobody can mess up my component.
[2706.84 --> 2710.00]  Now I can change the DOM and it's not a breaking change for my users.
[2710.56 --> 2718.50]  On the other hand, some people are like, well, you know, we have a design system right now where we just give teams like snippets of HTML and like a style sheet.
[2718.50 --> 2720.88]  And we want to upgrade to web components.
[2721.04 --> 2726.02]  We can't do that if that style sheet that they're already using can't reach inside the Shadow DOM and style stuff.
[2726.30 --> 2730.16]  So I've been trying to push on standards to help, you know, kind of bend a little bit here.
[2730.66 --> 2733.40]  I have a proposal called Open Stylable Shadow Roots.
[2733.56 --> 2735.16]  I was like, whoa, hold on, hold on, hold on.
[2735.24 --> 2738.96]  Like this whole thing was supposed to be in the shadows and here you are pulling it into the light.
[2739.14 --> 2742.10]  Like, I mean, it's cool that it would be an option, right?
[2742.10 --> 2744.44]  So there's backwards compatibility and all that jazz.
[2744.64 --> 2751.04]  Yeah, developers need knobs, you know, and I don't believe in being condescending to the developers who say that they need something and be like, no, you don't.
[2751.20 --> 2751.70]  That's a good point.
[2752.00 --> 2752.44]  Is that very true?
[2752.72 --> 2754.18]  Yeah, and especially for migration, right?
[2754.26 --> 2761.74]  Like maybe they have a kind of like, you know, not well encapsulated, you know, wires hanging out system today.
[2761.74 --> 2768.16]  And if you want them to be able to get to a system that's more structured and capsulated, you need to like not make them rewrite the world.
[2768.74 --> 2769.86]  Yeah, 100%.
[2769.86 --> 2785.56]  I think we ran into a hiccup with Shadow DOM at a place that I worked for where because constructible style sheets were not universal in the browser, like, you know, like we weren't able to leverage them in the way that we wanted to for the exact reason that you just said, you know?
[2785.56 --> 2791.36]  And so it's like very gratifying to actually hear you to be pushing this proposal forward.
[2791.52 --> 2794.16]  So like we'll have to we'll have to watch it.
[2794.36 --> 2794.50]  Yeah.
[2794.68 --> 2795.32]  I mean, who knows?
[2795.48 --> 2798.90]  There's there's definitely like a camp of people who are like, no, that breaks encapsulation.
[2798.90 --> 2800.34]  They don't want to support it.
[2800.46 --> 2801.78]  And you're like, well, yes, it does.
[2801.86 --> 2803.52]  That's kind of the point.
[2803.52 --> 2804.58]  But it's opt in.
[2804.74 --> 2806.70]  And, you know, you know, if you need it, you need it.
[2807.14 --> 2813.50]  So it reminds me of the early days of a lot of web frameworks are like we made the choices for you.
[2813.56 --> 2814.98]  You never have to make a different choice.
[2814.98 --> 2818.08]  And you get to a point where you say, well, actually, I do.
[2818.42 --> 2824.94]  So if you want me to keep using your framework, you need to give me some ways that I can plug into it because, yes, you handled my base case.
[2825.14 --> 2830.60]  But any sufficiently complex system, you end up with edge cases where you need to be able to tinker.
[2831.44 --> 2831.64]  Yeah.
[2831.64 --> 2835.30]  And we we've tried to do what we can in lit to help those use cases.
[2835.30 --> 2837.38]  Like we let you opt out of shadow DOM.
[2837.70 --> 2839.82]  But it comes with these like major caveats, right?
[2839.86 --> 2841.54]  Like now slots don't work anymore.
[2842.20 --> 2844.38]  People are like, can you make slots work without shadow DOM?
[2844.44 --> 2846.24]  We're like, no, actually, that's like a browser feature.
[2846.34 --> 2848.26]  Like lit is not doing anything with slots.
[2848.50 --> 2849.84]  So, yeah, it's tough.
[2849.84 --> 2851.12]  I feel like there's headway there.
[2851.68 --> 2866.80]  Like I think some of the standards people like are beginning to realize like it's not just this kind of idealistic, like best engineering practice use case, you know, for desktop apps or something that like there's a messy world out there and people are coming from even messier places.
[2867.64 --> 2870.26]  And, you know, I'm trying to convince everybody to like help.
[2870.56 --> 2870.64]  Yeah.
[2870.68 --> 2875.00]  If you design a standard only for Greenfield's development, you're going to dramatically limit your adoption.
[2875.38 --> 2875.68]  Yeah.
[2875.72 --> 2879.08]  And I think that has been kind of the perception of web components like for a long time.
[2879.08 --> 2883.48]  So we're trying to help them be a migration path, right?
[2883.54 --> 2885.58]  Not just a starting point.
[2885.98 --> 2886.10]  Yeah.
[2886.40 --> 2887.06]  Yeah, absolutely.
[2887.32 --> 2899.16]  And I guess kudos also to the Angular team because, I mean, they also help with custom elements and like kind of making people feel and use like feel more comfortable with them, but also just like leveraging them out of the box.
[2899.34 --> 2901.84]  So it's just love to see more of that.
[2902.66 --> 2907.30]  And so we've kind of so we've circled a little bit about governance and we've talked a little bit about standards.
[2907.30 --> 2915.98]  And was there anything you wanted to kind of call out specifically around, you know, what's maybe what's next around standards that we haven't covered yet, Justin?
[2916.50 --> 2916.60]  Yeah.
[2916.64 --> 2919.46]  I mean, the standards stuff is moving like really fast lately.
[2919.46 --> 2921.92]  I think like there was a lull, you know, during the pandemic.
[2922.20 --> 2924.22]  A lot of interesting stuff is happening right now.
[2924.22 --> 2931.28]  So declarative shadow DOM is a big one that has shipped in Chrome and Safari now, and it's streaming declarative shadow DOM.
[2931.50 --> 2933.64]  So we leverage this for SSR.
[2933.78 --> 2937.62]  We're able to generate HTML that preserves the DOM and style scoping.
[2938.34 --> 2939.22]  Let's see other stuff.
[2939.48 --> 2940.92]  Scoped custom element registries.
[2940.92 --> 2947.64]  So right now, the custom element registry where you register a tag name to go with an implementation is global.
[2948.22 --> 2951.54]  This is a proposal that I made a while back and kind of sat there for a little while.
[2951.62 --> 2956.04]  But we think we have most of the open questions answered and Chrome is prototyping that.
[2956.62 --> 2960.60]  That's going to be a big deal for like large enterprise apps with multiple teams.
[2960.96 --> 2963.10]  We're also seeing, you know, like I said, decorators.
[2963.18 --> 2964.38]  That's kind of on the JavaScript side.
[2964.46 --> 2969.20]  For us, that's going to be a big deal so that, you know, you don't need TypeScript if you want to have good DX there.
[2969.20 --> 2972.44]  And then also template instantiation and DOM parts.
[2972.84 --> 2980.10]  It's kind of hard to tell those two apart, but that's basically like that technique of locating the important parts in the DOM and updating them.
[2980.46 --> 2983.00]  There's some prototyping going on there and some spec discussions.
[2983.62 --> 2989.08]  And that's really exciting because, you know, I personally want everybody to make their own lit, be able to make their own lit if they can.
[2989.58 --> 2994.20]  And there's some tricks that we've had to do inside the code base that are kind of more complicated than I would like.
[2994.26 --> 2997.86]  And like if the browser just makes it easy to make your own template system, that's amazing.
[2997.86 --> 3000.34]  And then another big one is accessibility.
[3000.76 --> 3006.06]  We're seeing a lot of improvement on the specs that let you make very accessible web components by default.
[3006.24 --> 3006.84]  That's very cool.
[3006.92 --> 3008.64]  So, yeah, it's been pretty exciting recently.
[3008.98 --> 3010.12]  Yeah, that's a lot, a lot.
[3010.34 --> 3011.48]  That's like its own show.
[3012.06 --> 3018.00]  But we'll put links to all of these proposals in the show notes so every folks can check them out and follow along.
[3018.62 --> 3021.36]  The scoped custom element registry is huge.
[3022.60 --> 3024.32]  Are you the champion for that?
[3024.50 --> 3024.86]  You said you...
[3024.86 --> 3029.34]  Yeah, but I think, you know, I'm not really a spec writer myself and I'm not a browser implementer.
[3029.44 --> 3032.22]  So I think I've kind of carried that as far as I can.
[3032.56 --> 3036.80]  Like, and it was kind of at the point like, okay, implementers, like, is this part right?
[3037.06 --> 3037.76]  Is this realistic?
[3038.10 --> 3043.38]  You know, and so I'm glad that on the Chrome team, they've picked that up to prototype it and prove that it works.
[3043.38 --> 3044.64]  That's awesome.
[3044.84 --> 3045.40]  Very exciting.
[3046.00 --> 3061.42]  And so can you, as we kind of are wrapping up our discussion, I'm very curious, you know, as a maintainer, like, I'd love to hear about, like, what lessons you've personally learned, like, kind of shepherding and building out this massively impactful project.
[3061.42 --> 3062.18]  It's called Lit.
[3062.18 --> 3062.22]  Yeah.
[3062.76 --> 3063.12]  Yeah.
[3063.64 --> 3069.50]  I mean, there are a lot of different areas of lessons here, like technical, you know, design and community.
[3069.92 --> 3076.10]  You know, I think one of the biggest lessons here, I think, for me is, you know, the power of kind of continuity and incremental progress.
[3076.10 --> 3091.36]  I think that we had assumed in a lot of cases that because web components were interoperable, we could kind of make these step function changes and that people would just kind of move by going over that step and interoperating the thing.
[3091.52 --> 3093.00]  So, like, Polymer to Lit.
[3093.46 --> 3097.06]  I think we lost a good deal of momentum there, actually, when we made that change.
[3097.06 --> 3107.08]  And it would have been, even though it would have taken more effort and time, it would have been better to basically morph Polymer into Lit over time rather than have them both exist at the same time.
[3107.76 --> 3110.70]  Yeah, because if you look at, you know, like, Vue is so similar to Polymer.
[3111.20 --> 3112.50]  Vue is hugely popular.
[3113.16 --> 3114.44]  Like, the DX is very similar.
[3115.08 --> 3117.26]  And you go, like, okay, like, what's happening there?
[3117.32 --> 3123.84]  Part of it might be the difficulty, like, web components not being supported everywhere or some of the things like Shadow DOM, Interop.
[3123.84 --> 3131.64]  But I think some of it is just, like, being very, very good at not breaking your users and having, you know, incremental progress all the time.
[3132.04 --> 3135.72]  I think that builds a lot of goodwill and a lot of ecosystem there.
[3136.24 --> 3142.02]  So the next phase we want to focus on is, like, we're doing Lit 3.0 soon and it should be, you know, almost no breaking change for anyone.
[3142.50 --> 3147.84]  But the big thing is going to be kind of, like, trying to learn and adopt new ecosystem building methods.
[3148.20 --> 3152.84]  Getting more of the community involved in building it and talking about it and whatnot.
[3152.84 --> 3155.58]  So after Lit 3.0, that's going to be our big focus.
[3156.24 --> 3157.20]  That's so cool.
[3157.40 --> 3160.58]  I just want to give a shout out to you just in general for lots of things.
[3160.58 --> 3169.30]  But I saw right before we started recording this show that you posted an RFC for the NPM CLI to include Google's Wire It.
[3169.80 --> 3171.40]  And I was like, yeah, that's so cool.
[3171.54 --> 3178.36]  And it's so funny because last week we had Darcy Clark on the show to talk about the massive, like, manifest confusion bug.
[3178.50 --> 3179.50]  Really great episode.
[3179.50 --> 3180.62]  We'll link it in the show notes.
[3181.10 --> 3182.38]  Episode number 282.
[3182.90 --> 3188.28]  You know, and he was actually, while I was at NPM, I got to actually see him birth the RFC process.
[3188.54 --> 3190.22]  So I was like, it just felt like full circle.
[3190.48 --> 3193.04]  We talked about the RFC on the show a little bit.
[3193.14 --> 3196.32]  And then I saw you post an RFC to NPM.
[3196.44 --> 3199.60]  And I was just like, wow, Justin, like this circular world.
[3200.64 --> 3201.44]  And so...
[3201.44 --> 3204.90]  Yeah, we have an RFC process too as part of this kind of, like, involvement of people.
[3205.20 --> 3207.86]  Like, you know, it used to be we made a decision in a team meeting.
[3208.40 --> 3213.62]  And now we're like, we're going to do an RFC because we want other people to see that and do RFCs.
[3213.82 --> 3215.40]  Yeah, I was just going to ask about that.
[3215.40 --> 3227.84]  I will say you were talking about UpView and a couple other places, but they are a really interesting role model of a project that went from being a benevolent dictator for life to being much more community led.
[3228.06 --> 3232.62]  And so they might be a good role model there as well for the RFC process and things around that.
[3232.84 --> 3233.90]  Yeah, they're a big inspiration.
[3233.90 --> 3241.40]  I think, you know, Angular 2 is interesting because they very intentionally and explicitly kind of, like, create this big tent vibe.
[3241.98 --> 3249.16]  And, you know, I'm not a big marketer myself, but, like, I see how useful that is to not just be a big tent and be like, well, we're open to anybody who wants to come by.
[3249.68 --> 3253.48]  But to actually shout that and advertise it, make it obvious, be like, you're welcome here.
[3253.56 --> 3254.68]  Please come join us, you know.
[3254.84 --> 3255.98]  And so...
[3255.98 --> 3259.54]  Yeah, the Angular community has just been, like, exceptionally good at this for many, many years.
[3259.54 --> 3268.54]  And they've just been leading the way in terms of community, community engagement, transparency of roadmaps, and just, you know, ng-conf and, like, the whole...
[3269.10 --> 3272.26]  Most of the maintainer team showing up to that and engaging with the community.
[3272.44 --> 3273.70]  It's just fantastic.
[3274.32 --> 3276.50]  Hope to have folks from Angular here soon.
[3276.60 --> 3279.34]  I think Justin referenced signals earlier in the show.
[3279.72 --> 3284.72]  So we'd love to have folks from the Angular team come and talk about signals with us at some point soon.
[3285.28 --> 3288.90]  So before we wrap, I'm going to ask you my secret question to maintainers.
[3288.90 --> 3289.64]  It's not so secret.
[3290.82 --> 3295.24]  But I try to ask this to most maintainers, which is, like, what's your web wish?
[3295.24 --> 3298.90]  If you could, like, wave one magic wand for the web platform, like...
[3299.46 --> 3301.82]  And it actually could be expanded to anything.
[3302.02 --> 3303.24]  In JavaScript, anything at all.
[3303.28 --> 3304.46]  If you could, like, what would it be?
[3304.78 --> 3305.48]  I have one.
[3305.78 --> 3309.00]  I wonder if it's, like, either esoteric or involved, but...
[3309.00 --> 3309.46]  Get nerdy.
[3309.46 --> 3317.74]  There was a project at Google one time called Razer, which turned into a project called Sky, which turned into what people know today as Flutter.
[3317.74 --> 3328.54]  And it was a fast subset of the web that was designed to be embeddable into other apps and be, you know, 120 frame per second fast on mobile devices and whatnot.
[3329.16 --> 3331.76]  Flutter is good at what it does, but it's not the web anymore.
[3331.76 --> 3337.18]  And I actually think the web could really benefit, like, electron desktop apps, like mobile apps or whatever.
[3337.30 --> 3339.78]  I just want the web to have even more reach than it does now.
[3340.10 --> 3349.60]  And I really wish it had this kind of small embeddable subset that, say, Servo could target as a thing it could support without supporting the whole web or something like that.
[3349.86 --> 3356.30]  People could embed into their, you know, super apps in China or whatever, where the micro apps come into them and stuff.
[3356.30 --> 3361.66]  Like, I wish that there were, yeah, kind of a, the web, the good parts as a spec.
[3362.00 --> 3362.74]  As a spec.
[3362.82 --> 3363.12]  Interesting.
[3363.44 --> 3366.66]  Yeah, I didn't hear, I didn't have that context for Flutter.
[3367.18 --> 3374.40]  What I do know is that the JavaScript and HTML and CSS that Flutter spits out when people write, like, Dart.
[3374.40 --> 3381.68]  And, you know, it compiles to, like, iOS and it compiles to Java and it compiles to, you know, it creates a web output.
[3381.90 --> 3386.68]  Like, I know that that output for the web is pretty darn, like, it's hot garbage.
[3387.40 --> 3387.72]  Yeah.
[3387.86 --> 3388.18]  Oh, sorry.
[3388.22 --> 3390.70]  I was going to say hot garbage, but I was worried I was going to get censored.
[3390.98 --> 3392.38]  I can say, I can say hot garbage.
[3392.54 --> 3393.88]  It's, yeah, not great.
[3394.14 --> 3397.04]  It's a large, let's say it's a large bundle, you know.
[3397.28 --> 3397.98]  Yeah, bulky.
[3398.16 --> 3398.30]  Yeah.
[3398.32 --> 3401.40]  I think the web is, like, the greatest software delivery platform ever.
[3401.40 --> 3403.94]  I don't even think that's, like, very unique or controversial.
[3404.50 --> 3406.42]  But also people want to do cross-platform stuff.
[3406.62 --> 3412.92]  And I think if you want to do cross-platform and target the web, you've got to privilege the web and do web first because it's the most sensitive to code size.
[3413.34 --> 3416.70]  And I just wish, I wish there were something a little better for that.
[3417.18 --> 3418.62]  Yeah, that's my, that's my secret wish.
[3419.18 --> 3420.08]  Well, well said.
[3420.20 --> 3421.22]  And amen to that.
[3421.72 --> 3424.82]  Your lips to the, to the web god ears, you know.
[3424.92 --> 3426.66]  So thank you for that.
[3427.04 --> 3429.88]  So, yeah, it's been an absolute pleasure having you on the show, Justin.
[3429.88 --> 3435.98]  And I hope it's not going to be, like, another, like, five years before we have a conversation on a podcast again.
[3435.98 --> 3438.50]  So we'll have to have you back on air soon.
[3438.50 --> 3445.10]  And I'll put a link in the show notes to a podcast that Justin and I did in 2018 to talk about the birth of Lit.
[3445.14 --> 3445.72]  Baby Emil.
[3445.98 --> 3446.70]  Baby Justin.
[3446.70 --> 3447.02]  Yes.
[3447.50 --> 3448.58]  Yeah, baby, baby.
[3448.86 --> 3449.82]  Thanks for having me.
[3450.12 --> 3450.86]  Yeah, it's been a pleasure.
[3450.96 --> 3451.98]  How can folks connect with you?
[3452.06 --> 3453.10]  Where can folks find you?
[3453.10 --> 3456.42]  So Lit.dev is where our project lives.
[3456.70 --> 3459.82]  And you have links there to all of our, like, socials and Discord and whatnot.
[3460.42 --> 3463.16]  You can find me on Twitter at Justin Finiani.
[3463.46 --> 3465.44]  I keep meaning to stop using Twitter.
[3466.10 --> 3471.48]  And I also post a lot of, you know, politics and, you know, urban development stuff.
[3471.58 --> 3473.08]  So not just, not just web dev.
[3473.58 --> 3477.74]  So, yeah, I would recommend Lit.dev for the, like, official channels on everything.
[3477.74 --> 3481.14]  And then maybe one day we'll have a blue sky and all that mess.
[3481.48 --> 3481.88]  Threads.
[3482.06 --> 3482.50]  Threads.
[3482.58 --> 3484.14]  Threads is the new hotness, right?
[3484.48 --> 3485.18]  Oh, man.
[3485.34 --> 3486.08]  I can't keep up.
[3486.08 --> 3488.44]  Blue Masto Threads or something.
[3488.70 --> 3492.62]  This is like whack-a-mole for, like.
[3492.68 --> 3495.18]  I just want 2018 Twitter back.
[3495.58 --> 3496.02]  Seriously.
[3496.58 --> 3497.10]  It was so good.
[3497.34 --> 3498.38]  It was so good.
[3498.50 --> 3498.68]  Yeah.
[3499.04 --> 3499.44]  All right.
[3499.56 --> 3500.88]  Well, thank you.
[3501.48 --> 3505.72]  And I guess we'll add that to the other, like, we'll add that to the web wish list, right?
[3505.72 --> 3507.74]  Like, let's bring 2018 Twitter back.
[3507.82 --> 3508.34]  Like, amen.
[3508.48 --> 3508.98]  Please, please.
[3509.48 --> 3511.46]  But anyway, so it's been a great show.
[3511.58 --> 3512.60]  Thank you again for joining us.
[3512.68 --> 3514.48]  Thank you, KBall, for co-hosting.
[3514.68 --> 3517.32]  And yeah, with that said, we'll be back next week, everyone.
[3517.48 --> 3517.98]  Talk soon.
[3518.12 --> 3518.38]  Bye.
[3526.38 --> 3530.42]  Changelog++ members, stick around for some bonus Lit content.
[3530.96 --> 3535.70]  Amel asks Justin about routing, state management, and all the other stuff that accompanies Lit
[3535.70 --> 3535.78]  it.
[3536.02 --> 3537.92]  Turns out they're working on some cool stuff.
[3538.30 --> 3540.10]  The router's very, very kind of early.
[3540.22 --> 3541.58]  We haven't had a lot of time to work on it.
[3541.62 --> 3545.70]  But one of the interesting things about it is that it's super small because it uses the
[3545.70 --> 3552.56]  upcoming HTML navigation API and URL pattern, which are, like, so numerous people don't know
[3552.56 --> 3552.86]  about them.
[3552.86 --> 3556.90]  If you haven't jumped on the++ bandwagon yet, now's a good time.
[3557.32 --> 3562.12]  It's our membership program that lets you ditch the ads, get in on awesome bonuses like
[3562.12 --> 3565.60]  this extended episode, and directly support our work here at Changelog.
[3565.70 --> 3569.34]  Check it out at changelog.com slash plus plus.
[3569.92 --> 3574.80]  Thanks once again to our partners, FASC.com, Fly.io, and typesense.org.
[3575.04 --> 3579.06]  And to Breakmaster Cylinder for producing these banging beats for all of our pods.
[3579.62 --> 3580.88]  All right, that's all for me.
[3580.88 --> 3583.16]  We'll party together again next week.
