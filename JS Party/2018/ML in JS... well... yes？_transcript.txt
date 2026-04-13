[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.84]  on Linode servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.84 --> 23.92]  Rollbar. Move fast and fix things. Resolve errors in minutes and deploy with confidence. Head to
[23.92 --> 29.16]  Rollbar.com slash Changelog. Request a demo. Get started today. It's loved by developers,
[29.16 --> 35.78]  trusted by enterprises, and most of all, we use it here at Changelog. Move fast and fix things with
[35.78 --> 57.76]  Rollbar. Once again, Rollbar.com slash Changelog. Welcome to JS Party, a weekly celebration of
[57.76 --> 64.64]  JavaScript and the web. Tune in live on Thursdays at 1 p.m. U.S. Eastern at Changelog.com slash live.
[64.64 --> 68.92]  Join the community and Slack with us in real time during the shows at the Changelog.com
[68.92 --> 73.52]  slash community. Follow us on Twitter. We're at JS Party FM. And now on to the show.
[76.38 --> 82.92]  G'day. You're listening to another episode of JS Party. This is episode number 28. This is a weekly
[82.92 --> 88.18]  celebration of everything JavaScript. I'm Suze Hinton. I'm your host for this episode, and I'm
[88.18 --> 93.72]  joined as usual by some fantastic panelists as always. So first we have Cable on the panel.
[94.00 --> 95.00]  Hey, Cable. How's it going?
[95.34 --> 97.46]  Hey, doing good. Ready to roll.
[97.86 --> 101.28]  Awesome. Second of all, we have Chris. Welcome back, Chris.
[101.54 --> 101.92]  G'day.
[102.24 --> 106.16]  And last but not least, we also have Jared. Jared, it's great to have you.
[106.36 --> 109.08]  It's great to be here. I'm not a machine, but I'm here to learn.
[109.08 --> 112.74]  I was expecting something like this from you.
[114.66 --> 119.98]  So Jared has given a little bit of a spoiler of what we're going to be talking about this
[119.98 --> 126.06]  week. We're going to be covering machine learning. And that sounds a little bit weird given that
[126.06 --> 131.56]  we're talking about JavaScript on JS Party. But lately, there's been some really, really
[131.56 --> 138.10]  cool activities happening around the combination of data science, machine learning, and JavaScript.
[138.10 --> 144.94]  And so we're going to start out by just summarizing a conference that I actually was lucky enough
[144.94 --> 151.34]  to attend this week. It's called ML for All, which stands for Machine Learning for All. And
[151.34 --> 159.32]  if you go to ML for, which is the numeral for all, A-double-L dot org, you can actually go
[159.32 --> 164.34]  check out the videos, the schedule, and also just what the whole conference was about. But
[164.34 --> 170.24]  normally, when you think of machine learning conferences, you think of something like a very
[170.24 --> 178.14]  academic, very dry, and very kind of full of math and scary terms that you don't know. You know,
[178.30 --> 183.66]  you imagine a room where everyone sits and experiences that kind of thing. But this conference,
[183.66 --> 188.90]  which was organized by a really great community of people, including some of my colleagues,
[188.90 --> 198.82]  was designed to make it more accessible for people to be able to access machine learning in a context
[198.82 --> 203.42]  where they're just learning from the very beginning. So I thought that was really, really cool. I learned
[203.42 --> 210.80]  a ton. I was lucky enough to give a presentation at the conference too, even though I'm not an expert
[210.80 --> 216.24]  in machine learning. So I think that says a lot about the conference's approachability. So
[216.24 --> 221.60]  that's a quick summary. But the reason why I wanted to talk about this a little bit,
[221.78 --> 222.76]  Jared, did you have something to say?
[223.26 --> 228.34]  Well, I was just going to comment on the videos. They're all online now. And Sue's linked us up here
[228.34 --> 233.58]  in order to prepare. I was actually watching Kaleo Howe. I can't say his last name.
[233.58 --> 234.78]  Howe. It's Howe.
[234.90 --> 240.84]  Kaleo Howe's Jump or Not to Jump Solving Flappy Bird with Deep Reinforcement Learning, which I had never heard of
[240.84 --> 246.08]  reinforcement learning. And I'm like 80% of the way through that. He's kind of blowing my mind.
[246.34 --> 251.44]  So interested at a certain point today to get your thoughts on that topic as well.
[251.70 --> 255.94]  Yeah, absolutely. Kaleo's talk was one of my favorite there. We ended up doing a little behind-the-scenes
[255.94 --> 260.64]  interview too, and that's been hopefully uploaded to the same YouTube channel as well, which is really,
[260.64 --> 268.14]  really fun. Yeah, Kaleo took a reinforcement learning mathematical formula, ignores how scary
[268.14 --> 272.60]  it looked, and then he broke it down. So it made it really easy to understand. I'm really glad that you
[272.60 --> 277.92]  ended up looking at that video. Yeah, I started off intimidated, and he said I was asked to explain
[277.92 --> 282.84]  the math behind this, and I thought, hmm. But he did such a great job of setting it up that I was
[282.84 --> 287.04]  like, well, I'll give him five minutes. And then like five minutes in, I was hooked, and I was into it.
[287.04 --> 293.76]  So far, it actually does make sense as he describes the math, which that's a feat with me is to get me to
[293.76 --> 297.52]  understand deep math things. It's quite a task.
[298.88 --> 304.40]  I'm not that far behind either. I took advanced math in high school, but then sort of started bombing
[304.40 --> 308.04]  out my last few years of high school. So it's definitely something I've always wanted to be
[308.04 --> 315.14]  better at. The cool thing is that Kaleo also put his Flappy Bird example up on GitHub, so I'm yet to
[315.14 --> 317.76]  track that down, but he said it's definitely there. Nice.
[317.76 --> 322.92]  Cool. There were some other talks, though, that were really surprising to me because they actually
[322.92 --> 327.86]  called out JavaScript and machine learning. So I think the biggest one was Amy Chang's.
[328.16 --> 332.20]  She opened on the second day, and she talked about using machine learning to create art,
[332.26 --> 339.28]  and it became a very existential talk towards the end of it where she said, is this even art? Is using
[339.28 --> 345.36]  techniques that people have probably seen, such as style transfer where you can take a photo and then
[345.36 --> 350.66]  paint it in the style of Van Gogh, you know, that sort of example. She was asking questions such as,
[350.82 --> 358.12]  is this art or is this a machine just copying things? And she talked about this concept of this
[358.12 --> 365.18]  professor that she was reading an essay from about the concept of like the machine learning's aura,
[365.44 --> 369.98]  rather than it just copying like, you know, the aura of human art. And I thought that was really
[369.98 --> 374.02]  fascinating. What is the machine learning's aura? What do you mean by that?
[374.02 --> 378.94]  Yeah, apparently the essay doesn't really say what it is. But I think what they're saying is,
[379.44 --> 385.56]  right now we're using machine learning to just emulate human art or existing computer art. But
[385.56 --> 390.22]  what if machine learning was supposed to create like different art that was sort of
[390.22 --> 397.78]  more idiomatic to the actual neural network rather than, again, just directly copying human stuff.
[397.94 --> 402.14]  So apparently we're yet to see that. And I think the aura is insinuating that
[402.14 --> 405.46]  hopefully that will emerge at some point.
[405.56 --> 409.88]  One of the things I really like about this idea of using machine learning for art is it kind of
[409.88 --> 413.74]  plays into to one of the things that I think is the strength of machine learning and JavaScript,
[413.74 --> 420.38]  which is accessibility. It's bringing this stuff to perhaps a an audience that is a little bit less
[420.38 --> 426.10]  grounded in all of that crazy math and deep stuff and saying, hey, you know what,
[426.10 --> 430.44]  you can play with this right now, right away and do cool stuff with it. You don't have to
[430.44 --> 435.94]  understand all of the deep underlying pieces. That's a really excellent point. And Amy was
[435.94 --> 441.90]  talking about that in her talk because she used she used mostly JavaScript tools to do it. She
[441.90 --> 449.04]  used like Synaptic JS and MO5 JS. And MO5 JS, I think, is supposed to be sort of in the P5 JS family,
[449.26 --> 453.84]  which are like really friendly wrappers around Canvas. And so I think this is a friendly wrap around
[453.84 --> 460.34]  TensorFlow JS, if I'm not mistaken. And I really agree with that whole accessibleness. And I think
[460.34 --> 465.18]  she was saying something about it's easier to share stuff if you can just send someone a browser URL.
[465.98 --> 472.14]  Just I'm stuck back on the neural network, art idea and kind of these existential questions.
[472.36 --> 478.28]  Curious what everybody thinks, because if a neural network creates some art, then who is the artist
[478.28 --> 483.38]  who owns the copyright? All these questions kind of open up. And I think we have a whole new
[483.38 --> 488.76]  set of new questions that we start asking ourselves. Well, there's the intellectual property
[488.76 --> 492.84]  side. That's I didn't even go there at all. I was kind of coming back to this question of like,
[493.08 --> 500.90]  what is art? Right? Is it does do we? There's all this weird stuff about things that you or I might
[500.90 --> 506.00]  think are ugly or stupid, but it is considered art because of the mental state of the artist when they
[506.00 --> 513.04]  were doing it and what it got through. Is art defined by the process of creation or the process
[513.04 --> 514.68]  of observation and consumption?
[515.62 --> 519.88]  I think, yeah, I mean, that's the, that's, I don't think I asked before answer to that question. It
[519.88 --> 525.86]  might be beyond my pay grade, but I think with regards to like the creation side of it, if you have
[525.86 --> 532.78]  a human whose feet, I mean, specifically with machine learning based art, and let's use style
[532.78 --> 537.80]  transfer as an example, right? You have an existing image, which is selected by a human. And then you
[537.80 --> 542.96]  have a set of training data, which is selected by a human, right? Like that's the whole thing with
[542.96 --> 548.40]  machine learning is we teach them based on examples and we hand them all these images. And so that's
[548.40 --> 554.14]  like the machine isn't choosing those things, at least not yet. And then the final product is really
[554.14 --> 561.24]  a result of the input. So it's still like inputs and outputs. So in the, in, in the unique case of
[561.24 --> 565.56]  style transfer. So I guess for those who don't know what style transfer is, you have a source image,
[565.94 --> 572.48]  you have a, a, another image that has some specific style to it, and you're basically passing one
[572.48 --> 577.42]  through the other in order to create something brand new. Um, and it's more complex than that.
[577.50 --> 581.86]  But in that case, I think like the, the human is still doing all this stuff and the machine is just
[581.86 --> 586.92]  kind of chunking stuff out. But I think you're probably talking more down the line where we start
[586.92 --> 592.66]  to hand off more decision-making to the machine. Does that, is that where you're going with that?
[593.00 --> 597.74]  I think that if, if we look at the example of deep dream, where you had all those weird puppies and
[597.74 --> 603.86]  eyes everywhere, that was the result of them sort of feeding, you know, the machine back into itself.
[603.86 --> 608.82]  And so then it was just generating really, really weird stuff based on a reference image,
[608.82 --> 615.96]  which is not something that was really copying a specific artist or a human, but we, I, I honestly
[615.96 --> 620.04]  believe we interpreted that as art and I'm interested to hear what the other panelists think as well.
[620.42 --> 625.02]  It certainly, you know, I'm, I'm looking right now, there's a deep gene generator.com,
[625.12 --> 630.20]  like looking at this, I consume it as art, right? It looks to me and I'm like, wow, that's,
[630.32 --> 633.90]  that's amazing. Some of that is incredibly beautiful. And some of it is just bizarre,
[633.90 --> 637.72]  but that, that distribution of reactions is the same for me looking at a lot of human art,
[637.82 --> 641.20]  right? Some of this is incredibly beautiful and some of this is just why.
[642.06 --> 644.20]  Right. So one thing that I, oh, go ahead.
[644.20 --> 649.00]  Oh, sorry. So if, if, if I'm looking at deep, like something generated by deep green and I didn't
[649.00 --> 654.44]  know what made it, you know, if I, if I thought, well, maybe somebody, somebody drew this or painted
[654.44 --> 662.00]  it or whatever, um, I would say, wow, that's really trippy, like surrealist art. Sure. But because I know
[662.00 --> 666.52]  what created that, um, it, it just doesn't feel like art to me anymore.
[666.52 --> 669.62]  Oh man, the hummingbird on fire. That's so cool.
[671.62 --> 675.88]  I don't know. So, I mean, I don't, I don't look at a deep dream and, uh, you know, those pictures
[675.88 --> 682.34]  and think of them as, them as art. And I, I mean, I, I assume I'm not alone in that. Um, I think,
[682.40 --> 687.66]  you know, if, if, you know, we're looking at ML as a source for art, uh, there's going to be
[687.66 --> 692.86]  quite a few people who are going to have, you know, some issues with that, I think.
[692.86 --> 696.92]  Yeah. I mean, I, I don't have the philosophies around art, but I believe that it's, you know,
[696.96 --> 702.14]  it's created in order to invoke some sort of emotion or reaction. Right. And so there's,
[702.46 --> 706.42]  regardless of whether it actually connects with the consumer, like in cable, your situation,
[706.42 --> 710.70]  like some stuff you think is just crazy and isn't good. And I have the problem with some art where
[710.70 --> 715.28]  I'm like, this doesn't require skill. Like it's like, especially splatter paintings. I look at it,
[715.30 --> 719.72]  I'm like, you know, my, my three-year-old could do that. Is that art? Well, to somebody it is.
[719.72 --> 726.88]  Right. But, um, it's, there is a, there is an artist on one side of it. And that's why I kind
[726.88 --> 730.52]  of went to the question of like, what, who's the artist and maybe where that's where you're
[730.52 --> 735.06]  going with it. Chris saying it's not really art because it's, it's generated based on some sort
[735.06 --> 739.76]  of algorithm or some sort of, uh, inputs and outputs, but it's not like the person on one end
[739.76 --> 745.34]  said, I'm trying to make you sad or happy. And so therefore here's this hummingbird on fire.
[745.34 --> 752.40]  I mean, yeah, it's, it's not so much about that for me, it's, it's about intent. And if I intend
[752.40 --> 759.68]  to make art, well, you know, it's, it's, I get to call it art, but, uh, machine has no intent.
[759.94 --> 763.94]  You know, one of the, the really cool to me reasons why one might want to look at machine
[763.94 --> 768.42]  learning in JavaScript is kind of hearkening back to the shareability of it. You just put it online and
[768.42 --> 772.06]  it goes, what if we thought about this as a tool for creating collaborative art? You know,
[772.06 --> 777.46]  you throw your photos in and I throw my photos in and we, we kind of have the machine merge them
[777.46 --> 782.52]  together in an interesting way. And we could create art suddenly not limited to who you can
[782.52 --> 785.46]  get in a room, but you know, you could have millions of people co-creating.
[786.08 --> 792.96]  Sure. I mean, even just, you know, you have, you create a framework or some constraints,
[793.40 --> 799.94]  um, throw it up there on the web and allow people to use your website using ML to, to make their own art.
[799.94 --> 805.84]  And then it's, it is their art, even though it's ML as the tool behind it, right? Is ML that different
[805.84 --> 806.52]  than a paintbrush?
[807.18 --> 808.60]  That's deep, Kevin. Very deep.
[808.80 --> 815.66]  So there were a couple other talks that y'all, uh, that Suzy mentioned, um, beyond the ML to create
[815.66 --> 819.48]  art, which we could go on about art for a long time, but I don't know how, how much that's going
[819.48 --> 826.18]  to get us into JavaScript. But, uh, there was one on killing math, uh, which I think also ties back
[826.18 --> 832.16]  to this idea of making ML more accessible, something that, you know, you don't need a PhD
[832.16 --> 837.14]  in computer science to learn, but you can hack around with on your browser at home. You can maybe
[837.14 --> 842.20]  have a, you know, my kid is there learning to code. My kid's too young to learn to code yet,
[842.26 --> 846.06]  unfortunately, but at some point, you know, they could just be playing with this thing
[846.06 --> 852.58]  in a web browser without having to do anything. Um, and then you had to talk as well that you gave,
[852.64 --> 856.96]  I'm not going to make you plug yourself, but, um, I thought it was another really interesting example,
[856.96 --> 862.76]  uh, where you were essentially taking an extension, a browser extension or a bookmarklet
[862.76 --> 868.50]  and using it to auto annotate images for accessibility, right? Looking at an image and
[868.50 --> 873.44]  giving a summary of what is this thing. And it made me start wondering, like, does this,
[873.44 --> 879.70]  when you start thinking ML in browser extensions and ML, uh, you know, in pluggable snippets that we
[879.70 --> 885.22]  can sort of share around, does this give us whole new ways of, of kind of parsing and viewing the web?
[886.12 --> 891.66]  Yeah, I saw it more from the perspective of us repairing the web. And then hopefully we can use
[891.66 --> 896.48]  these techniques going forward to kind of, you know, once we've tended to the garden of the web and
[896.48 --> 902.52]  made it nice again, we can just keep it kind of trimmed, I guess. That's like my little analogy there,
[902.52 --> 911.82]  but I, I, I really like how you can use machines to identify subject material in images. And so I,
[911.82 --> 917.38]  I definitely have seen some not so great uses of that technology. And so I was trying to find
[917.38 --> 922.52]  something that would be a positive use, which is, um, being able to provide old texts for images
[922.52 --> 929.06]  on the net that don't have alt tags already applied to them because it's such a huge task to do.
[929.06 --> 934.58]  Uh, it would be, it would be great if people could either do it on demand or we could run jobs on
[934.58 --> 941.58]  websites and refresh those specific pages. So that was me exploring some very idealistic views about
[941.58 --> 947.12]  how we can use, um, things like just even REST API calls, because even if we don't want to run these
[947.12 --> 954.36]  models in a browser, we can make a REST API API call to a server that is able to run those, um,
[954.36 --> 959.76]  those models in order to identify the, the images. And so I was trying to show that you don't even
[959.76 --> 963.96]  have to create your own models. You can use existing ones that are out there and, you know,
[964.32 --> 967.46]  JavaScript is very, very good at making REST calls.
[968.02 --> 971.20]  That's interesting. You did it as a browser extension. My immediate thought, I guess,
[971.22 --> 976.78]  as a website creator is there's lots of pragmatic reasons that you would want this in your server-side
[976.78 --> 981.46]  markup as well. So I was thinking in terms of like tooling for developers,
[981.46 --> 987.30]  maybe it's a web pack plugin that you can just pull into your pipeline and it can go through and,
[987.30 --> 992.96]  you know, check all your image elements that don't have rel, rel attributes or titles,
[992.96 --> 999.10]  and then do the analysis and actually write that back into your, either your server-side code or in
[999.10 --> 1005.42]  your, your generated web pack HTML so that it wouldn't have to be subjective in terms of like the
[1005.42 --> 1008.90]  individual with the browser extension, but it actually like fix it at the source.
[1008.90 --> 1013.48]  That would be cool. I know that at the source, sometimes it's easier for a human to write them,
[1013.58 --> 1018.68]  especially if you don't have a large collection of images, but it would be great if stock photography
[1018.68 --> 1023.28]  websites, for example, were able to, uh, if you download an image from that and you're using a
[1023.28 --> 1028.08]  ton of them, maybe that's the use case for being able to like automatically attack them using a
[1028.08 --> 1032.70]  machine's intelligence. Right. Or user generated content where they're uploading images, but not
[1032.70 --> 1036.42]  necessarily, you know, they're not tending to your garden quite as well as you'd hope they would,
[1036.42 --> 1040.64]  your users, you know? Yeah, that's exactly why I use Instagram as an example of that because,
[1040.64 --> 1047.00]  you know, people tend to use pretty sort of ephemeral or, uh, vague sort of captions, even if
[1047.00 --> 1052.54]  they do put their own caption on there. So they're not always appropriate to use for alt text. Yes,
[1052.60 --> 1056.86]  you're right there. So, Suze, to, to make sure I understand how something like this would work,
[1056.92 --> 1063.86]  you, you would have a, a, a browser extension, um, and you know, you're visiting a webpage and there's no
[1063.86 --> 1069.14]  alt tags, uh, maybe you, you, you click the button or invoke the extension or maybe it runs
[1069.14 --> 1075.08]  automatically. And what it's going to do, it's going to scrape all those, um, images and send
[1075.08 --> 1080.04]  them off that basically it's going to take the images and, and, and post them or something to,
[1080.04 --> 1087.18]  to some endpoint. And that endpoint's going to come back with some alt text and that will be then
[1087.18 --> 1092.86]  applied to the DOM somehow. Is that basically what, what happens? Yes, that's exactly how it works.
[1092.86 --> 1098.06]  And so it will actually go and manipulate that image tag and add in the alt text attribute.
[1098.34 --> 1104.28]  I will say that there is a few privacy limitations around, um, being able to use this, which is why
[1104.28 --> 1109.06]  I haven't released it as an extension or anything like that, because a lot of, a lot of these models
[1109.06 --> 1114.36]  are privately owned by large companies and you don't necessarily have the permission to take people's
[1114.36 --> 1120.72]  photos and put them through, um, that system. And with DDPR, we're all extra, um, conscious of,
[1120.72 --> 1125.52]  of data privacy as well. And so whenever I do this demo, I usually just use it on my friend's
[1125.52 --> 1129.68]  Instagram profile page and I already got his permission to do that. So yeah, there's definitely
[1129.68 --> 1134.70]  a lot of kind of, um, discussions to have around the appropriateness of this technology, but yes,
[1134.70 --> 1139.12]  that if we had everyone's permission to do that, that's exactly how it would work, which would be
[1139.12 --> 1143.18]  amazing. That's, that's interesting. I mean, my next question was going to be about privacy
[1143.18 --> 1149.46]  because I mean, necessarily for this to work the way it's designed, you know, moreover,
[1149.54 --> 1155.12]  I mean, you're basically, as you browse the web, it's going to take a ton of images and,
[1155.12 --> 1160.18]  and send them off to some, some company, whoever owns that, you know, restful endpoint. So then
[1160.18 --> 1168.42]  going, going a bit further, um, what would it take to, uh, you know, run, run your own,
[1168.42 --> 1176.48]  I mean, basically have your own setup or, or run, run, run that, uh, in the browser where you have
[1176.48 --> 1184.24]  this, this kind of neural network all set up and you can, um, analyze images like maybe just like
[1184.24 --> 1190.70]  in the browser itself. I mean, what, what kind of memory requirements, I mean, like what's stopping
[1190.70 --> 1196.56]  that from happening? Why do we have to hit, uh, uh, a restful endpoint? I don't think we really do
[1196.56 --> 1200.46]  anymore. I think that's a really good point. And so one benefit we get from hitting that endpoint
[1200.46 --> 1205.52]  is that it's continually improved. And so, you know, it's going to get better and better. Um,
[1205.72 --> 1209.98]  and the, the downside of running your own model in your browser, which is completely plausible.
[1209.98 --> 1213.06]  And we're going to, I think we're going to talk about a couple of those examples in the next,
[1213.50 --> 1219.12]  the next segment of this show. Um, you could own that model and just run it locally. And I think
[1219.12 --> 1224.14]  that that would be perfectly fine to do. And I think that would get around those issues and you
[1224.14 --> 1228.10]  would really only be running the model on the images that you care about. So it's not as if
[1228.10 --> 1233.10]  you'd be running it through, through 10,000 images in a second. So I think that browsers would be more
[1233.10 --> 1237.60]  than capable of doing that. And we, we have some really cool tools now. And even before that,
[1237.84 --> 1244.54]  technically you could port open CV, uh, to web assembly and run it that way. And so, um, I think
[1244.54 --> 1249.44]  that that is a really good idea and I'm hoping that everyone's going to be able to kind of own their
[1249.44 --> 1254.50]  own models going forward and, and be able to understand how to constantly improve them.
[1254.50 --> 1257.26]  Uh, remind us what open CV is real quick.
[1257.40 --> 1262.12]  Oh yeah. So it's an open source computer vision library. And so it doesn't actually run in the
[1262.12 --> 1268.08]  browser. I forget what it was written in. It was, it's either C or it's Python. Um, and I think there
[1268.08 --> 1273.02]  just might be lots of different language wrappers for it. Um, but yeah, it's, it's basically a computer
[1273.02 --> 1279.82]  vision, um, executable where you can, you can run images through it to identify things like
[1279.82 --> 1284.76]  facial detection and also just like positioning of objects and things.
[1285.38 --> 1290.30]  Could we invert the problem where you have a, an available model that gets trained on,
[1290.34 --> 1295.30]  on images that don't have licensing problems in some form or another, but then each browser
[1295.30 --> 1299.92]  essentially pulls the updated model periodically. And you're always, so you're never sending back
[1299.92 --> 1302.70]  private people's private images. You're always just doing that in their browser.
[1303.02 --> 1308.16]  But you can still get updates from your public image data by pulling updated models.
[1308.70 --> 1310.14]  That's such a cool idea.
[1310.68 --> 1314.64]  You have to open a ticket on Chromium and WebKit and Edge.
[1314.66 --> 1317.86]  Or just build an extension, right? If you build an extension, that's going to end,
[1318.12 --> 1322.14]  and you need that, that database. So I'm not an expert in this area, but I know there's lots
[1322.14 --> 1326.28]  of images that are out there for, you know, that are, you know, creative commons licensed or
[1326.28 --> 1330.52]  things where you might be able to just kind of publicly use them without too much difficulty.
[1330.52 --> 1337.18]  Use that to train a model that you, and then export it as a set of configs that can be read
[1337.18 --> 1340.60]  by TensorFlow.js or something like that, and then have your extension pull it up.
[1340.60 --> 1351.66]  Hey, everyone. I'm Tim Smith, senior producer at Changelog. We're so excited to have added the
[1351.66 --> 1357.24]  React podcast to our stellar lineup of shows. Every week, Michael Jackson has conversations
[1357.24 --> 1362.06]  with developers doing great things in the world of React. You'll hear from people like Andrew Clark,
[1362.26 --> 1364.06]  a developer on the React core team at Facebook.
[1364.06 --> 1368.82]  I'm here on the podcast to talk about the thing that I spend most of my time thinking
[1368.82 --> 1375.80]  and dreaming and fantasizing and worrying about, which is React, because that is what I do all
[1375.80 --> 1378.88]  day, every day, even when I don't want to.
[1379.00 --> 1383.30]  James Long, who was frustrated with budgeting apps, so he decided to build his own called
[1383.30 --> 1385.30]  Actual with React and Electron.
[1385.40 --> 1391.82]  The UI design is just super overcomplicated in so many of the apps out there. I mean, you look
[1391.82 --> 1395.94]  at some of the screenshots of these apps, and there's like 50 numbers on the screen. The
[1395.94 --> 1400.44]  simplest question that you want to answer is what I just said, right? What is my finances
[1400.44 --> 1405.62]  right now? Should I buy this thing that's $200? Like, can I buy this PS4? Like, how much is that
[1405.62 --> 1406.14]  going to hurt me?
[1406.28 --> 1410.42]  Or Henry Zhu. Henry quit his job and is working on open source full time.
[1410.48 --> 1417.16]  I think overall, I feel pretty good about it, for sure. And there's definitely lots of unknowns
[1417.16 --> 1422.16]  and things I have to work out, whether it's just like personally or logistically, all that
[1422.16 --> 1425.08]  stuff. But I'm definitely excited for what's in store.
[1425.08 --> 1430.66]  Go to changelog.com slash react podcast, or wherever you listen to our shows. New episodes
[1430.66 --> 1432.28]  come out every Tuesday.
[1432.28 --> 1449.08]  So, I mean, the concern is that you're copying an image, basically?
[1449.42 --> 1454.38]  Yeah, and you're passing it through a model. And that model is basically like, theoretically,
[1454.84 --> 1459.74]  you're going to use their content to improve the model. I don't know how deep I want to get into
[1459.74 --> 1465.42]  this, but there has been controversial use of certain images for things like facial recognition
[1465.42 --> 1471.74]  and gender detection, where they've used images of actual people without their consent, if that
[1471.74 --> 1477.26]  makes sense. And so, if I'm passing images of Instagram through, there's going to be a lot of
[1477.26 --> 1482.78]  selfies in there. And so, that's sort of where that IP becomes a real concern. So, hopefully,
[1482.88 --> 1484.26]  that sort of gave you a bit of an idea.
[1484.26 --> 1490.02]  Yeah. Someone's personal photos are, in theory, private or protected data, unless they put some
[1490.02 --> 1493.64]  sort of license on it saying you can use it. I mean, your model maybe isn't training, but if
[1493.64 --> 1497.24]  we're sending it off to a REST server, they don't know that, you don't know that, that data is
[1497.24 --> 1498.64]  flowing through the web somewhere.
[1499.00 --> 1502.62]  I guess I was confused. I thought maybe you were talking about copy, copyright and electoral
[1502.62 --> 1506.58]  property stuff. But this is more like just ethical questions.
[1507.00 --> 1511.22]  Well, doesn't Instagram, I mean, there is an IP situation there as well, because don't you,
[1511.22 --> 1516.58]  you render some rights to Instagram when you publish on their platform. And so, there's
[1516.58 --> 1521.20]  certain claims that the company Instagram actually owns on that imagery as well.
[1521.34 --> 1526.36]  It's also a requirement of a lot of these API services. You have to either have permission
[1526.36 --> 1532.26]  to use the data or you need to own the data yourself. So, you're against the TNS if you're
[1532.26 --> 1533.28]  not doing that as well.
[1534.08 --> 1539.12]  Right. There's, it's a great area. I mean, there's like been, you know, the,
[1539.12 --> 1547.78]  there's like a recently a lawsuit where I think it was LinkedIn said, Hey, company,
[1547.92 --> 1553.42]  stop using our website because this company was basically scraping LinkedIn for stuff.
[1554.08 --> 1561.48]  And I can't remember what happened, but I think it was that the, the LinkedIn actually lost that suit.
[1561.48 --> 1569.32]  And that, that, you know, makes me think, well, you know, if that sets a precedent, then, you know,
[1569.38 --> 1577.20]  it kind of opens up stuff to, um, you know, I can, because you are presenting the, these images and
[1577.20 --> 1583.30]  because you're presenting this stuff on the web, it, it becomes public essentially. And, you know,
[1583.34 --> 1589.14]  it's going to end up in my browser cache. It's going to get copied around. Um, and maybe that's going
[1589.14 --> 1592.96]  to end up in some machine learning, uh, neural network somewhere.
[1592.96 --> 1598.22]  But with, with GDPR stuff going, there's a lot more impetus on companies though. You know,
[1598.22 --> 1601.72]  if you're using somebody's personal data, you have to give them a way to remove it.
[1601.96 --> 1608.08]  And once it's deep down in the model, I don't know that you can. So that, that would put a lot
[1608.08 --> 1611.82]  of liability on a company that was using that without permission.
[1611.82 --> 1616.06]  I prefer the wild west model where we all just do whatever we want, you know, I'm just like,
[1616.10 --> 1619.36]  let's not worry about any of that other stuff. We'll just, we'll let it shake out. We'll let
[1619.36 --> 1622.64]  the judges shake it out. No, just me. Okay.
[1627.06 --> 1633.18]  Well, yeah, it's kind of funny, not funny because, you know, a lot of, a lot of engineers say we're
[1633.18 --> 1636.30]  just engineers and we're just doing what we're told.
[1636.76 --> 1641.40]  Ethical problems are a big thing, right? Like if you're not going to stand up and say,
[1641.40 --> 1643.52]  this is unethical, who's going to?
[1643.82 --> 1647.28]  Well, I think part of the problem is there's going to be somebody who won't say that.
[1647.80 --> 1654.84]  And so we could do it or somebody else could beat us to it. I mean, you say, okay, I've got this,
[1654.84 --> 1662.90]  this, this cool new AI that, um, can fake a video of like the president saying something he didn't say.
[1663.52 --> 1671.38]  Um, and, uh, yeah, let's, let's release that to the world. I mean, that's, there's,
[1671.40 --> 1678.26]  exists. Right. Sure. Um, it, it exists and, and it's like, well, but you know, that's,
[1678.74 --> 1685.32]  that's problematic. That's a problematic technology. I mean, and you know, the, the people who,
[1685.40 --> 1689.82]  who invented that, I can't remember if it was Adobe or whatever, but if they didn't do it,
[1689.88 --> 1693.30]  somebody else was going to, you know, even if there were, there were engineers there that,
[1693.40 --> 1698.10]  that raised those ethical concerns, you know, because they could, well, certainly some other
[1698.10 --> 1703.64]  company could too. And somebody was going to do it and somebody was going to file the patent and
[1703.64 --> 1705.46]  yada, yada, yada. So.
[1705.62 --> 1710.38]  I'm not sure that slippery slope argument is, is a valid way to say, Hey, we as individuals
[1710.38 --> 1712.52]  shouldn't stand up for ethical decisions.
[1712.78 --> 1716.54]  Oh, I'm not, I'm not arguing that. I mean, I'm just saying this is how people think.
[1716.76 --> 1720.48]  Well, I think we need to change that. I mean, and who's going to change that except role models,
[1720.48 --> 1727.74]  right? Like if, if you have your set of lead engineers who are experienced in the industry,
[1727.84 --> 1733.08]  standing up and saying, Hey, we have to take a stand. It's not valid to say, Oh, but business
[1733.08 --> 1738.58]  said so we are going to still hold you accountable to that. Like that's how a culture changes. It
[1738.58 --> 1740.78]  doesn't change if nobody takes a stand.
[1741.18 --> 1746.04]  Yeah. I mean, but you know, the buck doesn't stop the engineers either. It's, it's even, even if the
[1746.04 --> 1750.32]  engineers say no, and then the business itself says, okay, you guys are right. I'm not going to,
[1750.32 --> 1754.00]  I'm not going to do that. We're not going to, we're not going to go there. Well, the next
[1754.00 --> 1759.24]  company, the company, their competitor will, you know? And so it's more of a, I don't know,
[1759.44 --> 1760.88]  it goes beyond engineers.
[1761.22 --> 1765.80]  It's a holistic problem, right? It's a social construct that we all participate in and our
[1765.80 --> 1766.68]  different roles. Yeah.
[1767.14 --> 1770.94]  Society, a societal problem, um, economic problem.
[1771.16 --> 1772.80]  It makes me think of, Oh, sorry.
[1772.98 --> 1778.66]  I was just going to say that I don't think the fact that there is a structural problem does not
[1778.66 --> 1783.10]  put individuals off the hook. The way that we change societies is we get enough people saying,
[1783.20 --> 1788.82]  Hey, this is not right. Law and that sort of thing is downstream from culture. So if you want
[1788.82 --> 1794.16]  to change the law and what's regulated and what's allowed and what's restricted, the, the way you
[1794.16 --> 1795.66]  target that is changing the culture.
[1796.18 --> 1797.64]  Unfortunately, it's not always downstream.
[1798.92 --> 1804.16]  Well, not always, but a lot of times it's sidestream to culture, right? It's despite culture,
[1804.16 --> 1806.24]  lots of times because of corruption and whatnot.
[1806.52 --> 1811.78]  True. But I mean, if you look at, for example, like the, the change on gay marriage, right? That
[1811.78 --> 1816.64]  came because of in, you know, we were going nowhere, nowhere, nowhere. And then there was a
[1816.64 --> 1821.14]  massive, you know, the culture shifted to the point where you had a majority of people saying,
[1821.22 --> 1825.84]  what is going on here? And very quickly the politicians followed. Uh, and I think we can,
[1826.26 --> 1830.64]  if you get enough momentum behind it, say, if you have, you know, two thirds of the industry
[1830.64 --> 1834.68]  talking about the ethics of this rather than saying, well, you know, I'm just an engineer.
[1834.80 --> 1839.32]  So what do I know? What am I going to do? Right. Things are going to shift. And that starts with a
[1839.32 --> 1843.12]  few people saying, you know what, we got to do this. And I, you know, there's, there are people
[1843.12 --> 1849.14]  out there talking about the ethics of this. It has become an active conversation in our industry,
[1849.14 --> 1857.08]  which I really appreciate. Um, at QCon last year, QCon SF, um, Leslie Miley, I think, um,
[1857.08 --> 1861.08]  did a keynote and he talked, he took it head on and was saying, you know, we're,
[1861.20 --> 1868.06]  we're creating these models that are essentially, uh, digital weapons of mass destruction, uh, in
[1868.06 --> 1871.96]  Facebook and things where we can massively do things. We have a responsibility to be thinking
[1871.96 --> 1877.58]  about it. So it is a rising tide of discussion in the industry, but you know, we need to keep
[1877.58 --> 1882.10]  pushing it. I think one thing that we could all, uh, have a read of too, and reference from
[1882.10 --> 1887.92]  going forward is a medium post by Laura James. It's called oaths, pledges, and manifestos,
[1888.04 --> 1894.58]  a master list of ethical tech values. And it has a bunch of links, um, including ones to AI,
[1895.02 --> 1900.84]  um, manifestos and pledges. Um, so I definitely, uh, definitely encourage you to read through that
[1900.84 --> 1905.78]  because there's definitely a movement happening online where, um, a lot of people are definitely
[1905.78 --> 1911.66]  signing up to start questioning themselves and their role in this. Cool. All right. So we talked a
[1911.66 --> 1918.20]  little bit in the first segment about, um, just that there are some JavaScript tools for creating
[1918.20 --> 1923.04]  like machine learning models and also running them. Uh, we did mention a couple of them,
[1923.04 --> 1930.18]  such as synaptic JS, ML5 JS, um, and TensorFlow JS. But I guess other than the shareability of it,
[1930.18 --> 1935.16]  which, um, which Amy was talking about as a strength of doing something like this with JavaScript
[1935.16 --> 1940.22]  during the browser, what are some other value propositions that you can think of for using
[1940.22 --> 1945.86]  machine learning using JavaScript, which I'm guessing will be a little bit slower than perhaps
[1945.86 --> 1951.08]  using other languages to do so. Could be slower though. JavaScript is bloody fast,
[1951.08 --> 1957.36]  but, uh, you know, I think there's a few different things that come immediately to mind. One is kind
[1957.36 --> 1963.68]  of in this idea of shareability, but just in terms of making it super easy to learn, uh, and play around
[1963.68 --> 1970.42]  with concepts. Uh, it's sometimes easy to forget if you're living in the web world, how, how much of a
[1970.42 --> 1974.32]  pain it can be to, to set up a development environment and do all sorts of things in
[1974.32 --> 1979.22]  tutorials that are, that have much more heavy backend requirements. Uh, whereas I saw a post
[1979.22 --> 1984.12]  recently, um, that was making the rounds called hello TensorFlow that literally just had an in-browser
[1984.12 --> 1990.04]  demo where you could play with it and you could tweak parameters and really start to understand how
[1990.04 --> 1994.98]  machine learning is working without having to install a thing. So you could do that. I mean,
[1994.98 --> 2001.48]  you could do that in the developing world on a tiny little laptop or Chromebook or even a phone
[2001.48 --> 2007.04]  potentially, and start learning these concepts without having to get a big environment set up.
[2007.34 --> 2012.48]  I really love the idea of that so much. Um, just literally just start tweaking stuff immediately with
[2012.48 --> 2014.64]  an example that's running in the browser. That's awesome.
[2015.04 --> 2018.46]  Yeah. I think we should distinguish, I mean, in the browser versus not when we talk about
[2018.46 --> 2023.38]  anything with JS, of course, but specifically with machine learning and JS and, and like Kevin said,
[2023.54 --> 2027.48]  I mean, JavaScript itself is not slow. I, but I think what we talk about, you know,
[2027.60 --> 2033.42]  specifically like training models in the browser on a phone or on an underpowered PC
[2033.42 --> 2038.28]  is going to be slow. Right. And the difference with JavaScript with most, most other languages is
[2038.28 --> 2043.62]  it exists in the browser. Of course, we'll, we'll get there with, uh, with WASM or WASM. I can't remember.
[2043.62 --> 2049.38]  Or WASM and whatnot. Don't get me off on that train, but you know, server side drop JavaScript,
[2049.66 --> 2054.38]  right. And node is, is completely capable of doing these things as well. Isn't it? I know a lot of
[2054.38 --> 2059.52]  people are doing Python for the actual training, but that doesn't mean you can't train machine
[2059.52 --> 2061.08]  learning models in JavaScript. Does it?
[2061.34 --> 2067.00]  No, you can totally train them. I think though that trying to import like a 35 gigabyte CSV file
[2067.00 --> 2073.34]  is going to be maybe a little bit tough for the UI thread at least. Right. I was kind of under the
[2073.34 --> 2079.84]  impression that, I don't know, like where, where did GPUs come in? I mean, do they? Uh, and if you
[2079.84 --> 2085.92]  want a GPU binding, you might not want to use JavaScript. Yeah. No TensorFlow runs in the GPU.
[2086.34 --> 2092.08]  Does TensorFlow JS give us access to the GPU and can we get access to the GPU from browser running
[2092.08 --> 2096.88]  JavaScript? That would be amazing. Yeah. So TensorFlow was designed to make as much use of the GPU as
[2096.88 --> 2102.90]  possible for this kind of stuff. I guess just trying to load that initial, um, large amount
[2102.90 --> 2108.92]  of memory to do the, the training just from the training data itself. Um, you wouldn't quite even
[2108.92 --> 2113.78]  be at the GPU stage at that point. That, that was my biggest concern. Well, even going back to Amy
[2113.78 --> 2121.22]  Cheng's talk at ML for all, she was going through the work she was doing with Synaptic JS and MI5 JS.
[2121.82 --> 2126.64]  And she said specifically, we can't use JavaScript to train models. There's simply too much data,
[2126.64 --> 2131.82]  which is kind of what you're saying there. Uh, she was speaking about in the browser specifically
[2131.82 --> 2137.02]  and she had fallback. She had trained the things with Python and then she was using TensorFlow
[2137.02 --> 2141.50]  JS to actually use the models. So that's a common trend right now. Yeah, that's right. I know that
[2141.50 --> 2148.50]  TensorFlow JS, um, supports, uh, both, uh, models that were trained by TensorFlow itself and also models
[2148.50 --> 2152.98]  that were trained with Keras, which is like a wrapper around TensorFlow, which is pretty cool.
[2152.98 --> 2158.74]  So this hello TensorFlow thing though, I mean, there's training happening in that demo.
[2159.16 --> 2163.22]  Yeah, it's a pretty simple model, right? They're trying in that example, they're
[2163.22 --> 2169.56]  essentially modeling a quadratic curve. So it's not, uh, or not quadratic, it's, uh,
[2170.02 --> 2175.34]  X to the third. So whatever that is, but, um, you know, they're, they're modeling a very simple
[2175.34 --> 2180.34]  mathematical formula rather than something really complex, like recognizing something,
[2180.34 --> 2185.42]  but it gives you sort of an understanding of what is the big picture of what's going on here.
[2185.64 --> 2189.76]  What is it that we're, we're doing when we're training something to recognize images or do
[2189.76 --> 2196.18]  things like that? Um, and yeah, with that simple of a model, it's just running it, the training in
[2196.18 --> 2201.34]  the browser. So where does it become too much? Like what's the threshold? I guess that's what I
[2201.34 --> 2206.66]  don't understand because if we're training in this demo on glitch or what have you, you know,
[2206.66 --> 2212.58]  why, why are we saying we can't use JavaScript to do it? Like what problems is it? Is it almost
[2212.58 --> 2219.90]  all problems that are real world are, are just going to, to eat up too much memory to, to do or,
[2219.96 --> 2224.52]  or what? Like, where is that? Where is the cutoff? When, when does, when is JavaScript or,
[2224.52 --> 2227.80]  or training in the browser no longer feasible?
[2227.80 --> 2233.18]  I mean, I think in some sense, I wonder if you end up being more network limited than anything
[2233.18 --> 2239.08]  else. Cause you could probably, you know, essentially stream data through so that you're
[2239.08 --> 2244.44]  not going to be memory limited necessarily. Um, though I'm not an expert cause maybe you need
[2244.44 --> 2251.52]  to load it all at once, but I wouldn't expect you would, but that's a lot of data to be, you know,
[2251.52 --> 2257.74]  probably depends, right? If you're on a desktop that's wired via fast ethernet connection,
[2257.90 --> 2261.30]  I don't know that it makes a big difference, but with the browser, you might well be on a phone
[2261.30 --> 2267.94]  somewhere, or you might well be on a, uh, you know, wifi network. Um, I don't know that I'd want to
[2267.94 --> 2272.66]  stream 30 gigabytes of training faces over my iPhone.
[2272.92 --> 2277.86]  Yeah. I think it's insightful that Monica uses numbers here and she even states in her,
[2277.86 --> 2283.30]  in her demo that numbers are much easier to handle than images. And so most of the things
[2283.30 --> 2288.16]  that we're going to be using these models against our images, audio streams, video streams, these
[2288.16 --> 2294.30]  are, these are large data consumption things, but I don't have a hard answer of, you know,
[2294.34 --> 2299.68]  at exactly this type of thing, Chris, you know, JS becomes, um, unuseful.
[2299.98 --> 2302.92]  There's, I think tremendous, go ahead.
[2303.18 --> 2306.78]  I was going to say, I mean, there's, there's more to, there are more problems than just,
[2306.78 --> 2311.58]  I mean, there, there are text-based document processing, uh, text files, reading text files,
[2311.66 --> 2316.14]  reading source files, uh, with, with ML, um, that seemed like they would be less,
[2316.46 --> 2319.64]  less intensive than, than something like image or video processing.
[2319.64 --> 2324.66]  You know, one thing I was thinking about in our last segment, um, that, that reminds me of is
[2324.66 --> 2329.58]  kind of tied into this accessibility context. We talked about using ML to auto annotate images,
[2329.58 --> 2335.58]  but what about to auto annotate essentially, you know, ARIA markup and things like that for sites that
[2335.58 --> 2340.64]  are not well-designed for screen readers, right? If I have a site that's doing all sorts of crazy
[2340.64 --> 2346.70]  things in CSS and reordering and whatever, such that the underlying markup is nonsensical, uh,
[2347.20 --> 2354.74]  could I use ML to take a, you know, to look at both the document content, but also how it visually
[2354.74 --> 2359.92]  ends up laying out and do something smart to make it more readable via a screen reader?
[2359.92 --> 2364.72]  That would be cool. I mean, you know, even just looking at a page and saying, okay, here's the,
[2364.98 --> 2369.88]  here's the nav bar up top. These, this is what a webpage looks like, right? There's a sidebar over
[2369.88 --> 2375.42]  there and here's the content in the main stage. It's got a lot of text. Okay. You would take all
[2375.42 --> 2384.70]  that crap and basically just distill it and turn it into new markup and, and, and add the, the ARIA,
[2384.70 --> 2390.16]  attributes and, and that sort of thing, right? That'd be cool. It seems difficult, but I mean,
[2390.16 --> 2396.46]  it's certainly something you could, you could learn a, a, a, a, uh, you know, a model could learn
[2396.46 --> 2402.66]  from, from just looking at thousands of web pages. Oh yeah. So this is where the content is.
[2403.10 --> 2407.82]  I think that has interesting potential. I think that the biggest hangup that people have about
[2407.82 --> 2411.94]  trying to make the sites accessible is that when they hear that they can't a hundred percent fully
[2411.94 --> 2417.84]  automate the fixes or automate, you know, um, the testing and CI, that's when they feel really
[2417.84 --> 2422.46]  discouraged. And I think that part of that manual testing is literally stepping through things with
[2422.46 --> 2428.54]  a screen reader or literally tapping through things with like the tab key or even just, um,
[2429.14 --> 2436.44]  color contrast is, is testable. But, um, in some cases you can't always predict when colors of text
[2436.44 --> 2441.16]  and background colors are going to be overlaid on top of each other. So what I would like to see is
[2441.16 --> 2446.88]  those, those really, really slow manual testing things and the things that, um, require a human
[2446.88 --> 2451.86]  to really reason about, well, this, this doesn't have a hard and fast rule, but in this scenario,
[2451.86 --> 2456.94]  does it actually work for somebody? I think they're the kind of avenues I'd like to see ML exploring.
[2457.18 --> 2461.42]  I think we're definitely a way off. It sounds super difficult, but I do like that this discussion
[2461.42 --> 2467.44]  is happening for sure. There's also tremendous value. You coming back to our question of models
[2467.44 --> 2474.00]  and training in just the, the model interpretation in the browser. Um, I think one of the, the coolest
[2474.00 --> 2482.10]  things I've seen recently with TensorFlow JS, um, was this, these folks who did, uh, real time
[2482.10 --> 2490.18]  human pose estimation. So they're essentially, you're looking at a video and recognizing how people's
[2490.18 --> 2495.64]  limbs are, uh, sort of like a Microsoft connect type thing would do where it's like, okay, I move my
[2495.64 --> 2500.04]  limbs in this way and it recognizes where my hands are and all these different things. Uh, and that
[2500.04 --> 2504.52]  really got me thinking, you know, right now, if you want to do some sort of interactive game, uh,
[2504.52 --> 2510.00]  where you're moving stuff around, uh, you kind of have to have hardware for that. You've got something
[2510.00 --> 2515.32]  that's going to be scanning you. Uh, maybe you've got a wand or something like that. Um, we've been
[2515.32 --> 2520.04]  getting better and better at that, but what if you just went to a website and you were able to play
[2520.04 --> 2525.50]  these interactive games, maybe we could, you know, stream content between you and a friend,
[2525.50 --> 2531.10]  uh, bring for Austin and set it up with web RCC or something like that. Um, and suddenly you've got
[2531.10 --> 2539.54]  interactive physical games just using a webcam, uh, which to me, I was, I had that, like, that sounds
[2539.54 --> 2546.28]  exciting. That sounds like the type of thing where suddenly the web is, uh, making a whole class of
[2546.28 --> 2552.90]  things that used to require dedicated hardware accessible. I really love this. And this is,
[2552.96 --> 2557.12]  this is timed very well around Xbox releasing their accessible controller recently, where you
[2557.12 --> 2562.20]  can plug a myriad of different devices into their inputs. And then that kind of replaces more
[2562.20 --> 2567.84]  traditional controls on a controller. I really like that. What you just said there as a suggestion
[2567.84 --> 2572.26]  really reminds me of that progress being made too. Kevin, you have all the best ideas. We need to,
[2572.36 --> 2576.22]  we need to just get you in a room and then just build all the stuff that you come up with.
[2576.56 --> 2581.52]  I'm down, man. You get, you get me started and I'm, I love making stuff and figuring out
[2581.52 --> 2587.78]  possibilities. Like that's the part of, of coding that gets me excited. I am not a polish every
[2587.78 --> 2592.50]  piece and get everything down. I'm a prototype. And what are the possibilities we can open up with
[2592.50 --> 2596.64]  this? So if y'all want to hack with me and, and help me make that happen faster, the problem is I
[2596.64 --> 2600.12]  never have time, right? Like clients will pay a little bit for that and they'll mostly pay for it.
[2600.12 --> 2601.70]  You got to actually finish this application.
[2601.70 --> 2607.22]  All the actual hard work of polishing it and shipping it.
[2607.44 --> 2613.78]  Yeah. I'm, I'm like that too, but I just say, I, I, I just never finish anything. So it's just all,
[2613.86 --> 2618.80]  Oh, I have this great idea. I'm going to hack up a prototype. Oh wait, this was way too ambitious.
[2619.94 --> 2622.88]  I think I'll think of something else and move on to that.
[2622.88 --> 2627.32]  I'm such a pessimist that I actually shoot down my own ideas before I start coding. So in that,
[2627.50 --> 2631.26]  in that sense, I'll save myself the time of building the prototype. Of course,
[2631.28 --> 2632.70]  that's also the joyful part, isn't it?
[2632.76 --> 2638.30]  That's actually a great skill that I wish I had was, was the able, was to be, is to be able to
[2638.30 --> 2640.14]  shoot down my own ideas a little more quickly.
[2640.30 --> 2644.66]  I've found that for me, it's two different mental modes, right? Like, and I actually, I,
[2645.22 --> 2650.32]  you'd be surprised, but the one I had to learn was the, uh, the opening and the imagining one.
[2650.32 --> 2654.54]  I started out being exactly like Jared, where I would just shoot everything down. Oh, that can't
[2654.54 --> 2658.36]  work because of this. Like that can't work because of that. Uh, which, you know, when I was,
[2658.44 --> 2663.88]  I co-founded a startup and my co-founder was a big idea person and she would always have these ideas
[2663.88 --> 2669.96]  and she got so frustrated with me for shooting them down. Uh, and what I learned is really that
[2669.96 --> 2675.62]  was counterproductive shooting it down that early because we, as humans have different modes of our
[2675.62 --> 2682.86]  minds. And when you're in exploratory idea generation, yes, the first idea is not going
[2682.86 --> 2686.84]  to be feasible. And the second idea probably isn't either. And if you shoot it down there,
[2686.86 --> 2690.72]  you never get to the third, the fourth, the fifth, the sixth, the seventh, which is where magic happens
[2690.72 --> 2695.08]  and where you start to see, Oh wow, there's actually something real and cool and possible
[2695.08 --> 2699.96]  there. And so you kind of have to, to shift your mental state into, I am not in judging mode.
[2699.96 --> 2705.68]  I am in creating and imagining mode and then just go. So I find that judging mode actually helps
[2705.68 --> 2710.06]  creativity mode. So maybe you have one person operating in one sense and one in the other in
[2710.06 --> 2715.06]  terms of, of actually saying, okay, this won't work because of reasons X, Y, and Z. And so that,
[2715.24 --> 2719.60]  that forces creativity mode to say, okay, let me adjust this factor. So it's not like
[2719.60 --> 2725.94]  a wholesale throw it out. It's more like, this is why there's holes in this. And then that refines.
[2725.94 --> 2731.96]  So I could definitely see where sometimes you're able to, to give the, the, the way you do. Okay,
[2732.24 --> 2736.82]  but we could do it this way or, and we could do it this way. Cause the concern is if you shut people
[2736.82 --> 2740.58]  down, they don't want to keep creating. So yeah, I agree. Cause strengths are awesome,
[2740.58 --> 2745.28]  but it needs to be directing towards a positive energy. And most of the time I'm just talking about
[2745.28 --> 2749.66]  how I talk to myself. So it's like, I'm shutting myself down or I'm, you know, I'm refining my own
[2749.66 --> 2754.32]  thoughts as opposed to like a creative, you know, four people in a room type situation. But yeah,
[2754.32 --> 2756.20]  I'm definitely on the same page with you there.
[2756.50 --> 2760.22]  We should train a model with a successful and failed projects.
[2761.50 --> 2765.78]  And then you can type your ideas into it and it'll tell you whether or not you're, you're,
[2765.82 --> 2772.66]  you're, uh, Oh, it's like hot or not, but for, for, for ideas, you know, is this idea hot or is it not?
[2772.88 --> 2776.88]  I love how every, everything that we say ends with, we should train a model. And I'm over here.
[2776.88 --> 2780.32]  I've never trained a model in my entire life. And I'm over here like, let's just train a model.
[2780.32 --> 2787.06]  I wonder if you could though, feed every single startup, like, you know, their name and, and,
[2787.06 --> 2791.02]  and what, what, what went wrong? And then you could feed that reasoning.
[2791.44 --> 2795.38]  The problem is the what went wrong part is very difficult to put your finger on lots of times
[2795.38 --> 2796.40]  because there's so many things.
[2796.70 --> 2801.78]  Well, and it's an interesting problem because it's going to be tricky to identify the relevant
[2801.78 --> 2807.10]  features that you've got to put into that, right? Like this is essentially what VCs are trying to do.
[2807.10 --> 2810.86]  They pattern match, they look at successful and they look at failed and they try to pattern match
[2810.86 --> 2817.78]  to, to new ones. And there's an increasing amount of discussion around the fact that it is, uh,
[2817.78 --> 2823.58]  extremely flawed because at least we as humans will fixate on a lot of features that don't
[2824.18 --> 2828.74]  happen to matter that much. Like the, the famous one is people fixating on young white men who went
[2828.74 --> 2834.98]  to a Stanford or a Harvard or one of these places, but, uh, which turns out to be a self-fulfilling
[2834.98 --> 2838.20]  prophecy. If you give them all the money, you're going to get all the successes out of them.
[2838.60 --> 2843.44]  Uh, and they start with a lot of money usually. So that's, uh, you know, self-fulfilling and not
[2843.44 --> 2849.38]  actually a valid feature. Uh, so when we're thinking about how do we train our ML models here,
[2849.50 --> 2855.08]  one, you're going to have problems where you perpetuate existing bias. Uh, oh, we gave all the
[2855.08 --> 2859.22]  money to, you know, the young white men out of Stanford. And so those are all our success cases.
[2859.22 --> 2865.56]  And now our model says that's who we should give money to. And we perpetuate that existing bias,
[2865.56 --> 2873.38]  which is entirely, you know, based on bad history rather than, uh, actual value creation. Uh, but
[2873.38 --> 2878.68]  then the other piece is when we're feeding this data in like, what data do we even choose to put
[2878.68 --> 2884.08]  in there about these startups, right? Maybe that, you know, those failures were due to, you know,
[2884.12 --> 2889.10]  co-founder issues, which is an extremely common source of failure where you have folks who used
[2889.10 --> 2894.24]  to get along and suddenly don't. And it rips the company apart. Uh, maybe that one was caused by,
[2894.24 --> 2899.96]  um, somebody got hurt. Like, how do we know to put in all this seemingly extraneous data?
[2900.34 --> 2906.12]  And how do you factor in the, the, the macroeconomics of the industry in which they were
[2906.12 --> 2910.94]  operating in during the exact time that they were operating in, but this new situation is now
[2910.94 --> 2916.28]  completely different, right? It gets, it gets hairy. It's interesting thinking about the bias
[2916.28 --> 2921.20]  thing is definitely a problem, right? Like, um, machine learning, as we said, is like,
[2921.22 --> 2926.40]  you're giving them examples, right? So basically a model, a machine learning model is effectively
[2926.40 --> 2933.14]  a bag of bias, right? It's a model of bias because what you're, it's based on the people that put the
[2933.14 --> 2938.14]  data in. Right. And so how do we fight against, like, like you said, Kevin, that problem of selecting
[2938.14 --> 2944.48]  based on history or based on our own conscious or subconscious biases in order to have high quality
[2944.48 --> 2951.08]  answers and not just the answers that we fed it. Yeah. This was discussed in, in a lot of the talks
[2951.08 --> 2956.22]  at ML for all this week, which made me so, so happy. And I know that Paige Bailey has actually
[2956.22 --> 2962.64]  put together this guide. It's on her GitHub account. Um, she is dynamic web page, but spelled P A I G E,
[2962.64 --> 2969.14]  which is amazing. But, um, she put together, yes, so good. She put together a resource, which has a
[2969.14 --> 2974.28]  bunch of questions that you should ask yourself before you even start going down this track. You know,
[2974.28 --> 2979.76]  is my data going to be biased? How can I tell if it is? And where is my data coming from? Do I have
[2979.76 --> 2985.44]  the permission to use it? What are the possible, um, negative outcomes that can come out of this?
[2985.44 --> 2992.54]  Like what is even our goal in the first place? And I think that that was so cool to see that somebody
[2992.54 --> 2997.28]  is not just starting to ask these questions, but they're putting a framework together because one,
[2997.38 --> 3003.02]  um, one saying, and I'm trying to remember who actually said it was that some people say that
[3003.02 --> 3008.64]  machine learning, uh, you know, training data can be a mirror of the existing world that's out there.
[3008.64 --> 3015.28]  Um, but some people go as far as to say it's an amplification because if you're concentrating that
[3015.28 --> 3020.84]  data into something that can make such big decisions for you, that's amplification rather
[3020.84 --> 3026.10]  than just mirroring. That's true. Well, and a lot of folks give it additional weight. They say,
[3026.10 --> 3030.48]  oh, this is impartial because a machine did it, right? How could it be biased? It's a computer.
[3030.60 --> 3036.38]  It's not a person. Uh, there's a relatively famous example of that where folks started trying to use ML
[3036.38 --> 3041.98]  to guide sentencing outcomes. And they found, you know, they trained it on historic outcomes and they
[3041.98 --> 3047.72]  found shockingly that people of color were assigned larger sentences than everyone else,
[3047.72 --> 3052.82]  because historically we've had that bias in our justice system, but now suddenly it had the
[3052.82 --> 3056.54]  veneer of impartiality because it was coming from a machine.
[3057.24 --> 3063.38]  Well, maybe ML is, is like, like violence. If it doesn't work, you just add more data.
[3064.82 --> 3072.32]  You said it's an, it's, it's an amplification of, of, of what you choose to put in. And so the more
[3072.32 --> 3078.12]  you put in, you know, the less, the less, like the less amplified it becomes.
[3078.12 --> 3082.36]  That's going to depend on whether or not of what you're adding ends up just more and more
[3082.36 --> 3087.30]  of the same bias, I guess. I think that there's certain, there's certain collections of data in
[3087.30 --> 3092.78]  the world that are just not appropriate for us to use, given that even when they're cleaned up and
[3092.78 --> 3096.66]  everything, they're just really perpetuating the same things that we're trying to use machine
[3096.66 --> 3100.76]  learning to avoid. A lot of people want to use machine learning because they see a machine as
[3100.76 --> 3106.38]  unbiased. Um, but if we are directly influencing it with, with our, our own sort of results of that,
[3106.38 --> 3111.50]  especially like very long ranged historical data, that's, that's when we've really got to think,
[3111.78 --> 3114.82]  think twice about whether or not that was actually a good idea.
[3115.24 --> 3116.40]  That might be a good place to end.
[3116.70 --> 3118.48]  Yes. It got really serious.
[3119.38 --> 3124.30]  Hey, do y'all mind if I do a shameless, shameless plug, not for myself, but for sort of for myself.
[3124.30 --> 3129.58]  So if you like this topic, especially around the ethics and these implications in the future
[3129.58 --> 3137.94]  of AI, we have a brand new show in the works from changelog called practical AI. And it's with people
[3137.94 --> 3143.82]  who are deep in the space. Um, very well-knowledged, very well-knowledged, can speak much better than I
[3143.82 --> 3150.28]  can, uh, well-versed in AI and it's coming to you very, very soon. So head to changelog.com slash
[3150.28 --> 3155.00]  practical AI and subscribe. If you liked this conversation, you will love that show.
[3155.00 --> 3159.20]  I am very excited. I'm going to be someone who will be very attentively tuning in. Thank you so
[3159.20 --> 3163.82]  much for letting us know about that. So I wanted to thank everyone for listening to the show and
[3163.82 --> 3167.72]  we hope you enjoyed it. A special shout out to the people who listened to us on the live stream.
[3168.04 --> 3171.54]  This has been another episode of JS party and we will catch you next time.
[3174.16 --> 3180.04]  All right. Thank you for tuning into JS party this week. Tune in live on Thursdays at 1 PM US
[3180.04 --> 3185.12]  Eastern at changelog.com slash live. Join the community and Slack with us in real time during
[3185.12 --> 3190.18]  the shows. Head to changelog.com slash community and do us a favor, share this show with a friend
[3190.18 --> 3195.38]  where you don't have a podcast going to overcast and favorite it. And thank you to Fastly, our
[3195.38 --> 3200.02]  bandwidth partner. Head to fastly.com to learn more. And we move fast to fix things around here at
[3200.02 --> 3205.30]  changelog because of roll bar. Check them out at rollbar.com. We're hosted on Leno cloud servers
[3205.30 --> 3208.74]  at a Leno.com slash changelog. Check them out and support this show.
[3208.74 --> 3213.44]  Our music is produced by break master cylinder, and you can find more shows just like this
[3213.44 --> 3216.78]  at changelog.com. Thanks for tuning in. We'll see you next week.
