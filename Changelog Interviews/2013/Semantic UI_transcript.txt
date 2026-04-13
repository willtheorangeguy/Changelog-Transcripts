[0.00 --> 10.58]  Welcome back, everyone.
[10.70 --> 11.46]  This is The Change Log.
[11.56 --> 14.26]  Remember, support a blog, podcast, and weekly email that covers it fresh.
[14.94 --> 17.78]  And what's new in open source, check out the blog at thechangelog.com.
[17.86 --> 20.84]  Our past shows at 5by5.tv slash changelog.
[21.26 --> 22.64]  And subscribe to The Change Log Weekly.
[22.78 --> 24.54]  It's our weekly email we send out every Saturday,
[25.12 --> 26.80]  covering everything that hits our open source radar.
[27.00 --> 28.84]  Subscribe to thechangelog.com slash weekly.
[28.84 --> 32.26]  The show starts by myself, Adam Stachovic, as well as Andrew Thorpe.
[32.32 --> 32.84]  Andrew, say hello.
[33.46 --> 34.68]  Yo, yo, what's going on?
[34.86 --> 35.50]  What's going on, man?
[35.50 --> 37.04]  This is episode 106.
[37.14 --> 39.56]  We're joined by Jack Lukic.
[40.70 --> 43.96]  He's the creator of MyFaves and Semantic UI.
[44.54 --> 45.50]  So, Jack, welcome to the show.
[46.40 --> 47.14]  Thanks for having me.
[48.34 --> 50.04]  We do have a sponsor.
[50.12 --> 51.30]  I want to give them a quick shout-out.
[51.36 --> 54.34]  DigitalOcean, they're sponsoring us for the next few shows.
[54.52 --> 57.66]  They're really supporting open source, and they love what we're doing with the show.
[57.66 --> 63.06]  So, they've been sponsoring us for the past few shows and the next few shows as well.
[63.12 --> 69.26]  But they're a simple cloud hosting provider dedicated to offering the most intuitive way to spin up a cloud hosting server.
[69.58 --> 71.92]  You can create a cloud server in 55-second.
[72.28 --> 74.84]  Pricing plans start at $5 per month.
[75.36 --> 82.92]  Half a gig of RAM, 20 gigs of SSD drive space, one CPU to move your stuff around, and one terabyte of transfer.
[82.92 --> 90.60]  They feature a 99.9% uptime SLA, and they have data centers here in the U.S., in New York, San Francisco, as well as abroad, and Amsterdam.
[91.16 --> 95.96]  We have a $10 promo when you enter your credit card info when buying the service.
[96.10 --> 97.16]  There's a promo code filled there.
[97.22 --> 101.96]  Use the coupon code THECHANGELOG104 to use our $10 promo.
[102.16 --> 105.32]  Check them out at digitalocean.com, and thank you so much for your support.
[106.12 --> 107.04]  Jack, how are you?
[107.52 --> 108.20]  I'm doing great.
[108.20 --> 116.34]  Why don't you kind of give us a little introduction to who you are, Jack, what you're doing, and how to correctly say your last name.
[116.72 --> 116.86]  Yes.
[118.56 --> 120.58]  So, I'm a front-end developer.
[121.32 --> 121.92]  No, you did good.
[122.18 --> 122.46]  Okay.
[122.82 --> 123.26]  Make it sure.
[125.00 --> 125.66]  So, yeah.
[126.54 --> 130.00]  I've been doing front-end dev for about eight years.
[130.00 --> 140.84]  I originally started off working sort of in advertising in San Francisco, doing stuff at design agencies just to build pedigree or whatever.
[140.96 --> 144.04]  I worked on the official redesign of Hyundai.com.
[144.52 --> 148.06]  I did Cheetos.com, 3AA, specialized, stuff like that.
[148.16 --> 152.14]  A lot of quick projects and all ad agency-based.
[152.14 --> 157.48]  And then I moved to New York, and I kind of wanted to restart, so I started working at a startup called Quirky.
[158.04 --> 159.52]  They're a social invention company.
[160.12 --> 170.40]  Basically, what they do is people submit ideas for consumer products on their website, and then we choose the best ones, make it into real products, do all the manufacturing, design, engineer.
[172.12 --> 174.16]  And so that was about two years ago.
[174.16 --> 179.34]  So, I was employee number like 45, I guess.
[180.08 --> 184.94]  And then in the last year and a half, two years, they've gotten up to 150 employees.
[185.68 --> 188.80]  So, I was, I guess, mid-stage hire.
[189.88 --> 191.48]  I was the first front-end developer, though.
[192.00 --> 199.46]  And I was sort of tasked with figuring out how to organize and sort of redo the front-end for this massive website.
[199.46 --> 208.52]  So, I spent some time sort of going through all the components I've written for previous projects and sort of figuring out what worked and what didn't.
[209.30 --> 214.86]  And also sort of working on redefining the visual language, so the UI elements, all that kind of stuff.
[215.68 --> 220.34]  And I sort of developed a component format, which I started to write components for.
[220.34 --> 230.34]  And over about a year or so of doing that, I noticed I was starting to get a pretty big library of components.
[231.44 --> 238.68]  And so, I tried to sort of look at them in a manner where they could all sort of fit into a larger picture.
[238.68 --> 255.10]  So, instead of it being one-off things, like in what way should I think about the language of the HTML, the class name, the structures, so that if anyone picked up any one piece of this, they would obviously understand that it's part of a larger framework.
[256.20 --> 259.88]  And so, I sort of looked at a bunch of different directions.
[261.80 --> 264.26]  And there's a lot more to get into about this.
[264.52 --> 267.04]  You mentioned some sort of background theory around this, too.
[267.60 --> 268.00]  Right.
[268.00 --> 270.22]  So, I'm really interested in linguistics.
[271.10 --> 274.02]  So, semantic UI refers to semiotics, which is the study of meaning.
[275.00 --> 276.00]  Semantic has sort of been…
[276.56 --> 277.54]  Thrown around pretty badly.
[278.00 --> 278.18]  Yeah.
[278.34 --> 283.38]  It's been misappropriated, in my opinion, in that it means sort of adherence to W3 spec now.
[283.64 --> 283.92]  Right.
[284.06 --> 285.50]  So, a little theory.
[286.72 --> 291.36]  Originally, the study of language was sort of based on this belief that there were prescribed ideals about language.
[291.80 --> 293.94]  So, you have good language and bad language.
[293.94 --> 301.76]  And the only way to preserve a correct language was to create sort of a central standards body organization that says, you know, oh, this word's allowed.
[301.96 --> 302.90]  This word isn't allowed.
[303.36 --> 309.84]  So, you have things like the Merriam-Webster Dictionary saying, this year we're accepting these 30 new words in, but no other words because they're not English.
[309.84 --> 315.72]  And then you have, you know, the French saying, let's create a government organization called the Académie Française.
[315.72 --> 317.62]  Sorry, I'm saying this terribly.
[318.34 --> 323.48]  Who basically says, let's preserve the French language and make it as French as possible.
[323.64 --> 327.44]  So, the English sounding word for French shouldn't be allowed and so on.
[328.18 --> 330.18]  And so, this is sort of called prescriptivism.
[330.32 --> 331.50]  It's prescriptive linguistics.
[331.62 --> 336.66]  This idea that you need to preserve the good features of language and toss out the bad ones.
[336.66 --> 342.40]  And you're sort of working towards this ideal of what, you know, the perfect language is or something like that.
[342.70 --> 346.96]  Then the 20th century happened and a lot of crazy movements started coming around.
[347.12 --> 352.80]  You know, you have postmodernism and art and this sort of reinterpretation of meaning.
[352.80 --> 370.30]  So, in linguistics, sort of what that meant was that all these old practices of saying, you know, this is what language should be like, were sort of replaced by this new practice, which is called descriptive linguistics, which is let's just look at the language and see what words people are using.
[371.30 --> 376.30]  And if it becomes used across a large group of people, then it's a figure of the language.
[376.30 --> 387.74]  So, this is a fundamental shift and it sort of got rid of all these like creaky old things from language because all of a sudden we're saying, you know, languages is evolving faster than we can keep track of it.
[388.44 --> 389.78]  Why are we slowing it down?
[391.14 --> 393.00]  And so, how does this relate to program languages?
[393.06 --> 393.72]  I was about to ask you.
[394.12 --> 395.40]  How's this going to be sent to you?
[396.02 --> 397.64]  Thanks for the background for sure though.
[398.18 --> 404.98]  So, program languages are like other languages except for they're made for computers.
[404.98 --> 405.92]  And so, what are computers?
[405.92 --> 412.04]  There's these, you know, big ones and zero processors that, you know, can only understand a very primitive language.
[412.46 --> 426.42]  So, what you had originally was in academic institutions, a small group of people who were very, very smart and figured out ways that we could type in sort of almost English words into a screen that would be interpreted into these ones and zeros.
[426.88 --> 430.62]  So, what you have is very similar to the Academy of Franceses or Merriam-Webster's.
[430.92 --> 433.94]  Like, here's the small dictionary of what language should be.
[433.94 --> 437.26]  And it was sort of the only way to do things.
[438.14 --> 443.32]  So, most program languages evolved out of this tradition of prescriptive linguistics.
[443.90 --> 445.64]  And that's because they're instruction-based.
[445.96 --> 447.42]  You're saying do this and do this.
[447.66 --> 454.42]  And English is good at saying things like there are three tall men in the room, but it's really terrible at saying, hey, look at how this watch works.
[454.42 --> 458.56]  And program languages were doing these things about saying, you know, here's a very complex behavior.
[458.68 --> 460.82]  Let's describe it in terms that a computer can understand.
[460.82 --> 467.30]  So, my thought, my theory is that front-end development is different than programming.
[467.84 --> 474.78]  Front-end development is a describing of virtual scenes in a way almost like what natural language does.
[475.10 --> 477.02]  It says there's these things on a page.
[478.02 --> 478.82]  What are they?
[479.06 --> 479.94]  How should they look?
[479.94 --> 483.66]  And I don't think programming languages are particularly good at solving that problem.
[483.66 --> 498.28]  I think natural languages have all these sort of figures which have evolved out, like plurality, the use of verbs, direct objects, these kind of things, which allow for very concise expressions of physical scenes.
[498.28 --> 515.28]  So, in semantic, what I'm trying to do is take some of these figures from natural language, like plurality, the idea of commonality between groups of things and the use of verbs for describing behavior, and port it over to front-end development.
[515.84 --> 517.54]  So, it's a huge departure.
[517.92 --> 526.82]  It's kind of iconoclostic, and I don't know if you read the Hacker News article, but it seems to be taking up – people are taking up sides on the issue.
[526.82 --> 540.02]  So, this is – so, semantic UI kind of came out of your desire to – would you say that you kind of want to be the standard for linguistics around the front-end of stuff like that?
[540.08 --> 541.58]  I mean, is that kind of the goal of this project?
[542.22 --> 549.94]  I think it's not – and the thing is, is like whenever you talk about a standards organization, it's going back almost to like Merriam-Webster or something like that.
[549.94 --> 554.30]  The way I think about user interface – so, you look at something like flat design.
[554.30 --> 569.64]  What flat design is saying is that we used to have angel fire websites with massive fire GIFs and under construction signs, but now the language has evolved so that it's a very small subset of things that are allowed or appropriate for signaling design cues.
[569.64 --> 585.16]  So, my idea is that the language has gotten small enough that someone can look at a bunch of websites, go to angellist.co and just click around every startup, and just come up with a list of maybe 50 or so design elements.
[585.16 --> 590.34]  And so, what I'm trying to do is sort of describe how people use design elsewhere.
[590.86 --> 595.30]  And so, it has to be constantly evolving, and it will change as it's being used.
[595.64 --> 602.54]  And the things that don't work should disappear from the library, and the things that come into play, if there's a new design trope that doesn't exist, it should be added.
[602.54 --> 614.60]  And I'm hoping to sort of make this a community effort so that it – like the problem with having one person in charge of a front-end library like this is that, obviously, like I would like to be objective, but I'm just one view on language.
[614.60 --> 622.08]  Ideally, there would be a group of core contributors who are all looking around at the web saying, hey, we don't have a button that can do this.
[622.20 --> 629.36]  Or, hey, haven't you seen this cool thing like on New York Times when you get to the bottom of an article, it says, read this article afterwards in the corner.
[629.84 --> 632.34]  And that's an interesting design trope, and a lot of sites are using it now.
[633.20 --> 636.52]  So, yeah, it's more about describing what exists out there.
[636.52 --> 645.92]  Gotcha. So you're obviously very interested in the theory behind all this, and it's not just another bootstrap or something like that.
[646.06 --> 652.50]  But why don't we kind of rein it back a little bit and give us the high-level description.
[652.68 --> 653.88]  What is Semantic UI?
[654.66 --> 661.88]  Semantic UI is a set of individual components which can be used individually or without subscribing to the framework.
[661.88 --> 665.42]  So you can say only use a button or only use a menu class or something like that.
[665.42 --> 668.68]  And each of them is a visual design trope.
[668.68 --> 671.42]  And the goal is sort of to create a visual definition.
[671.92 --> 680.10]  So it's a list of things that it can do on the page, ways it can vary, different types of that element, and states that it can exist in.
[680.10 --> 686.64]  So, like, for example, if you have a button, you would say a button can change color.
[686.78 --> 687.70]  It can be different sizes.
[688.38 --> 692.06]  It might exist in a group of buttons, so there's a concept of plurality.
[692.78 --> 694.22]  It might have different types.
[694.22 --> 699.76]  So the standard is sort of very rigorous about how this works.
[699.98 --> 709.10]  So, like, a button is a homogenous element in the sense that, like, a form or something where there's a variety of different elements that exist together.
[709.56 --> 711.32]  A button is just sort of one thing.
[711.40 --> 712.60]  It can exist in plural groups.
[712.60 --> 722.60]  So there's sort of five UI definition types I've created sort of describing ways to define these different design tropes.
[723.36 --> 724.92]  Sorry, this is getting a little bit long-winded.
[725.28 --> 727.96]  It's actually a fairly complex thing.
[728.24 --> 733.90]  So it's very hard for me to, like, figure out how to share in a podcast format.
[733.90 --> 734.34]  Right.
[734.78 --> 743.28]  So would you say, though, let's kind of, I guess, try and kind of dig into it a little bit, like, you know, where we could easy, where it would be easy for laymen like myself to understand.
[743.66 --> 750.00]  Would you say that Semantic UI is a competitor to those, like, you know, frameworks like Bootstrap and Foundation?
[750.00 --> 751.94]  Would you say that it can be used alongside?
[751.94 --> 753.90]  Or how would it relate to those?
[754.44 --> 754.86]  Absolutely.
[755.82 --> 769.18]  So for people who are, like, looking for, on GitHub, just, like, searching for, like, a new modal or searching for a new pop-up, it offers sort of all of those components.
[769.78 --> 775.96]  So people who just need sort of one-off elements can go to Semantic and say, let's check out your pop-up.
[775.96 --> 785.62]  And also for people who want to sort of take on the whole thing, you can have a website that looks linguistically semantic by using, you know, all these components together.
[786.30 --> 794.86]  So I don't know if you've checked out the code samples, but the desire is sort of to have the class names read like English language.
[795.34 --> 802.16]  So you have sort of nouns, which are UI elements, and then adjectives, which sort of modify them.
[802.76 --> 804.06]  There's two types of adjectives.
[804.06 --> 807.12]  There's something which sort of says this is a type of an element.
[807.32 --> 814.62]  So this is – if it's an icon button, it can't also be an icon button and a labeled icon button.
[814.74 --> 815.88]  They're sort of mutually exclusive.
[816.54 --> 817.20]  That's one type.
[818.02 --> 823.06]  And then the other half of that is called a variation in Semantic UI.
[823.44 --> 830.96]  And what a variation is is saying here's a change to the element that can also exist harmoniously with other changes.
[830.96 --> 836.14]  So you can have a large button, but if large is used in the context of red, you have a large red button.
[836.66 --> 841.44]  If large and red are used in context of an icon, then it's a large red icon button and so on.
[841.44 --> 848.84]  So it sort of gives these features in a way that it's like a palette.
[849.00 --> 853.10]  So someone can choose, do I want to use this feature of the library or that?
[853.60 --> 865.50]  And not necessarily are required to use a button that looks like this is a very heavy-handed design button that was what the framework decided.
[865.50 --> 869.40]  So there obviously is a learning curve when you're using this project.
[869.96 --> 876.02]  And it seems like to me it's the kind of thing where if you buy into it and you decide I'm going to invest a little bit of time.
[876.20 --> 880.00]  I mean I went through the guides and it starts to kind of get clear as you go through the guides.
[880.08 --> 881.04]  So it's not a ton of time.
[881.12 --> 889.00]  But if you invest a little bit of time into this, then the goal is to kind of – you get things from this like – that you get from other projects, right?
[889.00 --> 895.54]  Like you have a grid and you have elements and you have features like modals and accordions and stuff like that.
[895.88 --> 910.80]  But then what it takes a step further is it's trying to kind of bridge the gap between designers, front-end developers, and back-end developers by making the language something that you're already familiar with, which is a structured language instead of just a bunch of random classes all over the place.
[910.90 --> 911.20]  Is that right?
[911.84 --> 912.48]  Right, completely.
[912.48 --> 918.38]  And aside from everything I said today, which you can probably tell I get really excited about talking about.
[919.02 --> 919.48]  We can tell.
[921.22 --> 922.08]  That's cool though.
[922.50 --> 926.66]  I'm a programmer, so at the end of the day, all the things that I like about programming are in there.
[927.56 --> 935.54]  There's – in the JavaScript modules, every component has a trace that gives performance data as the modules function.
[935.54 --> 949.18]  So instead of having inline comments inside of the JavaScript that just sort of is there for other developers, the idea is that each of those places where I would put a comment, instead there's a trace call.
[949.64 --> 955.12]  And that call sort of tracks how long it was before that statement and the previous statement and things like that.
[955.12 --> 965.70]  So you can sort of see the flow through the JavaScript, what functions it hits, what arguments are called to each function, and how many milliseconds it took to execute.
[966.12 --> 975.16]  So you get all this trace in a Firebug console or in a Chrome console, and it's sort of presented in a grouped structured layout.
[975.30 --> 981.58]  So you can sort by milliseconds execution or whatever you feel like.
[981.58 --> 983.42]  So that's one feature.
[987.22 --> 989.24]  Yeah, also everything's namespace.
[989.64 --> 998.66]  So CSS, basically if you choose a button class, you can still use the word button anywhere else, only when you use a UI button.
[999.12 --> 999.32]  Yeah.
[999.74 --> 1008.62]  And so all of the other – what seem like free-floating classes, which you might have something like a right-floated menu inside of another menu.
[1008.62 --> 1014.04]  So the word right-floated is only defined in the context of a UI menu.
[1014.58 --> 1016.90]  So none of those classes are actually free-floating.
[1017.02 --> 1018.98]  None of them are sort of including namespace.
[1019.84 --> 1023.96]  And so that's a neat little design thing that it has going on.
[1023.96 --> 1030.62]  If you look at kind of a lot of the projects out there that are similar, it's interesting.
[1030.72 --> 1032.26]  Every single one of them has like a modal.
[1032.48 --> 1046.54]  Every single one of them has – not every one of them, a lot of them have like custom form elements like checkboxes and how you make those better looking and constant across different devices and reveals and stuff like that.
[1046.54 --> 1049.86]  But Semantic UI has some unique ones, right?
[1049.98 --> 1055.66]  And so you kind of alluded to this before, like the rating element that you – or the rating module that you have in Semantic UI.
[1055.84 --> 1056.44]  That's different.
[1056.56 --> 1058.80]  That's not something that you're going to get with all of these.
[1059.32 --> 1069.66]  And so it's because the mindset is a little different where like if you find, as you said, tropes that are common all over the place that people want, you're going to implement that.
[1069.66 --> 1076.12]  It's not based on like your own view of what a framework should have.
[1076.20 --> 1079.80]  It's based on like, hey, people want this, so we should support that, right?
[1080.34 --> 1080.50]  Yeah.
[1080.68 --> 1082.70]  Hopefully I should have no say in how the library evolves.
[1082.80 --> 1087.10]  It should just be based on what's used in the design world.
[1088.12 --> 1088.30]  Yeah.
[1088.48 --> 1095.06]  So how does that – so right now – so you said ideally it wouldn't be one person making all these decisions.
[1095.06 --> 1099.50]  So right now do you have other people that are like core contributors to this project or is it just you?
[1100.38 --> 1103.60]  Well, I have – so a little bit of background on the project.
[1104.36 --> 1110.60]  I wasn't ready sort of to release this, but then all of a sudden someone found it on the internet and put it on Hacker News.
[1111.14 --> 1114.80]  And so all of a sudden I was like, shit, what is this doing on Hacker News?
[1114.80 --> 1128.80]  I was getting all this traffic and I had to create these semantic versioning and all this stuff so that it would be ready for people to consume and power components, all this stuff.
[1129.66 --> 1134.34]  So a lot of this stuff has just been figured out in the last two weeks or so.
[1135.72 --> 1138.92]  I created – there's this project management software called Trello.
[1139.24 --> 1144.48]  I've created Trello boards which are open to the public where people can submit ideas for new types of interface elements.
[1144.48 --> 1148.00]  People are also submitting ideas for that in GitHub issues.
[1149.00 --> 1153.96]  The idea being that you post on the public board, it gets voted up, then it gets added to the roadmap.
[1154.60 --> 1165.06]  The roadmap – hopefully there will be a team of core contributors who will pick out each individual component and own it and say, you know, I really like working on a cart view.
[1165.06 --> 1167.62]  So like it's an interesting design trope.
[1167.74 --> 1168.60]  It's all over the web.
[1168.88 --> 1170.96]  What are all the components that make up a shopping cart?
[1171.72 --> 1175.74]  And then that person will be tasked off and, you know, go to town.
[1177.38 --> 1189.24]  But at this point, you know, I've – it's one of those things where I feel like I have to fill in the full picture before I will get too many core contributors just because it's so nascent.
[1189.24 --> 1197.84]  But I'm hoping – I'm crossing my fingers every day that someone will, you know, come on and GitHub issues and really take ownership over some, you know, part of the project.
[1199.16 --> 1199.56]  Right.
[1199.82 --> 1201.90]  It's a really cool – I mean, it's different.
[1202.14 --> 1209.78]  And that's kind of what you get from the beginning is you look at it and you're like, okay, this is similar to other things that I've seen, but it's different.
[1209.94 --> 1211.48]  This is – there's something to this.
[1211.48 --> 1218.76]  And I have a feeling that the challenge for you is going to be, you know, those UI modules right now, you have 12 of them.
[1219.28 --> 1220.98]  And, you know, you have 11 elements.
[1221.06 --> 1224.62]  It seems like the elements might be kind of standard and not grow too much.
[1224.66 --> 1229.76]  But you can see those modules could potentially get kind of crazy, right, like – and get out of control.
[1229.76 --> 1249.40]  So I think the challenge is going to be how to keep that from getting out of control and how to, you know, prevent it from just somebody being like, I want to be able to support, you know, a marquee scrolling, you know, like getting too precise with what the modules are, right, and keeping it so that it's still like a, you know, minimal viable product.
[1249.40 --> 1251.62]  But it supports kind of everything.
[1252.18 --> 1253.94]  I definitely think that's going to be the challenge.
[1253.94 --> 1259.96]  Do you kind of have any, like, standards that you would adhere to to kind of help that?
[1260.96 --> 1269.90]  Yeah, my thought with Semantic is that unlike Bootstrap where, you know, you might just grab the whole thing and just put it in the head tag of your page and then you're done.
[1270.26 --> 1274.38]  I'm hoping it's more like a buffet where, like, if you're eating everything at the buffet, then you're, like, doing it wrong.
[1274.52 --> 1277.16]  You've got to, like, pick the things that work for you.
[1278.16 --> 1281.58]  That's the biggest thing that drives me crazy about Bootstrap and Foundations.
[1281.58 --> 1288.78]  Sometimes I just want certain pieces and it's just not quite as easy to, like you said, just buffet it.
[1289.20 --> 1289.34]  Yeah.
[1289.90 --> 1291.66]  So, like, Foundation supports that.
[1291.80 --> 1299.66]  I think it's a little bit clunky to, you know, figure it out too easily in their documentation, especially if you're using it in, say, like a Rails project or something like that.
[1299.74 --> 1303.72]  But how do you handle that as Semantic UI?
[1303.72 --> 1308.00]  Like, how do you – is there documentation?
[1308.30 --> 1313.34]  Is there instructions on how you can only pick and choose pieces you want and, you know, not need all the JavaScript for everything and stuff?
[1313.92 --> 1320.22]  Yeah, that's part of switching from pre-release version to full release is that there's no build tools right now.
[1320.52 --> 1320.76]  Right.
[1320.76 --> 1322.30]  So that's the first thing I'm working on.
[1322.72 --> 1328.18]  One reason behind that is that, like, I chose less, but I wasn't really sure at the time.
[1328.60 --> 1333.04]  Like, I think that CSS preprocessors are sort of, like, in their infancy right now.
[1333.50 --> 1340.76]  Like, it's kind of interesting because, like, you have all these really highly evolved templating languages that, you know, like people have been using handlebars for a while.
[1340.88 --> 1342.70]  People have been using all this stuff.
[1342.76 --> 1343.82]  And it's basically the same thing.
[1343.88 --> 1347.30]  It's processing a text file, which is a CSS file, and outputting a different file.
[1347.30 --> 1354.32]  But people got really excited because it has these extra built-ins that say I can also lighten a hex code color or something like that.
[1354.96 --> 1360.90]  So I'm just a bit worried that less is missing some of the features that would be useful for doing everything we want to do.
[1361.42 --> 1363.70]  So, like, there's no loops in less, for instance.
[1364.08 --> 1372.02]  So, like, having people choose a color palette and then having it define color rules based on the palette and the name chosen for the palette, it's, like, it's more difficult.
[1372.14 --> 1374.24]  Although there are hacks out there that let you do loops.
[1374.24 --> 1383.22]  So I guess what I'm trying to do is sort of figure out, like, I don't want to, you know, prescribe to, like, too many of these iconoclastic libraries.
[1383.34 --> 1386.28]  Like, a lot of people have talked about, like, adding Angular wrappers.
[1386.88 --> 1391.80]  And, you know, it always makes sense to me as, like, maybe a third-party contribution in a separate repo.
[1392.04 --> 1395.94]  But I really don't want to say, like, this is what you have to use to develop a website.
[1396.38 --> 1399.06]  Although, you know, there is that jQuery thing, which is hard to get rid of.
[1400.44 --> 1403.84]  Well, there's Zepto, right, which is, like, seems like it's growing into jQuery.
[1403.84 --> 1407.20]  Like, the goal is to be smaller, but it kind of seems like it's continuing to grow.
[1408.22 --> 1418.20]  Yeah, and another unique thing about semantic is that there's also this concept of, like, a UI view, which is, like, a trope about how to present data.
[1419.14 --> 1420.90]  Are you scratching something over there, Jack?
[1421.74 --> 1422.74]  Oh, no, sorry.
[1423.02 --> 1423.96]  Yeah, I get careful.
[1424.86 --> 1427.50]  Hopefully the listeners are like, ah, I like Jack a lot.
[1427.62 --> 1428.36]  This is really awesome.
[1429.26 --> 1429.96]  I'm just kidding.
[1430.04 --> 1430.44]  Go ahead.
[1430.44 --> 1439.92]  So things like having a feed of comments under a news article or having an activity feed, like a Facebook activity feed.
[1440.08 --> 1444.36]  These have also become, like, web tropes, but none of the other libraries have really addressed that yet.
[1445.08 --> 1445.56]  And that's right.
[1445.60 --> 1448.00]  You got comment, you got feed, you got item, and you got list.
[1448.62 --> 1449.42]  Yeah, it's a small list.
[1449.50 --> 1453.34]  And I liked the idea of feed, and I also liked just the idea of some of the other things you've got in there as well.
[1453.34 --> 1455.82]  But this was pretty neat to see as part of this.
[1456.96 --> 1457.58]  Yeah, thanks.
[1459.08 --> 1462.00]  Again, this has sort of been, like, I'm one person.
[1462.10 --> 1463.10]  I can only code so much.
[1463.62 --> 1464.72]  And I've been, like, coding, like, crazy on this.
[1464.72 --> 1467.22]  Well, that's why you come on the show, so you can let people know about it.
[1467.84 --> 1468.66]  Yeah, please come.
[1468.66 --> 1471.04]  And here in a minute, we'll tell you about the call to arms and stuff like that.
[1471.36 --> 1476.60]  But so you were talking a bit about less.
[1476.60 --> 1480.24]  It sounds like you might be on the fence in terms of you're just not sure.
[1481.16 --> 1484.92]  I guess I just have to commit because, like, these build tools need to be made.
[1486.02 --> 1491.96]  And it's very easy to sit on the fence and say I don't really want to choose a side because, you know, none of them are perfect.
[1492.34 --> 1493.64]  But nothing is ever, I guess.
[1494.98 --> 1505.02]  So I guess talking about choices then, I guess in terms of the fan that you are of linguistics and the semantics and the things we talked about a little bit earlier in the show,
[1505.02 --> 1514.82]  a lot of people who write SAS, write CSS, have subscribed to Jonathan Snook's way of doing SMACs.
[1515.04 --> 1518.38]  There's a couple others like RAM, I believe, or B-E-M, BAM.
[1518.44 --> 1519.56]  I'm not sure how you pronounce that.
[1519.84 --> 1526.52]  There's, like, three or four different popular methods that kind of all revolve around state, variation.
[1526.68 --> 1529.54]  A lot of the things you're subscribing to here where you have types, content, variations.
[1530.40 --> 1531.62]  How do you apply to that?
[1531.62 --> 1535.64]  I honestly think they're just getting some of the fundamental features wrong.
[1536.16 --> 1542.88]  I think that in language we have this concept of words, which are individual classes of things in the world.
[1543.74 --> 1548.14]  But in CSS what we always have is these dashed words where it's, like, BTN-active.
[1548.86 --> 1551.18]  And it's because I think those are separate concepts.
[1551.38 --> 1553.20]  They're describing completely different things.
[1553.46 --> 1555.16]  You have something that's active and something that's a button.
[1555.50 --> 1560.26]  If you want to describe it as both being a button and active, you need to describe the intersection of those two concepts.
[1560.26 --> 1572.52]  But creating a separate concept, which you define as a dashed word and then has a special definition, is missing the best feature of language, which is, you know, you can define each of these things individually and together you can define the differences.
[1573.26 --> 1575.30]  So that's sort of what it's doing differently.
[1575.30 --> 1582.26]  You say on your homepage, I guess kind of keying off of that is lose the hieroglyphics.
[1583.04 --> 1583.40]  Exactly.
[1583.74 --> 1584.04]  You know?
[1584.74 --> 1585.10]  Exactly.
[1585.98 --> 1593.22]  And I think one of the scariest things of being a front-end developer is, like, you take on a freelance project and you're like, what is this code base going to be written in?
[1593.42 --> 1593.82]  Right.
[1593.82 --> 1598.86]  And you're like, who is this developer who decided this should all be camel case and this should be whatever?
[1599.28 --> 1605.92]  And I don't think anyone can argue that words that look like English words are particularly confusing for someone to grok if they're picking a project.
[1606.38 --> 1609.26]  I wonder if, like, and it kind of just clicked.
[1609.46 --> 1616.50]  Like when, you know, you're looking at, I don't know, and I don't know if this is my own, you know, problem or maybe something on the homepage.
[1616.50 --> 1624.62]  But when I'm looking at the homepage of Semantic UI and I see the Semantic version on the left and the Bootstrap version on the right, I'm like, I don't, I mean, I don't know.
[1625.40 --> 1632.98]  Both of these seem pretty, like, easy to understand to me because, you know, I've been using Foundation for so long and I use Bootstrap.
[1633.12 --> 1634.10]  And these all make sense to me.
[1634.14 --> 1634.98]  I've seen this so much.
[1635.08 --> 1644.22]  But I think that you hit on something right there that maybe really could shine some clarity on what this is.
[1644.22 --> 1649.18]  I don't know if this makes sense to be on the homepage, but you talked about that if you want.
[1649.32 --> 1653.22]  So on the Semantic version on the left, let's just take the first example, for instance.
[1653.36 --> 1655.70]  You have a, this is all separate words.
[1655.80 --> 1659.78]  You have a three-column grid, and then inside of that you have three columns.
[1660.66 --> 1666.12]  And on the Bootstrap version you have a row, and inside of that you have col-lg-4.
[1666.12 --> 1677.22]  And it takes me, I have to assume at this point now that this is like a 12-column grid, that these are three different columns, and that each one of them is large.
[1677.32 --> 1678.70]  I'm assuming LG is large.
[1679.40 --> 1688.32]  And so that's kind of what you just mentioned was, like, they created the hyphenated version of, like, all these different things that come together to make this one element.
[1688.32 --> 1698.30]  And I think that maybe the hard part is, like, this is great for a, you know, maybe a designer.
[1698.48 --> 1700.54]  Maybe, I'm not a front-end developer, they've used it.
[1700.56 --> 1704.48]  This is great for, like, a designer or somebody that just wants to get in and maybe just, like, tinker.
[1704.70 --> 1709.04]  But the learning curve is almost from the other side now.
[1709.04 --> 1718.36]  Like, the back-end, front-end developers that are familiar with col-lg-4 are going to have to kind of wrap their minds around this English way of using it, right?
[1718.48 --> 1723.18]  I mean, the more appropriate way of using it and maybe have a little bit of learn to do there.
[1723.28 --> 1727.78]  But they're the people who are capable of learning programming languages and of learning, you know what I mean?
[1727.86 --> 1730.94]  Like, those are the people that should be learning this, not the other way around.
[1731.28 --> 1732.62]  Yeah, you hit the nail on the head.
[1732.74 --> 1735.00]  There's actually something else I totally forgot to talk about.
[1735.00 --> 1739.98]  But the other thing that sort of inspired me to do this project was I was really excited about Code Academy.
[1740.12 --> 1741.30]  I was really excited about Khan Academy.
[1741.82 --> 1745.66]  I was really excited about all these things where people are trying to make programming more accessible.
[1746.52 --> 1748.48]  And I think they're doing great things.
[1748.48 --> 1755.80]  They're making, you know, easy-to-consume lessons that are fun, that make learning easier.
[1756.22 --> 1764.02]  But I think there's also a separate way you can attack that problem, which is to make the actual languages themselves more easier to adopt.
[1764.02 --> 1772.48]  And I think the best way to do that is to get rid of all the assumptions that us as developers have grown to, you know, adopt.
[1772.68 --> 1777.80]  Like, for instance, in the first Bootstrap example, like you look at call-lg-4.
[1778.30 --> 1784.28]  One, you have to understand that Bootstrap works off a 12-column grid, which how would you know that unless you knew Bootstrap?
[1784.60 --> 1786.92]  Two, how would you know what LG stands for?
[1787.00 --> 1788.22]  Could it be the columns large?
[1788.34 --> 1790.20]  Is it only showing on large screens?
[1790.46 --> 1791.28]  Which it is.
[1792.20 --> 1793.30]  But how would you know that?
[1794.26 --> 1801.70]  And then three, it's like, so there's a row and a column, but how does that fit into this larger picture of, like, how does the row relate to the column?
[1802.76 --> 1807.52]  What is – how is this coordinated together as a group or, you know, a whole thing?
[1808.02 --> 1814.16]  So that's a lot of what I'm trying to solve is that mostly what it is is just stealing things from language.
[1814.16 --> 1822.96]  Like, all these concepts are, like, are things that have existed for thousands of years that were, like – another thing in terms of language is, like, it's a highly evolved system.
[1823.36 --> 1824.50]  Like, we're cognitivisers.
[1824.62 --> 1831.44]  We're constantly deciding to make language more concise but while optimizing for comprehension.
[1831.44 --> 1844.24]  So what we have is we're stealing knowledge from, you know, 100,000 years of evolution of a system and just taking those concepts and applying it to an already existing system, which is this front-end development.
[1844.24 --> 1844.88]  So –
[1844.88 --> 1845.08]  Right.
[1845.16 --> 1854.18]  I mean, it's interesting because if I've never – let's say I'm a developer I've never used – or just say I'm just somebody, developer maybe not, that's never used Bootstrap.
[1854.26 --> 1858.54]  If I look at this, I'm either going to make assumptions or I'm going to go read Bootstrap's documentation.
[1858.54 --> 1866.64]  And I think that it's funny because as a developer, somebody that, like, I love going in, you know, RTFM, right?
[1866.66 --> 1869.32]  I love going and reading documentation and figuring out what's going on.
[1869.40 --> 1879.74]  But people that haven't kind of, like, transformed their mind into that way of thinking don't even necessarily know that documentation exists for everything.
[1880.32 --> 1880.88]  You know what I mean?
[1881.02 --> 1881.12]  Yeah.
[1881.12 --> 1887.90]  So they would look at this and be like, I don't know what this is saying at all and I don't know that it's possible to know it.
[1887.90 --> 1890.74]  And we have one of our friends on the show, Kenneth Reitz.
[1890.80 --> 1894.44]  He talked about this tribal knowledge that you gain in these communities, right?
[1894.52 --> 1900.80]  And so in Ruby or Python or whatever the community you're a part of, there's, like, the syntax and semantics.
[1900.94 --> 1904.14]  But then there's this tribal knowledge that you gain over the years.
[1904.18 --> 1912.68]  And that comes from reading documentation and, you know, listening to people fight about things on the internet and, you know, all the different ways that you kind of pick these best practices up.
[1912.68 --> 1923.28]  But we can't assume that somebody, A, knows that tribal knowledge and that if they don't know it, that they, you know, then can go find that tribal knowledge.
[1923.84 --> 1931.58]  And so you're borrowing from just something that we all know or, you know, I think the one assumption is that they know English.
[1932.28 --> 1932.34]  Yeah.
[1932.34 --> 1937.62]  But pretty much, like, if you get involved in development, you pick up English or, you know, whatever.
[1938.10 --> 1940.98]  But, well, that's not necessarily true, but you know what I'm saying.
[1941.34 --> 1944.46]  And that's an assumption I think is probably safe to make.
[1944.62 --> 1951.78]  But the assumption of, like, they know how to go find documentation is a big one.
[1951.82 --> 1954.20]  And I think it's one that we overlook a lot as developers.
[1954.20 --> 1954.64]  Right.
[1956.60 --> 1965.24]  And I think with, like, flat design and things like this, people are asking the question, well, if all design is going to look like this now, then what are designers going to do?
[1965.40 --> 1967.42]  Like, what are they going to design?
[1967.52 --> 1969.62]  It's just, you know, there's nothing left to design anymore.
[1969.74 --> 1971.58]  It's just icons and buttons on a page.
[1971.92 --> 1972.90]  And I think that's a good thing.
[1973.20 --> 1976.44]  I think we're narrowing down the language into only the things that work.
[1976.44 --> 1985.18]  And hopefully we'll all be out of jobs one day and that anyone, you know, can go to community college and then be the guy who makes the websites.
[1985.30 --> 1986.86]  That's, like, that's my dream world.
[1987.26 --> 1994.76]  I think we're, like, sort of the machinists of our generation, you know, highly technical, evolved to understand a very particular instrument.
[1995.24 --> 1997.44]  But eventually our job will be done by robots.
[1998.70 --> 2005.38]  Yeah, we'll be the people that our whole career will be made by fixing the homeowner's mistakes when they fix the light bulb in their house kind of a thing.
[2005.38 --> 2006.56]  Yeah, exactly.
[2007.44 --> 2008.52]  That's a great way to put it.
[2009.48 --> 2013.10]  Yeah, well, this is, I think, so semantics, obviously, in a kind of early stage.
[2013.18 --> 2014.94]  I mean, it's on 0.3.1.
[2015.24 --> 2020.88]  I don't know what your roadmap looks like to get to 1.0, but you said this is in pre-release, you know, build tools.
[2021.02 --> 2027.58]  So it's pretty early on, and it started to obviously take some kind of to grow some legs and to start to run.
[2027.90 --> 2028.84]  It's cool to see the project.
[2028.84 --> 2034.22]  I mean, I looked at it when I first emailed you about a couple weeks ago, and I've looked at it a few times since then.
[2034.22 --> 2037.82]  I've seen so much change, you know, in the last couple weeks.
[2038.08 --> 2039.76]  So it's cool to see this thing growing so fast.
[2039.98 --> 2047.18]  And maybe, you know, we'll kind of have you on the show again when you do hit that 1.0 to kind of talk about.
[2047.26 --> 2055.18]  Because I have a feeling you're going to have some hurdles to jump, you know, with stubborn developers that don't like to change their way of thinking, including myself.
[2055.18 --> 2063.52]  And I'd love to hear, you know, how they kind of, like, fight back and the pushback you get.
[2063.58 --> 2074.02]  Like, things that are just so interesting to me is such a different way of thinking about it is that on your grid, you use the word column in the row, and you use the word column in the columns, right?
[2074.02 --> 2077.70]  So stubborn developers are going to look at that and be like, no, that's not the right way to do it.
[2077.94 --> 2082.10]  But technically it is because you're combining these words, and it's a three-column grid.
[2082.30 --> 2085.02]  That word column by itself does not mean the same thing.
[2085.14 --> 2087.06]  And that's really cool, a different way to think about it.
[2087.56 --> 2087.92]  Right.
[2088.48 --> 2089.42]  You know, maybe in…
[2089.42 --> 2090.84]  Words have meaning in context.
[2091.48 --> 2092.20]  Exactly, yeah.
[2092.20 --> 2100.50]  In Chinese, ma, like, with the four tones, meaning everything from mother to horse to question to weed.
[2101.58 --> 2105.42]  So, you know, it just goes to show.
[2105.84 --> 2105.96]  Yeah.
[2106.22 --> 2113.94]  So maybe we'll look for you to get to your 1.0, and we'll bring you on and kind of talk about lessons learned and how you've revolutionized the thing.
[2115.08 --> 2116.46]  Well, thanks for having me.
[2116.94 --> 2117.84]  I'm really excited about that.
[2118.14 --> 2118.80]  Yeah, we'll get there.
[2118.80 --> 2124.68]  Let's go ahead and kind of for new listeners, we kind of have the same three questions that we ask at the end of every show.
[2124.96 --> 2125.82]  We'll go ahead and ask them.
[2126.06 --> 2129.96]  So the first one submitted by…
[2129.96 --> 2130.32]  No, I'm just kidding.
[2130.42 --> 2134.06]  The first question that we ask everyone, Jack, is for a call to arms.
[2134.16 --> 2135.02]  So you're young.
[2135.08 --> 2135.98]  The project is young.
[2136.88 --> 2141.06]  What is it that you would like to see the community kind of pitch in to help out with?
[2142.50 --> 2146.96]  So Semantic is one of those projects where the larger it is, the better it is.
[2146.96 --> 2158.66]  And I think the best way to contribute is if you just want to submit ideas, go to our project contributing page, click on the link to the board, submit an idea for an element.
[2158.66 --> 2174.90]  If you really want to contribute to the project specifically with code, look at the roadmap, find one of the elements that's planned for version 1 or for 1x and just grab it off.
[2175.38 --> 2179.02]  Look at websites that make that element, all the different ways that it can exist.
[2179.34 --> 2181.34]  Look at our guide for language and just start coding.
[2181.34 --> 2188.26]  I'm very happy to help people write code for the library.
[2188.40 --> 2190.22]  I'm very happy to be on Gchat and Skype.
[2191.98 --> 2193.80]  I am working on this full time now.
[2195.36 --> 2197.52]  And yeah, just come join.
[2198.30 --> 2198.42]  Cool.
[2198.66 --> 2200.36]  Where's the roadmap at?
[2201.20 --> 2203.36]  The roadmap is on contributing page as well.
[2203.36 --> 2210.82]  So I was going to say, the contributing page, if you go to semantic-ui.com, there's a little thumb to pull out the sidebar.
[2211.36 --> 2215.62]  And when you pull out the sidebar under the project header, there's the contributing page.
[2215.68 --> 2215.86]  Gotcha.
[2216.04 --> 2216.20]  Okay.
[2217.22 --> 2220.44]  So you can kind of see the roadmap and all that he's talking about right there.
[2221.28 --> 2221.64]  Oh, no.
[2221.68 --> 2222.66]  I'm missing the roadmap link.
[2223.04 --> 2224.94]  I do have the contributing links, though, there.
[2226.08 --> 2228.90]  But I will push that later.
[2228.90 --> 2229.50]  Yeah.
[2230.40 --> 2230.58]  Yeah.
[2230.66 --> 2231.04]  Oh, well.
[2231.42 --> 2240.16]  So if you weren't doing what you're doing now, Jack, what would you be doing, whether it was another project or language or surfing?
[2240.78 --> 2248.38]  So I have this other fantasy dream of employment, which is I want to go to a country that has really bad beer and open a brewery there.
[2248.68 --> 2250.14]  Like, where the bar is really low.
[2250.88 --> 2252.06]  I don't know where that would be.
[2253.36 --> 2254.44]  Yeah, we don't want to knock.
[2254.52 --> 2257.48]  We don't want to take shots at any country's brewing systems.
[2257.48 --> 2261.34]  You'd have to figure that out yourself and be secretive about it.
[2262.14 --> 2263.76]  So do you homebrew, then?
[2264.26 --> 2264.46]  Yeah.
[2265.06 --> 2265.72]  I'm a homebrewer.
[2266.14 --> 2268.48]  I've always had a fantasy of doing a craft brewery.
[2268.94 --> 2275.60]  But it's one of those things where you look at the statistics of craft breweries failing and succeeding, and you're just like, I'm a programmer.
[2275.76 --> 2276.62]  I can't make this choice.
[2277.10 --> 2279.98]  Did you see the Kickstarter for the – I think it's a homebrew system.
[2280.08 --> 2281.24]  I can't recall what it's called, though.
[2281.94 --> 2285.76]  Yeah, it was like a little box that did – I think it did most of the work for you, homebrew.
[2285.76 --> 2287.56]  And I think that was interesting.
[2287.70 --> 2288.58]  But you could program it, right?
[2288.76 --> 2293.38]  Couldn't you – wasn't it part of like – I'm sure later on they'll have some sort of SDK for it.
[2293.70 --> 2294.20]  Yeah, yeah.
[2294.32 --> 2302.60]  And I think it's interesting because a lot of people at Homebrew take pride in their method and the specific little details they do.
[2302.60 --> 2314.02]  But once again, the interesting thing about when we ask that question, and this is yet another example, is a lot of developers, they go in the direction of creating something with their hands.
[2314.16 --> 2320.36]  Whether it's food, we've had that before, obviously beer, woodworking, things like that.
[2320.42 --> 2329.42]  A lot of developers are kind of drawn because we sit behind a computer and create digital things all day, are kind of drawn to the notion of creating a physical product, right?
[2329.42 --> 2337.12]  And so I'm super interested in woodworking and I'm not very good at it at all, but that would be totally something I would do if I were given more time.
[2337.30 --> 2347.14]  But once again, I think that's a kind of little interesting little side story that maybe we can kind of document one day is like the many desires of developers to create with their hands.
[2347.14 --> 2351.32]  And the last question that we ask is for a programming hero.
[2351.46 --> 2355.98]  So just somebody in your life, Jack, that has been influential in your career.
[2357.24 --> 2357.44]  Yeah.
[2357.58 --> 2361.98]  So I'm a huge fan of John Resick, the guy who created jQuery.
[2363.26 --> 2366.26]  I remember when I first moved to San Francisco, it was like my first year there.
[2366.46 --> 2368.44]  I was like, you know, my early 20s.
[2368.44 --> 2373.42]  And there was like a jQuery meetup and this is sort of like when jQuery was around with new tools and prototype.
[2373.98 --> 2376.50]  And like they weren't really like winning the race yet.
[2376.56 --> 2378.58]  It was like kind of like a three pony race.
[2379.22 --> 2383.60]  And I went to the meetup and I saw him there and I got freaked out and I left the room.
[2383.76 --> 2384.90]  I couldn't be here.
[2384.90 --> 2388.82]  And then like, you know, it's been five years or whatever.
[2389.10 --> 2391.06]  But I still remember that.
[2391.14 --> 2399.28]  And he made a massively popular library that basically just took all the things that were hard to do in web design and put them all together into one library.
[2399.76 --> 2402.38]  So that's fucking amazing.
[2402.82 --> 2403.54]  So revolutionary.
[2405.24 --> 2405.48]  Yeah.
[2406.50 --> 2406.94]  Awesome.
[2407.36 --> 2407.70]  Cool.
[2408.06 --> 2409.48]  I hear your fans spinning up.
[2409.56 --> 2410.02]  It must be in.
[2410.06 --> 2410.84]  It's time to go.
[2410.84 --> 2416.92]  So I do want to thank again our sponsor, DigitalOcean, for taking care of us for this show and many others.
[2417.30 --> 2427.72]  You can get their $10 promo by going to DigitalOcean.com, popping in your credit card and in the promo code field, throw in the code, the changelog104.
[2428.16 --> 2429.72]  You can only hear that in audio.
[2429.80 --> 2430.56]  We're not going to put it on the site.
[2430.64 --> 2433.76]  So you have to listen to this audio to use the code.
[2433.76 --> 2436.14]  So it's the changelog104.
[2436.14 --> 2442.56]  We'll get $10 off, which basically is like two bucks or sorry, two free months if you got their basic plan.
[2442.70 --> 2446.16]  But super huge thanks to DigitalOcean for being our sponsor.
[2446.26 --> 2452.52]  And Jack, thanks for being the linguistic person that you are and being a fan of just semantics in general.
[2452.52 --> 2460.14]  And the hard work you're putting into this to kind of bring your ideas to fruition with front-end development.
[2460.56 --> 2463.08]  And definitely want to have you back on the show when you hit 1.0.
[2463.28 --> 2468.26]  But Andrew, thanks to you as well for kicking this show off.
[2468.40 --> 2469.64]  And you, the listener, for listening.
[2469.82 --> 2470.82]  But for now, let's say goodbye.
[2471.82 --> 2472.20]  All right.
[2472.26 --> 2472.96]  Thanks so much, Jack.
[2473.64 --> 2474.30]  Thanks, you guys.
[2474.30 --> 2474.36]  Thanks, guys.
[2474.36 --> 2474.38]  Thanks, guys.
[2482.52 --> 2512.50]  Thanks, guys.
