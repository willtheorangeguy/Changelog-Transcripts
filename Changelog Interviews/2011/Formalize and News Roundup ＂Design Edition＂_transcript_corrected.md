[0.00 → 18.02] Welcome to the Changelog episode 0.5.3.
[18.22 → 19.02] I'm Adam Stachowiak.
[19.44 → 20.32] And I'm Won Netherlands.
[20.48 → 21.46] This is the Changelog.
[21.50 → 23.56] We cover what's fresh and new in the world of open source.
[24.00 → 26.82] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.06 → 27.96] We're also up on GitHub.
[27.96 → 29.34] At thechangelog.com.
[29.68 → 34.20] You'll find some training repos, some feature repos from the blog, as well as our audio podcasts.
[34.74 → 36.18] If you found Twitter, follow Changelog Show.
[36.42 → 37.44] And me, Adam Stack.
[37.86 → 40.18] And I'm Penguin, P-E-N-G-W-I-N-N.
[40.80 → 45.90] Joined for a special roundup episode by Mr. Nathan Smith, a.k.a. the 960 Dude.
[49.18 → 53.70] Nathan, why don't you introduce yourself for the three people out there that don't know who you are.
[54.78 → 55.60] Hey, guys.
[55.60 → 58.88] I'm back again because Won wanted me to be on the show.
[59.16 → 59.46] Not Adam.
[59.46 → 60.08] So I am.
[61.40 → 62.48] Oh, and Adam.
[63.06 → 64.18] So thanks for having me.
[64.98 → 65.38] Cool.
[65.52 → 68.96] You've got some new codes to talk about since the last time you were on the Changelog.
[69.02 → 72.28] So last time we talked about the 960 CSS Grid system.
[72.48 → 77.12] Now you're out with Formalize at formalize.me is the URL.
[77.38 → 78.10] What's this all about?
[78.54 → 78.82] Oh, yeah.
[78.82 → 79.88] I kind of alluded to that.
[79.88 → 83.14] It was in progress last time we talked, but it wasn't launched yet.
[83.14 → 87.52] Basically, it's as close as you can get to a form reset.
[88.36 → 94.04] So rather than try to make the forms look crazy different or replace anything on the fly with JavaScript,
[94.38 → 97.48] creating accessibility issues, it just tries to take the elements that are there
[97.48 → 104.24] and make them look as close to the default that you can that all the browsers will kind of agree on.
[104.24 → 109.12] So at a glance, it's not supposed to stand out necessarily.
[109.26 → 111.80] It's just supposed to look at it and say, yeah, it looks like a form.
[112.70 → 114.02] So that's pretty much it.
[114.10 → 119.90] But, I mean, there's quite a bit of code involved, but it's an accessible approach.
[120.26 → 121.34] So what's the idea here?
[121.46 → 125.16] So that the forms look exactly the same in all browsers or just enough?
[125.16 → 134.16] As close as humanly possible without resorting to, like, hiding elements and creating fake elements with JavaScript.
[135.04 → 137.38] So what's the deal with browsers and forms anyway?
[137.52 → 142.36] I mean, is this an operating system affinity that they have,
[142.44 → 147.16] or is it more just each browser has its own way of displaying form elements?
[147.62 → 149.94] Honestly, it's kind of like Seinfeld says,
[149.94 → 152.64] Who are the ad wizards who came up with that one?
[152.64 → 156.78] I would love to sit down with whoever decided, you know,
[156.84 → 162.22] on all these different browsers that we're going to go a different way than the operating system or whatever.
[162.40 → 167.18] I mean, Chrome on OS X looks totally different from Chrome on Windows
[167.18 → 170.76] or Chrome on Ubuntu or, you know, Linux or whatever.
[171.38 → 172.96] Same with, like, Firefox and stuff.
[173.08 → 176.84] So, I mean, they try to keep to the operating system default,
[176.84 → 180.32] but they're even different amongst themselves within the same operating system.
[180.32 → 185.72] So, Formalize is an attempt to get them as close as possible to one another.
[186.32 → 192.26] So, 960 is pure CSS, but on Formalize, you've got JS library support for Dojo, Moo Tools,
[192.58 → 195.32] Cents ha, jQuery, Prototype, even GUI.
[196.06 → 198.14] So, what's the JavaScript component here?
[198.52 → 201.52] It's just a little, whatever you call it,
[201.58 → 207.54] polyfill that will add HTML5 form support to browsers that don't have it natively.
[207.54 → 211.88] So, if you're in, like, IE6 or IE7, the autofocus attribute will work,
[211.94 → 214.60] the placeholder attribute will work, stuff like that.
[214.86 → 218.60] So, and it, you know, it does a check first to see if those already work in the browser,
[218.70 → 222.38] and if so, it leaves them alone so you get the browser native handling.
[223.96 → 230.08] Have you seen the exhaust of HTML5 cross-browser polyfills on the Modernizer repo up in GitHub?
[230.08 → 231.08] I have.
[231.86 → 232.80] Those are pretty cool.
[233.64 → 235.98] For this, I just wanted to do pretty much the styling,
[236.20 → 241.56] and then the small polyfills were low-hanging enough fruit, you know,
[241.64 → 247.76] just the autofocus and placeholder and that type of thing.
[249.44 → 251.74] So, I mean, because a lot of those already exist,
[251.82 → 254.00] I didn't want to attempt to just recreate the wheel there,
[254.00 → 260.28] but what I couldn't find was something that made form elements look kind of defaults across the browser spectrum.
[261.52 → 264.14] What sort of feedback are you getting on Formalize from the community?
[264.66 → 266.08] Seems to be pretty well-received.
[266.34 → 269.26] Actually, I had a guy call me at 1030 last night that wanted to talk about it.
[269.86 → 270.66] That's always fun.
[270.72 → 274.76] Wasn't sure how he got my email or, um, sorry.
[275.02 → 275.28] Your home phone number?
[275.48 → 276.22] Yeah, sorry.
[276.52 → 278.38] Wasn't sure how he got my home phone number, I should say.
[278.94 → 281.10] So, I was like, really love to talk to you about that,
[281.10 → 282.92] but if you email me, it would be a lot better,
[283.40 → 284.42] because, you know, when you've got a kid,
[284.48 → 287.82] you don't want to be talking web at, like, 1030 at night, so.
[289.76 → 291.46] Talking web at 1030 at night,
[291.56 → 295.68] so this is not something you normally do with your wife, is talk web?
[296.22 → 297.48] I mean, I'll chat with people,
[297.48 → 300.36] but, I mean, it's a whole other thing to have a phone conversation
[300.36 → 302.48] with somebody that doesn't even introduce themselves.
[303.14 → 304.34] Just immediately pick up the phone.
[304.38 → 305.46] Hey, did you do Formalize?
[306.40 → 306.76] Yes.
[307.52 → 308.86] Cool, I have a few questions.
[309.36 → 310.16] Who are you?
[310.16 → 311.78] You know, a little weird.
[312.48 → 313.48] Were you telling me the other day
[313.48 → 315.04] that you went out to dinner with your wife
[315.04 → 318.32] and she didn't want to talk HTML5, JavaScript, or CSS3?
[318.92 → 320.84] Right, so, you know, I said I could frame it
[320.84 → 322.30] as food, clothing, and shelter,
[322.48 → 324.64] but, you know, that didn't go over too well.
[326.38 → 327.32] Well, looking at the demo,
[327.40 → 329.94] you actually have quite a bit of different camp support.
[330.02 → 332.18] You got Dojo, you got jQuery, Moo Tools.
[332.80 → 334.94] Seems you've put demonstrations up in each one.
[334.94 → 336.08] What was involved in that?
[337.02 → 338.20] Initially, I did it in jQuery.
[338.20 → 342.62] Then I had somebody kind of volunteer with a pull request for Moo Tools,
[342.74 → 345.68] and I thought, well, if somebody wanted to do it for Moo Tools,
[345.78 → 347.90] there's probably a chance that they want it for other libraries too.
[348.38 → 351.26] So I went ahead and did the Dojo prototype and Yahoo ones,
[351.36 → 352.58] because I was already familiar with those.
[353.08 → 357.08] And then another guy volunteered to do the Sentry one,
[357.08 → 359.46] or the I guess it's ext.js.
[360.96 → 365.08] So, yeah, basically I didn't want people to look at it and say,
[365.12 → 366.60] oh, this is cool, but oh, I can't use it
[366.60 → 370.56] because we've already standardized on a library that it doesn't support.
[371.10 → 372.56] So I'm going to ask the number one question,
[372.62 → 373.48] probably on everybody's mind,
[373.52 → 376.38] is that your recent SAS support, or SAS convert,
[376.50 → 378.16] but this is in CSS.
[379.00 → 379.30] Right.
[379.30 → 383.54] Well, it actually comes with an underscore formalized.SAS file
[383.54 → 384.96] that you can use if you want.
[386.58 → 387.02] Boom.
[387.90 → 388.66] Just like that.
[389.16 → 389.58] So boom.
[390.26 → 393.86] So what's a CSS to SAS convert look like these days?
[395.30 → 397.78] Pretty much like a web developer.
[398.84 → 399.36] I don't know.
[399.84 → 401.88] I guess the last time on the show you asked me about SAS,
[402.00 → 403.00] and I hadn't really used it,
[403.06 → 405.72] so my answer was like, yeah, it seems good.
[405.72 → 410.30] My initial response to win was get off my lawn, you know.
[410.56 → 411.30] I remember that.
[411.42 → 416.00] But, you know, I've been using it since starting this new job at HP,
[416.12 → 417.00] and we use it as a team.
[417.16 → 419.88] So kind of like, you know, you jump on the project
[419.88 → 424.34] and it's already in the project, so you kind of run with it.
[424.42 → 426.86] And I really thought I would miss the curly braces
[426.86 → 428.92] and even was wondering like, oh, man,
[428.94 → 430.34] is this going to ruin me for real CSS?
[430.64 → 433.06] But I think, you know, after a certain point you realize
[433.06 → 437.04] CSS is not so complex that it's going to kill your understanding
[437.04 → 437.90] of the language itself.
[437.90 → 439.98] So beyond just killing CSS,
[440.24 → 443.80] what about things like CSS3 support, like round of corners,
[443.92 → 446.76] the things that actually take up like eight lines to support all browsers?
[447.00 → 449.76] Oh, yeah, I mean, not having to type like dash WebKit, dash MOZ,
[449.84 → 451.88] and all the permutations is awesome.
[451.94 → 453.00] How much time do you think you've saved?
[454.20 → 455.58] I don't know.
[455.70 → 457.36] I mean, not just time, but also just brain cycles.
[457.36 → 460.16] Yeah, I think, too, at the end of the day,
[460.26 → 464.08] you're not typing all that stuff over and over.
[464.36 → 466.72] So, I mean, probably saving on like metacarpals.
[467.06 → 467.46] I don't know.
[470.08 → 472.88] I can't quantify the exact amount of time,
[472.94 → 475.00] but I certainly feel more productive using Sass.
[475.42 → 477.40] I kind of hear this song in the background.
[477.48 → 477.92] Do you hear that?
[478.94 → 479.88] It's a whole new world.
[482.24 → 484.24] Going back to Aladdin, is that where you're going with that?
[484.24 → 486.62] Yeah, dude, you put the movie things out there all the time,
[486.70 → 488.32] so I pull one out of the cuff.
[488.34 → 491.32] I just like probably some crack-tip at your choice of movies.
[491.52 → 493.26] It's like children's cartoons and things.
[493.32 → 493.76] It's great.
[494.04 → 495.04] I keep it simple, you know.
[495.60 → 496.84] You know, what's funny is, you know,
[496.90 → 499.20] I love the indented syntax of Sass,
[499.32 → 503.24] and, you know, the SCSS syntax still supports the curly braces,
[503.40 → 507.50] but, you know, we both prefer the indented syntax,
[508.06 → 509.32] the original Sass syntax.
[509.32 → 510.50] But what's funny is, you know,
[510.58 → 513.20] I prefer the indented white space in Sass,
[513.30 → 515.02] but yet, you know, I prefer Ruby to Python.
[515.48 → 518.60] But just to prove there is a yin and yang to the universe,
[518.68 → 520.68] it seems like I'm giving all the curly braces back
[520.68 → 522.28] in my moustache templates.
[522.44 → 524.48] I love moustache as a emulating language.
[525.12 → 525.88] You guys used it?
[526.66 → 526.92] No.
[527.56 → 527.86] No.
[528.74 → 529.38] I have not.
[530.26 → 530.60] However,
[530.84 → 533.08] so much to teach you guys.
[533.52 → 534.40] Since Won likes it,
[534.42 → 535.60] I have the feeling I'll be using it
[535.60 → 538.54] on a project in the future very soon.
[538.54 → 539.52] Absolutely, dude.
[540.00 → 542.30] Well, the good thing about Sass, really,
[542.46 → 544.98] is that it's so easily converted from one to the other,
[545.08 → 546.88] so you can pick a camp if you want.
[547.74 → 549.30] Like, for me, I got a couple extensions out there
[549.30 → 550.26] that I actually deploy.
[551.00 → 552.08] I write the Sass,
[552.22 → 555.22] but I have a rake task to convert it to SCSS
[555.22 → 556.92] before I actually ship the gem,
[557.02 → 559.22] so it's available to both camps.
[559.42 → 560.14] I'm agnostic.
[561.00 → 561.20] Huh.
[561.90 → 563.34] To me, just as an end user,
[563.74 → 565.36] and it sounds like you prefer Sass, too,
[565.36 → 568.00] but I thought I would like SCSS,
[568.16 → 569.30] but once I got into it,
[569.38 → 569.72] it's like,
[569.82 → 571.36] if you're going to go different,
[572.04 → 572.98] go all out, you know,
[573.06 → 574.76] and save that typing.
[575.14 → 575.44] I don't know.
[575.48 → 576.42] It just seems more logical.
[576.66 → 576.94] Oh, yeah, totally.
[577.04 → 577.46] I'm with you,
[577.54 → 578.74] but the point, really,
[578.86 → 579.66] with that is that
[579.66 → 582.40] you've got people who are scared of Sass
[582.40 → 582.82] as like,
[582.86 → 584.16] oh, I've got to change things,
[584.28 → 586.32] just like the comment for you had at first, too,
[586.84 → 588.42] but if they're just a CSS player,
[588.50 → 590.20] they can easily just use that Sass,
[590.32 → 591.22] or sorry, the SCSS,
[591.44 → 593.66] because it's basically CSS.
[594.54 → 595.54] I mean, you could just drop CSS
[595.54 → 596.94] right in that file and it runs.
[597.14 → 597.60] No problem.
[598.16 → 599.26] I guess what I like about Sass
[599.26 → 600.62] is when you go into a Sass file,
[600.72 → 601.92] you know that you're in a Sass file.
[602.00 → 602.88] You don't have to look and say,
[602.96 → 604.80] okay, are there any variables being used in here?
[605.14 → 606.00] Aside from, I mean,
[606.04 → 607.62] obviously looking at the file extension,
[607.62 → 612.20] but it seems a little more straightforward to me.
[612.92 → 615.10] You know, one of the things that you liked
[615.10 → 616.90] when we chose the intended syntax
[616.90 → 618.20] for the project we're working on
[618.20 → 621.38] is the one less decision to make
[621.38 → 623.44] around how do I format my style sheets,
[623.54 → 624.92] because with the intended syntax,
[625.20 → 626.46] there's really only one way
[626.46 → 629.72] to arrange your style sheet code
[629.72 → 633.50] with the CSS traditional syntax.
[633.80 → 635.54] You know, everybody's got their own opinions.
[635.54 → 636.06] Oh, yeah, I mean,
[636.06 → 638.34] it keeps the one-line CSS riff-raff out.
[639.46 → 640.00] Well, not only that,
[640.08 → 640.42] but I mean,
[640.48 → 643.22] not to jump on the sister project of Sass,
[643.22 → 645.56] but Hamill does the same thing for HTML.
[646.38 → 647.54] Yeah, I can't tell you how many times
[647.54 → 648.86] I've got to the end of a file,
[649.48 → 651.04] you know, ERA or HTML file,
[651.12 → 652.84] and you see closed DIV, DIV, DIV, DIV, DIV, DIV,
[652.86 → 653.76] and you're like, what?
[654.12 → 656.28] Well, okay, I know somewhere something's unclosed,
[656.36 → 657.30] but I don't know what it is.
[657.90 → 659.18] You haven't felt it the best
[659.18 → 662.90] unless you've actually dealt with a conflict with Git,
[663.02 → 664.88] and you've got a massive ERA file
[664.88 → 666.92] or straight-up HTML file,
[667.02 → 669.52] and try to work your way out of that.
[669.68 → 671.68] What's worse is when one of the closing ditties,
[671.68 → 673.78] the missing ones are down on a partial somewhere.
[674.76 → 675.92] Yeah, that's true.
[676.58 → 677.50] On the flip side,
[677.66 → 678.30] sometimes I'm like,
[678.40 → 680.44] I really just want to do a data dash attribute.
[680.70 → 681.92] Is that so hard?
[683.12 → 684.34] As with any abstraction,
[684.54 → 685.18] it seems like the
[685.52 → 688.00] yeah, the simple things are what become hard,
[688.08 → 688.24] you know,
[688.30 → 689.68] with abstractions that make
[689.68 → 691.22] the incredibly hard things very simple.
[691.44 → 692.62] Yeah, I think there's trade-offs either way,
[692.68 → 693.80] but I mean,
[693.82 → 695.70] I prefer Hamill if it's on a project already.
[696.40 → 698.42] I would probably say that I,
[698.42 → 699.34] you know,
[699.42 → 700.20] that's the old saying,
[700.48 → 700.82] or whatever,
[701.14 → 701.90] came for the Hamill,
[701.98 → 702.70] stayed for the SAS.
[703.10 → 704.04] Except I came for the SAS,
[704.16 → 704.64] and Hamill,
[704.74 → 705.36] I'll take or leave.
[705.98 → 706.44] Kind of like,
[706.52 → 706.74] meh,
[706.98 → 707.56] I like it,
[707.64 → 708.52] but I wouldn't like,
[709.48 → 709.82] you know,
[710.86 → 712.16] cry if it wasn't in a project.
[712.44 → 713.94] But I would cry if there was no SAS,
[714.00 → 714.56] that's for sure.
[714.78 → 715.66] I might shed a tear.
[716.04 → 717.48] I would definitely shed a tear.
[718.00 → 719.24] With so much SAS talk,
[719.30 → 720.48] I know we're a little lighter
[720.48 → 722.24] on the listenership so far,
[722.24 → 724.40] because there were some comments
[724.40 → 726.82] in the Convoy room the other night
[726.82 → 728.22] about someone saying,
[728.42 → 729.88] if I hear Hamill and SAS one more time
[729.88 → 730.40] on the changelog,
[730.44 → 731.60] I'm going to shoot myself in the face.
[731.76 → 732.10] Uh-oh.
[732.46 → 733.88] Our condolences to your families.
[735.58 → 736.82] Let's do a roundup show,
[736.88 → 737.18] shall we?
[737.48 → 739.08] Let's kick it off.
[739.12 → 739.56] Who's first?
[739.88 → 741.16] And this is totally unscripted.
[741.64 → 741.98] Obviously.
[742.84 → 743.56] So Adam,
[743.64 → 745.44] what would you like to talk about first?
[746.28 → 748.30] I think just kind of continuing down
[748.30 → 751.30] the whole style framework,
[751.30 → 752.58] let's talk about HSL.
[753.14 → 755.04] So before this conversation,
[755.04 → 757.96] I kind of got a little bit of a brain-teaser
[757.96 → 759.94] from Wynn about what HSL is.
[760.16 → 760.64] And Nathan,
[760.72 → 761.74] I guess you kind of backed me up
[761.74 → 763.04] with not really being sure
[763.04 → 764.10] about where this fits in.
[764.52 → 764.84] Right.
[764.94 → 765.12] Yeah.
[765.16 → 765.48] Initially,
[765.56 → 765.90] I was like,
[765.98 → 766.36] so wait,
[766.84 → 768.84] I know RGB is like a numerical equivalent
[768.84 → 769.46] of hex,
[769.54 → 770.62] but what is HSL?
[771.04 → 771.34] Right.
[771.42 → 772.46] So we got Brandon Mathis
[772.46 → 775.02] picking up the cool domain,
[775.18 → 776.80] hslpicker.com,
[776.82 → 778.42] and he threw up a very snazzy,
[778.86 → 780.08] very beautiful site
[780.08 → 781.80] to demonstrate a lot of,
[781.88 → 782.12] I guess,
[782.12 → 783.32] some of to sass in the behind
[783.32 → 785.36] because I know that he's a sass dude.
[785.78 → 787.24] And then some nifty JavaScript,
[787.50 → 788.22] but Wynn,
[788.50 → 789.04] HSL,
[789.16 → 789.56] what is it,
[789.64 → 789.72] bud?
[790.36 → 791.48] For those that don't know,
[791.72 → 792.72] HSL is hue,
[792.88 → 793.34] saturation,
[793.80 → 795.94] and either lightness or luminosity,
[796.08 → 796.82] depending on your flavour.
[797.64 → 798.04] Basically,
[798.30 → 799.22] it's the three dimensions
[799.22 → 799.84] that I think
[799.84 → 801.04] how the human brain works
[801.04 → 801.76] around picking colour.
[801.90 → 802.80] Because normally,
[802.90 → 803.56] when you sit down
[803.56 → 804.64] to pick a colour,
[805.32 → 806.40] you start playing
[806.40 → 807.50] with those RGB sliders,
[808.08 → 808.58] and you're like,
[808.80 → 809.76] what the heck?
[809.76 → 811.16] And then you flip over,
[811.28 → 812.42] if you're on Mac,
[812.50 → 813.60] you flip over to those crayons,
[814.16 → 815.54] and you pick the one
[815.54 → 816.00] that's closest
[816.00 → 817.20] just by the crayon colour.
[817.36 → 817.74] That's right.
[818.42 → 819.44] But HSL,
[819.52 → 820.04] give it a look.
[820.44 → 820.80] Basically,
[820.92 → 821.54] you have three sliders.
[821.62 → 822.38] The first one's the hue,
[822.46 → 823.46] so it goes from red to red.
[823.82 → 824.64] So you can choose
[824.64 → 826.28] red through the oranges,
[826.60 → 827.30] colours of the rainbow,
[827.42 → 827.94] all the way to
[827.94 → 829.10] meets red on the other side.
[829.52 → 830.08] The second one
[830.08 → 831.10] is the saturation.
[831.34 → 832.64] So the zero saturation
[832.64 → 834.52] is totally greyscale,
[835.18 → 836.78] and 100% saturation
[836.78 → 838.36] has the full colour component
[838.36 → 838.90] of the colour.
[838.90 → 838.94] colour,
[839.04 → 840.66] and then the third
[840.66 → 841.58] dimension there
[841.58 → 842.64] is the luminosity
[842.64 → 843.34] or the lightness,
[843.58 → 844.30] and so you can go
[844.30 → 845.06] darker or lighter.
[845.22 → 846.08] So that's usually how
[846.08 → 847.12] a designer,
[847.24 → 847.78] when we sit down
[847.78 → 848.70] to pick colours
[848.70 → 849.50] for a design,
[849.58 → 850.14] you want something
[850.14 → 850.86] that's a little warmer
[850.86 → 851.78] or something's
[851.78 → 852.36] a little darker,
[853.06 → 853.98] something's a little
[853.98 → 854.80] more washed out,
[855.06 → 855.20] you know,
[855.22 → 856.76] those types of scenarios.
[856.94 → 858.24] So this is a good way
[858.24 → 858.72] to pick those.
[859.32 → 860.34] And for those of you
[860.34 → 860.78] who know,
[860.84 → 861.76] Brandon Mathis from,
[861.88 → 863.54] I think it was 0.1.1.
[864.02 → 864.86] Fancy buttons.
[865.18 → 865.40] Yeah,
[865.46 → 866.44] not only fancy buttons,
[866.44 → 868.60] but also the kind of
[868.60 → 870.82] file-based blogging,
[870.92 → 871.44] what was it called?
[872.24 → 873.10] What was that show called?
[873.58 → 873.98] Octopuses.
[874.36 → 874.62] Oh, no,
[874.74 → 875.56] not his project,
[875.70 → 876.64] but what was that show
[876.64 → 876.92] about?
[877.58 → 877.94] Oh,
[878.02 → 878.68] open source publishing.
[878.94 → 879.20] Okay.
[879.76 → 880.06] So yeah,
[880.06 → 881.02] he's got that cool
[881.02 → 883.72] Octopuses kind of fork
[883.72 → 884.52] of Jekyll,
[884.72 → 885.68] which is snazzy
[885.68 → 886.30] because it kind of
[886.30 → 887.02] jumps out of the box
[887.02 → 887.36] with some cool styles.
[887.36 → 888.64] And Octopuses is cool,
[888.88 → 890.02] but I will out Brandon.
[890.28 → 891.38] He IM'd be the other night
[891.38 → 892.14] and said he was taking
[892.14 → 893.14] a serious look at Nest,
[893.30 → 893.96] Nest CMS.
[893.96 → 894.60] Oh,
[894.60 → 895.16] of course.
[895.28 → 895.72] Why wouldn't he?
[896.32 → 896.60] Of course,
[896.66 → 897.22] those links will be
[897.22 → 897.80] in the show notes.
[898.96 → 899.96] Up next is,
[900.08 → 901.00] I guess,
[901.18 → 901.66] Reveal,
[901.84 → 903.70] which is a jQuery modal
[903.70 → 904.84] for HTML5
[904.84 → 905.58] and data attributes.
[905.68 → 905.78] Now,
[905.84 → 906.78] I haven't actually had
[906.78 → 908.92] a lot of experience
[908.92 → 910.22] with these data attributes yet,
[910.26 → 911.92] but I've been meaning to.
[912.46 → 912.80] So,
[912.88 → 913.56] we've got an expert
[913.56 → 914.34] on the show,
[914.62 → 915.24] Mr. Nathan Smith.
[915.24 → 915.92] Tell us what
[915.92 → 917.30] data attributes are.
[918.20 → 918.28] So,
[918.40 → 918.94] in the past,
[919.08 → 921.02] you know,
[921.08 → 922.58] you would have a tag
[922.58 → 923.32] and you would want to store
[923.32 → 924.12] just a little bit
[924.12 → 925.40] of information.
[925.74 → 925.88] So,
[926.06 → 926.94] if it was a link,
[927.00 → 927.48] you could abuse
[927.48 → 928.24] the REL attribute
[928.24 → 929.06] even though you weren't
[929.06 → 930.14] really describing
[930.14 → 930.98] what you're linking to.
[931.06 → 932.08] You just have like a dead link
[932.08 → 932.60] with a pound
[932.60 → 933.78] and you say REL equals
[933.78 → 935.52] triggers modal or whatever.
[936.30 → 936.60] So,
[936.66 → 936.98] I think,
[937.04 → 937.72] you know,
[937.78 → 939.80] the HTML working group,
[939.86 → 940.66] they realized
[940.66 → 941.30] that people were
[941.30 → 942.64] yearning.
[942.80 → 943.80] There's this deep yearning
[943.80 → 944.78] in the hearts
[944.78 → 945.52] of web developers
[945.52 → 947.18] for some custom attribute.
[947.40 → 947.50] So,
[947.62 → 947.96] for that,
[948.50 → 949.54] you have data dash
[949.54 → 950.16] and then whatever.
[950.16 → 950.42] So,
[950.48 → 950.96] you could say like
[950.96 → 952.12] data dash
[952.12 → 953.02] filling equals
[953.02 → 954.36] and say peanut butter jelly
[954.36 → 955.10] and that's valid
[955.10 → 956.20] because you have data dash
[956.20 → 956.64] at the beginning.
[957.66 → 957.78] So,
[958.10 → 959.22] recently,
[959.38 → 960.68] Dojo 1.6 came out
[960.68 → 961.70] and they used to have like
[961.70 → 962.84] you would say,
[963.24 → 963.50] you know,
[963.56 → 964.24] tag name DIV
[964.24 → 965.62] Dojo widget equals
[965.62 → 966.60] and then whatever
[966.60 → 967.30] and now instead
[967.30 → 968.42] they say data dash
[968.42 → 969.54] and they have those
[969.54 → 970.12] type of things
[970.12 → 971.00] kind of prefixed
[971.00 → 971.52] with data
[971.52 → 973.14] to make it
[973.14 → 974.42] valid HTML5.
[975.34 → 975.40] So,
[975.54 → 976.40] why data dash
[976.40 → 976.96] and not just
[976.96 → 977.96] using the attributes
[977.96 → 979.58] that no name spacing?
[980.16 → 981.12] I think it's just
[981.12 → 981.90] makes it easier
[981.90 → 982.40] on the browser
[982.40 → 984.14] to know
[984.14 → 984.62] that they're all
[984.62 → 985.08] kind of living
[985.08 → 985.86] off the same thing
[985.86 → 987.34] and eventually
[987.34 → 988.06] with JavaScript
[988.06 → 989.04] like it's not
[989.04 → 989.58] implemented
[989.58 → 991.46] cross browser
[991.46 → 991.98] but eventually
[991.98 → 992.46] you'll be able
[992.46 → 993.02] to say like
[993.02 → 993.98] you know,
[994.04 → 994.56] have your element
[994.56 → 996.02] and say dot data dot
[996.02 → 996.90] whatever the dash
[996.90 → 997.44] is after that.
[997.58 → 997.64] So,
[997.74 → 998.08] say you have
[998.08 → 998.70] data dash
[998.70 → 999.46] peanut butter dash
[999.46 → 999.80] jelly
[999.80 → 1000.78] you could say
[1000.78 → 1001.84] data dot peanut butter
[1001.84 → 1002.88] dot jelly
[1002.88 → 1003.60] and that would return
[1003.60 → 1004.22] you the value
[1004.22 → 1004.74] of whatever
[1004.74 → 1005.68] is inside that
[1005.68 → 1006.36] the quoted
[1006.36 → 1007.38] attribute value.
[1007.38 → 1009.14] So,
[1009.22 → 1009.56] that would be cool
[1009.56 → 1010.00] because it's kind
[1010.00 → 1010.76] of object-oriented
[1010.76 → 1012.08] way to store
[1012.08 → 1013.00] little data snippets.
[1013.88 → 1014.88] This modal is from
[1014.88 → 1015.22] Curb.
[1015.34 → 1016.44] It's 100% buzzword
[1016.44 → 1016.96] compliant
[1016.96 → 1018.26] because it's jQuery
[1018.26 → 1019.00] HTML5
[1019.00 → 1019.70] and has data
[1019.70 → 1020.20] attributes.
[1020.42 → 1020.80] But Curb
[1020.80 → 1021.94] does some awesome
[1021.94 → 1022.54] work if you haven't
[1022.54 → 1023.02] checked out their
[1023.02 → 1023.40] designs.
[1023.52 → 1024.34] They've got a nice
[1024.34 → 1024.94] little sandbox
[1024.94 → 1027.40] up at Zurb.com
[1027.40 → 1028.06] where they show
[1028.06 → 1028.54] a lot of their
[1028.54 → 1029.28] CSS tricks.
[1030.12 → 1030.70] It's actually funny
[1030.70 → 1031.40] you post this one
[1031.40 → 1031.90] too because like
[1031.90 → 1033.20] the day before
[1033.20 → 1033.80] you posted this
[1033.80 → 1034.08] I was like
[1034.08 → 1034.28] wow,
[1034.34 → 1034.92] this is awesome.
[1034.92 → 1035.96] Oh,
[1036.06 → 1036.80] actually I posted
[1036.80 → 1037.20] this one because
[1037.20 → 1038.02] I saw you watched
[1038.02 → 1038.54] it on Get Out.
[1038.54 → 1038.76] Okay,
[1038.96 → 1039.40] okay,
[1039.56 → 1039.98] nice.
[1040.74 → 1041.56] And I watched it
[1041.56 → 1041.88] because I was like
[1041.88 → 1042.34] I've got a blog
[1042.34 → 1042.90] about this
[1042.90 → 1043.90] and you beat me
[1043.90 → 1044.12] to it
[1044.12 → 1044.62] which is awesome.
[1045.32 → 1045.80] I'm going to
[1045.80 → 1046.24] switch gears
[1046.24 → 1047.00] and talk about
[1047.00 → 1047.70] Roller.
[1049.20 → 1049.92] You guys seen
[1049.92 → 1050.36] Roller?
[1051.08 → 1051.64] I have not.
[1052.20 → 1052.88] I have not.
[1052.98 → 1053.50] Did we actually
[1053.50 → 1054.56] hear about this
[1054.56 → 1055.50] from our friends
[1055.50 → 1056.24] over on the
[1056.24 → 1056.56] Ruby show?
[1057.60 → 1058.38] Did we really?
[1058.56 → 1058.76] Yeah.
[1059.54 → 1060.34] About two or
[1060.34 → 1061.00] three episodes ago
[1061.00 → 1061.50] maybe four.
[1062.08 → 1062.64] I'm happy to give
[1062.64 → 1063.20] a shout-out.
[1064.00 → 1064.40] Holly.
[1065.92 → 1066.62] So Roller
[1066.62 → 1067.22] basically is a way
[1067.22 → 1067.72] to crawl your
[1067.72 → 1068.26] website and find
[1068.26 → 1068.84] broken links.
[1069.22 → 1070.52] So it's a gem
[1070.52 → 1070.90] you install,
[1071.00 → 1071.38] gem install
[1071.38 → 1071.74] Roller.
[1072.96 → 1073.70] It's got a nice
[1073.70 → 1074.10] command line
[1074.10 → 1074.74] interface but you
[1074.74 → 1076.02] basically say
[1076.02 → 1077.24] Roller and give
[1077.24 → 1078.08] it a URL and
[1078.08 → 1078.54] they're in the
[1078.54 → 1079.74] blog post.
[1079.86 → 1080.30] I give it the
[1080.30 → 1081.76] changelog.com and
[1081.76 → 1082.58] it starts crawling
[1082.58 → 1083.10] our website.
[1083.52 → 1084.96] Looking for 404s.
[1085.00 → 1085.42] Luckily we didn't
[1085.42 → 1085.92] find any.
[1086.10 → 1086.64] Got a lot of
[1086.64 → 1088.82] 301s just the way
[1088.82 → 1090.18] that Tumblr works
[1090.18 → 1091.24] but it's a nice
[1091.24 → 1092.76] way to crawl your
[1092.76 → 1093.34] website looking for
[1093.34 → 1094.00] broken links.
[1094.00 → 1094.72] Thanks.
[1094.92 → 1095.76] This is actually
[1095.76 → 1096.62] quite good news
[1096.62 → 1097.92] actually to probably
[1097.92 → 1099.58] anyone or two
[1099.58 → 1100.38] Sees that listen
[1100.38 → 1101.92] to this because I
[1101.92 → 1102.84] can imagine becoming
[1102.84 → 1104.06] into a project and
[1104.06 → 1104.64] wanting to know
[1104.64 → 1106.18] like tell me about
[1106.18 → 1106.62] my site.
[1106.78 → 1107.44] You know spider this
[1107.44 → 1107.74] thing.
[1108.30 → 1109.04] Give me a gist of
[1109.04 → 1110.14] like past things and
[1110.14 → 1111.54] have some you know
[1111.54 → 1112.82] kind of calendar
[1112.82 → 1115.22] data against what
[1115.22 → 1115.96] was spidered and
[1115.96 → 1116.80] what was found and
[1116.80 → 1118.80] what was not.
[1119.34 → 1119.72] Yeah I mean because
[1119.72 → 1120.32] when you're content
[1120.32 → 1121.12] farming you want to
[1121.12 → 1121.88] make sure that your
[1121.88 → 1122.84] crops are well
[1122.84 → 1123.40] watered right.
[1124.40 → 1125.12] Speaking of
[1125.12 → 1126.56] speaking of
[1126.56 → 1127.82] challah even
[1127.82 → 1129.06] you guys seen
[1129.06 → 1129.82] Maha lo.
[1130.54 → 1130.94] Boom.
[1132.22 → 1133.28] With the content
[1133.28 → 1134.56] farm rules change
[1134.56 → 1135.42] of what Google's
[1135.42 → 1135.86] doing to those
[1135.86 → 1136.14] guys.
[1136.38 → 1136.98] So you have 20%
[1136.98 → 1137.40] layoff.
[1138.72 → 1139.64] That's the suck.
[1139.74 → 1140.42] Yeah so basically
[1140.42 → 1141.32] people were getting
[1141.32 → 1142.34] used to and even
[1142.34 → 1143.06] getting down to a
[1143.06 → 1143.88] science being able to
[1143.88 → 1144.94] game Google's
[1144.94 → 1145.32] algorithm.
[1145.58 → 1146.32] They recently had an
[1146.32 → 1147.72] update to it which
[1147.72 → 1148.76] pushed a lot of those
[1148.76 → 1149.98] content farms off the
[1149.98 → 1151.12] first page and you
[1151.12 → 1152.20] know subsequently
[1152.20 → 1153.18] dropped all their
[1153.18 → 1154.12] revenue from ads and
[1154.12 → 1154.42] whatnot.
[1155.30 → 1156.08] Would you classify
[1156.08 → 1157.38] ehow.com in that
[1157.38 → 1157.70] category?
[1158.44 → 1161.14] Uh I say about.com
[1161.14 → 1162.26] ranks above them but
[1162.26 → 1163.10] even that's kind of
[1163.10 → 1164.40] questionable so yeah.
[1165.12 → 1166.12] When you see you
[1166.12 → 1169.58] know how to articles
[1169.58 → 1172.10] on how to beat a
[1172.10 → 1173.72] nicotine addiction I
[1173.72 → 1174.28] guess that one's
[1174.28 → 1175.14] semi-useful.
[1175.34 → 1176.16] I saw one article that
[1176.16 → 1176.60] was talking about
[1176.60 → 1177.44] content farms and it
[1177.44 → 1178.12] linked to one that was
[1178.12 → 1178.94] like how to make
[1178.94 → 1179.64] friends at college.
[1179.76 → 1181.16] It was like step one
[1181.16 → 1182.18] go meet people.
[1182.38 → 1182.76] Like really?
[1183.04 → 1184.10] Step two don't just
[1184.10 → 1184.82] stay in your dorm room.
[1185.06 → 1186.90] Like uh how's that an
[1186.90 → 1187.18] article?
[1187.96 → 1188.78] Interesting to see how
[1188.78 → 1189.92] the change in the
[1189.92 → 1190.86] Google index changes
[1190.86 → 1192.26] the web.
[1192.52 → 1193.16] You know because you
[1193.16 → 1193.96] know Google's index I
[1193.96 → 1194.76] think is slanted towards
[1194.76 → 1195.50] folks like us.
[1195.72 → 1196.70] It's amazing how you can
[1196.70 → 1198.96] put in just an ordinary
[1198.96 → 1200.18] word that happens to be a
[1200.18 → 1201.08] GitHub repo and that
[1201.08 → 1202.22] repo's at least in the
[1202.22 → 1202.70] top three.
[1202.92 → 1203.58] It's pretty good on
[1203.58 → 1204.50] medical terms too.
[1205.58 → 1207.00] But yeah every everyday
[1207.00 → 1207.88] ordinary searches.
[1208.12 → 1209.28] Kind of hit or miss.
[1210.34 → 1211.14] Did you guys see
[1211.14 → 1211.54] Inception?
[1212.56 → 1213.14] I did.
[1213.26 → 1214.14] I actually saw it three
[1214.14 → 1214.98] times in the theatre.
[1216.36 → 1217.16] Three times in the
[1217.16 → 1217.34] theatre.
[1217.46 → 1218.22] I think the first time
[1218.22 → 1219.20] that I saw it was on a
[1219.20 → 1219.82] four-inch screen.
[1222.66 → 1223.50] We'll have to put that
[1223.50 → 1224.40] in the show notes to
[1224.40 → 1225.26] explain that weird
[1225.26 → 1225.62] noise.
[1226.20 → 1227.04] So I had to watch it
[1227.04 → 1227.78] again when I got home
[1227.78 → 1229.56] and then you know check
[1229.56 → 1230.78] out the repo that we
[1230.78 → 1231.66] posted on the changelog.
[1231.72 → 1232.74] This one was Uber
[1232.74 → 1233.34] popular.
[1234.44 → 1235.56] Inception the movie
[1235.56 → 1236.96] explained in C code.
[1236.96 → 1237.80] This was from our
[1237.80 → 1239.42] friend Steve Flank.
[1239.88 → 1240.82] Actually I saw this
[1240.82 → 1241.44] when it came out.
[1241.50 → 1242.80] It came out I guess
[1242.80 → 1243.26] last summer.
[1244.28 → 1245.08] I hadn't seen the
[1245.08 → 1246.16] movie so it wasn't that
[1246.16 → 1247.02] interesting to me at that
[1247.02 → 1248.18] point, but after I saw the
[1248.18 → 1249.44] movie it's crazy but
[1249.44 → 1252.58] came out on DVD and
[1252.58 → 1253.64] Steve posted this and
[1253.64 → 1255.30] 181 retweets on this
[1255.30 → 1255.48] deal.
[1255.56 → 1256.88] It's just crazy popular.
[1257.30 → 1258.18] For those that don't
[1258.18 → 1259.36] know it's basically the
[1259.36 → 1260.24] plot of the movie
[1260.24 → 1261.80] written in C.
[1261.80 → 1264.44] We also had a version of
[1264.44 → 1265.48] this in JavaScript.
[1266.20 → 1266.58] Right Nathan?
[1267.54 → 1268.94] Yeah there's a gist out
[1268.94 → 1269.56] there we can put in the
[1269.56 → 1270.52] show notes basically.
[1271.52 → 1272.50] And I think that's where
[1272.50 → 1274.40] we discovered console. Group
[1274.40 → 1275.84] which is pretty cool.
[1275.84 → 1276.00] For Firebug?
[1276.66 → 1278.00] Yeah so in Firebug and
[1278.00 → 1279.76] I'm WebKit inspector and
[1279.76 → 1280.88] so forth you can not only
[1280.88 → 1282.04] say console.log but you
[1282.04 → 1284.00] can say console. Group and
[1284.00 → 1284.78] then every subsequent
[1284.78 → 1286.40] console.log will roll up
[1286.40 → 1287.14] under that group.
[1287.86 → 1288.84] So what this guy had done
[1288.84 → 1290.42] was had several console. Groups
[1290.42 → 1291.36] one representing each
[1291.36 → 1292.26] dream level and then
[1292.26 → 1293.16] gone all the way down
[1293.16 → 1295.40] you know to the undefined
[1295.40 → 1297.42] dream space and you
[1297.42 → 1298.72] now and then bubbled
[1298.72 → 1299.44] all the way back up.
[1299.52 → 1300.04] So it's a pretty cool
[1300.04 → 1300.42] example.
[1302.00 → 1303.04] It's a good way I guess
[1303.04 → 1304.08] to teach people that
[1304.08 → 1305.64] know about the movie how
[1305.64 → 1307.16] to read JavaScript and or
[1307.16 → 1307.84] vice versa.
[1309.10 → 1309.78] I was kind of
[1309.78 → 1310.34] disappointed at the
[1310.34 → 1311.02] bottom it didn't have a
[1311.02 → 1311.70] little token though.
[1312.06 → 1312.16] Yeah.
[1312.34 → 1312.46] Totem.
[1313.30 → 1313.56] Well.
[1313.72 → 1314.30] Totem is that what they
[1314.30 → 1314.54] called?
[1314.72 → 1314.92] Yeah.
[1315.44 → 1315.84] Totem.
[1316.64 → 1319.72] Like the beer fest 2011
[1319.72 → 1320.40] site.
[1321.04 → 1321.80] What was the URL to
[1321.80 → 1321.98] that?
[1322.56 → 1323.22] I'll put it in the
[1323.22 → 1323.56] show notes.
[1323.66 → 1324.30] I'll have to find that
[1324.30 → 1324.40] one.
[1324.46 → 1325.42] But that was for a party
[1325.42 → 1326.44] at South by Southwest.
[1327.88 → 1328.92] That was done by Alex
[1328.92 → 1330.68] Guymon of CSS Beauty
[1330.68 → 1334.12] and include N-C-L-U-D
[1334.12 → 1334.82] dot com.
[1336.46 → 1337.98] Made perfect use of
[1337.98 → 1339.48] CSS 3 animation so as
[1339.48 → 1340.62] you scrolled it zoomed in
[1340.62 → 1341.54] further and further and
[1341.54 → 1342.26] further and if you went
[1342.26 → 1342.92] all the way down there
[1342.92 → 1344.00] was a little spinning
[1344.00 → 1344.92] top totem and we
[1344.92 → 1346.30] clicked it zoom all the
[1346.30 → 1347.18] way back out and say
[1347.18 → 1349.34] beer by Southwest or
[1349.34 → 1350.22] something to that
[1350.22 → 1351.38] effect with a little
[1351.38 → 1352.46] sound effect.
[1352.92 → 1353.76] We've seen that effect
[1353.76 → 1354.90] in opening title
[1354.90 → 1356.14] sequences for movies for
[1356.14 → 1356.82] years.
[1357.02 → 1357.62] I wonder if this is
[1357.62 → 1358.08] going to be something
[1358.08 → 1359.52] that this is just a
[1359.52 → 1360.64] novelty if this is going
[1360.64 → 1362.14] to be of use in any
[1362.14 → 1363.24] sort of application
[1363.24 → 1365.06] scenario the zoom into
[1365.06 → 1366.14] the app interface.
[1366.80 → 1368.60] We shall stay tuned.
[1369.30 → 1369.98] Compass Magic.
[1370.24 → 1371.18] We can't get away from
[1371.18 → 1372.76] Sass especially since
[1372.76 → 1374.84] Nathan is on board.
[1375.02 → 1376.20] So Compass Magic extends
[1376.20 → 1377.60] Sass with the power of
[1377.60 → 1378.26] image magic.
[1378.26 → 1378.88] Did you guys see this
[1378.88 → 1379.04] one?
[1380.30 → 1381.12] I remember you
[1381.12 → 1381.84] mentioning it.
[1382.86 → 1384.26] Well it's built on
[1384.26 → 1385.58] R Magic and Image
[1385.58 → 1386.12] Magic.
[1386.30 → 1387.18] Those are the two
[1387.18 → 1388.20] standard tools if you're
[1388.20 → 1389.22] slinging the Ruby and
[1389.22 → 1389.82] want to do anything with
[1389.82 → 1390.50] Image Magic.
[1391.16 → 1392.70] Compass Magic, you know
[1392.70 → 1393.60] Compass supports out of
[1393.60 → 1395.06] the box CSS gradients
[1395.06 → 1397.08] but not all browsers
[1397.08 → 1397.70] support them.
[1397.84 → 1398.88] So this one will
[1398.88 → 1400.56] actually build static
[1400.56 → 1401.88] images based on the
[1401.88 → 1403.52] same linear gradient
[1403.52 → 1405.52] syntax and just compile
[1405.52 → 1406.72] images on the fly so you
[1406.72 → 1407.40] can just ship those
[1407.40 → 1408.44] images with your CSS
[1408.44 → 1409.54] code, and they work in
[1409.54 → 1410.10] any browser.
[1411.72 → 1412.94] That is awesome.
[1413.74 → 1414.58] It's pretty nifty.
[1416.16 → 1417.28] So who wrote this?
[1418.40 → 1420.42] This is from, I knew
[1420.42 → 1420.96] you were going to ask
[1420.96 → 1421.76] that, let me click the
[1421.76 → 1422.04] link.
[1423.80 → 1425.46] Stan Angel off.
[1426.04 → 1426.48] Angel off.
[1426.68 → 1427.74] Not Ash kenos?
[1427.74 → 1430.26] Not Jeremy Ash kenos.
[1430.34 → 1430.90] Not this one.
[1431.72 → 1432.52] There's at least three
[1432.52 → 1433.80] repos in the changelog that
[1433.80 → 1434.84] are not Jeremy Ash kenos.
[1435.84 → 1436.68] This is actually really
[1436.68 → 1439.06] cool because a lot of
[1439.06 → 1440.46] times I catch myself in
[1440.46 → 1441.88] this scenario without this
[1441.88 → 1443.48] just putting a background
[1443.48 → 1447.54] colour being lazy or, you
[1447.54 → 1448.32] know, going in the extra
[1448.32 → 1449.78] stretch of actually doing
[1449.78 → 1450.60] the grading if I really
[1450.60 → 1452.08] want to be nice to the
[1452.08 → 1452.88] browser who don't support
[1452.88 → 1453.06] it.
[1453.30 → 1454.34] You know, all it's doing
[1454.34 → 1455.28] is providing mix-ins,
[1455.44 → 1455.62] right?
[1455.66 → 1456.60] So you can still mix and
[1456.60 → 1457.84] match those standard
[1457.84 → 1458.90] compass mix-ins for the
[1458.90 → 1460.26] linear gradient but just
[1460.26 → 1463.12] also supply a magic
[1463.12 → 1466.80] G-I-C-K namespace to
[1466.80 → 1468.94] mix-in above that one so
[1468.94 → 1470.10] that for older browsers it
[1470.10 → 1470.76] would pick that up.
[1471.04 → 1472.00] So basically it outputs
[1472.00 → 1474.12] like a PNG which is
[1474.12 → 1475.58] immediately re-declared as
[1475.58 → 1478.44] a CSS3 gradient so that if
[1478.44 → 1479.26] the browser doesn't
[1479.26 → 1480.46] understand that CSS3
[1480.46 → 1481.52] gradient it already has in
[1481.52 → 1483.10] its mental model of how
[1483.10 → 1485.04] to paint it to use the
[1485.04 → 1485.92] background image instead?
[1486.50 → 1486.92] Exactly.
[1487.16 → 1487.46] Nice.
[1487.78 → 1488.72] It's a nice little syntax
[1488.72 → 1488.98] too.
[1489.10 → 1491.14] So the example that we
[1491.14 → 1492.44] listed here on the blog is
[1492.44 → 1494.56] magic erase blue which
[1494.56 → 1495.44] sets a default background
[1495.44 → 1496.52] colour for whatever you're
[1496.52 → 1497.98] painting there and then a
[1497.98 → 1499.50] linear gradient you supply
[1499.50 → 1501.66] your colour stops and then
[1501.66 → 1503.76] set your left and right
[1503.76 → 1504.58] corners that will actually
[1504.58 → 1506.10] draw rounded corner images
[1506.10 → 1506.56] for you.
[1507.24 → 1508.66] So I guess next up we had
[1508.66 → 1510.04] jQuery mobile alpha 3.
[1510.04 → 1512.26] which is the pow, pow.
[1512.26 → 1512.28] You excited about this
[1512.28 → 1512.44] one?
[1513.78 → 1514.14] Say what?
[1514.56 → 1515.56] Have you played with this
[1515.56 → 1515.78] one?
[1516.04 → 1517.02] I have a little bit yeah
[1517.02 → 1517.70] it's pretty cool.
[1518.38 → 1520.48] What I like is that it
[1520.48 → 1521.84] takes you know the look
[1521.84 → 1523.58] and feel of I guess
[1523.58 → 1524.54] several different mobile
[1524.54 → 1526.84] OSes, and it tries to kind
[1526.84 → 1528.46] of hit a sweet spot of
[1528.46 → 1530.40] looking good within each
[1530.40 → 1531.32] one without trying to
[1531.32 → 1531.86] look native.
[1533.22 → 1534.84] And I guess the logic
[1534.84 → 1536.34] there I mean I haven't
[1536.34 → 1537.46] talked to the jQuery
[1537.46 → 1538.66] mobile team directly about
[1538.66 → 1539.68] why they chose that way
[1539.68 → 1540.66] but I think it's kind of
[1540.66 → 1542.34] cool because then let's
[1542.34 → 1543.30] say like there's an iOS
[1543.30 → 1544.32] update that changes the
[1544.32 → 1545.90] way buttons look or
[1545.90 → 1546.96] the way you know a
[1546.96 → 1548.10] particular background on
[1548.10 → 1549.46] a type of page looks.
[1549.84 → 1550.64] That way you're not
[1550.64 → 1551.66] scrambling to try to
[1551.66 → 1552.70] update every time because
[1552.70 → 1553.38] you have your own look and
[1553.38 → 1554.32] feel for your app.
[1555.18 → 1557.44] It's you know it looks
[1557.44 → 1559.54] it looks tasteful, yet it's
[1559.54 → 1562.12] not trying to go one to
[1562.12 → 1563.88] one with the OS that it's
[1563.88 → 1564.06] in.
[1565.02 → 1565.86] You know the thing that
[1565.86 → 1567.56] struck me over the alpha 2
[1567.56 → 1568.60] release that was prior to
[1568.60 → 1569.88] this is just the amount
[1569.88 → 1571.58] of speed so the alpha 2
[1571.58 → 1573.06] as you would scroll even
[1573.06 → 1574.28] on the iPhone 4 which is
[1574.28 → 1575.42] quite a beefy mobile
[1575.42 → 1576.54] device you would see the
[1576.54 → 1578.28] chequerboard transparent
[1578.28 → 1579.42] background underneath the
[1579.42 → 1580.80] document for you know a
[1580.80 → 1581.86] ways down the page while
[1581.86 → 1582.60] it was trying to paint the
[1582.60 → 1583.48] document and this one
[1583.48 → 1585.26] seems a lot zippier.
[1585.64 → 1586.04] Yeah I know they've been
[1586.04 → 1587.40] working a lot on speed and
[1587.40 → 1587.98] responsiveness.
[1588.94 → 1589.50] It's got to be a big
[1589.50 → 1590.42] problem to build a mobile
[1590.42 → 1591.52] framework that spans the
[1591.52 → 1592.62] amount of devices that
[1592.62 → 1594.08] they're looking to support
[1594.08 → 1595.66] with a single code base.
[1595.66 → 1597.52] Yeah I mean it's its a
[1597.52 → 1598.10] large undertaking.
[1598.34 → 1600.08] I heard John Remix on a
[1600.08 → 1601.44] another podcast I can't
[1601.44 → 1602.26] remember which one but
[1602.26 → 1603.88] You listen to other
[1603.88 → 1604.52] podcasts?
[1604.82 → 1605.32] I know right?
[1606.76 → 1608.00] I mean I always check this
[1608.00 → 1610.08] one first and then I
[1610.08 → 1611.00] double check and then if
[1611.00 → 1612.08] nothing else is posted on
[1612.08 → 1612.94] the changelog then I go
[1612.94 → 1613.86] listen to other podcasts.
[1614.34 → 1614.70] Good deal.
[1614.78 → 1616.04] But anyway John Remix had
[1616.04 → 1617.36] said you know he's talking
[1617.36 → 1618.42] about the expense that would
[1618.42 → 1619.70] go into testing on every
[1619.70 → 1622.32] mobile OS and how
[1622.32 → 1623.10] many phones you'd have to
[1623.10 → 1624.84] buy and the interviewer was
[1624.84 → 1625.90] saying oh wow, so how do
[1625.90 → 1626.42] you guys do it?
[1626.44 → 1627.82] And he said we buy a
[1627.82 → 1628.64] bunch of mobile phones and
[1628.64 → 1629.76] test on every OS you know
[1629.76 → 1631.66] like they there's no real
[1631.66 → 1633.10] way around it in his
[1633.10 → 1634.08] mind he was saying that's
[1634.08 → 1634.92] something that jQuery mobile
[1634.92 → 1636.92] tries to do so that you as a
[1636.92 → 1638.14] web developer don't have to
[1638.14 → 1640.42] to go, and you know incur that
[1640.42 → 1641.08] cost yourself.
[1641.70 → 1643.18] They shoulder the burden for
[1643.18 → 1643.54] you, huh?
[1644.40 → 1644.76] Yep.
[1645.68 → 1646.82] So how does this change the
[1646.82 → 1647.30] markup?
[1648.00 → 1649.14] Yeah there's a little I mean
[1649.14 → 1650.38] there's somewhat generated
[1650.38 → 1651.06] markup.
[1651.78 → 1653.14] Back to data attributes buddy.
[1653.70 → 1654.00] Boom.
[1654.26 → 1654.72] That's right.
[1655.42 → 1656.62] Yeah so they have you know
[1656.62 → 1658.24] the data dash attribute
[1658.24 → 1661.46] making generous use of that
[1661.46 → 1663.88] to mark which DOM elements
[1663.88 → 1665.18] need to be styled by jQuery
[1665.18 → 1665.46] mobile.
[1666.38 → 1667.36] What's kind of cool though is
[1667.36 → 1669.74] because most I would say all
[1669.74 → 1671.58] mobile browsers all good ones
[1671.58 → 1675.04] anyway understand that the
[1675.04 → 1677.78] what's called attribute
[1677.78 → 1679.34] selector so you can use that
[1679.34 → 1680.58] and not have to worry about
[1680.58 → 1681.76] browsers like IE6 not
[1681.76 → 1682.86] understanding that and so it's
[1682.86 → 1684.64] something you can sprinkle in
[1684.64 → 1686.06] your markup and know that it's
[1686.06 → 1686.82] just going to work.
[1687.36 → 1688.66] Speaking of jQuery you just got
[1688.66 → 1690.42] back from Drupal Con.
[1690.62 → 1691.74] Gave a jQuery talk up there
[1691.74 → 1691.94] right?
[1692.34 → 1692.80] I did.
[1693.48 → 1694.84] What was the turnout at
[1694.84 → 1695.84] Drupal Con this year?
[1696.20 → 1697.04] It was pretty cool.
[1697.20 → 1699.04] It was about 3,000 people total.
[1700.16 → 1701.74] I'm not sure the exact turnout to
[1701.74 → 1703.78] my talk, but it was pretty packed
[1703.78 → 1704.48] so that was cool.
[1704.48 → 1706.24] I talked a little bit about
[1706.24 → 1708.14] formalize and a little bit about
[1708.14 → 1709.86] the jQuery desktop.
[1710.00 → 1712.02] It was just kind of fun to see if
[1712.02 → 1713.00] I could do it desktop in a
[1713.00 → 1713.24] browser.
[1714.42 → 1714.86] So it was good.
[1714.94 → 1716.82] I talked about why you should
[1716.82 → 1718.28] namespace your JavaScript and not
[1718.28 → 1719.90] have a bunch of global functions
[1719.90 → 1721.34] sitting out in the global
[1721.34 → 1721.90] namespace.
[1723.22 → 1724.36] It was pretty cool.
[1724.44 → 1725.22] I'm hoping they'll have the video
[1725.22 → 1727.06] posted soon and let you guys know
[1727.06 → 1727.48] if they do.
[1728.48 → 1729.66] So what got you into Drupal?
[1729.66 → 1732.38] Actually it was my friend Matt
[1732.38 → 1734.38] Farina who does a lot of work in
[1734.38 → 1736.82] Drupal and works for Palantir.net.
[1737.04 → 1738.20] They do big Drupal projects.
[1738.48 → 1739.88] He said there's going to be a
[1739.88 → 1742.16] design for Drupal kind of camp in
[1742.16 → 1743.60] Boston at MIT and you should really
[1743.60 → 1744.10] come speak.
[1744.22 → 1745.50] I was like dude I know nothing
[1745.50 → 1747.70] about Drupal, and I'm not sure if
[1747.70 → 1748.20] I want to use it.
[1748.50 → 1749.76] And he said well you know just come
[1749.76 → 1750.72] and talk on 960.
[1750.88 → 1754.44] So I submitted a talk and one of the
[1754.44 → 1755.26] other guys that was going to be
[1755.26 → 1757.20] there unbeknownst to me had
[1757.20 → 1759.06] already given a talk on 960 at
[1759.06 → 1761.78] several Drupal camps and in
[1761.78 → 1763.00] different countries and so forth.
[1763.06 → 1764.26] So he said hey do you want to just
[1764.26 → 1766.12] like come partner with me and
[1766.12 → 1767.40] pretty much read off my slides.
[1767.48 → 1768.58] And I said yeah that'd be great
[1768.58 → 1768.86] you know.
[1768.98 → 1771.78] So you know it kind of came for the
[1771.78 → 1773.64] talk and stayed for the community.
[1773.92 → 1774.68] It was pretty cool.
[1775.52 → 1776.74] Once I started looking at it and
[1776.74 → 1778.06] wrapped my head around it is you
[1778.06 → 1779.48] know found the theming to be pretty
[1779.48 → 1779.84] intuitive.
[1780.16 → 1783.26] So it's definitely not something I'd
[1783.26 → 1783.92] want to write myself.
[1784.12 → 1785.90] So you know as a front-end guy any
[1785.90 → 1788.38] CMS that kind of helps me is a
[1788.38 → 1788.88] good one to me.
[1789.44 → 1791.10] You're running 960 GS on it?
[1792.90 → 1793.30] Yeah.
[1793.54 → 1795.72] So on my own side I've got it in
[1795.72 → 1795.90] there.
[1796.10 → 1796.88] And they actually launched
[1796.88 → 1799.02] Drupal.org based on 960.
[1799.66 → 1800.94] Stripping out the know the
[1800.94 → 1803.56] CSS classes they didn't need and
[1803.56 → 1805.50] kind of renaming them to what they
[1805.50 → 1805.76] wanted.
[1805.92 → 1808.12] But the grid is there in full
[1808.12 → 1808.46] effect.
[1809.16 → 1809.54] Boom.
[1810.32 → 1811.30] I guess the only thing I want to
[1811.30 → 1813.54] say about that just to plug myself
[1813.54 → 1815.18] for a quick second since there's a
[1815.18 → 1816.46] some loud booms going on.
[1817.40 → 1818.88] Swordforge.net actually runs
[1818.88 → 1820.54] something that's similar to 960 as
[1820.54 → 1821.82] well called Grid Coordinates.
[1822.24 → 1823.36] Grid Coordinates.
[1823.52 → 1824.26] A SaaS project.
[1824.34 → 1825.90] But we talked plenty about SaaS so
[1825.90 → 1827.78] that was just a quick plug but
[1827.78 → 1831.20] bigger in the world is the world of
[1831.20 → 1833.24] open source as it pertains to the
[1833.24 → 1833.52] government.
[1833.92 → 1835.62] We had a post a while back called
[1835.62 → 1837.40] Open Government, and it was
[1837.40 → 1839.38] intended to essentially shine a
[1839.38 → 1842.44] light on OpenGovernment.org which is
[1842.44 → 1844.34] an open source Ruby project headed
[1844.34 → 1846.48] up by Sunlight Foundation and those
[1846.48 → 1847.74] good folks which we actually had an
[1847.74 → 1849.70] episode on a long time back.
[1850.72 → 1852.00] Seems to be a growing space.
[1852.70 → 1854.90] There's a whole conference that I'll
[1854.90 → 1857.70] be attending in Oklahoma City in
[1857.70 → 1861.00] May called Gov20A which will be
[1861.00 → 1863.30] talking a lot about open government
[1863.30 → 1865.30] but we had these guys on the show to
[1865.30 → 1867.50] talk about Open Congress and some of
[1867.50 → 1868.64] their efforts in the Open States
[1868.64 → 1869.02] project.
[1869.24 → 1870.48] It was fascinating to see
[1870.48 → 1873.22] transparency shining a light into our
[1873.22 → 1874.78] government and letting us see a
[1874.78 → 1879.28] little bit more about the gears of
[1879.28 → 1881.58] government and sometimes how scary
[1881.58 → 1882.06] that is.
[1883.62 → 1884.82] I think one cool thing about this is
[1884.82 → 1887.62] just that if you're kind of the kind
[1887.62 → 1889.20] of person who wants to step up,
[1889.40 → 1891.20] maybe just learn about code, you can
[1891.20 → 1893.48] jump into this Rails-based project and
[1893.48 → 1894.68] learn a few things.
[1894.84 → 1896.28] There are tons of API stuff.
[1896.42 → 1898.74] They were pulling stuff from Google and
[1898.74 → 1900.14] many other sources to bring in all this
[1900.14 → 1900.48] data.
[1900.72 → 1903.24] So it's, in my opinion, visually as well
[1903.24 → 1906.38] as for back-end devs, it's quite a nice
[1906.38 → 1908.00] project to just kind of cherry-pick from.
[1908.94 → 1910.10] You know, that's the cool thing about
[1910.10 → 1913.68] having GitHub out there that has not only
[1913.68 → 1915.30] projects that you can go and fork and run
[1915.30 → 1917.72] yourself but live sites that you can go
[1917.72 → 1919.82] and you want a feature on the site, you can
[1919.82 → 1921.90] contribute the feature and give it back.
[1921.90 → 1924.44] And if the patch is accepted, they'll push it
[1924.44 → 1924.76] live.
[1925.00 → 1927.24] I remember, you know, Gem cutter, which became
[1927.24 → 1930.70] the new rubygems.org started out that way.
[1930.80 → 1932.98] You know, we wanted avatar support.
[1933.06 → 1934.22] You go, and you fork it, you add the avatar
[1934.22 → 1936.70] support and boom, it's up in the site in a
[1936.70 → 1937.80] couple of weeks.
[1938.14 → 1938.36] Boom.
[1938.68 → 1941.14] This is broadcast brought to you by boom!
[1941.14 → 1941.22] Boom.
[1944.32 → 1945.64] But this is a fun project.
[1945.86 → 1946.68] I like this a lot.
[1946.86 → 1949.30] I'm a speech empath, so when people start
[1949.30 → 1952.02] using phrases around me, I pick them up.
[1952.10 → 1953.64] So that's not always a good thing.
[1954.82 → 1955.98] That's why I don't hang around with people
[1955.98 → 1956.70] with Tourette's.
[1959.82 → 1960.14] Stylus.
[1962.08 → 1962.74] I don't know.
[1963.88 → 1964.20] Stylus.
[1964.20 → 1967.24] This is one of yours, buddy.
[1968.30 → 1969.14] I know, I know.
[1969.24 → 1970.74] But I'm saying, you know, just in general,
[1970.88 → 1972.38] well, here's the first thing about this,
[1972.42 → 1976.38] is that the CSS preprocessor world,
[1976.66 → 1977.16] a.k.a.
[1977.22 → 1982.66] SAS, LESS, SASS, whatever, has got one more,
[1982.80 → 1984.46] not so much a contender, but, you know,
[1984.80 → 1988.36] contributor to the importance of preprocessing
[1988.98 → 1989.32] CSS.
[1990.26 → 1991.12] And here's the deal.
[1991.12 → 1992.96] There are so many ways to preprocess.
[1994.20 → 1997.32] CSS, and we're talking compass, SAS, LESS JS,
[1997.42 → 1999.46] Stylus, all of these out there.
[2000.44 → 2003.50] It just belies, you know, a broken language,
[2003.78 → 2006.92] something that is just begging for more power,
[2007.10 → 2007.36] Captain.
[2008.50 → 2010.64] Yeah, I think, you know, when CSS was created,
[2010.82 → 2012.76] the idea was like, well, let's treat designers
[2012.76 → 2013.46] with kid gloves.
[2013.58 → 2016.02] But I think, you know, more and more things are
[2016.02 → 2018.86] shifting from web pages and websites to web
[2018.86 → 2019.38] applications.
[2020.28 → 2022.38] You know, front-end developers slash designers
[2022.38 → 2025.44] are wanting that power in more of a programmatic
[2025.44 → 2025.92] environment.
[2027.10 → 2030.62] So by happenstance, Adam, you retweeted a Feldman tweet
[2030.62 → 2034.36] over the weekend from, I guess, a year ago,
[2034.44 → 2035.00] where he said,
[2035.68 → 2039.18] real web devs code, or real web designers code,
[2039.28 → 2040.22] always have, always will.
[2040.22 → 2044.94] That was the leading message in a Southwest-Southwest
[2044.94 → 2047.10] panel I attended last weekend.
[2047.80 → 2051.86] Pretty much the same name, designers who can't code,
[2052.22 → 2052.86] no excuse.
[2053.24 → 2055.04] But what I found interesting, I went there, you know,
[2055.04 → 2058.12] looking for, you know, any hint of compass, SAS,
[2058.20 → 2061.28] any sort of, you know, even jQuery frameworks and things.
[2061.42 → 2065.02] And, you know, the skewed audience of the room,
[2065.14 → 2067.68] their definition of code was getting out of Photoshop
[2067.68 → 2069.04] and actually writing the markup.
[2069.26 → 2073.40] So I think there's this slider between Adobe world
[2073.40 → 2075.36] and what goes in the browser.
[2076.00 → 2079.36] And I think we've made it our mission to get more
[2079.36 → 2083.38] developer experience into the hands of designers
[2083.38 → 2085.14] and also, you know, on the other end,
[2085.52 → 2090.12] try to help developers not make their pages suck as much.
[2090.86 → 2092.60] I mean, there's only so much automation you can do
[2092.60 → 2096.46] in the SAS slash, you know, pre-processing world.
[2096.46 → 2101.42] But definitely, I think that it kind of aggravates me a little bit
[2101.42 → 2104.48] to see such a phenomenal designer have no idea how to make it
[2104.48 → 2105.70] a real webpage.
[2106.62 → 2108.62] You know, at the end of the day, you can't teach
[2108.62 → 2114.12] or you can't, you know, program things like white space
[2114.12 → 2116.62] and vertical rhythm with your typography and colour theory
[2116.62 → 2117.34] and some of these things.
[2117.46 → 2120.62] Like, even the white space thing, 960 does a great job
[2120.62 → 2124.26] of giving you a groove, but it still takes a human eye
[2124.26 → 2127.68] to figure out, you know, the elements of a good design.
[2127.78 → 2131.12] I guess what frustrates me is curmudgeon-y designers
[2131.12 → 2133.14] that don't want to learn new tools
[2133.14 → 2136.46] and would rather command C, command V either way,
[2137.34 → 2139.50] you know, just brute force to a new design
[2139.50 → 2140.92] instead of working a little faster
[2140.92 → 2143.58] and putting more brainwaves, as you said earlier,
[2143.78 → 2145.88] on the actual design itself.
[2146.20 → 2147.80] So I mostly agree with that,
[2147.86 → 2150.60] but I'll play devil's advocate for a second here.
[2151.38 → 2154.40] I've worked with people that are phenomenal designers
[2154.40 → 2156.00] that do know how to code,
[2156.08 → 2158.08] and it translates to, as a front-end developer,
[2158.08 → 2160.48] if you are handed a design they've done,
[2161.16 → 2162.44] you know, it's super easy to slice it up
[2162.44 → 2163.86] because they know the medium,
[2164.00 → 2166.08] and they're designing for what's possible
[2166.68 → 2167.58] and what you can accomplish.
[2168.26 → 2171.44] I've also worked with guys that are amazing designers,
[2171.66 → 2173.02] understand everything about typography
[2173.02 → 2174.70] and white space and texture and so forth,
[2175.12 → 2176.26] who would be the first to tell you
[2176.26 → 2177.52] that they don't code.
[2178.40 → 2179.64] And some of those, though,
[2179.70 → 2182.14] really challenging to translate into code
[2182.14 → 2183.76] when you are handed that type of design
[2183.76 → 2185.44] is actually kind of fun
[2185.44 → 2187.08] because here's somebody that's not designing
[2187.08 → 2188.38] with constraints in mind at all,
[2189.16 → 2191.00] and it was not only challenging
[2191.00 → 2192.82] but fun to bring that to fruition
[2192.82 → 2195.66] as a web page, you know, in the browser
[2195.66 → 2197.10] and say, look, there's no compromise
[2197.10 → 2198.06] on the design at all,
[2198.14 → 2199.54] but, man, I really had to think kind of,
[2200.10 → 2201.58] how am I going to make some of these things work
[2201.58 → 2203.52] because the person handing me the design
[2203.52 → 2206.66] didn't put in place
[2206.66 → 2208.12] any code constraints on themselves.
[2208.36 → 2209.58] Yeah, I've heard that argument in the past.
[2209.64 → 2210.90] I guess I've seen people
[2210.90 → 2212.98] that have pulled off both extremely well,
[2213.32 → 2214.22] and they're rare,
[2214.82 → 2216.16] Elliott J. Stocks being one of them,
[2216.46 → 2217.36] but, you know,
[2217.40 → 2219.20] that really get both ends of it,
[2219.26 → 2220.18] so I guess I've just,
[2220.60 → 2221.72] I'm not sold on the idea
[2221.72 → 2224.08] that you're mutually exclusive,
[2224.24 → 2226.06] that you can be a great designer,
[2226.06 → 2228.22] and suddenly if you start learning
[2228.22 → 2231.34] the development medium
[2231.34 → 2231.90] that, you know,
[2232.06 → 2233.32] things are going to fall out of your head
[2233.32 → 2234.96] or you start putting artificial constraints
[2234.96 → 2236.78] on your design.
[2236.78 → 2238.26] Yeah, I think it would definitely behoove
[2238.26 → 2240.34] any purely visual designer
[2240.34 → 2241.76] to learn more about the medium
[2241.76 → 2242.36] they're working in,
[2242.44 → 2244.56] whether that be knowing paper weight
[2244.56 → 2245.12] and, you know,
[2245.80 → 2247.82] the stock of what's going to be printed
[2247.82 → 2249.32] or, you know, in our case,
[2249.56 → 2251.00] how it's going to translate into the web.
[2251.20 → 2252.38] I think that's the biggest one.
[2252.38 → 2253.62] You know, I've worked with a lot
[2253.62 → 2255.36] of really, really gifted print designers,
[2255.82 → 2257.66] and, you know,
[2257.68 → 2259.24] I got, I started cutting my teeth
[2259.24 → 2260.94] in print design years ago,
[2261.22 → 2263.52] but working with those guys,
[2263.64 → 2264.44] if they don't understand,
[2264.54 → 2265.42] as you say, the medium,
[2265.68 → 2266.82] they don't understand, you know,
[2267.46 → 2270.58] something so basic as browser width
[2270.58 → 2272.58] and screen size, screen resolution,
[2273.14 → 2275.14] then it's just very hard to translate
[2275.14 → 2277.38] even what they do know of design
[2277.38 → 2278.24] into that new medium.
[2278.24 → 2281.54] You know, one of the best
[2281.54 → 2282.56] that I know of, at least,
[2282.68 → 2283.98] print designers turned web developer,
[2284.22 → 2285.38] sorry, web designer,
[2285.96 → 2286.68] correct myself there,
[2286.80 → 2289.88] but his name is Makes,
[2290.10 → 2291.10] works at Personified,
[2291.32 → 2292.40] and I'm sure that you guys
[2292.40 → 2294.44] will echo this whenever I shut up,
[2294.58 → 2297.90] but he's by far one of the best
[2297.90 → 2300.30] print designers turned web designer
[2300.30 → 2302.68] that I just adore his designs.
[2303.88 → 2304.74] Yeah, I think, you know,
[2304.76 → 2306.54] when you have that background,
[2306.54 → 2307.50] you know, or, you know,
[2307.52 → 2308.88] take somebody like Jason Santa maria,
[2309.06 → 2310.70] too, that went to school for design,
[2311.34 → 2312.94] has, you know, done the letterpress,
[2313.12 → 2314.70] knows, you know, the medium
[2314.70 → 2315.82] through and through in the history
[2315.82 → 2318.14] behind every typographical decision
[2318.14 → 2318.88] he makes, you know,
[2319.18 → 2320.22] I think that does translate
[2320.22 → 2321.16] into the web, and, you know,
[2321.22 → 2324.06] somebody like, like you were saying,
[2324.46 → 2326.86] that can, it gives you a depth,
[2327.08 → 2328.46] a richness to what you produce
[2328.46 → 2330.08] that you probably wouldn't see
[2330.08 → 2330.76] if you didn't have
[2330.76 → 2331.48] that type of background.
[2331.48 → 2333.76] I always feel like a hack
[2333.76 → 2335.06] when I try to do any type of
[2335.06 → 2336.86] grunge or textured background.
[2337.04 → 2338.56] I'm like, I can do it,
[2338.64 → 2339.64] but I never feel like,
[2340.14 → 2340.88] I always feel like I'm trying
[2340.88 → 2341.48] to pass it off,
[2341.56 → 2342.30] I'm like, does this look
[2342.30 → 2343.30] grungy enough?
[2343.32 → 2344.30] Because I don't know.
[2345.12 → 2346.42] So this entire conversation
[2346.42 → 2348.62] kind of popped up around Stylus,
[2348.70 → 2350.48] which was one of the latest
[2350.48 → 2351.38] creations of Learn Boost.
[2351.48 → 2352.74] We've covered, I don't know,
[2352.82 → 2354.38] how many Learn Boost projects
[2354.38 → 2354.84] have we covered?
[2355.82 → 2356.62] Ah, Learn Boost,
[2356.70 → 2358.22] and even TJ on his own.
[2359.18 → 2359.48] Yeah.
[2360.20 → 2362.12] But Stylus has a beautiful homepage,
[2362.50 → 2363.50] so the next question I have
[2363.50 → 2365.60] for you, and which is sort of loaded,
[2366.26 → 2368.08] is how does Stylus' homepage
[2368.08 → 2370.42] stack up against the top 10 reasons
[2370.42 → 2371.62] why I won't use
[2371.62 → 2372.82] your open source project?
[2373.18 → 2374.42] I feel like I need to set
[2374.42 → 2375.90] a big fat caveat on that.
[2376.68 → 2377.92] If you read the first paragraph
[2377.92 → 2378.62] of the post,
[2378.74 → 2379.78] it was in the snarkiest,
[2379.90 → 2380.82] the link bait headline,
[2381.38 → 2382.36] proves to be,
[2382.54 → 2384.12] but hey, it did drive some traffic.
[2384.22 → 2384.84] I was happy with that.
[2386.06 → 2386.68] Just some pointers.
[2386.68 → 2387.72] People don't read on the web.
[2387.72 → 2388.50] People don't read.
[2388.58 → 2389.38] They read headlines,
[2389.50 → 2390.68] they retweet, you know,
[2390.78 → 2392.00] and even Dr. Nick,
[2392.06 → 2393.02] when we had him on the show
[2393.02 → 2393.68] a couple of shows ago,
[2393.74 → 2393.88] he's like,
[2393.92 → 2394.08] you know,
[2394.10 → 2394.90] I only read the first couple,
[2395.60 → 2398.66] but I always, you know,
[2398.74 → 2399.66] am suspect of somebody
[2399.66 → 2400.86] that's tweeting me
[2400.86 → 2402.24] when his wife's having a baby, too,
[2402.34 → 2403.70] so I doubt he was actually
[2403.70 → 2404.70] reading the post.
[2405.24 → 2406.88] But 10 things that you can do
[2406.88 → 2409.42] to get the word out
[2409.42 → 2411.96] about your open source project.
[2412.24 → 2414.54] So not necessarily a litmus test.
[2414.54 → 2415.08] So what's funny is,
[2415.08 → 2416.38] we've had loads of mail
[2416.38 → 2418.60] at ping at the changelog.com
[2418.60 → 2419.74] if you would like to submit.
[2420.18 → 2420.58] Name and town,
[2420.66 → 2421.22] name and town,
[2421.74 → 2422.92] if you wish to opine.
[2424.50 → 2424.84] You know,
[2424.96 → 2428.32] top 10 reasons of submitting your,
[2428.60 → 2431.44] or to promote your open source project.
[2431.68 → 2432.10] It's funny,
[2432.16 → 2432.96] we get submissions now
[2432.96 → 2433.46] that say, you know,
[2433.50 → 2435.76] here's my 10-point checklist,
[2435.90 → 2436.66] and I think you'll find
[2436.66 → 2437.94] that I meet all of these criteria.
[2439.14 → 2439.48] It's like,
[2439.54 → 2439.98] well, it's not,
[2440.18 → 2440.86] I mean, I appreciate it.
[2440.86 → 2441.78] It started a movement, dude.
[2442.36 → 2442.82] I guess.
[2442.84 → 2443.94] Yeah, you get like 200 points
[2443.94 → 2444.84] for spelling your name right
[2444.84 → 2445.70] on the SAT, right?
[2445.70 → 2445.94] Yes.
[2445.94 → 2446.32] There you go.
[2446.34 → 2446.76] Read me.
[2446.82 → 2447.18] There you go.
[2448.98 → 2452.34] So it's not meant to be a filter.
[2452.64 → 2454.34] What it is meant to guide you
[2454.34 → 2455.82] in just practical things
[2455.82 → 2456.50] that you can do
[2456.50 → 2458.82] to expose the world
[2458.82 → 2460.08] to your great open source project.
[2460.08 → 2460.64] Because, you know,
[2460.70 → 2461.96] we scratch a scratch
[2461.96 → 2464.06] on a scratch on open source,
[2464.16 → 2466.08] and we just can't cover it all.
[2466.24 → 2467.40] We're drinking from this fire hose,
[2467.40 → 2468.66] and we pick up things
[2468.66 → 2469.78] that interest us.
[2469.86 → 2471.26] And for the guys out there
[2471.26 → 2472.36] that say that we cover
[2472.36 → 2473.26] too much Ruby and JavaScript,
[2473.50 → 2474.12] well, you know,
[2474.20 → 2474.86] if you know Python,
[2474.98 → 2475.40] hey, contribute.
[2475.48 → 2476.22] Or in this case,
[2476.50 → 2478.86] this episode's a big,
[2479.12 → 2480.78] gigantic gorge of SaaS talk
[2480.78 → 2482.14] and front-end talk.
[2482.54 → 2483.52] Yeah, this is the
[2483.52 → 2484.82] Changeling Design Edition
[2484.82 → 2485.56] is what this one's
[2485.56 → 2486.34] going to go out as.
[2487.26 → 2487.74] But nonetheless,
[2488.04 → 2489.84] this post was,
[2490.80 → 2491.34] I've been talking
[2491.34 → 2492.38] with John Long about Serve.
[2492.44 → 2493.38] He was on the last podcast
[2493.38 → 2495.24] with us, 05.2.
[2495.24 → 2496.66] But, you know,
[2496.72 → 2497.92] we actually took this list
[2497.92 → 2498.74] and started comparing
[2498.74 → 2500.80] what we want Serve's homepage
[2500.80 → 2502.16] to be in comparison
[2502.16 → 2502.96] to what this is
[2502.96 → 2504.62] and just does the project add up.
[2504.66 → 2505.52] So I think this truly
[2505.52 → 2506.38] does have some legs.
[2506.48 → 2506.84] And you're right,
[2507.00 → 2508.74] the people don't read,
[2508.90 → 2510.48] the headline totally,
[2510.58 → 2511.00] you know,
[2511.48 → 2511.90] painted the world
[2511.90 → 2512.56] for this post.
[2512.68 → 2514.02] Not that it's not creditable,
[2514.12 → 2515.42] but it certainly gave it
[2515.42 → 2516.02] a lot of legs
[2516.02 → 2516.90] and sort of controversy
[2516.90 → 2517.74] and sort of conversations.
[2517.86 → 2518.56] But I honestly think
[2518.56 → 2520.24] that this is extremely helpful.
[2521.04 → 2521.72] Well, if you're not
[2521.72 → 2522.58] turning anybody off,
[2522.64 → 2523.60] you're not turning anybody on,
[2523.60 → 2525.64] I guess is the takeaway.
[2526.26 → 2527.34] So I'm glad that,
[2527.36 → 2527.60] you know,
[2527.96 → 2528.68] a couple of folks
[2528.68 → 2530.06] at least have sent me
[2530.06 → 2530.82] private messages
[2530.82 → 2531.84] that, you know,
[2532.50 → 2532.96] they went out
[2532.96 → 2533.92] and created a homepage
[2533.92 → 2534.66] for their project
[2534.66 → 2536.70] just after reading this post,
[2536.78 → 2538.68] which makes me happy.
[2538.94 → 2539.82] I'd be even happier
[2539.82 → 2541.74] if they use 960 grid system
[2541.74 → 2543.72] on said post.
[2544.38 → 2545.10] Well, actually,
[2545.76 → 2546.10] you know,
[2546.18 → 2547.30] at the time you wrote
[2547.30 → 2547.76] that post,
[2547.98 → 2549.50] Formal S was out there.
[2549.58 → 2550.24] It was on GitHub.
[2550.48 → 2551.96] It had multiple library support
[2551.96 → 2552.34] or whatever,
[2552.48 → 2553.82] but there's no homepage.
[2554.28 → 2555.40] So that's kind of
[2555.40 → 2555.92] what spurred me
[2555.92 → 2556.94] to make a homepage for it.
[2556.98 → 2557.44] There you go.
[2557.52 → 2557.64] You know,
[2557.70 → 2559.26] and here's the last point on that.
[2559.28 → 2560.10] And the reason I said this,
[2560.14 → 2561.32] and I actually had a tweet
[2561.32 → 2561.88] back and forth
[2561.88 → 2562.62] with Ryan Bates
[2562.62 → 2563.60] who runs the excellent,
[2563.68 → 2565.16] most excellent railscast.com.
[2565.22 → 2565.90] So if you came into
[2565.90 → 2567.56] the Rails community
[2567.56 → 2569.60] after he started that,
[2569.64 → 2570.30] I'm sure that you
[2570.30 → 2571.48] cut your teeth
[2571.48 → 2573.94] on those awesome screencasts
[2573.94 → 2574.48] where he walks you
[2574.48 → 2575.10] through different parts
[2575.10 → 2575.46] of Rails.
[2575.60 → 2576.42] But, you know,
[2576.54 → 2577.74] we were going back and forth
[2577.74 → 2578.76] on Hacker News
[2578.76 → 2579.52] where he said,
[2579.74 → 2581.06] basically,
[2581.18 → 2582.04] I don't buy into
[2582.04 → 2583.18] the whole SEO argument
[2583.18 → 2583.80] of why you need
[2583.80 → 2585.92] a homepage for your project
[2585.92 → 2586.98] because, you know,
[2587.02 → 2587.94] I searched for Cancan,
[2588.12 → 2589.14] which is one of his projects,
[2589.42 → 2590.54] and, you know,
[2590.58 → 2592.34] it's an ordinary term, right?
[2592.38 → 2593.18] It's a dance, right?
[2593.66 → 2594.32] Form a theatre,
[2594.58 → 2596.60] and yet his GitHub project
[2596.60 → 2599.34] is the first hit on Google.
[2600.50 → 2602.28] But my retort was,
[2602.36 → 2602.62] you know,
[2603.16 → 2603.70] that's true,
[2603.82 → 2605.20] but then you have to know
[2605.20 → 2605.90] what you're searching for.
[2605.98 → 2606.68] But if I search for
[2606.68 → 2607.40] Ruby authorization,
[2607.72 → 2609.06] which is what Cancan provides,
[2610.16 → 2611.62] the only hit on the first page
[2611.62 → 2612.02] of Google
[2612.02 → 2613.36] is a blog post
[2613.36 → 2614.66] not written by him,
[2614.84 → 2615.64] but that's outlining
[2615.64 → 2616.58] how much they love Cancan.
[2617.50 → 2618.36] That's really what
[2618.36 → 2619.60] the change log's doing.
[2621.02 → 2621.84] We're doing nothing
[2621.84 → 2623.32] but shining a light
[2623.32 → 2624.70] on other people's projects,
[2624.84 → 2625.10] right?
[2625.12 → 2626.44] We're just trying to expose
[2626.44 → 2627.20] the great work
[2627.20 → 2627.56] that you,
[2627.62 → 2627.96] the listeners,
[2627.96 → 2628.56] are doing.
[2629.30 → 2632.36] And so part of how we do that
[2632.36 → 2633.68] is we take your project,
[2633.68 → 2635.64] we take your witty
[2635.64 → 2637.38] yet poorly SEO'd
[2637.38 → 2638.40] project description,
[2638.76 → 2639.68] and we turn it into
[2639.68 → 2641.72] a sometimes a link bait headline.
[2641.84 → 2643.46] If we can work HTML5 in there,
[2643.58 → 2644.46] it works really well.
[2645.54 → 2646.44] Speaking of which,
[2646.62 → 2647.78] HTML5 boilerplate
[2647.78 → 2649.66] was just hit 1.0
[2649.66 → 2650.52] and was updated today.
[2650.74 → 2651.22] Boom!
[2651.56 → 2652.46] Paul Irish needs to come
[2652.46 → 2652.84] on the show.
[2652.92 → 2653.80] I saw him at Southwest.
[2654.00 → 2654.48] He's promised.
[2654.84 → 2656.82] So we'll have to start
[2656.82 → 2657.76] turning the screws on that.
[2657.76 → 2658.94] I have to put that into,
[2659.04 → 2661.30] what was that .ly service
[2661.30 → 2663.46] we used for getting
[2663.46 → 2664.04] Sanatory?
[2664.04 → 2664.60] Probably not.
[2664.98 → 2665.96] It might not even be up
[2665.96 → 2666.38] at this point.
[2666.46 → 2667.32] That whole domain's Libya.
[2667.76 → 2668.40] Oh, that's true.
[2669.24 → 2669.80] But just to complete
[2669.80 → 2670.32] the thought of that,
[2670.40 → 2671.20] what we're doing is just
[2671.20 → 2673.02] pointing traffic
[2673.02 → 2673.82] at your project
[2673.82 → 2675.78] and then over time,
[2676.28 → 2676.68] of course,
[2676.74 → 2677.52] your GitHub project's
[2677.52 → 2678.34] going to be the number one
[2678.34 → 2679.58] hit for your project
[2679.58 → 2680.32] on Google,
[2680.50 → 2681.44] and that's the way
[2681.44 → 2681.92] we want it.
[2682.02 → 2682.54] We just want people
[2682.54 → 2683.36] to know about your project.
[2684.06 → 2684.58] So to add some weight
[2684.58 → 2685.08] to that argument,
[2685.24 → 2685.86] I just did the search
[2685.86 → 2686.58] for formalize,
[2686.74 → 2687.34] and other than
[2687.34 → 2689.08] the definition inline
[2689.08 → 2691.28] from the dictionary.com,
[2691.78 → 2692.54] the number one result
[2692.54 → 2693.44] is my blog post,
[2693.54 → 2694.58] and then number four
[2694.58 → 2695.68] down is formalized me,
[2696.40 → 2696.98] and if you search
[2696.98 → 2697.82] for form CSS,
[2698.32 → 2699.70] mine's number six.
[2700.94 → 2701.92] So there you go.
[2702.00 → 2702.56] Great points.
[2702.68 → 2703.24] You need to blog
[2703.24 → 2704.40] about your stuff too.
[2705.06 → 2706.26] That's an excellent point.
[2707.28 → 2707.62] And I just,
[2707.74 → 2707.92] I mean,
[2707.94 → 2709.66] I love how you owned
[2709.66 → 2711.94] a word of the English language.
[2712.68 → 2713.70] I'm just going to take,
[2713.86 → 2714.20] you know,
[2714.32 → 2715.30] ordinary word,
[2715.30 → 2715.70] and I'm going to make
[2715.70 → 2716.36] a project out of it,
[2716.40 → 2717.52] and I will be number one
[2717.52 → 2718.06] in PageRank.
[2718.72 → 2719.04] Well,
[2719.20 → 2719.74] to be fair,
[2719.82 → 2720.72] I did search
[2720.72 → 2721.14] and make sure
[2721.14 → 2721.60] that nobody else
[2721.60 → 2722.04] had a project
[2722.04 → 2722.58] by that name.
[2722.76 → 2723.20] Did you really?
[2723.78 → 2725.32] It's like the new
[2725.32 → 2726.08] trademark search
[2726.08 → 2726.98] for open source stuff,
[2727.02 → 2727.24] you know?
[2727.86 → 2728.66] What's funny is that
[2728.66 → 2730.36] there was a Java library
[2730.36 → 2731.02] called jQuery
[2731.02 → 2732.10] before John Rejig
[2732.10 → 2732.94] made it into
[2732.94 → 2733.80] a JavaScript library,
[2734.26 → 2734.94] and I think they had
[2734.94 → 2735.82] to like to change their name
[2735.82 → 2736.80] or kill the project
[2736.80 → 2737.22] or something,
[2737.38 → 2738.16] but I mean,
[2738.20 → 2738.62] there's no way
[2738.62 → 2739.06] you're going to find
[2739.06 → 2739.54] that one now
[2739.54 → 2740.10] when you search.
[2741.06 → 2741.32] You know,
[2741.34 → 2741.70] it's funny.
[2741.86 → 2743.18] I come across repos
[2743.18 → 2743.50] all the time
[2743.50 → 2744.08] on GitHub that,
[2744.08 → 2744.46] you know,
[2745.24 → 2746.24] formally so-and-so
[2746.24 → 2747.18] because there was
[2747.18 → 2748.24] this other project
[2748.24 → 2748.70] out there,
[2748.76 → 2748.98] right?
[2749.14 → 2749.68] We even talked
[2749.68 → 2750.14] about that
[2750.14 → 2751.34] in Hudson
[2751.34 → 2752.34] that became Jenkins.
[2753.04 → 2754.46] The name they wanted
[2754.46 → 2754.94] was Alfred.
[2755.18 → 2755.72] There was already
[2755.72 → 2756.66] that Alfred app,
[2756.76 → 2757.62] which you like,
[2757.70 → 2757.86] Nathan.
[2758.40 → 2758.66] Yeah,
[2758.66 → 2759.04] it's awesome.
[2760.26 → 2760.68] Basically,
[2760.88 → 2761.96] Quicksilver on steroids.
[2763.60 → 2764.68] Quicksilver on steroids
[2764.68 → 2765.58] or as,
[2766.42 → 2767.50] was it,
[2767.68 → 2768.18] I think it was
[2768.18 → 2768.94] Brandon Mathis
[2768.94 → 2769.74] was talking about
[2769.74 → 2770.08] how,
[2771.12 → 2771.46] you know,
[2771.62 → 2771.88] if,
[2773.20 → 2774.32] you know,
[2775.00 → 2775.98] I guess Alfred
[2775.98 → 2776.76] was a tricycle
[2776.76 → 2777.52] and Launch Bar
[2777.52 → 2779.48] was a motorcycle
[2779.48 → 2781.18] with a rocket pack.
[2782.34 → 2783.06] Launch Bar is my favourite.
[2783.36 → 2784.18] I don't want a rocket pack.
[2784.28 → 2784.88] I just need something
[2784.88 → 2786.54] getting me quickly
[2786.54 → 2787.66] from point A to point B
[2787.66 → 2788.44] just locally.
[2788.84 → 2789.00] Well,
[2789.02 → 2790.40] Alfred's not open source,
[2790.50 → 2791.20] but since we're talking
[2791.20 → 2791.50] about it,
[2791.50 → 2792.40] I use Launch Bar
[2792.40 → 2793.80] and the only reason
[2793.80 → 2794.58] I haven't switched
[2794.58 → 2795.30] is because
[2795.30 → 2796.72] I like to hit
[2796.72 → 2799.02] Command-Alt-Return,
[2799.44 → 2800.24] which basically
[2800.24 → 2801.08] gives me the last
[2801.08 → 2801.98] 25
[2801.98 → 2805.44] clipboard history,
[2805.70 → 2806.06] basically.
[2806.12 → 2806.56] And that's the only
[2806.56 → 2807.22] reason I don't move
[2807.22 → 2808.04] because I love,
[2808.58 → 2809.42] I use so much
[2809.42 → 2810.16] my clipboard history,
[2810.24 → 2810.80] especially if you're
[2810.80 → 2811.90] like copying and pasting code
[2811.90 → 2814.10] or you're writing something
[2814.10 → 2814.82] and you kind of
[2814.82 → 2815.70] need to go back
[2815.70 → 2816.00] in history
[2816.00 → 2816.82] with what you copied.
[2816.82 → 2817.66] It's been
[2817.66 → 2819.12] really nice for me,
[2819.26 → 2819.40] like,
[2820.38 → 2821.08] tons of stuff.
[2822.54 → 2822.94] Yeah,
[2822.94 → 2823.62] I've got the same shortcut
[2823.62 → 2825.36] wired up to Command-Slash.
[2825.44 → 2826.50] I get my clipboard history.
[2826.60 → 2826.86] It's really,
[2827.02 → 2827.24] really cool.
[2827.80 → 2829.20] So you use Launch Bar as well?
[2829.84 → 2831.08] I am a Launch Bar guy.
[2831.22 → 2831.46] Yeah.
[2831.58 → 2831.94] Definitely.
[2832.50 → 2833.26] And the only reason
[2833.26 → 2834.18] I think it's because
[2834.18 → 2835.08] it came with Mac Heist,
[2835.78 → 2838.38] which was the precursor
[2838.38 → 2839.38] to the new AppSumo.
[2839.58 → 2840.04] Have you guys seen
[2840.04 → 2840.60] all these deals?
[2841.72 → 2843.62] That's where we got our...
[2843.62 → 2845.06] Changelog Sticker Mule stickers.
[2847.72 → 2849.10] So the show did have a sponsor.
[2850.58 → 2851.26] Oh, actually,
[2851.26 → 2851.42] no,
[2851.48 → 2852.24] we paid them money.
[2852.24 → 2853.60] But Sticker Mule,
[2853.66 → 2854.26] if you're listening,
[2854.60 → 2855.66] we know that you're fans
[2855.66 → 2856.02] of the show
[2856.02 → 2858.18] because I have a tweet
[2858.18 → 2859.42] to back that up.
[2860.98 → 2861.66] We would love it
[2861.66 → 2862.32] to run at these.
[2862.50 → 2863.34] We're holding you to it.
[2864.92 → 2865.26] Cool.
[2865.36 → 2866.42] That's it for this
[2866.42 → 2867.98] special design edition
[2867.98 → 2868.68] of the Changelog.
[2868.74 → 2869.18] Do you want to throw
[2869.18 → 2870.12] in that one last thing,
[2870.18 → 2871.02] which is how to style
[2871.02 → 2872.14] Firefox specifically?
[2872.96 → 2873.82] Oh, dude.
[2874.30 → 2874.84] We can put that
[2874.84 → 2875.38] in the show notes.
[2875.38 → 2875.52] I forgot all about that.
[2875.78 → 2876.16] So, yeah,
[2876.26 → 2876.84] just like,
[2876.94 → 2877.30] you know,
[2877.30 → 2878.34] what was the other thing
[2878.34 → 2879.20] that we learned about
[2879.20 → 2880.94] the group
[2880.94 → 2882.08] and console.
[2882.34 → 2882.90] Who knows how long
[2882.90 → 2883.44] that's been out
[2883.44 → 2884.82] in WebKit
[2884.82 → 2886.62] or Firebug.
[2886.66 → 2887.24] Firebug, yeah.
[2887.34 → 2887.54] You know,
[2887.60 → 2888.22] we've been doing this
[2888.22 → 2888.60] for years
[2888.60 → 2889.54] and you learn
[2889.54 → 2890.26] something every day.
[2890.56 → 2891.98] You found out
[2891.98 → 2892.80] a way to target
[2892.80 → 2894.14] Firefox today
[2894.14 → 2895.30] without adding a class
[2895.30 → 2896.32] to the HTML
[2896.32 → 2896.98] or body tags.
[2897.34 → 2897.48] Yeah,
[2897.56 → 2898.54] so don't go overboard
[2898.54 → 2899.02] with this,
[2899.08 → 2899.50] but if you need
[2899.50 → 2900.42] to do slight tweaks,
[2900.56 → 2900.96] you can say
[2900.96 → 2902.72] Atmos document
[2902.72 → 2903.36] space
[2903.36 → 2905.12] URL-prefix
[2905.12 → 2906.24] with parentheses
[2906.24 → 2907.16] and you can pass
[2907.16 → 2908.18] in your URL
[2908.18 → 2909.60] or you can leave it blank
[2909.60 → 2910.32] and it'll just apply
[2910.32 → 2910.96] to whatever page
[2910.96 → 2911.76] it happens on.
[2912.40 → 2912.96] And then within there
[2912.96 → 2914.16] you just put your styles
[2914.16 → 2914.74] like span,
[2915.42 → 2915.78] colour,
[2915.86 → 2916.12] black,
[2916.26 → 2916.40] font,
[2916.46 → 2916.58] weight,
[2916.84 → 2917.20] whatever,
[2917.40 → 2917.62] bold.
[2918.14 → 2918.88] So we'll have a little,
[2919.44 → 2919.86] we'll have a link
[2919.86 → 2920.68] to that in the show notes
[2920.68 → 2922.68] and a gist, probably.
[2923.54 → 2924.74] And as my wife would say,
[2924.98 → 2925.94] as my wife would say,
[2926.58 → 2927.44] yet you've never picked up
[2927.44 → 2927.82] any chicks
[2927.82 → 2928.42] with these skills.
[2930.06 → 2930.64] Says who?
[2931.12 → 2931.52] True.
[2932.40 → 2933.42] But it's the skills
[2933.42 → 2934.32] that pay the bills.
[2934.86 → 2935.32] That's true.
[2937.02 → 2937.82] I'm going to steal
[2937.82 → 2938.54] that bit of yours
[2938.54 → 2939.92] as you might like
[2939.92 → 2940.36] to know them.
[2941.06 → 2941.32] Food,
[2941.46 → 2941.62] shelter,
[2941.68 → 2942.02] and clothing.
[2943.12 → 2943.36] Yup,
[2943.40 → 2943.56] yup.
[2944.24 → 2945.20] That's it for a special
[2945.20 → 2946.18] design edition
[2946.18 → 2946.82] of the Changelog.
[2946.88 → 2947.14] Thanks,
[2947.50 → 2948.30] Mr. Nathan Smith
[2948.30 → 2949.18] for joining us.
[2949.36 → 2949.60] Yes,
[2949.62 → 2949.72] sir.
[2949.76 → 2950.14] Thank you.
[2950.84 → 2951.56] Thank you for having me.
[2951.94 → 2952.24] Cool.
[2953.32 → 2954.46] And we'll see you next time.
[2954.46 → 2954.52] Bye.
[2954.52 → 2954.60] Bye.
[2954.60 → 2954.62] Bye.
[2954.62 → 2954.70] Bye.
[2954.70 → 2954.72] Bye.
[2954.72 → 2955.18] Bye.
[2955.18 → 2955.72] Bye.
[2955.72 → 2956.62] Bye.
[2956.64 → 2956.70] Bye.
[2956.70 → 2956.72] Bye.
[2956.72 → 2957.22] Bye.
[2957.22 → 2957.70] Bye.
[2957.70 → 2958.62] Bye.
[2958.62 → 2958.70] Bye.
[2958.70 → 2959.22] Bye.
[2959.22 → 2959.70] Bye.
[2959.70 → 2960.94] Bye.
[2961.50 → 2961.68] Bye.
[2961.80 → 2962.72] Bye.
[2962.74 → 2963.70] Bye.
[2969.24 → 2971.64] Bye.
[2973.14 → 2973.62] Bye.
[2979.30 → 2979.50] Bye.
[2980.06 → 2981.28] Bye.
[2982.52 → 2983.42] Bye.
[2988.12 → 2988.78] Bye.
[2988.88 → 2989.42] Bye.
[2989.52 → 2990.06] Bye.
[2990.06 → 3020.04] Thank you.
