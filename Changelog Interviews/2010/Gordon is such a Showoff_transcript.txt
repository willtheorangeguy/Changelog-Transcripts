[0.00 --> 21.96]  Welcome to the Changelog episode 0.1.2. I'm Adam Stikowiak.
[21.96 --> 26.98]  And I am Winn Nethelen. John Nudermaker stuck around and we ran through the projects on our
[26.98 --> 32.62]  Radarm. The ones that we posted up on thechangelog.com. And when we do that, they become featured projects
[32.62 --> 37.88]  over on GitHub at github.com forward slash explore. It's also a great way to catch up on
[37.88 --> 43.82]  some old episodes that maybe you haven't seen. Also, I'd like to remind you, you can go out to
[43.82 --> 49.86]  tail.thechangelog.com and see a real-time view of the world of open source as open source commits
[49.86 --> 53.62]  flow in and out of GitHub. We've gotten lots of good feedback on that actually on Twitter.
[53.62 --> 60.24]  Yeah, I was proud that iTodd added us at Changelog Show and told us that he appreciated the
[60.24 --> 63.12]  application since we appreciate his project, Fluid.
[63.46 --> 68.40]  Yeah, I think it's kind of fun too when people discover that when they first get there, they
[68.40 --> 72.74]  see this sort of tail-like application of what's happening on GitHub. But then they also notice
[72.74 --> 79.12]  that they can have filters applied to that either through the normal constant flowing tail
[79.12 --> 82.64]  or through that more spot where you can actually just scroll the infinite scroll.
[82.64 --> 85.20]  And browse backwards in time on the more application?
[85.40 --> 91.00]  Yeah, it's kind of fun to just see people discover tail.thechangelog.com first. And then
[91.00 --> 96.24]  they're like, oh, oh, wow, I can actually filter by event types and then also languages.
[97.16 --> 102.36]  So I often just sit there and whenever I'm looking for cool stuff to post to the Changelog,
[102.54 --> 107.80]  I often just sit there with a certain filter and look across because I'm all about Ruby.
[107.80 --> 111.24]  I'm always filtering just by Ruby, right? Only Ruby stuff.
[113.60 --> 117.74]  But it's also great to be able to filter out those event types that you don't care about.
[118.28 --> 122.80]  And if you just remove the pushes, then it becomes a lot more manageable to kind of drink
[122.80 --> 125.58]  from that fire hose. Where else can folks catch up with us?
[125.96 --> 131.56]  Well, I think if they're on Twitter, they should go to Twitter right now and follow us.
[131.56 --> 136.28]  The show is Changelog Show, oddly enough. It's not The Changelog. It's Changelog Show.
[136.46 --> 140.40]  And I have a Twitter account. It's AdamSTAC. And who are you, Wynn?
[140.88 --> 146.00]  I'm Penguin, P-E-N-G-W-Y-N-N. What about in person? I know we're going to be at FOA at the end of the month.
[146.22 --> 150.34]  Yeah, FOA. We'll be at the Future of Web Apps held by Carsonify down in Miami, Florida.
[150.34 --> 156.20]  That is happening May 22nd through the 24th. Both myself and Wynn will be there.
[156.32 --> 161.78]  We'll be there probably representing the Changelog, of course, and also the Web 2.0 show.
[161.98 --> 164.82]  So if you see us, say hi.
[165.22 --> 166.00]  We'd love to meet you.
[166.20 --> 166.60]  Absolutely.
[167.16 --> 168.06]  Ready to get to the episode?
[168.40 --> 168.86]  Absolutely.
[169.42 --> 169.94]  Let's do it.
[169.94 --> 182.56]  All right. John's kind enough to stick around and talk through the news with us.
[182.76 --> 189.54]  And it's usually news of the week, but we wanted to go back a bit and catch up on some items that we dropped over the Christmas break.
[189.54 --> 193.64]  And so the first item up is Friendly. NoSQL with MySQL and Ruby.
[194.12 --> 196.52]  So this is from James Gullick, I believe, right?
[197.06 --> 197.28]  Yeah.
[197.28 --> 208.12]  So your take, John, since you've got a Mongo mapper out there for MongoDB, this is kind of a similar approach in Schemeless Database, but they're doing it with a relational backend in MySQL.
[208.28 --> 209.12]  So what's your take on this repo?
[209.70 --> 210.94]  I think it's pretty interesting.
[211.18 --> 220.72]  I mean, you know, whether you use MySQL or use a NoSQL database from the beginning, it's just the concepts that matter.
[221.00 --> 224.06]  And, you know, the concept that they're doing with this is the same.
[224.06 --> 227.26]  They're just – they're kind of writing some of the code that would maybe be in Mongo.
[227.42 --> 232.36]  But I think they – I think these guys actually did try Mongo, and they ran into some issue that they had.
[232.48 --> 233.44]  I don't know what it was.
[234.64 --> 236.42]  But – so I think it's a pretty interesting project.
[236.42 --> 242.08]  I – for me, it's – I mean, being – I'm probably wrong.
[242.18 --> 248.36]  But for me, I would say it's kind of like using CakePHP instead of Rails, but I could be horribly wrong on that.
[248.44 --> 251.18]  I haven't looked at it a ton, but it seems really interesting.
[251.32 --> 255.18]  And I definitely plan on, like, going through the code because I'm sure there's some interesting stuff in there.
[255.24 --> 256.64]  James usually puts out good work, so.
[256.64 --> 264.92]  But it's nice to see that the – you know, NoSQL, for the lack of a better term, the schemeless database approach is really getting prevalent.
[265.44 --> 265.66]  Yeah.
[265.84 --> 272.44]  Well, and the other great thing is that if – there's some organizations that they don't want to support a million databases and stuff, and they don't want to update.
[272.44 --> 277.64]  And so if they want to use MySQL, but you still want to get the benefits of NoSQL, this is great for that.
[277.76 --> 279.00]  I mean, this is perfect, you know.
[279.48 --> 286.06]  And I'm sure, like – I mean, I know they've talked about it before, but this was made to handle, like, a lot of traffic and a lot of stuff.
[286.20 --> 288.22]  So I think it's pretty interesting.
[288.36 --> 293.10]  It's definitely – for some people, it's going to be perfect, and for others, it won't be.
[293.44 --> 299.26]  But that's the great thing is everybody's different, and, you know, there's – whether it's split right down the middle, it doesn't matter.
[299.62 --> 300.86]  There's no sides.
[300.86 --> 301.90]  So I think it's really cool.
[301.90 --> 307.46]  That's a nice segue into more of a front-end project in SCSS.
[307.64 --> 309.38]  It's CSS-style syntax for SAS.
[309.98 --> 311.76]  It seems like SAS, you either love it or hate it.
[312.00 --> 313.06]  You SAS at all, John?
[314.94 --> 323.04]  No, I was a hater, but we're actually – and this is, like – we're actually thinking about throwing some SAS functionality into Harmony.
[323.40 --> 323.68]  Oh.
[324.48 --> 325.32]  Yeah, so we're going to –
[325.32 --> 325.72]  Get me excited.
[325.72 --> 330.94]  Well, we just kind of – Steve added it as an issue the other day and kind of smiled at me.
[331.44 --> 334.54]  And I – at first, I was like, oh, I hate Hamlin SAS.
[334.84 --> 336.68]  But then I was like, you know, I've never really looked at SAS.
[336.82 --> 341.20]  And we've talked about supporting variables and things like that, so why not use something that already works?
[341.20 --> 349.34]  So I would say that's probably going to come to a Harmony near you in the next month or so is some kind of support for SAS out of the box.
[349.80 --> 354.22]  Did Steve share any opinions on SAS with you that you can share here on the change log?
[354.22 --> 360.20]  Well, I think what got him excited – so Steve's the designer, the aesthetic of half of ordered lists.
[360.78 --> 368.82]  And so I think what got him excited is, you know, the ability to do a little bit of programming with – I mean, both of us have always had a few things that we think CSS should do.
[369.06 --> 373.16]  And one of them is variables because you reuse colors, you reuse, like, things.
[373.22 --> 373.96]  That just makes sense.
[374.06 --> 378.58]  And the other thing that SAS does, you know, it allows you to do functions, which is kind of interesting.
[378.98 --> 382.68]  The other thing that is huge, I think, is nesting declarations.
[382.68 --> 392.68]  So, you know, if you want to – if you have a div with an idea of main and you have, like, some posts or something inside of that, you can do a declaration with curly braces for main.
[392.76 --> 402.40]  And then inside of that, you can do, like, .post, and it will actually automatically add, like, sharp main.post as, like, the full selector for that thing.
[402.92 --> 410.92]  So there's some really cool stuff with SAS that it does in that aspect that I think that's what really drew him to it because it can remove some duplication from your style sheets.
[410.92 --> 411.68]  Yeah, so –
[411.68 --> 412.76]  I was thinking about that the other day.
[413.16 --> 418.54]  Actually, sadly enough, I'm working with WordPress on this other site I'm working with.
[418.70 --> 421.66]  It's the Web2O show, web2oshow.com.
[421.72 --> 423.24]  But I'm working on a new theme for it.
[423.32 --> 430.44]  And I – you know, through Wins Help, we actually have a gem out there called Compass WordPress where we actually use SAS and Compass to work with WordPress.
[430.44 --> 432.38]  Just – it's kind of wild.
[432.38 --> 439.22]  But I was thinking to myself, geez, if I had to write this with actual CSS, how much repetition I would actually do.
[439.28 --> 442.52]  I was just thinking – this morning, too, when I was making the coffee, I was – I don't know why I reflected on it.
[442.58 --> 448.14]  I'm thinking, if I had to repeat all those selectors, how much time would I waste doing that CSS?
[448.32 --> 448.92]  It's just insane.
[449.04 --> 450.02]  But that's wild.
[450.30 --> 450.56]  Cool.
[450.82 --> 452.10]  I'm happy to see that come to Harmony.
[452.10 --> 465.04]  As in one way that the schemeless approach is kind of creeping into web development, if there's so many projects out there that are taking this approach, it cries that a problem is out there, right?
[465.10 --> 469.92]  And I think it's the same thing with CSS processors and meta frameworks, whatever you want to call them.
[469.92 --> 480.80]  If there's so many approaches between SAS and less CSS and XSS and you name it, there's a project out there in your language to do this type of work to generate this CSS,
[480.80 --> 485.38]  I think it just speaks to maybe CSS needs some modernization.
[486.12 --> 487.56]  Yeah, and I don't know if you guys know this.
[487.66 --> 493.06]  Does it – when it does like some of the things – I've read about what it does, but does it use the spec if it's there?
[493.28 --> 495.04]  Because I know there's a spec for variables already.
[495.14 --> 498.86]  I didn't know if maybe they use the same syntax or –
[498.86 --> 499.44]  I don't know.
[499.56 --> 500.24]  I'm not sure.
[500.38 --> 501.54]  Chris would definitely be able to answer that.
[501.54 --> 508.76]  Maybe in your free time, pipe out on Twitter and just say, hey, at Chris Epstein, does SAS leverage CSS's natural variable?
[508.76 --> 509.76]  So –
[509.76 --> 517.80]  I think that would be really cool to have a processor that actually supports the standards that are set that will be in browsers someday when they update, and that would be kind of interesting.
[518.00 --> 523.80]  Yeah, currently I think since browser support is limited for those particular variables in CSS, I don't think they're doing that currently.
[523.92 --> 527.78]  I think it's all pre-processed and then just vanilla CSS comes out the other side.
[527.78 --> 533.22]  One project I wanted to touch on was Configulari, which is still a tongue twister for me.
[533.22 --> 536.48]  But we had an excited Mr. Flip.
[536.64 --> 546.52]  He's the guy behind this project, and he was thrilled to get such a rousing endorsement from the Changelog show that it's probably not crap.
[547.20 --> 555.12]  So now that we've got a heavyweight Rubyist on the show, I wanted to get your take on this particular project and the problem it aims to solve.
[555.18 --> 559.80]  And I'm sure that you've got a gist that does this for you automatically.
[559.80 --> 563.56]  Yeah, so configuration is a part of every project.
[563.80 --> 564.78]  It's just – it's guaranteed.
[565.38 --> 567.90]  And it's another one of those things that everybody does differently.
[568.14 --> 571.92]  So, I mean, I'm looking at it right now, and it looks pretty similar.
[572.14 --> 576.06]  I haven't looked at the code, but, like, the API is pretty similar to, like, what we use.
[576.14 --> 578.98]  I actually have – I think I might even post it on Rails Tips.
[579.06 --> 581.06]  If you search Config on Rails Tips, it might be up there.
[581.14 --> 588.20]  But we use this, yeah, like a YAML-type, you know, slurp thing that just literally pulls it in, and then boom, you have settings.
[588.20 --> 590.98]  So it's real similar to kind of what he's doing.
[591.26 --> 596.58]  But this – I mean, this is obviously something that everybody's struggling with because there are a lot of config frameworks out there.
[596.72 --> 600.42]  And this one seems like one of the more simple ones that I've seen, which is – that's good.
[600.84 --> 601.40]  So –
[601.40 --> 602.24]  Still love the name.
[602.84 --> 603.06]  Yeah.
[604.44 --> 607.48]  So would you say that it's probably crap or probably not crap?
[608.10 --> 611.60]  That's his – no, I said I don't know if it's crap.
[611.84 --> 615.56]  And then you said – you laughed at that remark.
[615.56 --> 616.52]  I'm just joking around.
[617.18 --> 618.18]  I'm just messing around.
[618.88 --> 619.16]  Gotcha.
[620.28 --> 623.34]  Gordon, an open source flash runtime written in pure JavaScript.
[623.58 --> 629.14]  This one went from just a few watchers to several hundred in one day on GitHub.
[629.14 --> 636.06]  And we were working with Chris Weinstrauth over at GitHub when I think he was working on the trends on GitHub at the time.
[636.20 --> 641.38]  And this was one of the projects that came up in that conversation because now we're up over 1,000 watchers just a week later.
[641.60 --> 642.94]  So what do you guys think?
[643.00 --> 645.22]  Open source flash runtime in pure JavaScript.
[645.92 --> 646.74]  I think it's awesome.
[647.36 --> 649.36]  I mean, like I thought it was a joke.
[649.70 --> 651.68]  I checked my calendar to see if it was April Fool's.
[653.00 --> 654.68]  I mean, it's really cool.
[655.50 --> 660.54]  It doesn't – I think if it could support like some of the net streaming stuff like video and things like that, I don't think it does now.
[660.60 --> 661.76]  I think that would be epic.
[662.06 --> 664.28]  But even just now, I mean, that's really cool.
[664.52 --> 665.68]  And this one got me excited.
[665.82 --> 668.30]  Twitter Node, node.js based tweet streaming.
[668.30 --> 673.08]  So we've got a streak here that we've got to keep going with mentioning node.js in our episodes.
[673.26 --> 677.74]  But this one from Technowini, which you mentioned in the interview portion of the show.
[678.16 --> 679.54]  And that's Rick Olson.
[679.68 --> 682.10]  If you don't know Technowini's handle on GitHub.
[682.10 --> 689.68]  This is a node.js server for streaming Twitter updates.
[689.68 --> 692.30]  Just straight up, node.js is the future.
[692.64 --> 695.54]  I mean, it is – JavaScript is such an awesome language.
[695.70 --> 697.44]  I'm going to go out on a limb and just claim it.
[697.64 --> 701.22]  Like I looked at it the other day and I had been ignoring it for quite a while.
[701.22 --> 704.80]  And I finally just was like, okay, what's this node.js stuff about?
[704.98 --> 706.52]  You know, kind of like the crazy Mongo database.
[707.30 --> 709.00]  And I was just blown away.
[709.20 --> 711.30]  I mean, in like two seconds, you know, I used Homebrew.
[711.54 --> 712.40]  It's on GitHub.
[712.60 --> 718.78]  And I did brew install node.js and like made a little tiny server and did a hello world.
[719.00 --> 722.70]  And I mean, I haven't had a geek out like that in a long time.
[722.78 --> 723.46]  It was really cool.
[724.38 --> 728.54]  Right about now is the time that we've been challenging with Resig's quote about JavaScript.
[728.94 --> 730.06]  I'm not going to do that this time.
[730.06 --> 731.32]  You'll have to listen to an older episode.
[733.80 --> 738.24]  But, you know, it forces you to – if you're going to embrace these server-side JavaScript frameworks,
[738.36 --> 742.42]  I think a lot of us – they're more involved code, I would imagine.
[742.54 --> 744.66]  I haven't done a lot of this firsthand on the server side.
[744.80 --> 749.16]  But I'll give you another JavaScript quote that I saw, and I'm not sure who to attribute this to.
[749.22 --> 750.60]  I need to go back and look and put it in the show notes.
[750.86 --> 751.68]  You can attribute it to me.
[752.10 --> 752.54]  There you go.
[752.62 --> 754.34]  I'll put it next to Jay Nunamaker.
[754.34 --> 765.46]  So they liken JavaScript as the incredibly hot girl at the party that always makes her loser boyfriend DOM.
[766.84 --> 767.36]  Right?
[767.74 --> 773.40]  And so, you know, if you're writing server-side JavaScript, you're finally cut loose of the DOM, the document object model.
[773.40 --> 780.72]  And so it forces you to – well, I guess you're free now to organize your JavaScript in a more sophisticated manner.
[781.06 --> 783.22]  And part of that is just simply writing better JavaScript.
[783.38 --> 789.36]  And we talked about it in an earlier episode of semicolons, good or bad, writing server-side JavaScript.
[789.36 --> 795.56]  And a big piece of that is, I guess, if you're going to have validating JavaScript is using JSLint.
[795.66 --> 796.42]  Have you used this project?
[797.10 --> 797.88]  No, I haven't.
[798.58 --> 801.56]  So JSLint basically is a validator for JavaScript.
[801.56 --> 802.16]  Oh, yeah, yeah.
[802.18 --> 802.94]  I have used JSLint.
[803.02 --> 803.20]  Sorry.
[803.36 --> 807.88]  If you've used the TextMate bundle to validate your JavaScript, choosing Lint behind the scenes.
[808.20 --> 809.64]  So jQuery Lint came out.
[810.04 --> 812.72]  That's the longest intro segue in history.
[812.72 --> 822.74]  jQuery Lint came out this week, and it plugs into Firebug and validates and makes suggestions for improving your jQuery.
[823.18 --> 825.14]  So I was really excited about this particular project.
[825.78 --> 827.40]  You see the screenshot up on the change log.
[827.48 --> 842.34]  You see that it inspects the selectors that you use for your jQuery code and then recommends different selectors, which – you know, that's a big deal when writing jQuery is just caching those selectors and being a lot more optimized in the selectors that you use.
[842.34 --> 843.32]  You write a lot of jQuery?
[844.56 --> 844.92]  Yes.
[846.16 --> 850.88]  Harmony is actually – has more JavaScript than Ruby.
[852.42 --> 855.90]  So, yeah, we have a ton of jQuery in there.
[856.00 --> 858.66]  So, yeah, I need to – I saw this the other day, but I haven't tried it yet.
[859.22 --> 861.22]  But I'm pretty curious about it.
[861.52 --> 862.34]  It looks interesting.
[862.84 --> 869.92]  So on top of that, does it also not require you to do, like, console log and stash the variable until you can see it in the console?
[870.00 --> 870.88]  Does it do that for you in?
[871.54 --> 872.68]  You know, I haven't used it firsthand.
[872.76 --> 873.88]  I need to kick the tires.
[874.02 --> 880.30]  But from the intro, I don't believe that you had to do anything special to manually inspect those variables.
[880.96 --> 883.66]  Yeah, I know lint itself is really cool, the JSLint.
[884.08 --> 886.64]  I've done – you know, I had the TextMate bundle for a while.
[886.86 --> 888.68]  I ended up turning it off because it was a little bit slow.
[890.16 --> 897.50]  But, yeah, it's pretty cool how you can, like, just – you know, I found a lot of places where, like, I just, you know, missed a semicolon or forgot a var.
[897.50 --> 899.14]  You know, it just happens randomly.
[899.14 --> 905.72]  And so, I mean, I can imagine that doing the same kind of thing, like, on top of that for jQuery, that's pretty sweet.
[905.80 --> 906.80]  I'd definitely be checking that out.
[907.00 --> 913.60]  As a side note, we should probably make a note to get a hold of someone like Remy Sharp who does jQuery for designers.
[914.10 --> 915.24]  He'd probably be good to have on the show.
[915.24 --> 916.06]  Yeah, absolutely.
[916.44 --> 916.58]  Yeah.
[917.20 --> 924.02]  Show off the best darn presentation software a developer could ever love from our friend Scott Chacon over at The Hub.
[924.64 --> 925.88]  I have played with this one.
[926.10 --> 926.60]  It's pretty cool.
[926.68 --> 929.64]  I have a presentation coming up next week on SaaS, of all things.
[929.78 --> 932.66]  So I thought about giving this a try.
[932.88 --> 935.10]  I guess, ultimately, I'm still addicted to Keynote.
[935.20 --> 938.28]  I think that's one of the apps this one has in its sights.
[938.28 --> 947.62]  But it's essentially a – looks like a built-in Sinatra web app that allows you to build your presentations in HTML, JavaScript, and CSS.
[950.14 --> 952.60]  Yeah, I became a big fan of Keynote.
[953.14 --> 959.08]  I teach a JavaScript class at Notre Dame in the fall, and so I had to learn how to show code in presentations and things like that.
[959.82 --> 961.52]  And so I started using Keynote.
[961.62 --> 964.10]  And at first, it's a little bit awkward, but it definitely gets the job done.
[964.10 --> 977.80]  So I can't see myself switching, but it was interesting, and I think there's definitely an opportunity because it doesn't sound like anybody's ever real happy with code presentations and stuff like that and what it takes to get it going.
[979.38 --> 980.96]  So I think it looks pretty cool.
[981.10 --> 983.44]  So you tried it out, and what do you think?
[983.94 --> 984.56]  I did.
[984.90 --> 985.82]  I mean, it's still early.
[985.98 --> 986.82]  It's a brand-new project.
[987.02 --> 993.14]  I'm not sure that it's ready for me personally, but I could see where – I definitely see the problem it's trying to solve.
[993.14 --> 996.96]  And as you mentioned, showing code in your presentations is one of the most difficult things you can do.
[997.12 --> 1006.12]  For all of the benefits of something like Keynote, showing code in a way that fits the limited resolution that you normally have on a projector is difficult.
[1006.40 --> 1015.82]  And then there are certain times if you have to wrap text, a lot of times that may or may not be valid in the particular language that you're trying to display.
[1015.82 --> 1020.12]  So do you have any tips for the listeners?
[1020.36 --> 1024.68]  Say that you do this in Keynote as far as displaying your code in Keynote?
[1025.14 --> 1031.38]  Yeah, I've got a draft blog post I've just been waiting to put together because there's a few things you can do, and it makes it a lot easier.
[1031.66 --> 1037.68]  I think it's Dr. Nick has a copy as RTF, rich text format bundle, and that is, like, priceless.
[1037.68 --> 1044.76]  If you install that for TextMate, you can literally code your stuff up and just copy and paste your syntax highlighting right into Keynote.
[1045.46 --> 1051.26]  So a lot of times I go with white background because you don't have to worry about contrast on the screen and stuff like that.
[1051.60 --> 1059.86]  And then I just use one of the white themes in TextMate, and I can do copy as RTF and paste it right in, bump up the font size a little bit, and the code just looks great.
[1059.86 --> 1066.94]  And I know I found – and I'm sure the same is true with other developers, but the students really reacted to the syntax highlighting.
[1068.00 --> 1071.18]  Like, being able to see that really helped them understand what was going on.
[1071.66 --> 1074.96]  So I think the copy as RTF was one of the biggest things that I figured out.
[1075.12 --> 1082.50]  And then, you know, going with a simple background color so that you don't have to worry about, like, things looking washed out or stuff like that has helped me the most.
[1082.76 --> 1085.96]  So what are you teaching America's youth at the university?
[1085.96 --> 1090.86]  Basically, it's just an intro to JavaScript.
[1091.14 --> 1093.70]  It's literally, like, English majors and history.
[1093.80 --> 1098.62]  I mean, they don't have any programming experience at all, so I have to teach them just enough HTML to get it going.
[1098.80 --> 1104.02]  And then it's, you know, basics of JavaScript, learning how to program variables, you know, functions, stuff like that.
[1104.06 --> 1105.68]  And then the second half of the class is all jQuery.
[1105.92 --> 1113.06]  So it's literally just, like, pedal to the metal, get something going, and it's pretty fun.
[1113.06 --> 1119.72]  It's a lot of fun to see people get excited for the first time again, like, you know, when they make something draggable.
[1119.90 --> 1122.42]  And they're just, their eyes light up, like, whoa, I can show my friends this.
[1123.30 --> 1123.32]  So.
[1123.76 --> 1126.64]  And you find yourself, when you teach a subject, you really have to know the subject.
[1127.34 --> 1127.66]  Yeah.
[1128.14 --> 1128.44]  Yep.
[1128.44 --> 1130.48]  Because they ask questions that I have never even thought.
[1131.28 --> 1132.44]  So, yeah, it is.
[1132.52 --> 1132.98]  That's very true.
[1133.40 --> 1134.16]  That's kind of tough.
[1134.60 --> 1135.24]  That's kind of tough.
[1135.24 --> 1145.84]  Before we go away from show off real quick, I think some things we're not really thinking about there with what it does is in its future plans, it actually intends to be, like, this dynamic presentation server.
[1145.96 --> 1151.40]  And what's cool about that is that it has plans for actually having the audience interact with the presentation.
[1151.80 --> 1152.16]  So, wow.
[1152.16 --> 1162.52]  The fact that it's, like, this presentation server, it runs on a URL, and you can kind of get dynamic with it, like, show tweets in it, and very, very dynamic where you actually include the audience.
[1162.72 --> 1166.60]  And I think that's what every person who gives a presentation tries to be very interactive.
[1167.14 --> 1167.30]  Yeah.
[1167.30 --> 1171.76]  And if we're going to go down that road, why not try to build it into the software that does the presentation?
[1172.26 --> 1175.54]  And not only that, but it's, you know, let's face it, it's code, right?
[1175.54 --> 1180.24]  So you can throw it into a Git repository, share it with the world like we do with our open source software.
[1181.00 --> 1182.80]  And, you know, that's a big, big win there, too.
[1182.82 --> 1184.62]  You can't really share a keynote like that.
[1184.70 --> 1185.70]  I mean, I guess you can, right?
[1185.78 --> 1187.16]  But can you version a keynote?
[1188.50 --> 1189.14]  I don't know.
[1189.44 --> 1190.08]  I mean, I think it's just…
[1190.08 --> 1190.86]  Only at the binary level, I guess.
[1191.08 --> 1191.22]  Yeah.
[1191.22 --> 1192.20]  And that's always awkward.
[1192.32 --> 1193.46]  But, yeah, it's a good point.
[1193.56 --> 1195.50]  You know, you could fork a presentation.
[1196.12 --> 1196.38]  Yeah.
[1197.30 --> 1199.04]  Fork my presentation, baby.
[1201.54 --> 1202.74]  Next up, Kongo Mongo.
[1202.94 --> 1204.34]  Use MongoDB from Clojure.
[1204.54 --> 1208.90]  So I think we've probably beat the MongoDB horse on past episodes and this one.
[1208.96 --> 1213.54]  But what makes this one interesting to me is the fact that you're calling it from Clojure.
[1214.16 --> 1218.30]  And it seems to be a rise in these functional programming languages.
[1218.42 --> 1220.32]  Have you dabbled in these at all, John?
[1221.12 --> 1222.16]  No, I haven't.
[1222.76 --> 1223.70]  They seem cool.
[1223.70 --> 1227.10]  I'm, you know, not like a computer scientist or anything.
[1227.28 --> 1230.28]  So I haven't really gotten into that part of functional programming.
[1230.66 --> 1232.08]  But, yeah, I mean, it seems interesting.
[1232.52 --> 1238.28]  I have Clojure and some of them are on my radar for maybe kind of tinkering with in the next year or so.
[1239.50 --> 1246.64]  At our last Ruby meetup here in Dallas, some of the guys are starting a functional programming languages user group here in the Dallas area.
[1246.64 --> 1248.16]  And they're calling it Lambda, Lambda, Lambda.
[1250.38 --> 1251.08]  That's awesome.
[1251.48 --> 1252.56]  I thought that was a perfect name.
[1252.56 --> 1254.34]  All righty.
[1254.44 --> 1256.84]  We should have saved this one for the last talk.
[1257.14 --> 1259.30]  Adam, you may have to do some splicing in post-production.
[1259.42 --> 1260.80]  JavaScript as a teaching tool.
[1260.90 --> 1261.50]  Here you go, John.
[1262.14 --> 1266.26]  Learn classic computer science approaches using a language you probably already know.
[1266.94 --> 1267.74]  So have you seen this repo?
[1268.42 --> 1268.82]  Yeah.
[1268.98 --> 1269.84]  I looked through it a little.
[1269.94 --> 1276.46]  I bookmarked it to look at it later because I want to go through it mostly because I have no computer science background at all.
[1276.46 --> 1280.28]  So I've always found algorithms and stuff like that interesting.
[1280.72 --> 1282.44]  And JavaScript is such an awesome language.
[1283.44 --> 1287.56]  But, no, I haven't – I mean, I would say definitely JavaScript is a great language for teaching programming.
[1287.56 --> 1292.88]  But I – you know, this computer science stuff is really interesting too.
[1293.88 --> 1294.50]  Just curious.
[1294.56 --> 1297.02]  When you said you bookmarked, did you mean you watched?
[1297.02 --> 1298.02]  No.
[1299.34 --> 1304.02]  So I typically don't use watch because then I get every commit and it kind of overloads it.
[1304.18 --> 1307.68]  So I think I might have talked about it in the other episode.
[1308.06 --> 1311.76]  But I have a tiny little Heroku MongoHQ app that I use.
[1311.94 --> 1320.10]  And it's just like a bookmarklet, like Instapaper type thing but not as fancy as Instapaper where you can just mark something to look at it later.
[1320.10 --> 1322.16]  And so I do everything in batches.
[1322.74 --> 1326.74]  So I, you know, get all my feeds, find all the interesting things, bookmark them to read later.
[1326.84 --> 1328.70]  And then when I have time, I usually go back and look at them.
[1328.78 --> 1330.34]  So this is on the radar to do that.
[1330.94 --> 1333.50]  So I'm looking at the network graph for this particular project.
[1333.76 --> 1338.36]  And it's interesting to see folks forking it and adding their own examples.
[1339.56 --> 1343.22]  So PHP MoAdmin, MongoDB admin tool for PHP.
[1343.22 --> 1352.26]  And I know they're riffing off PHP MyAdmin, which we all know, love, and probably hate from former lives of dealing with MySQL.
[1352.68 --> 1355.48]  But I love the Mo in this.
[1355.74 --> 1357.70]  It's MoAdmin and PHP MyAdmin.
[1358.34 --> 1362.84]  But, you know, we've seen a lot of these crop up, these GUI tools for Mongo.
[1362.94 --> 1370.02]  When we had Mike Deroff for MongoDB from TenGen on the show, we talked about, you know, where is the GUI for MongoDB?
[1370.62 --> 1371.56]  What's your thoughts on that?
[1371.58 --> 1372.08]  Do we need one?
[1372.08 --> 1374.32]  Yeah, I think it would be really cool.
[1374.60 --> 1377.54]  I know, I mean, SQL, I think is what it's called.
[1377.62 --> 1380.24]  That's one that I used for MySQL and still do occasionally.
[1381.16 --> 1384.52]  I just saw, I don't know if you've seen this or not, but there's a new one out.
[1384.70 --> 1390.44]  I think it's a Mac app called MongoHub 2, which I haven't really checked out yet.
[1390.52 --> 1392.54]  But that is kind of interesting to me too.
[1392.98 --> 1397.22]  But, yeah, I know, like when I was in PHP, PHP MyAdmin was, that was awesome.
[1397.28 --> 1398.56]  I learned on PHP MyAdmin.
[1398.56 --> 1401.70]  So I definitely have some roots with that.
[1401.80 --> 1404.62]  So it's interesting to see other stuff crop up like this for Mongo.
[1404.62 --> 1406.70]  I think it's only a matter of time.
[1406.80 --> 1407.82]  But, you know, you mentioned SQL.
[1407.90 --> 1410.02]  I use that primarily for MySQL as well.
[1410.12 --> 1411.02]  I love that app.
[1411.36 --> 1415.52]  I'm glad to see that it's continued to develop as it has.
[1416.28 --> 1422.42]  You know, with the comparison that I would draw is probably with Futon, if you've ever played it with Couch TV.
[1422.42 --> 1425.68]  I think they have a nice web interface that's built in.
[1425.82 --> 1426.58]  It's really functional.
[1426.74 --> 1428.74]  I think Mongo could benefit from something similar.
[1430.00 --> 1430.44]  Yeah, definitely.
[1430.70 --> 1433.20]  I think that, you know, you always want to be able to see your data.
[1433.30 --> 1437.00]  I've had a few people, you know, on the MongoMapper mailing list that are like, how do I see my data?
[1437.78 --> 1439.26]  I'm like, well, you can use a shell.
[1439.40 --> 1441.18]  But I think some people are just used to GUI tools.
[1441.40 --> 1446.74]  So, you know, they're not quite ready for that level of hacker to open up the green term screen.
[1446.74 --> 1452.64]  Well, it's always nice, too, to get a GUI on something that can be, you know, a little difficult from a different level.
[1452.86 --> 1457.60]  But as soon as you start to pull out GUI tools, you start to get to a more mainstream audience as well.
[1458.52 --> 1459.20]  Great point.
[1460.30 --> 1462.36]  Fusebox, a safer way to monkey patch JavaScript.
[1463.50 --> 1473.46]  So I was checking out this repo, and I thought it was interesting in the way that it aims to provide a sandbox for monkey patching certain built-in objects in JavaScript.
[1473.46 --> 1477.16]  And I think people differ on monkey patching in general.
[1477.32 --> 1482.94]  I know in Ruby there seems to be debates on whether open classes and monkey patching is a good thing or not.
[1483.50 --> 1491.84]  With JavaScript, usually, though, it's a little harder to debug because you don't have those debug tools that you've got with other languages.
[1492.32 --> 1503.06]  And so when somebody's opening up prototypes and adding methods and then, you know, what you expected that you're adding to a string prototype is not necessarily there because someone else has stepped on it.
[1504.14 --> 1505.62]  It can be confusing sometimes.
[1505.80 --> 1510.08]  So have you checked out Fusebox yet and the approach that it takes with this namespacing?
[1510.70 --> 1511.96]  No, this is really interesting.
[1513.40 --> 1519.36]  I've always kind of shudder at namespaces, but I can understand definitely with JavaScript when this would be handy.
[1519.54 --> 1522.50]  But, yeah, this is pretty cool that you can do that so easily.
[1522.66 --> 1524.72]  I hadn't seen it yet behind on my feeds.
[1524.72 --> 1531.36]  But, I mean, I know personally I've – usually I don't override anything in JavaScript.
[1531.58 --> 1535.64]  I usually just kind of add to it, you know, things like first and last on Array or stuff like that.
[1535.64 --> 1543.78]  But, yeah, projects like this and Underscore are definitely – I mean, that's – as people write more JavaScript, it's necessary.
[1544.38 --> 1545.62]  You mentioned Underscore.
[1545.72 --> 1547.72]  So have you used that very much?
[1547.72 --> 1549.96]  Just a little bit.
[1550.50 --> 1553.62]  Like the next project I start, I'll definitely be using it to try it.
[1554.14 --> 1559.32]  You know, most of the projects that I have, I started – that I'm working on now, I started before Underscore.
[1559.48 --> 1564.38]  So I have other, you know, like for each patches and things like that that I end up using.
[1564.38 --> 1567.00]  But I think Underscore is definitely what I would use next.
[1567.42 --> 1579.92]  Before we pull away from that too, we should probably mention in the comments the owner of that repo, that project, John Dalton, actually chimed in and said he recently added support for the sandboxed Boolean native constructor as well.
[1580.86 --> 1584.94]  Yeah, and this is supposed to be part of Fuse.js, which I'm still confused about what it's going to be.
[1584.98 --> 1585.60]  I wanted to plug it.
[1585.60 --> 1590.18]  But Mr. Dalton's splash page just says it's going to launch sometime in January.
[1590.18 --> 1595.36]  So we've just got about three days left to let us know what Fuse.js is going to be.
[1595.82 --> 1596.94]  We've got our eyes on you, John.
[1597.14 --> 1597.80]  You can't hide.
[1598.50 --> 1599.46]  But you mentioned Underscore.
[1599.58 --> 1607.12]  For the guys that don't know, Underscore.js was on episode five, I believe, from Document Cloud, which those guys are turning out some great code over there.
[1607.34 --> 1610.42]  We talked to Jeremy about Underscore.
[1610.54 --> 1616.88]  And I think I've added it to every project that I've started since that came on my radar.
[1617.18 --> 1618.28]  It's a nice little library.
[1618.28 --> 1621.10]  Next up, App Sales Graph.
[1621.20 --> 1623.44]  Graph your App Store sales data.
[1624.04 --> 1629.48]  I don't think any of us have any apps in the App Store, but it is cool to see people.
[1629.56 --> 1630.64]  I guess they're scraping this data.
[1630.72 --> 1632.84]  I'm trying to figure out where they're getting this data.
[1633.02 --> 1635.30]  A couple of these have popped up in the last week.
[1635.30 --> 1639.24]  But I thought it was interesting to – the App Store has just gotten so big.
[1639.42 --> 1645.46]  And the reason I wanted to highlight this one today, we probably have a hard stop here at the top of the hour with John waiting on the Apple keynote.
[1645.46 --> 1650.56]  Just how big the App Store has gotten.
[1651.00 --> 1654.62]  Do you guys foresee any sort of iPhone integration with Harmony?
[1655.32 --> 1656.44]  Yeah, totally.
[1656.78 --> 1660.30]  I mean, we plan on having like a full API eventually.
[1660.42 --> 1661.68]  We'll probably start with just a little bit.
[1661.68 --> 1670.90]  But we've already had a few people talk to us about making a Mac application for like editing your themes and uploading files and changing content.
[1671.32 --> 1673.56]  And the same thing with an iPhone, man.
[1673.62 --> 1678.10]  I would love the idea to be able to look through comments right from my iPhone and stuff like that.
[1678.10 --> 1680.12]  So I would definitely say someday we will.
[1680.40 --> 1683.54]  And I mean, man, everybody who makes an iPhone app is rich.
[1683.72 --> 1685.38]  So why not jump on board, right?
[1686.00 --> 1686.40]  Absolutely.
[1687.22 --> 1691.54]  Do you guys think there's an untapped market out there for I guess maybe software as a service?
[1691.72 --> 1694.60]  In this case, we have this app sales graph.
[1694.80 --> 1702.14]  But anything hosted where you can actually pull this data in and sell a subscription to a developer to help them better manage their sales and their processes?
[1702.14 --> 1707.56]  Or is it just part of the iPhone application on the store in general?
[1708.10 --> 1710.70]  I think it would be interesting.
[1710.88 --> 1717.00]  The problem that you might run into is just with Apple choosing to cut it off at any time.
[1717.18 --> 1717.42]  Right.
[1717.64 --> 1720.18]  That does suck in that regard because they do have so much power.
[1721.32 --> 1721.80]  Yeah.
[1721.96 --> 1723.08]  Just drop it like a bad habit.
[1725.92 --> 1727.56]  Things-RB.
[1727.70 --> 1729.02]  I know this is Adam's report.
[1729.10 --> 1729.92]  He's quite excited about this.
[1729.92 --> 1732.58]  He even posted the screenshot of his Hootsuite conversation.
[1733.68 --> 1734.64]  Well, that's not my conversation.
[1734.64 --> 1737.10]  That's just a couple of good friends of mine.
[1737.18 --> 1740.68]  Andy Shen and Josh Price was just chatting on Twitter.
[1740.88 --> 1745.22]  And I follow them both and just kind of caught at a glance their conversation about things.
[1745.28 --> 1747.46]  And I've been a things user for probably about a year and a half now.
[1747.60 --> 1750.10]  And I use it on the desktop as well as the iPhone.
[1750.46 --> 1751.94]  And I've been a lover of it.
[1751.94 --> 1754.08]  I store lots of notes, things to do, projects.
[1754.32 --> 1756.62]  I mean, I use it pretty in-depth.
[1757.10 --> 1763.52]  And I thought it was a really cool take when I found the repo, the project on GitHub.
[1763.64 --> 1765.24]  And I just stumbled on it maybe a few weeks ago.
[1765.78 --> 1770.34]  And when I stumbled on this conversation, I'm thinking, well, I should really post that repo because these guys would appreciate it.
[1770.34 --> 1774.04]  And the next thing you know, when we posted it, it had 30 watches.
[1774.30 --> 1776.82]  And before the end of the day, it was like up to 75.
[1777.14 --> 1782.38]  So it just shows you that there's people out there who really want to cling to this information that's in GitHub.
[1782.58 --> 1784.16]  And it just needs to find a way to get out.
[1785.10 --> 1786.42]  Yeah, it's almost up to 100 watchers now.
[1786.52 --> 1790.52]  I got some buzz when we posted it that day.
[1790.60 --> 1795.70]  It's nice to, as you say, shine a light on some of the lesser-known projects even if they're extremely niche.
[1795.72 --> 1797.12]  I think that's kind of the whole point of the show.
[1797.12 --> 1806.36]  So even the developers that own the projects, they're more than ecstatic about it too because they're not really looking to get famous by any chance.
[1806.40 --> 1807.42]  But they want people to use their code.
[1807.64 --> 1813.26]  Doesn't everybody want people to use their code and find some usefulness in what they provide back to open source?
[1813.36 --> 1815.64]  I think it's just kind of wild to give that back.
[1815.72 --> 1819.84]  But the cool thing here to take away is that if you're geeks like us, you're probably using Terminal anyways.
[1820.30 --> 1823.10]  And you probably are on the command line most often.
[1823.10 --> 1829.72]  So why not be able to just pop up in a new tab and type in a quick command and get today's to-do list from things?
[1829.84 --> 1834.64]  So you can still go back to your things UI either on your iPhone or whatever.
[1835.28 --> 1838.08]  But you don't have to keep things running at all times either.
[1838.22 --> 1842.00]  So you can just have things closed but still access that data via the CLI.
[1842.54 --> 1843.88]  And it's kind of wild.
[1843.96 --> 1848.64]  And they also piggyback off of a tool called Geek Tool to keep to-dos on your desktop, which I haven't checked out yet.
[1848.64 --> 1849.66]  But I've heard that's kind of cool.
[1850.36 --> 1850.92]  Yeah, that is cool.
[1851.02 --> 1855.30]  I actually did that before when I was using Todoist or something, a web service.
[1855.54 --> 1860.78]  I added a little bit of Ruby stuff and showed to-dos on the desktop with Geek Tool.
[1860.86 --> 1861.50]  Geek Tool is pretty cool.
[1861.64 --> 1862.12]  I mean, it's fun.
[1862.22 --> 1865.08]  You can't customize everything, but you can make it look pretty decent.
[1865.50 --> 1867.44]  I think projects like this too, they're really fun.
[1868.34 --> 1873.02]  What people don't realize is desktop software, it all uses either SQLite or XML or something.
[1873.02 --> 1878.28]  So if you have a desktop app out there and you want to get into it, you can get into it.
[1878.34 --> 1882.32]  You just have to go to the application and figure out where it's storing the data.
[1882.58 --> 1885.08]  And you can hack around and make stuff work.
[1885.44 --> 1887.72]  So I think it's awesome when people do stuff like this.
[1887.74 --> 1888.40]  And it's a lot of fun.
[1888.46 --> 1889.44]  I know I've done it a few times.
[1889.86 --> 1890.88]  Yeah, that's the beauty of GitHub.
[1891.06 --> 1898.08]  Not every project is going to be this massive community effort that solves a particular problem that every web app needs.
[1898.08 --> 1902.54]  Some of it's just going to be tiny little niche hobbyist-type projects just like this one.
[1903.50 --> 1916.26]  The takeaway too on this, I guess on John's note, the fact that you can access that XML or MySQL or SQLite database is that if you have an application you want to get access to, go take a look at this project, see how it's working.
[1917.02 --> 1921.34]  And reverse engineer it and make it work for your case.
[1921.48 --> 1923.68]  And you just got to learn a little bit of Ruby and you're good to go.
[1924.68 --> 1927.98]  One other takeaway from that too, Wayne, is that…
[1927.98 --> 1929.66]  That's five takeaways if you're scoring it.
[1929.66 --> 1931.46]  Hey, I'm taking lots of takeaways here.
[1931.48 --> 1932.54]  There's nothing left to take.
[1932.54 --> 1933.54]  I'm on the podium.
[1933.82 --> 1934.42]  Give it to me.
[1935.44 --> 1936.06]  I'm just kidding.
[1936.86 --> 1938.74]  Somebody – actually, Andy.
[1939.42 --> 1940.74]  Let's rewind here for a second.
[1940.90 --> 1946.60]  So when we released Tail, defunct Chris Wanstrow actually got pretty excited about it obviously as we know.
[1947.14 --> 1949.98]  And then he's like, now I just want to see Tail in my terminal.
[1950.68 --> 1955.56]  And then Andy piped back up and said maybe we should use Geek Tools to show Tail in our terminal.
[1955.56 --> 1958.66]  So yeah, no, I think that's – I totally think that's great.
[1958.96 --> 1961.74]  Geek Tool, that shows on the desktop too.
[1961.82 --> 1964.46]  You can actually make it your desktop background I think.
[1965.58 --> 1966.38]  That's how I've used it.
[1966.60 --> 1968.36]  I don't know if I've ever used it in terminal.
[1968.36 --> 1975.12]  But like you can actually make it overlay with opacity on your desktop to show stuff.
[1975.90 --> 1981.22]  So yeah, I bet you could totally do like a live – I did like a minute refresh on the little dumb thing I made.
[1981.22 --> 1985.96]  Yeah, I saw that tweet and I was kicking around the how of actually how to pull that off.
[1986.02 --> 1991.26]  I'm going to have to pick your brain, John, because I think that would be cool to actually tail the changelog without having to go through the web interface.
[1991.60 --> 1993.40]  We should talk about that sometime.
[1993.92 --> 1994.14]  Totally.
[1994.34 --> 1994.92]  That sounds fun.
[1995.76 --> 1998.52]  Jspec, robust BDD for both client and server JavaScript.
[1998.68 --> 2002.22]  So we talked about server-side JavaScript earlier and then client-side JavaScript with jQuery.
[2002.46 --> 2007.98]  So here's a BDD, behavior-driven development library for JavaScript.
[2007.98 --> 2011.24]  Do you find yourself testing JavaScript in this way?
[2011.82 --> 2015.00]  You know, JavaScript testing, let's be honest, it kind of sucks right now.
[2015.50 --> 2015.78]  Absolutely.
[2015.78 --> 2021.16]  So I mean the things that we need for testing or that I've found I need is more integration-related.
[2021.94 --> 2027.38]  Most of the stuff that I use that is more library-based already has tests.
[2027.54 --> 2032.94]  I haven't really written a lot of libraries for JavaScript that I want to test and stuff.
[2032.94 --> 2041.18]  So I mean I think this is awesome and I definitely think for Node.js, stuff like that, server-side testing, this is great.
[2042.82 --> 2053.12]  But I think I'd really like to see some even more improvement in the integration area for testing JavaScript-type stuff, like with HTML and those kinds of things.
[2054.58 --> 2057.52]  But yeah, this is a cool project, especially if you like RSpec.
[2057.52 --> 2060.50]  Yeah, I like the vocabulary here.
[2060.62 --> 2062.82]  It's really familiar if you come from that background.
[2064.40 --> 2067.40]  Foursquare X, talking about another hobbyist project.
[2068.22 --> 2074.72]  This one's an OS X client for Foursquare, which seems to be locations all the rage on Twitter these days.
[2074.92 --> 2075.94]  Either you guys use Foursquare?
[2076.52 --> 2077.10]  No, I don't.
[2077.18 --> 2079.08]  I actually use Gowalla, I think.
[2079.12 --> 2080.44]  Yeah, I'm a Gowalla fan myself.
[2081.12 --> 2083.22]  I'm paying the Gowalla guys this morning for an API.
[2083.36 --> 2086.90]  I'm dying for that API to write a wrapper.
[2086.90 --> 2088.06]  We were calling you out, Gowalla.
[2088.52 --> 2089.04]  I did.
[2090.32 --> 2093.26]  But Foursquare's got their API out there and they've got a little traction.
[2093.82 --> 2100.08]  This is a really nice-looking app for doing that on the desktop without having to use the iPhone or the web interface.
[2100.48 --> 2103.44]  And it's cool that they made it open source that anybody can forget and add features.
[2103.92 --> 2104.64]  It's really nice.
[2104.64 --> 2107.00]  A special note is that you actually have to have Snow Leopard, not just Leopard.
[2107.66 --> 2113.78]  Yeah, I saw some grumbling on Twitter, on the Twitter about that.
[2113.78 --> 2116.74]  But, you know, how long has Snow Leopard been out?
[2116.84 --> 2117.64]  It's like, upgrade already.
[2118.60 --> 2119.28]  Well, that's me.
[2119.44 --> 2123.94]  I've been delaying because of what that does to me.
[2124.16 --> 2132.32]  That puts me out of, I guess, out of practice for a bit because I've got to reinstall new gems and set up the system again.
[2132.38 --> 2134.88]  It's just a big, massive undertaking that I'm not feeling doing right now.
[2135.34 --> 2140.90]  Actually, you know, I kind of like that process because, like, spring cleaning, cleaning house.
[2141.08 --> 2143.72]  Back when I was on the Windows platform, I think I did it at least once a month.
[2143.98 --> 2145.04]  Well, yeah, I wouldn't do it.
[2145.10 --> 2146.20]  It's just a big butt.
[2146.66 --> 2147.52]  I had to, right.
[2147.90 --> 2150.34]  There's just so much going on right now that right now is bad timing.
[2150.34 --> 2151.88]  And I don't think it's going to get any better.
[2152.08 --> 2155.54]  But it's kind of resisting because, I don't know.
[2156.56 --> 2158.50]  They're announcing Summer Leopard in about a half an hour.
[2158.60 --> 2159.68]  So you might as well just wait for that.
[2159.68 --> 2168.20]  Speaking of installing things, one that we have not highlighted on the show that we will feature because now we're mentioning it on the show that has got a lot of traction.
[2168.46 --> 2170.98]  And I've seen you talk about it a couple of times, John, is Homebrew.
[2172.38 --> 2172.74]  Yes.
[2173.10 --> 2174.06]  Homebrew is awesome.
[2174.46 --> 2175.48]  It's really good.
[2176.18 --> 2187.18]  So what makes it so cool is if you're someone like me that does not want to compile and MD5 check some things and stuff like that, I just want to install something.
[2187.54 --> 2188.92]  I like Max Drag and Drop.
[2188.92 --> 2195.68]  So being able to just say brew install and then some name, it's perfect.
[2196.08 --> 2197.90]  So it's definitely great.
[2198.20 --> 2199.52]  It's got to be easier than Mac ports, right?
[2200.36 --> 2201.00]  Oh, man.
[2201.10 --> 2201.22]  Yeah.
[2201.96 --> 2203.28]  Mac ports, I always run into.
[2203.34 --> 2207.64]  I still have Mac ports installed because of one thing that kind of relies on it.
[2207.92 --> 2210.98]  But, yeah, it's definitely easier than that.
[2211.04 --> 2212.84]  And it doesn't mess up with your system at all.
[2212.96 --> 2217.54]  It's all – you can put it in wherever you want, and it will only affect that place, which is really cool.
[2218.02 --> 2218.48]  All righty.
[2218.48 --> 2220.34]  Well, thanks for sticking around and running down the news with us, John.
[2220.94 --> 2221.56]  My pleasure.
[2221.66 --> 2222.28]  This was a blast.
[2222.76 --> 2223.64]  It was a blast.
[2226.12 --> 2226.86]  No, seriously.
[2226.96 --> 2228.48]  Thanks for joining us on the show.
[2228.60 --> 2232.98]  It's always a pleasure to have someone else's take on what's happening in open source.
[2233.08 --> 2239.68]  I think it's awesome and really appreciate you taking the time to sit down with us for, I don't know what, an hour and a half now between the interview and the news.
[2239.68 --> 2244.12]  I appreciate you taking the time out of your day and enjoy Apple's announcements today.
[2244.78 --> 2245.12]  I will.
[2245.44 --> 2245.92]  Thanks a lot.
[2245.92 --> 2254.74]  Thank you for listening to this edition of the Change Log.
[2255.82 --> 2262.52]  Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[2262.52 --> 2272.24]  Also, be sure to head to github.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of the Change Log.
[2272.24 --> 2302.22]  We'll be right back.
[2302.24 --> 2305.24]  I'm out of bed
[2305.24 --> 2308.22]  For us to try
[2308.22 --> 2309.78]  Bring it down
