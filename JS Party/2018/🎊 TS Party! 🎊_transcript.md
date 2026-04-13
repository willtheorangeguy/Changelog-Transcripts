[0.00 --> 5.24]  Hi, everyone. Tim Smith here, senior producer for Changelog. In the first segment of this show,
[5.40 --> 12.28]  Jared was using his MacBook microphone instead of his Heil PR40. This was done to bring awareness
[12.28 --> 20.82]  to a very specific issue. Every day, thousands of podcasts are recorded with a laptop mic,
[21.28 --> 28.36]  making it immensely difficult for the audience to listen. In 2018, we're baffled that this is
[28.36 --> 35.92]  still a problem. Go to choosetherightsource.org and join us in this fight. Now on with the show.
[36.78 --> 43.40]  Bandwidth for Changelog is provided by Fastly. Learn more at fastly.com. We move fast and fix
[43.40 --> 48.64]  things here at Changelog because of Rollbar. Check them out at rollbar.com. And we're hosted on Linode
[48.64 --> 56.28]  servers. Head to linode.com slash changelog. This episode is brought to you by Rollbar. Move fast
[56.28 --> 61.46]  and fix things. Resolve errors and minutes and deploy with confidence. Head to rollbar.com
[61.46 --> 66.98]  slash changelog. Request a demo. Get started today. It's loved by developers, trusted by enterprises,
[66.98 --> 74.24]  and most of all, we use it here at Changelog. Move fast and fix things with Rollbar. Once again,
[74.24 --> 76.32]  rollbar.com slash changelog.
[86.28 --> 97.20]  Welcome to JS Party, a weekly celebration of JavaScript and the web. Tune in live on Thursdays
[97.20 --> 103.40]  at 1 p.m. U.S. Eastern at changelog.com slash live. Join the community and slack with us in real
[103.40 --> 108.08]  time during the shows at the changelog.com slash community. Follow us on Twitter. We're at
[108.08 --> 118.78]  JS Party FM. And now onto the show. All right. It is time once again for JS Party. Today's show
[118.78 --> 124.44]  going to be a little bit different. It's not going to be a JavaScript party. It'll be a superset of a
[124.44 --> 131.04]  JavaScript party because our topic of conversation for today is not JavaScript. Well, it's kind of
[131.04 --> 136.38]  JavaScript, but we'll get into that. It is TypeScript. So we are officially calling this a TS Party.
[136.38 --> 142.04]  This podcast will compile to JavaScript. That's right. So go ahead and run it through your web
[142.04 --> 146.62]  pack and see what comes out the other end. If you've been hanging out in the chat, thanks for
[146.62 --> 151.96]  sticking with us. We actually turned it into Troubleshoot Party as our live stream had issues,
[152.08 --> 156.70]  but we're over that. We're here. We're happy. And we're going to have an interesting conversation
[156.70 --> 163.34]  about TypeScript. So joining me today, by the way, my name is Jared. Joining me is Nick Neesey.
[163.40 --> 165.60]  What's up, Nick? Hey, how's it going? It's going very well.
[165.60 --> 169.44]  How about you? How are you doing? I am doing wonderful. I'm excited to talk about TypeScript.
[169.76 --> 175.26]  And you talked about Dojo last week. I saw on Twitter that you are also on another podcast
[175.26 --> 180.78]  talking Dojo. Is that correct? Yeah. I'll be talking about Dojo recording just after this
[180.78 --> 187.00]  one, actually. It's the Script and Style podcast with David Walsh and Todd Gardner.
[187.24 --> 191.22]  Very cool. Well, after that goes live, share the link and we will share it through the JS Party
[191.22 --> 195.56]  channels as well. Also joining me today is Chris Hiller. Chris, how are you?
[195.60 --> 201.74]  Hello. I've had a lot of coffee this morning, so I'm ready to do this. Let's do it.
[201.82 --> 206.04]  All right. So let's start off. TypeScript. What is it and why should we give a darn? Nick,
[206.20 --> 212.06]  you are the, I've been calling you the TypeScript bull as this will show is your idea. And as
[212.06 --> 216.32]  you're very deep in the TypeScript community and using it, I believe on a daily basis,
[216.44 --> 222.96]  or at least on a regular basis. So why don't you give us the intro and get us started?
[222.96 --> 229.84]  All right, cool. Yeah. So TypeScript is, as you said, a superset of JavaScript. And it was introduced
[229.84 --> 237.38]  in 2012 by Microsoft. And they brought it, brought it out after a couple of years of internal development
[237.38 --> 243.20]  and introduced it to the world. And I have to say that when it first came out, the site,
[243.20 --> 249.44]  found the company I was at, was really looking into it almost right away, I think. And I wasn't
[249.44 --> 256.16]  enthusiastic about it because I had these horrible flashbacks of like CoffeeScript and, and changing
[256.16 --> 263.24]  JavaScript into something that it's not. But that's not at all what TypeScript is. It's really just a
[263.24 --> 272.06]  superset of JavaScript that adds in optional types so that you can bring type safety to your apps on
[272.06 --> 277.80]  your own terms as you need them or slowly over time or all at once right away, whatever you want
[277.80 --> 284.88]  to do. And it was created by a guy named Anders Halsberg. And he also created C Sharp, Delphi,
[285.12 --> 289.14]  and Turbo Pascal. And he's at Microsoft continuing to work on this.
[289.14 --> 290.90]  He has no credentials, is what you're saying?
[291.08 --> 299.36]  Yeah, he has no idea what he's doing. No, he's a brilliant guy. And it shows through his work,
[299.42 --> 303.56]  obviously. He was on the changelog, wasn't he, in the past?
[303.72 --> 309.64]  That's right. Yeah, we had Anders on, man, it's probably a couple of years ago now, episode 152,
[310.00 --> 316.78]  back in April of 2015. And he gave the backstory, the inside story at Microsoft of TypeScript.
[316.78 --> 323.10]  TypeScript. Jonathan Turner was also in that show. So if you want the deep dive onto it being formed
[323.10 --> 328.42]  inside Microsoft and then coming out and at least the history between 2012 and 2015,
[328.96 --> 333.54]  go back and listen to that. We'll put it in the show notes. But no doubt there's been progress and
[333.54 --> 340.44]  really just massive adoption is what I've seen mostly from the outside of TypeScript into different
[340.44 --> 346.02]  projects, different companies, different libraries. But I'm curious, Chris, what's your experience
[346.02 --> 352.10]  with TypeScript? I'll tell you mine, none. So I write JavaScript. I actually liked CoffeeScript
[352.10 --> 357.82]  back in the day. Nick, you know that. I was a fan of CoffeeScript because I didn't like
[357.82 --> 365.14]  a lot of the older JavaScript trappings. And CoffeeScript kind of spoke to my aesthetic sensibilities.
[365.70 --> 371.86]  I've since moved on back to ES6 and style JavaScript. But I haven't actually used TypeScript at all.
[371.86 --> 376.32]  Like I've seen it. I've talked a lot about it, but I don't have any practical experience. Chris,
[376.36 --> 382.96]  how about you? I was also pretty wary of TypeScript. I didn't enjoy working with CoffeeScript actually.
[384.68 --> 390.34]  But so I, you know, another thing that compiles down to JavaScript, not that excited about it,
[390.42 --> 397.30]  but you know, I, I, so it was a while before I tried TypeScript. All I've really done with it is,
[397.30 --> 405.18]  is basically try it. So I've tried to use it, um, like two or three different, on two or three
[405.18 --> 411.68]  different occasions on, on personal projects and, um, just haven't gotten too terribly far with it.
[411.94 --> 418.10]  Um, I, I do like, you know, some of the things that it offers, but you know, it, it, I also have,
[418.24 --> 424.80]  I, I struggle with it. So I suppose we can talk about some of that. Um, but that's, that's pretty much
[424.80 --> 430.30]  my experience with it. I'm really trying to get into it, but it just, it just hasn't really clicked
[430.30 --> 437.08]  for me. So maybe we could start with why, so you, it hasn't clicked and you've had a few false starts,
[437.08 --> 442.42]  but you still say you're really trying to get into it. So apparently you do see some value,
[442.42 --> 446.46]  even though you haven't quite got there, Chris, what is it about TypeScript that it offers
[446.46 --> 448.98]  that you're interested in taking advantage of?
[448.98 --> 454.02]  You know, for me, it's, it's really all about the, the type, the introspection and, and,
[454.02 --> 459.88]  and such offered by the, the server. And so your, your IDE, your editor can talk to the TypeScript
[459.88 --> 468.12]  server and get all this information about your code, um, that it's terribly difficult to get in,
[468.12 --> 475.00]  in, you know, vanilla JavaScript, um, because, you know, there's too much loosey goosey type stuff
[475.00 --> 481.50]  going on. Um, and, and of course, TypeScript makes it kind of easier to understand, you know,
[481.68 --> 488.10]  what, what goes here, what goes where, what, what this function can do. It's just, uh, especially
[488.10 --> 494.14]  in VS code, there's, there's a ton of, you know, kind of, uh, inline and, and context sensitive help
[494.14 --> 498.66]  and all that cool stuff. Um, so for me, it's, it's the tooling.
[498.90 --> 503.36]  Yeah, I would agree with that. The, the tooling is the biggest, uh, win for TypeScript and it's
[503.36 --> 511.26]  why I really like it. Um, I just use, uh, Vim for all of my development work. Uh, but because,
[511.26 --> 517.22]  um, because TypeScript does provide this, this TS server, uh, and that's what VS code and others
[517.22 --> 523.12]  are talking to, um, Vim can talk to that as well through plugins. And, uh, I get much of the same
[523.12 --> 529.60]  benefits right there. I can do completion, smart refactoring, um, renaming of things, um, and,
[529.60 --> 536.94]  and also get information about what the actual value is of a variable under my cursor, uh, or get
[536.94 --> 541.02]  like information about the, the comments. If there's JS comments associated with that,
[541.06 --> 544.76]  I can get that information too. So one thing I learned while talking with the VS code team
[544.76 --> 550.12]  recently about VS code and how you're talking about the TypeScript server and really the tooling
[550.12 --> 556.56]  wins that that provides is that even when you're using JavaScript, you don't have TypeScript
[556.56 --> 562.88]  in your build tool chain, for instance, or you're not like opting in because TypeScript is a strict
[562.88 --> 569.44]  superset, basically all JavaScript going back to like, you know, yes, three or something like
[569.44 --> 575.44]  really old JavaScript, all that is valid TypeScript. And so they're able to not even use the JavaScript
[575.44 --> 578.62]  language server in the back end. They're using the TypeScript server, even when you're writing
[578.62 --> 583.50]  JavaScript. And so there are some features I think you can take advantage of, or that VS code
[583.50 --> 588.76]  specifically is giving you with JavaScript, even though you're down, you don't know about it.
[589.02 --> 594.14]  Yeah, that's exactly right. So VS code does take advantage of that for your JavaScript work too. So
[594.14 --> 600.86]  it's passing all of your JavaScript code through, um, the TS server to infer what it can about, uh,
[600.86 --> 606.10]  the files and all of the variables and everything within there. So if you're setting, uh, this,
[606.22 --> 610.40]  this variable somewhere in your file to a number, then it knows it can infer that that's going to be a
[610.40 --> 615.52]  number. And if you change it to something else or try and use a string method on it, uh, then it can
[615.52 --> 620.38]  provide you with some intelligent, um, tool tips that tell you, Hey, you probably can't do this
[620.38 --> 624.46]  because it's, you're using a number. We think that you're using a number and that's, that's one of the
[624.46 --> 633.12]  big benefits. So TypeScript, um, it is just JavaScript and then it does, it just allows you to add in these
[633.12 --> 638.78]  type annotations, but you don't have to go crazy with that because, uh, you can, you can just rely on
[638.78 --> 643.50]  TypeScript being able to infer what you're passing around to it as well. And so that's kind of the,
[643.56 --> 649.78]  the minimal standard that, um, that VS code would use for something like a JavaScript file and doing
[649.78 --> 657.66]  that. It also, uh, is smart enough to understand, um, some of the basics of JS.comments. And so if you
[657.66 --> 662.62]  have a JS.comment above a function and you are describing the arguments that that function takes,
[662.82 --> 667.60]  uh, you're not adding any TypeScript specific code to that. You're just doing it in a comment and the TS
[667.60 --> 673.44]  server can, um, infer from that comment, what the, what types of variables can be passed to this
[673.44 --> 677.54]  function and then give you warnings if you're using it in an improper way. So I had a question
[677.54 --> 684.50]  about that. Is it like a traditional like daemon or whatever that just kind of, it runs in its own
[684.50 --> 689.92]  process and responds to like remote procedure calls or something? How does, how does that work?
[690.18 --> 695.62]  Uh, I don't know the specifics of that. Um, but it does like on every keystroke in your editor,
[695.62 --> 702.14]  uh, like, and that can depend on the editor too. Uh, but on every keystroke, it's, um, effectively
[702.14 --> 707.22]  blowing away what it knows and then recompiling the world to, or recompiling its understanding of the
[707.22 --> 713.50]  application to give you intelligent insights on everything. Uh, so I think so, but yeah, it does run
[713.50 --> 717.84]  in the background like that and it's for every specific file. So I understand how that would work
[717.84 --> 722.84]  inside of VS code, even with the client server architecture with a separate process, or maybe, uh,
[722.84 --> 727.40]  I wouldn't imagine it uses the network necessarily, but how about inside of them? Like, do you,
[727.82 --> 733.90]  do you have to have the TS server like installed with node or like what's your setup to take advantage
[733.90 --> 739.56]  of those features in editors that aren't Microsoft's editor? I can, I can really only speak for Vim in
[739.56 --> 747.02]  this case. Um, but I have a plugin called ale or the asynchronous linting engine. It's very similar to
[747.02 --> 753.44]  other plugins like syntastic or, um, I'm forgetting the names of other ones that I've used in the past.
[753.68 --> 758.46]  Uh, but those in the past, I've used those just for linting. So every time I save a file that will
[758.46 --> 764.58]  go through and pass what the file that I'm working on to, uh, ES lint or JS hint or whatever it was in
[764.58 --> 768.46]  the past. And then that will come back and tell me all of the linting problems that I did and highlight
[768.46 --> 776.34]  the lines. Uh, ale does that all in real time as I'm typing. It's just constantly updating them with,
[776.34 --> 782.12]  um, information about the line that I'm typing and what it understands so that I get real-time
[782.12 --> 787.00]  feedback on everything. And so it's going through that and it's just reaching into on, on my TypeScript
[787.00 --> 791.76]  projects, it's reaching into the local version of TypeScript that I would have installed in the
[791.76 --> 795.60]  node modules for that project, or it can go for the global version if you have that as well.
[795.60 --> 800.18]  So it's using your local, your node modules that are relative project, relative node modules.
[800.34 --> 800.74]  Correct.
[801.00 --> 803.02]  Via the Vim plugin or extension. Okay.
[803.24 --> 807.48]  Right. And then there's other plugins as well. Uh, I'm using one currently called Tisukinomi,
[807.74 --> 808.98]  uh, and I'm looking at it.
[808.98 --> 809.26]  Say what?
[810.16 --> 811.88]  I think that's how it's pronounced.
[812.50 --> 813.90]  Excuse you. You sound like you sneeze.
[814.70 --> 822.10]  Yeah. Um, I'm looking at another one called, um, in Vim TypeScript that, um, allows you to do other
[822.10 --> 828.02]  things like it adds in method functions that you can call from within Vim. So I can like take the
[828.02 --> 833.38]  word that I'm, my cursor is over and give me what you think the type is, or give me the, the definition
[833.38 --> 838.34]  or the, the comments or go to the definition of that file. So navigate over to that. So it,
[838.44 --> 843.94]  it uses the TS server to further enhance the capabilities of the editor to be able to,
[843.94 --> 846.92]  to have a more holistic understanding of my project.
[846.92 --> 850.26]  So where is the line drawn between, cause I'm all about getting those free features,
[850.42 --> 854.84]  but not necessarily committing to anything if possible. Where, what is the line drawn between
[854.84 --> 860.18]  what it can give me automatically on my JavaScript code by using the TypeScript language server in
[860.18 --> 866.66]  the background? And then what features I can't get, or I could get if I actually, you know,
[866.68 --> 873.50]  put dot TS or, you know, opted in to using like proper TypeScript, even, uh, syntax.
[873.50 --> 880.42]  So if you're just using, uh, JS files, uh, with no type annotations in there at all, uh, then you're
[880.42 --> 885.62]  really only going to be getting what the TypeScript server can infer from your code. And so your code
[885.62 --> 891.08]  would have to be run to be written cleanly, um, using those, those common kind of de facto,
[891.08 --> 898.28]  um, standards that we do within code, like not, not changing the types of variables or, um,
[898.28 --> 907.02]  or other things and, and kind of having a strict set of arguments to a function, for, for example,
[907.56 --> 912.18]  um, anything that it can infer from, from that. So how you're using the code, like what
[912.18 --> 917.32]  variables you pass into a function call when you do it, or what, what you're actually trying to do
[917.32 --> 922.60]  with the variables inside of that function, uh, it can infer that. And then when you're doing
[922.60 --> 927.50]  something that it doesn't understand, then it, um, it, it can warn you about that and let you know.
[927.60 --> 931.48]  So in my previous example, like you pass in a number and then you're trying to use a string
[931.48 --> 936.68]  method on the number, uh, it can warn you that, Hey, it looks like you passed a number here. Um,
[936.68 --> 942.26]  or in this case, you passed a number or a string. So it can actually do, um, a union type and it
[942.26 --> 947.42]  understands that. So it can say that in this variable that you pass in as either a string or a
[947.42 --> 951.74]  number, and then it can warn you if you're passing something else in, uh, and then you can build in
[951.74 --> 956.94]  type guards within that function to, to say that when it's a string, do you like, it's safe to do
[956.94 --> 961.14]  this. And when it's a number, it's safe to do this. Oh, that's cool. So those guard clauses are,
[961.32 --> 965.72]  can you like return early or anything like that in terms of the guards? Yeah. And the guards are
[965.72 --> 970.20]  just set up because it's not really extending the language in any way. Those guards are set up with
[970.20 --> 978.26]  like type of calls. So you can say if a type of, or sorry, type of a equals string. Um, then inside of
[978.26 --> 982.76]  that if statement, it's going to assume that a is always a string outside of that, it could be
[982.76 --> 988.04]  the union type again, a string or a number or whatever. And you can, and you can refer return
[988.04 --> 993.40]  from within there. Uh, then the return type of that function could be, uh, undefined or a string
[993.40 --> 997.10]  or a number or whatever, whatever the case is for the types that you're returning.
[997.48 --> 1001.80]  So Chris, going back to your desire to take advantage of some of the tooling, have you,
[1002.02 --> 1008.10]  have you tried what VS code offers through the TS server or do you use JS doc perhaps with Mocha?
[1008.10 --> 1012.26]  Like, are there things that you could get for free without having to, you know, get over
[1012.26 --> 1018.40]  the hurdles that you've hit a couple of times? Yeah. Um, I even, uh, was able to kind of make,
[1018.78 --> 1027.80]  um, uh, I, I recently started using VS code and, um, I was a web storm person before then. And I
[1027.80 --> 1037.88]  had like made a web storm kind of do this, um, uh, kind of inference about JavaScript using,
[1038.10 --> 1044.52]  TypeScript type. So if I'm using a, um, like some third party library from, if I'm using like a
[1044.52 --> 1052.72]  Lodash or something, um, I would, um, have a copy of the, uh, you know, there's all these,
[1053.04 --> 1058.72]  we'll get to definitely type, but I mean, there's all these, uh, uh, definitions, TypeScript
[1058.72 --> 1063.90]  definitions for third party libraries like Lodash. Basically, if anything's popular, somebody's got a,
[1063.90 --> 1070.48]  has written TypeScript definitions for them. And so I can pull those down and, um, uh, web storm
[1070.48 --> 1077.14]  would use those type definitions to, you know, kind of infer about the JavaScript I was, I was writing
[1077.14 --> 1086.40]  and, um, you know, that works okay. Um, and it, it seems to work okay in VS code, um, with, with,
[1086.40 --> 1095.46]  with the JavaScript. It's, it's not like, it's not that awesome. It helps a bit. Um, but, uh, yeah,
[1095.56 --> 1103.54]  it's, it's, you know, not everything uses JS stock, not everything uses JS stock the same way. Um,
[1103.72 --> 1111.66]  and you know, it's, it can only do so much with JavaScript. Now, uh, I've tried to use, you know,
[1111.66 --> 1119.60]  TypeScript, uh, in VS code and TypeScript in web storm and yeah, it's great. Um, you know, it's,
[1119.88 --> 1126.12]  uh, I think TypeScript, I mean, uh, VS code does a better job with the integration. Um, but still,
[1126.26 --> 1133.36]  um, yeah, it's, uh, it's, it's cool, but you know, I, I still have problems with it.
[1133.36 --> 1145.60]  So this episode is brought to you by the O'Reilly Fluent conference. Make your plans now to attend
[1145.60 --> 1152.28]  Fluent in San Jose, California, June 11th through June 14th to learn the latest JavaScript tools
[1152.28 --> 1158.00]  and methods. Be part of what past attendees call quote, a great center for modern web development
[1158.00 --> 1164.48]  and disruption and quote, the best place to see the current state of the web. Use the discount code
[1164.48 --> 1170.32]  JS party to save 20% on most passes. Learn how to build a better web with better user experiences
[1170.32 --> 1175.22]  at O'Reilly Fluent conference. Head to fluentconf.com to learn more and register.
[1188.00 --> 1194.12]  So guys, we talked about how you can take advantage of some of TypeScript's tooling features
[1194.12 --> 1200.44]  with vanilla JavaScript. What if you don't want to go all in, but you do want some of the TypeScript
[1200.44 --> 1208.76]  features? What's the easiest way, I guess, or the happiest path to, I have a .js file and I want to
[1208.76 --> 1213.62]  go beyond taking advantage of the TypeScript language server. And I want to use some TypeScript features.
[1213.62 --> 1218.60]  How do I get started? Like what's the, what do I got to do to dip my toe in TypeScript water?
[1218.84 --> 1224.64]  So TypeScript is a, it's a module that you install from NPM. And so you can bring that into your
[1224.64 --> 1230.84]  project and then you'll want to create a TS config file. And you can do that through the,
[1230.84 --> 1237.54]  the TypeScript CLI. So you can just say NPX TSC, dash dash init, or maybe it's just init.
[1238.14 --> 1243.60]  And that will ask you some questions and then it will create a TS config.json file from there.
[1243.62 --> 1248.66]  And this is the file that configures how the TypeScript, excuse me, how the TypeScript compiler
[1248.66 --> 1257.20]  actually runs. And so, um, theoretically you could start renaming files to .ts. And then in the
[1257.20 --> 1262.42]  includes section of the TS config, you could have it have some globs in there that point to those
[1262.42 --> 1267.80]  specific files. And you could start as bigger, as small as you want and just have it start, um,
[1268.40 --> 1273.60]  compiling those to JavaScript. And so if you just rename the files, um, you would see a little
[1273.60 --> 1279.76]  bit of change, uh, with the, the outputted, uh, .js files. And you can specify if you want it to
[1279.76 --> 1288.16]  compile to, uh, .es or an esx file, an es5 file, or an es3 file, uh, to take advantage of whatever,
[1288.16 --> 1293.74]  whatever platform you're trying to run on the minimum platform there. So typically it's es5,
[1293.74 --> 1301.20]  um, right now. And you can just have it run those through, compile those, and then you have the
[1301.20 --> 1305.74]  JavaScript files that you can then start running. Uh, there's also different cases with Webpack where
[1305.74 --> 1311.34]  you can start doing that and using TypeScript and JS interoperably with, um, with Webpack's TypeScript
[1311.34 --> 1316.72]  loaders, uh, along with others. And so it gets even easier from there. So you can start slowly,
[1316.72 --> 1323.00]  uh, adding files or converting files from JS to TS. And when you first do that, uh, it kind of will
[1323.00 --> 1328.58]  all go back to the TS config where it's, um, going to be running those type, those compiler options.
[1329.02 --> 1334.40]  And depending on the level of strictness that you have set up in there, uh, that is going to
[1334.40 --> 1338.66]  determine how much the TypeScript compiler actually yells at you going forward. So you can have it really
[1338.66 --> 1343.16]  relaxed. So it's not yelling at you for a whole lot of things, or you can go the route that the
[1343.16 --> 1348.56]  projects I'm on typically go, which is strict, true, where everything is turned on, uh, and it
[1348.56 --> 1353.00]  will yell at you for every little thing. So, I mean, it would seem to me that if, if you have a
[1353.00 --> 1359.38]  project, uh, you know, a web project and, and you've got your Webpack config and you've got a
[1359.38 --> 1366.92]  billion loaders set up and then you want to sprinkle some TypeScript on, um, that seems like it might be
[1366.92 --> 1374.04]  very disruptive, um, to that Webpack config. Uh, because if you have, you know, some TS files,
[1374.18 --> 1379.58]  some JS files, and then, you know, what about what happens with the code splitting and, and yada,
[1379.66 --> 1385.94]  yada, yada. And so, um, is that, uh, I I've never tried anything like that, but I can speculate that
[1385.94 --> 1392.12]  that sounds painful. I mean, uh, do you have any experience with that? Uh, yeah, a little bit. And,
[1392.12 --> 1399.14]  and so you should be able to really add like the, the TS loader and then add, um, the dot TS or TSX
[1399.14 --> 1406.02]  extensions as resolvable extensions. And then from your, you can start compiling or renaming files to
[1406.02 --> 1410.22]  dot TS. And then from your JavaScript files, you should be able to, if they're written in like the
[1410.22 --> 1415.44]  ES module syntax, you should be able to just pull them in like normal. And because you added those
[1415.44 --> 1420.56]  extra resolvers in there, it will just run the, the TypeScript files through the TS loader,
[1420.56 --> 1426.22]  uh, and load those in. And then, um, it should be able to take care of things like code splitting
[1426.22 --> 1431.48]  and others, uh, but allow you to work with, with both formats while you're in that transition
[1431.48 --> 1439.28]  pretty easily. Um, but of course, Webpack can be a black hole that just sucks all of your time away.
[1439.28 --> 1446.40]  So, um, ideally that would work. I mean, most of us, don't we all just kind of find a Webpack config
[1446.40 --> 1452.34]  on the internet that sort of works and then just like cobble ours together based on that blog post.
[1452.34 --> 1457.30]  And then once it works, never, ever, ever, ever touch it ever again.
[1457.44 --> 1464.98]  Yeah, exactly. And that's where, uh, where other tools like, um, we talked about Dojo last week and
[1464.98 --> 1469.78]  Angular and others, they have their own CLIs that are based off of Webpack, but they really abstracted
[1469.78 --> 1474.68]  away so that you don't have to deal with that. And you're just dealing with, with a simplified
[1474.68 --> 1480.76]  abstraction for, uh, for all of that configuration. And those two projects, uh, in particular are built
[1480.76 --> 1484.58]  on TypeScript. So it gives you that TypeScript right out of the box. I actually have a Webpack
[1484.58 --> 1488.78]  life hack that I think I shared on maybe the change. Like, I don't know. I've shared it before,
[1488.84 --> 1493.08]  but I'll share it again for those out there. Cause like in the chat, Alex raised, just working on a
[1493.08 --> 1498.56]  Webpack config right now. If you are stuck with Webpack, the life hack is this. You turn to Twitter
[1498.56 --> 1507.28]  and you complain loudly about Webpack and you tag it Webpack or you at mention Sean Larkin. You don't
[1507.28 --> 1511.68]  have to at mention him. I don't know if he's still doing this because he's gotten very busy, but Sean
[1511.68 --> 1517.36]  Larkin, who's one of the Webpack core contributors used to just watch Twitter constantly for anybody.
[1517.62 --> 1522.66]  And he would like live help almost anybody who's got problems with Webpack. And it was an amazing
[1522.66 --> 1527.88]  thing to behold. And, um, you can get personal one-on-one attention from a Webpack core contributor,
[1527.88 --> 1531.86]  mostly by just complaining on Twitter. So there's a life hack for everybody out there.
[1532.82 --> 1537.46]  That's how I've cobbled together a couple of Webpack configs in my days. Anyways, back,
[1537.56 --> 1541.36]  yeah, go back to TypeScript. Go ahead, Chris. Oh yeah. So about that, uh, the TypeScript loader,
[1541.44 --> 1547.88]  like last time I checked, I mean, that TypeScript loader is not like a core part of,
[1548.18 --> 1553.16]  it's not like an official loader, is it? I don't think so. I want, I'm just, I guess I'm wondering if
[1553.16 --> 1559.80]  that's like kind of on the, on the roadmap or I mean, does the Angular team use this,
[1559.80 --> 1567.04]  this loader as well? I would be saddened, but not really surprised if, if that TypeScript loader was
[1567.04 --> 1574.78]  some random single maintainer, um, somewhere, uh, that, that all of these tool chains are, are, uh,
[1574.78 --> 1582.62]  depending on. Yeah, that is a concern. Uh, it's under the TypeStrong, um, organization on GitHub.
[1583.34 --> 1589.96]  Uh, so I'm not sure if that's a company or what, but they also have like the TypeDoc project and
[1589.96 --> 1594.56]  others. Uh, so there's a lot of good popular projects in the TypeScript ecosystem out there.
[1595.22 --> 1598.72]  Um, and it's the one I've used. There's also another one called Awesome TypeScript loader,
[1598.72 --> 1605.38]  um, that I have less experience with that one because TS loader seems to, to work in,
[1605.46 --> 1610.64]  in a majority of cases. Yeah. I remember when I tried it, I, I wound up using the, the, the,
[1610.64 --> 1616.64]  the awesome one because the official one didn't like, I don't know, for some reason it was like
[1616.64 --> 1622.26]  behind and didn't work with the latest version of TypeScript or I don't even know. But, um, uh, I,
[1622.26 --> 1628.70]  I, I, as I recall correctly, the awesome TypeScript loader is, um, just kind of,
[1628.72 --> 1635.36]  of a, a personal like project of a person. It seems this TypeStrong one, the TS dash loader
[1635.36 --> 1640.98]  link in the notes will, has about 70 people contributing. But if you look at the contribution
[1640.98 --> 1646.34]  graph, it's, there's two people that have, there's three people with double digit commits,
[1646.34 --> 1650.96]  but one of them has 10 on the nose. So there's, it's mostly two people running it, but it appears
[1650.96 --> 1657.46]  to be pretty well supported. That being said, 106 open issues. That's the, uh, that's the joy
[1657.46 --> 1662.74]  of open source, right? Is, uh, figuring out what's worth pulling in and, and what's maybe
[1662.74 --> 1669.32]  more of a, uh, liability than an asset in terms of dependencies. But what's the official way
[1669.32 --> 1674.02]  to do it? Like that's the web pack way, right? But is, if you went to typescript, scriptlane.org
[1674.02 --> 1678.68]  or wherever you would go, what is like the official supported? Like, this is how you should use
[1678.68 --> 1683.06]  TypeScript. Will they say use the NPM module or what will they say?
[1683.06 --> 1687.42]  Uh, so you would just install the NPM module. So that's typescript and that will give you a,
[1687.42 --> 1693.38]  um, a CLI command TSC or typescript compiler. And that's, what's going to run. So if you,
[1693.56 --> 1699.86]  you can, uh, pass in command line arguments to that all you want, or that TS config file that I
[1699.86 --> 1705.06]  mentioned that it, uh, just configures it by default. So you don't have to remember all of
[1705.06 --> 1708.74]  the command line arguments over and over. You can just have it all in one config and then check that
[1708.74 --> 1715.58]  in with the project. And one of the config options in there is the, uh, type of module that you want
[1715.58 --> 1722.36]  to support. And so you can, uh, TypeScript by default supports, uh, ES modules, common JS modules,
[1722.36 --> 1728.06]  or AMD modules. And so if you were working in, uh, with AMD or common JS in your existing project,
[1728.06 --> 1733.84]  you can configure TypeScript to, uh, take the TypeScript files that you're writing with the ES
[1733.84 --> 1739.30]  module syntax and actually output that as common JS or AMD, and then provide your own AMD loader or
[1739.30 --> 1746.62]  common JS loader, like require JS or, um, browserify. Is that the other one? Um, and then just load,
[1746.78 --> 1750.48]  load the project, uh, as you would normally. And so it all really comes down to that. When you run
[1750.48 --> 1755.64]  the TSC file, uh, the TSC command, it looks at that config compiles all of the JavaScript that you
[1755.64 --> 1760.84]  have, uh, sorry, the TypeScript to JavaScript, puts that in a, uh, build directory that you specify
[1760.84 --> 1765.34]  in that config. And then, uh, those are the assets that you can actually run in the browser.
[1765.96 --> 1772.30]  So we've mentioned that has TypeScript has gotten broad adoption by huge names, right? Microsoft,
[1772.48 --> 1782.32]  Google, Lyft, Slack, Dojo, RxJS. These are all either projects or businesses that are operating at a huge
[1782.32 --> 1789.52]  scale. And that's really what the, the sales pitch is, right? Like TypeScript is a super set of
[1789.52 --> 1794.98]  JavaScript that's going to help your JavaScript libraries or applications scale. It's interesting
[1794.98 --> 1801.72]  that most of what we're talking about is tooling and documentation and refactoring abilities,
[1801.72 --> 1806.44]  but really like the, the old school argument of like dynamic types versus static types
[1806.44 --> 1812.94]  or strong versus weak. I never remember the exact lingo. Gary, uh, Vayner, not Vaynerchuk,
[1813.08 --> 1817.78]  Bernhardt would probably, you know, kill me if he hears that because he's very strict on what means
[1817.78 --> 1823.68]  what, but I always think of stronger or I think of dynamic versus static typing is like,
[1823.68 --> 1829.64]  as your project gets bigger, you're either more or less likely to write bugs if you have,
[1829.64 --> 1834.26]  you know, static types, but none of us are talking about types. I mean, we're talking about,
[1834.34 --> 1839.14]  it allows our tooling to introspect our code and allows us to refactor at a click of a button,
[1839.22 --> 1844.58]  stuff like this, but we're not talking about bug reduction or the things that you think about at
[1844.58 --> 1849.84]  scale, right? Like, is that, I just wonder what you guys think about that. Well, um, I think that
[1849.84 --> 1857.72]  for me, the, the reason why TypeScript has been a struggle is, um, I'm kind of a perfectionist. And so,
[1857.88 --> 1864.12]  um, that's, that's difficult, uh, as, as somebody who spends their time coding, because it's,
[1864.16 --> 1870.80]  it's really hard for me to call code good enough. Um, and so if I'm using TypeScript, I have,
[1870.80 --> 1877.58]  I now have types and I have to figure out what the type is of these things. And I have to be very
[1877.58 --> 1885.76]  meticulous about, um, you know, what I call this or that. And, and I think for me, it, it just,
[1885.90 --> 1892.58]  it pulls me way down the rabbit hole of thinking about types when I really just need to be thinking
[1892.58 --> 1899.22]  about the code and what it does. Um, and so that, uh, I, I think I said it's, it's poison for
[1899.22 --> 1905.58]  perfectionists because for me, it just, it just, uh, it just, it just, it just, it's so distracting.
[1906.00 --> 1911.60]  Um, just to, just to, to struggle to say, I have to get this type right. I have to get,
[1911.66 --> 1919.88]  get it perfect and, um, not being content to use the, the wild card, any type. Um, and that's,
[1919.96 --> 1925.78]  that's, that's just tough. Uh, but as far as like in enterprise adoption and, and, uh, you know,
[1925.78 --> 1931.20]  bug reduction, I have no idea. I don't even think I've gotten to writing too many tests. So,
[1931.20 --> 1937.94]  well, so Chris, I mean, uh, I'm curious what you mean by, you know, like worrying about the types
[1937.94 --> 1942.50]  because I mean, you gotta think about it at some point, right? Like I, I think of it in the
[1942.50 --> 1946.80]  classical sense of like, you know, a function accepting arguments and even Nick, that's what
[1946.80 --> 1952.28]  you were giving the example. Like this function takes a string and operates on it and returns a new,
[1952.28 --> 1958.72]  a new string, for instance. Um, it, you gotta think about that as a string at some point.
[1958.92 --> 1963.70]  And so where are you getting caught up? Cause you know, what, what tends to happen? I write
[1963.70 --> 1968.40]  in dynamic languages all the time, Ruby and JavaScript. I do not use TypeScript. Um, even
[1968.40 --> 1973.92]  Elixir is another language I use, which is dynamically typed. And I have, you know, I have to think about
[1973.92 --> 1978.86]  that a lot of times inside the bodies of my functions. Like, you know, what, what if this is
[1978.86 --> 1982.16]  not what I'm expecting? What do I do about it? And so you do have to make those
[1982.16 --> 1985.38]  decisions. I'm just wondering, like, is it pushing it too far up your mental stack? So
[1985.38 --> 1989.90]  like think of it all up front and you get stuck and you're used to thinking about it later or,
[1990.32 --> 1997.56]  uh, no, I mean, it's certainly not, the problem is not primitives. The problem is not string or
[1997.56 --> 2003.42]  number. It's your own types. The, yeah, the, the problem is these objects that, you know,
[2003.42 --> 2008.84]  maybe there it's an interface and I I'm passing these objects around that have this, these certain
[2008.84 --> 2017.08]  properties, or perhaps I'm expecting somebody to give me a callback and then describing using
[2017.08 --> 2024.34]  TypeScript, what that callback back looks like and what it can or cannot return. Um, and then,
[2024.40 --> 2029.86]  you know, just like throwing generics on top of everything is that's, that's kind of where it falls
[2029.86 --> 2037.44]  apart for me. It's just like, Oh no. Um, like, okay, this, this function accepts this, this object
[2037.44 --> 2045.86]  that is this duct type thing that is, you know, some abstract, ah, I don't know. It's, that's,
[2045.92 --> 2053.12]  that's just where it, there's just too much there for me to, yeah, that's, that's just all it is.
[2053.36 --> 2058.18]  It makes sense that it's, it's more, it's more about your own types and your own objects and it's
[2058.18 --> 2064.94]  about derivatives. Um, I, I find as in my situation as very much working on small teams or even lots
[2064.94 --> 2071.58]  of times a team of one and I make apps, right? I'm not a library, uh, maintainer. And so I'm my,
[2071.86 --> 2077.74]  I'm most of my codes user, right? Like my end users are using a website or a desktop app or something.
[2077.74 --> 2082.90]  So most of the time a website, I'm almost always going to be my own user. And so, you know, the
[2082.90 --> 2089.30]  annotations, even the documentation, you know, like defining the types of front for me just slows
[2089.30 --> 2095.98]  me down and doesn't allow me to kind of mold the code as I go or have to go back and change the
[2095.98 --> 2099.30]  types. And so that's, that's what I hit. And so that's why it makes sense to me that it's good
[2099.30 --> 2103.52]  for scale, but if you don't need scale, maybe not for you. And so that's kind of where I feel like
[2103.52 --> 2109.10]  I'm sitting. Um, Nick, you work, you know, at scale or you work on larger teams and larger projects.
[2109.10 --> 2113.12]  So tell us your experience. Yeah. First off, I would agree with both of you that, that that is
[2113.12 --> 2117.88]  one of the hardest parts to getting started. And it does feel like it's, um, impeding your
[2117.88 --> 2122.60]  productivity when you're just worrying about types, because at the end of, of the day, the types are
[2122.60 --> 2128.36]  compiled out at compile time and have no effect on the runtime at all. So it seems crazy to spend so
[2128.36 --> 2135.10]  much time on something that will never run. Um, but when you do get to a larger team, uh, with,
[2135.26 --> 2138.92]  with a lot more developers or a really big code base that you can't keep everything in your
[2138.92 --> 2143.96]  head, uh, I do think that it has benefits there because, uh, and it goes back to, to the tooling
[2143.96 --> 2149.32]  that we've been talking about because the, your, your editor, uh, will be able to tell you how to
[2149.32 --> 2152.74]  use something that you may have written six months ago without you having to go back and even look at
[2152.74 --> 2158.08]  the code. Uh, it can just, you know, infer like, or, or show you this expects two arguments that are
[2158.08 --> 2163.26]  this and this, or it's going to expect an object that has all of these parameters, but some of them are
[2163.26 --> 2169.34]  optional. Um, and you know, all of that. So it, it, it does help you with that helps you to keep
[2169.34 --> 2173.66]  everybody on a bigger team on the same page, uh, because you're really writing contracts for
[2173.66 --> 2178.96]  everybody to, to adhere to. And then they're strictly, um, they have to strictly adhere to it
[2178.96 --> 2183.58]  because the TypeScript compiler will, will yell at them otherwise. Uh, so it really does help with
[2183.58 --> 2188.04]  that. But when you're, if you're just trying to do some rapid prototyping, uh, it can definitely get
[2188.04 --> 2192.36]  in the way because it makes you feel like you have to really think about things, uh, and flesh them
[2192.36 --> 2197.32]  out and then, uh, you write the types for them or write interfaces for them and then go back and
[2197.32 --> 2201.18]  change those if you have to. So there's just a lot more code to change in between iterations,
[2201.18 --> 2208.74]  which can be tough. Um, or if it's, if it's just a, um, a smaller project, maybe that tooling,
[2208.74 --> 2213.40]  like if you can keep everything in your head, maybe it doesn't make as much sense, uh, to have all of
[2213.40 --> 2217.82]  that because you can, it's just getting in your way and you can go faster without it. I totally get that too.
[2218.04 --> 2222.80]  And then it further complicates things when you have third party JavaScript that you want to,
[2222.92 --> 2229.70]  to use within TypeScript that I have spent so much time trying to get types loaded and to find the
[2229.70 --> 2234.00]  correct types for things that are written in JavaScript, just so that I can get the compiler
[2234.00 --> 2239.36]  to not yell at me about, you know, some jQuery function I'm using or, or something along those
[2239.36 --> 2245.74]  lines, like something external that's, that just has these, these, um, type definition files that have no
[2245.74 --> 2252.24]  real, um, association with the project other than that they exist on, uh, in the definitely typed repo or,
[2252.24 --> 2259.26]  or other places. Um, and that can be challenging to get started up on, uh, especially when you're first
[2259.26 --> 2264.00]  starting off on a project, that's like the slowest thing. I was just doing this yesterday, trying to get a
[2264.00 --> 2270.92]  project started up and trying to use some older, uh, dojo stuff with the dojo types. And it's still a struggle
[2270.92 --> 2276.76]  to get all of that set up and working properly. I think, you know, just if, if there was a large project
[2276.76 --> 2283.34]  and, um, say there were two at your company and, uh, one of them was written in JavaScript and one of them
[2283.34 --> 2290.76]  was written in TypeScript and you, uh, one, you were expected to choose between them and, and which one are you
[2290.76 --> 2295.84]  going to step into and start maintaining and, and learn from scratch? Yeah, you should pick the TypeScript one
[2295.84 --> 2303.02]  because it's going to be so much more clear about what everything is. Like I, I totally see that, um,
[2303.06 --> 2312.12]  that benefit. It's, it's, it, it, it helps, uh, you know, if somebody has done it for you, sure. Like
[2312.12 --> 2319.62]  there's, there's all these, you know, you have to do it yourself. Yeah. Yeah. I, I like, uh, you know, I,
[2319.62 --> 2325.72]  I have contributed a few little random PRs to TypeScript projects and it's fun. Uh, it's easy
[2325.72 --> 2331.22]  to understand what's going on, but, uh, just having to think about that stuff myself is, it's pain for
[2331.22 --> 2338.38]  me. We've seen a lot of open source library teams and authors adopt TypeScript for that reason that,
[2338.38 --> 2344.32]  you know, they're willing to put in that extra effort, um, up front, if you will, or while they are,
[2344.32 --> 2351.94]  you know, building out the architecture in order to ease adoption from contributors and, uh,
[2352.34 --> 2356.52]  Makes sense. Yeah. I mean, that, that makes sense from, from my perspective. I've never,
[2356.52 --> 2362.92]  um, tried to, you know, I've never opened a PR on a TypeScript project and thought, oh, this is way
[2362.92 --> 2368.08]  better. I just haven't come across that situation, but it's interesting hearing, uh, Chris, that,
[2368.20 --> 2372.60]  that that's an experience you've had. And I think that's a testament to, to what it provides.
[2372.60 --> 2376.78]  And I think it's important to note that, or maybe not important. It's just like,
[2376.82 --> 2381.90]  it's interesting to recognize that I never felt that way about a CoffeeScript project. Uh, like
[2381.90 --> 2386.50]  if there was a CoffeeScript, something written in CoffeeScript and I wanted to like, I wouldn't send
[2386.50 --> 2391.20]  the PR, you know, uh, if I was like, oh, there's a bug in this thing, I could, I should go fix it.
[2391.20 --> 2394.76]  And I go and look and it's CoffeeScript, forget it. Well, yeah. I mean, CoffeeScript was a departure
[2394.76 --> 2400.70]  though. So there was, you know, it's, it's, it's more of a dialect as opposed to TypeScript, which
[2400.70 --> 2406.76]  you could say is also a dialect, I guess, of JavaScript, but, uh, more syntactically familiar.
[2406.98 --> 2412.78]  Whereas CoffeeScript was introducing not just syntactic sugar, but also, you know, new functionality.
[2412.78 --> 2417.08]  So I could see where that would be a stopping point. And we've seen libraries switch from
[2417.08 --> 2421.10]  CoffeeScript to either vanilla JavaScript or who knows, maybe now TypeScript because of,
[2421.50 --> 2426.84]  because of that, that road bump it's putting, it was putting in people's, but yeah, it definitely
[2426.84 --> 2430.82]  helped push the industry forward though. So I think it was, I think it was a net win for
[2430.82 --> 2437.28]  programming. Um, but I'm glad that it doesn't have to be out there in, in mass use anymore.
[2437.28 --> 2443.08]  Yeah. And I think that TypeScript, uh, being a superset of JavaScript is that that's one of
[2443.08 --> 2448.62]  its big benefits too, in that, uh, JavaScript is always changing. You know, every year we're
[2448.62 --> 2453.10]  getting new, uh, TC39 proposals going through that process and getting added to the language
[2453.10 --> 2458.04]  and TypeScript isn't standing still. It's staying on top of all of those. And as features
[2458.04 --> 2464.80]  become more, uh, as they pass through that, uh, stage process from TC39, uh, when, when
[2464.80 --> 2470.68]  they reach like stage three, if they can be transpiled back to like ES5, they do get supported
[2470.68 --> 2477.34]  into, uh, TypeScript. And so it is kind of a, a safe way to use the next version of JavaScript
[2477.34 --> 2478.98]  with types as well.
[2478.98 --> 2484.98]  Is there any proposal, uh, currently in the pipeline that would, um, that TypeScript couldn't,
[2484.98 --> 2491.06]  um, implement because it would conflict with its own language?
[2491.06 --> 2500.94]  So there's the, um, the class properties proposal. And with that, there's the privates. Um, so being
[2500.94 --> 2505.88]  able to use that, that pound sign for, for privates, uh, on classes natively in, in JavaScript,
[2505.88 --> 2511.56]  TypeScript has already been using the private keyword to do that. Uh, but of course that's
[2511.56 --> 2516.22]  just a compile time check. This would actually be a runtime check. There are also some, some
[2516.22 --> 2520.70]  differences. So, um, there is an issue open. I can find it and put it in the show notes,
[2520.70 --> 2527.94]  uh, that, um, discusses that, but I don't know the exact outcome. I think last I, I checked, um,
[2528.40 --> 2533.22]  it makes sense for them both to exist, but, uh, I don't know if, if they would ever reconcile.
[2533.22 --> 2538.54]  Yeah, it would need to be something like a, just a, a purely syntactic thing that has,
[2538.54 --> 2545.04]  uh, like a, a conflict. Um, I can't think of anything. It's, it's probably in the best
[2545.04 --> 2553.96]  interests of everybody. Um, as much as I'm sure the TSC or, uh, the, uh, uh, you know, the TC39 team
[2553.96 --> 2559.84]  doesn't want to have to worry about TypeScript. They, it's probably a good idea to not just,
[2559.84 --> 2563.04]  you know, brazenly introduce things that will break TypeScript.
[2563.30 --> 2568.54]  Right. And that's where I think it's a safe thing, like, like a safe way to stay on the
[2568.54 --> 2571.64]  latest versions of JavaScript because you're not on the bleeding edge. You're not on the
[2571.64 --> 2577.30]  stage zero, stage one, stage two proposals. You're on this prescribed, these are likely not
[2577.30 --> 2581.58]  going to change. And so they're supported by TypeScript. And if they, for some reason they
[2581.58 --> 2587.32]  changed, uh, there would probably be some kind of, um, conversion within TypeScript to,
[2587.32 --> 2591.70]  to help handle that, uh, potentially, but usually they don't get there and they don't,
[2591.70 --> 2597.38]  they don't implement them in the language until the, the syntax is, is certain. The only exception
[2597.38 --> 2601.82]  to that is decorators. Oh, right, right, right, right, right. Yeah. Yeah. TypeScript has its own
[2601.82 --> 2609.26]  idea of, about decorators and, uh, that has diverged from, I don't even know where that proposal is
[2609.26 --> 2614.94]  anymore, but. Yeah. But they have it because of, uh, because of Angular, when, when Angular was
[2614.94 --> 2618.46]  switching over to TypeScript, they actually wanted to have a superset of TypeScript called
[2618.46 --> 2623.38]  AtScript that basically added that and some other features. Uh, but then those were actually brought
[2623.38 --> 2627.72]  down into TypeScript in version 1.5. Uh, and it just stayed as TypeScript.
[2627.72 --> 2638.94]  Hey everyone, I'm Tim Smith, senior producer here at Changelog. You know how important it is to stay
[2638.94 --> 2644.90]  in the know and our weekly newsletter helps you and thousands of other developers do exactly that.
[2645.06 --> 2651.04]  It's the developer news that matters, nothing more and nothing less. Visit changelog.com and subscribe
[2651.04 --> 2671.90]  today. All right. We are switching gears just a little bit. This is related to TypeScript in a sense
[2671.90 --> 2677.28]  that it's about types, but it's a different conversation. I wanted to talk about developer
[2677.28 --> 2684.84]  titles and, uh, the difficulty of titling us, what we do, who we are, stuff like that. There's two
[2684.84 --> 2690.24]  distinguishments that we see out there. Um, one I think is completely arbitrary. So I'm playing my cards
[2690.24 --> 2696.40]  right up front and I think it's not useful, but I've started to see a trend where people are
[2696.40 --> 2706.50]  distinguishing between the terms programmer, developer, coder, engineer, and maybe there's more,
[2706.50 --> 2713.24]  but those are the four that I see often either just used or perhaps compared and contrasted.
[2713.96 --> 2720.32]  A second type that I think is more useful, perhaps just as hard to distinguish between,
[2720.98 --> 2727.34]  is between the idea of a junior and a senior in terms of a developer slash programmer slash
[2727.34 --> 2734.00]  engineer, et cetera. So I wanted to talk about that and get your guys' take because my take on the
[2734.00 --> 2740.22]  first topic of this distinguishment, and I've seen it twice recently by people that I respect and
[2740.22 --> 2749.82]  somewhat admire, is, uh, distinguishing specifically between engineers versus programmers. And, uh, both
[2749.82 --> 2755.76]  examples were different. That's why I say, I think it's arbitrary. Like neither one of them were
[2755.76 --> 2760.58]  agreeing. They were completely different criteria by which they were explaining what makes an engineer
[2760.58 --> 2767.48]  versus a programmer. And both of them introduced kind of a class hierarchy in terms of you want to
[2767.48 --> 2771.92]  be an engineer and now you don't want to be a programmer. So the programmer is somehow less than,
[2772.76 --> 2776.90]  um, so let's start with that, what you guys think are. First of all, what do you call yourself to people
[2776.90 --> 2783.38]  and does that matter? And do you see what I see and what are your thoughts on programmer or developer
[2783.38 --> 2790.32]  titles? Uh, so my official title at my, at the company I'm at is senior software engineer. Uh,
[2790.32 --> 2797.50]  but I typically just go with developer. Um, I, I don't really care about the distinction or,
[2797.56 --> 2802.48]  or think about it much. What do you think about it when other people use it? So for instance,
[2802.48 --> 2808.76]  what if I'm ignorant of the distinction and I call myself a programmer because that's just a word that
[2808.76 --> 2814.82]  I've used, but out there exists or there's beginning to form a distinction in which programmer is somehow a
[2814.82 --> 2822.66]  lower level expert or skill set. Um, maybe I'm pigeonholing myself. Is this a trend that you are,
[2822.84 --> 2828.10]  you know, you for, against, indifferent to these distinctions? Like you don't seem to care
[2828.10 --> 2833.18]  personally, but do you care if we kind of adopt a social norm around these things?
[2833.64 --> 2839.14]  This, this is kind of, this is kind of a tough, yeah. Somebody said in the, the Slack chat,
[2839.14 --> 2847.60]  it's a powder keg of a topic. Um, personally, so my job title is developer advocate, but the cross
[2847.60 --> 2855.30]  section of people who have any idea what that means is, is very, very few. And so, uh, it can just,
[2855.40 --> 2862.24]  it's like when I say, you know, my job is such and such, I, uh, you know, depending who I'm talking
[2862.24 --> 2870.30]  to, I could say, you know, I'm, uh, it's usually, I'll just say I'm a programmer. Um, if, uh, if I'm
[2870.30 --> 2878.32]  writing something on like a form that wants to know what my job is, I put software engineer. Um, but
[2878.32 --> 2889.58]  yeah, as far as like official titles, like I don't even know, I do not know. Um, I, there's,
[2889.58 --> 2894.38]  there's all sorts of, you know, title of inflation, you know, there are states where you can't call
[2894.38 --> 2902.26]  yourself an engineer without, you know, um, it's like illegal to, to, to do that or something. Um,
[2902.72 --> 2909.98]  you know, because the, the, the term engineer is reserved for, you know, civil engineers, mechanical
[2909.98 --> 2915.98]  engineers, um, people with certifications. Right. And there is, there is no such certification for,
[2915.98 --> 2921.62]  for software engineers, though there might be in some States. Uh, I don't remember, but yeah,
[2922.04 --> 2928.94]  that's tough. I think I saw a few years back, um, when this topic came up again, somebody referring
[2928.94 --> 2935.22]  to, to a better term, which would be like a software gardener, uh, because that's more appropriate to
[2935.22 --> 2940.74]  what we actually do. We kind of grow software from, from seemingly nothing. I think that was,
[2940.82 --> 2945.40]  well, I, I know specifically a blog post that I think about often was Steve Klabnick's,
[2945.40 --> 2952.02]  um, open source is like gardening or something like that. Referring to how you like actually
[2952.02 --> 2957.82]  maintain and, and grow an open source project is more like, it should be modeled after the way
[2957.82 --> 2961.90]  a gardener goes about maintaining and growing a garden. So that definitely resonates. I haven't
[2961.90 --> 2966.36]  heard anybody say I am a software gardener or we should be calling ourselves software gardeners,
[2966.36 --> 2971.58]  but I think that's a fit metaphor. So like, this is, this is a distinction that I, I heard a quote of
[2971.58 --> 2976.80]  that kind of got me thinking down this, where the one distinguishing, and I'm not, I'm not here to
[2976.80 --> 2981.62]  call anybody out, so I won't even quote who it is, but just the, the idea is that a programmer seeks
[2981.62 --> 2987.60]  first to solve a problem and perhaps later understands the problem better. And then an engineer seeks first
[2987.60 --> 2993.58]  to understand the problem and perhaps later solves the problem. And so, I mean, that's completely out of
[2993.58 --> 2998.06]  context. That was a quote I saw on Twitter that got me thinking of like, what are we doing here?
[2998.06 --> 3004.86]  Like what, this seems like somehow now an engineer, you know, is a deeper thinker than a programmer.
[3005.18 --> 3010.42]  I've also heard elsewhere where, you know, people degrade the word coder because that's if you're a
[3010.42 --> 3015.46]  code monkey or you like don't actually think you just go type into a keyboard, but a developer is
[3015.46 --> 3020.80]  like an enlightened person. And so it seems like a troubling trend, um, where the three of us don't
[3020.80 --> 3024.82]  seem to have opinions on these words. I think they're just swap them in, whatever makes you feel good.
[3024.82 --> 3032.28]  But I think labeling other people as certain ones and then creating distinctions where I don't believe,
[3032.50 --> 3036.66]  you know, there's a standard around how they actually are distinguished. I think engineer might be,
[3036.78 --> 3044.18]  like you said, Chris, eventually more of a distinction if there is a license, I hope not, or a, you know,
[3044.24 --> 3048.16]  accreditation that makes you an engineer and now, you know, gets you a raise or whatever.
[3048.16 --> 3054.00]  But I fear that, you know, these things could be used to basically lord over other people,
[3054.00 --> 3058.02]  uh, whose skill sets are, you think, inferior to others.
[3058.38 --> 3064.60]  Yeah, I do have a problem with it when it's referred to in this way. Uh, because to me that
[3064.60 --> 3068.80]  implies that, uh, a programmer will never be an engineer and an engineer will never be,
[3069.06 --> 3074.18]  well, will not like downgrade to a programmer in the, in this context. Um, and it, like it,
[3074.18 --> 3078.96]  to me though, like, you know, the, the order of which you do things, solving a problem, uh, and
[3078.96 --> 3084.00]  then trying to understand the problem or vice versa, that comes with experience. And I don't think that
[3084.00 --> 3086.88]  being more experienced would magically change you into an engineer.
[3087.24 --> 3090.62]  Yeah. I mean, just thinking about how I talk about myself, I, and I don't think any of these terms,
[3090.62 --> 3095.24]  uh, hold weight over the others, but I will tend to just say, you know, what do you do? I just say,
[3095.24 --> 3101.54]  I write software or as, uh, Montes Lu says in the chat, what do you do? I make websites like to laymen.
[3101.54 --> 3105.48]  And that's actually something that makes sense to them. I make websites, but, uh, for industry
[3105.48 --> 3109.22]  insiders. And of course these distinctions are happening inside our industry. It's not like
[3109.22 --> 3114.74]  we're making distinguishments for the general public to use, but I think we see it inside HR
[3114.74 --> 3120.12]  departments and in hiring practices, it could perhaps become toxic. Let's go to, uh, the other one,
[3120.12 --> 3126.60]  which I think is much more useful, but also just as hard to, to define because it seems like it's a,
[3126.60 --> 3131.12]  the field goalposts are always moving, which is what makes a junior developer versus a senior
[3131.12 --> 3139.34]  developer. And, uh, I saw a funny tweet about this that I was pulling up from Trek Glowowski.
[3139.34 --> 3144.42]  Since our industry seems hell bent on giving people senior titles who are in the first decade
[3144.42 --> 3149.58]  of their career, I'd like to propose we introduce a new layer of elder software engineer for people in
[3149.58 --> 3155.20]  the 11 to 20 year range and ancient software engineer for those 21 plus. So a bit tongue in
[3155.20 --> 3160.46]  cheek there, but Trek is, you know, lamenting the fact that, uh, senior is not being used the way he likes
[3160.46 --> 3165.56]  it. Right. And people who are, you know, not, they're still in their first decade. And so he's
[3165.56 --> 3170.14]  saying it's, it's about decades, but curious what your guys are thoughts on senior versus junior
[3170.14 --> 3175.54]  developer. Is there a distinguishment that we can come to, you know, uh, is it completely in the eye
[3175.54 --> 3181.10]  of the beholder? If you, if your title is a junior, then, um, that just means your company pays you less.
[3181.36 --> 3184.14]  That's definitely a fact. So how do you get them to call you a senior?
[3184.14 --> 3192.12]  I don't even know. You don't know. I mean, I was, I was, I was a senior. Oh, let me see here. How
[3192.12 --> 3199.66]  many years into it? Um, it would have been, yeah, I was, I was a senior before, before my first decade
[3199.66 --> 3204.06]  was out. Sure. Software moves a lot faster than decades. Kind of like dog years, you know,
[3204.14 --> 3209.04]  seven for everyone or something like that. Yeah. So like there's, there's a lot of experience that
[3209.04 --> 3214.22]  you can get. And then, um, you have to stick at it, stick with it. Uh, and you learn how to learn,
[3214.22 --> 3218.46]  I think. And that might be some kind of distinction, but I don't think that it really,
[3219.04 --> 3226.92]  I don't know. I don't, I don't really like that term either. Um, I, I like thinking of them in terms
[3226.92 --> 3235.44]  of like, uh, a mentor mentee type, type thing where, where a, uh, a junior developer would be more of a,
[3235.44 --> 3243.08]  um, you know, they, they would be learning to learn. And then the, the senior would be kind
[3243.08 --> 3248.20]  of helping to facilitate that learning, but also trying to learn because that's, you should never
[3248.20 --> 3253.10]  stop. Uh, and, and I'm not, I'm not trying to say that seniors can't learn from, from juniors at
[3253.10 --> 3259.62]  all. Um, but they're just, I don't know. I feel like I'm painting myself into some weird corner now.
[3259.62 --> 3268.26]  Google's idea on, on job titles, I think, you know, for as many issues as Google has, um,
[3268.86 --> 3275.44]  that's not a bad idea, but others may disagree. So, uh, as far as I know, like most everybody,
[3275.44 --> 3282.80]  uh, there is just software engineer and there's no senior, there's no junior, there's no programmers,
[3282.80 --> 3287.94]  there's no, you know, software engineer three. Um, you know, there's nothing like that.
[3287.94 --> 3289.96]  They just have pay levels associated with that.
[3290.08 --> 3295.58]  Yeah. As far as I know, that's just, everybody's a software engineer there, but, um, maybe some
[3295.58 --> 3298.84]  people have different titles. I don't, I don't know. That's just the impression I got.
[3298.94 --> 3302.90]  That was similar to how the way GitHub handled itself in the early days. I'm not sure how it
[3302.90 --> 3309.48]  works anymore, but everybody came on at the specific exact, as everybody was software engineers
[3309.48 --> 3316.32]  or developers or coders back then at first. Um, and they wore many hats as a small startup,
[3316.32 --> 3322.56]  but they all started at the exact same salary. And then it was just like every year you just got
[3322.56 --> 3327.92]  a raise and it was just standard. And so it's just based on not how many years you've been in,
[3327.92 --> 3333.16]  in, in the industry, but specifically your salary was just based on how long you were at GitHub.
[3333.88 --> 3340.32]  Um, and I think that had a change as they grew as a company. So, but yeah, that's kind of level,
[3340.58 --> 3344.96]  level ground. I'm definitely a fan of level ground in terms of the nomenclature that we use
[3344.96 --> 3349.76]  amongst ourselves. I understand that inside businesses, you have to come up with a structure
[3349.76 --> 3354.60]  and businesses picks different structures. And so they can all have their own definitions of
[3354.60 --> 3361.94]  these things. But I do think that there's, there's a, there's a, there's a con, there's a negative
[3361.94 --> 3367.62]  connotation towards juniors that it's like, you're trying to escape that. All right. Like when can I
[3367.62 --> 3375.82]  become not a junior anymore? And it seems like the goalposts are always moving. Um, so tricky things
[3375.82 --> 3380.22]  for sure. I think that it can be detrimental to call yourself a senior too. I know that when I
[3380.22 --> 3386.78]  quote unquote earned that title, um, I felt like I lost permission to ask stupid questions. And I think
[3386.78 --> 3393.62]  that that, um, that put me into a, a period of burnout for a little while, uh, or, or imposter
[3393.62 --> 3400.40]  syndrome, it like took over, which led to burnout. Uh, so I think that, that it can be dangerous in
[3400.40 --> 3404.74]  that sense too. That was just, you know, me coping with that. I know I can ask stupid questions and I
[3404.74 --> 3410.36]  do regularly. Uh, but, uh, it really felt like you're a senior now. You shouldn't do that.
[3410.68 --> 3411.08]  All right.
[3411.28 --> 3411.76]  Know this.
[3412.22 --> 3417.92]  Cool. Interesting stuff. Well, uh, fun little diversion, uh, from typescript, but, uh, you know,
[3418.02 --> 3422.58]  can't be all a TS party. We had a, we had a, we had to work some more, some more stuff in here.
[3422.58 --> 3429.70]  That being said, I do want to promote our call in line. We would love to hear listener voices on
[3429.70 --> 3434.54]  this show. Uh, that's one of the reasons why when we relaunch, we expanded the panel. We want more
[3434.54 --> 3441.40]  voices, whether you're a junior or a senior or just a little coder or a big software engineer,
[3441.64 --> 3447.30]  whoever you are out there, we want to hear from you. Let us know what you think. And you may even
[3447.30 --> 3454.96]  hear your own voice on a future JS party. The number to call is 888-974-CHLG like change log.
[3455.26 --> 3463.40]  That's 888-974-2454. Hit extension one for JS party. Leave your name, leave your comment. If you
[3463.40 --> 3467.38]  have a question, maybe you have something to say about typescript that didn't get represented and
[3467.38 --> 3471.62]  you want that played in a future show. Maybe if you have a great way to distinguish between junior
[3471.62 --> 3476.84]  and senior devs and you want to tell us, call that number, leave us a message. We will receive it.
[3477.30 --> 3482.20]  And you may hear your own voice on an upcoming episode. We would love to have even more people
[3482.20 --> 3489.24]  at this party, but that is it for today's show. Uh, Chris and Nick, thanks for hanging out with me.
[3489.52 --> 3494.42]  Thanks for teaching me about typescript and, uh, that's all folks. You don't have to go home,
[3494.42 --> 3501.10]  but you can't stay here. All right. Thank you for tuning into JS party this week. Tune in live
[3501.10 --> 3508.16]  on Thursdays at 1 PM U S Eastern at change law.com slash live. Join the community and slack with us
[3508.16 --> 3512.66]  in real time during the shows head to change law.com slash community and do us a favor,
[3512.80 --> 3517.26]  share this show with a friend, read us an Apple podcast, go into overcast and favorite it.
[3517.40 --> 3523.02]  And thank you to fastly, our bandwidth partner, head to fastly.com to learn more. And we move fast to
[3523.02 --> 3527.32]  fix things around here at change law because of roll bar, check them out at robot.com. We're
[3527.32 --> 3532.58]  hosted on Leno cloud servers at the leno.com slash change law. Check them out and support this show.
[3532.70 --> 3537.28]  Our music is produced by break master cylinder, and you can find more shows just like this
[3537.28 --> 3540.60]  at change law.com. Thanks for tuning in. We'll see you next week.
