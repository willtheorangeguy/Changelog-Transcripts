[0.00 → 13.32] you are listening to js party the award-winning weekly celebration of JavaScript and the web
[13.32 → 18.46] thanks to our friends at fast for shipping our shows superfast all around the world check them
[18.46 → 24.26] out at fastly.com and to our partners at fly deploy your app servers and database close to
[24.26 → 31.98] your users no ops required check them out at fly.io okay hey it's party time you all
[31.98 → 47.16] ahoy hoy welcome to js party I'm your host this week nick nisi hello and I am joined today by
[47.16 → 53.12] amelia how's it going its good I'm very excited about today's episode yeah it's going to be
[53.12 → 60.06] a very colourful episode I think speaking of which we have a special guest and that is Adam Cargill Adam
[60.06 → 65.88] how's it going what's up can I use colourful language you all have a healthy beep button in there right
[65.88 → 71.04] sure yeah I'm sure I'll keep it I'll keep it cool
[71.04 → 78.40] uh yeah no it's its really exciting to have you back on I think last time was probably
[78.40 → 84.32] was it one of the game shows uh it was a game show yeah yeah a feud episode I think those are
[84.32 → 88.96] fun and embarrassing you watch it again, and you're just like why can't you just say the right
[88.96 → 95.36] answer dork, and you're like well because I'm at the moment, and it's hard so yeah I still can't get
[95.36 → 103.56] over not being able to name a browser it's pretty bad brains they fart you know what are you going to do
[103.56 → 110.68] I don't know, but we're not here to talk about that today we're here to talk about colour and there
[110.68 → 118.24] is a lot of wild things that we can do with colour now nowadays with just like pure CSS I think I mean
[118.24 → 123.06] that's what you're going to tell us right yeah well and JavaScript so like if you're is you're a JS
[123.06 → 129.22] person that's just like I love objects and calling functions and manipulating data you're just like cool
[129.22 → 133.36] do you like colour because colour is totally like that you're like oh colour no, no dude I'm serious like
[133.36 → 139.22] colour is totally a really fun object to play with in JavaScript just as much as dates I don't know
[139.22 → 143.98] if it actually dates are fun money you know like there's like these rich I know yeah those suck
[143.98 → 148.30] uh colour is way more fun, and it gives you something to see so as you do all these things
[148.30 → 154.34] you can show it, and it's not just like dollars went up you know like you get to see like a colour
[154.34 → 159.42] change, and it's its fun anyway yeah I'm sold yeah I'm saying couldn't have said it better
[159.42 → 166.36] so why don't you catch us up on where we're at because when I think of colour there's a couple
[166.36 → 174.58] of things there is hex or RGB or RGBA or pretty much the main ones that I use there's also HSL and
[174.58 → 182.58] SLA uh which I've also used and IQ saturation and something that's about that's about the extent of
[182.58 → 188.98] my colour knowledge so uh can you enlighten me a little more yeah, and you are not alone we look at the
[188.98 → 195.38] like almanac data and there's like nobody even using HSL they're all it's like hex all day um
[195.38 → 203.12] maybe some RGBA which by the way RGBA is dead SLA dead it's now just HSL or RGB, and you put a little
[203.12 → 207.08] slash at the end, and you can put your percentage there you don't have to change the function you're
[207.08 → 212.38] calling any more just to add some alpha because you all know that was so annoying anyway so yeah
[212.38 → 218.50] i I had no idea I saw some syntax like that with like a slash in there I was like why are they
[218.50 → 225.76] dividing in the middle of this it's like a classic CSS thing there are slashes in border radius there's
[225.76 → 231.80] slashes anyway they're like to denote a break in sort of the parsing anyway uh yeah Amelia where are
[231.80 → 236.74] you at with colour I want to know where your baseline is too, and we'll, we'll work up from there and oh I'm
[236.74 → 245.36] at I'm still using colour names like pink sky blue there's tomato red is a good one there's cornflower
[245.36 → 251.88] blue these are my top hits um that's where I'm most comfortable those are awesome all right so
[251.88 → 257.98] few fun things about those, so the named colours are really fun to prototype with, and they have a fun
[257.98 → 264.14] attribute many of them uh like deep pink I really like deep pink because it's so hot uh and if you
[264.14 → 268.92] look on your colour picker when you put deep pink in there, and you pop it open the little dot
[268.92 → 275.28] is in the far top right of the colour square, and you're like yeah give me that brightest most saturated
[275.28 → 284.24] colour you know and um and that is the brightest hot pink that can be found in RGB which is standard
[284.24 → 290.04] dynamic range, so this is okay lets we'll like roll this into kind of what we're talking about today is
[290.04 → 296.32] all these colours on the web have been SDR standard dynamic range and what we're getting and what we've
[296.32 → 302.48] gained is HDR colours high dynamic range so all these TVs you buy your iPhones your laptops all
[302.48 → 309.34] these things all have millions and billions of colours, and you're like right on you know um but
[309.34 → 313.84] then everything's using them like the movies you're watching the images you're looking at oh come on take
[313.84 → 317.72] a picture with an iPhone or an android pixel, and you're like look at the colours, and you're like that
[317.72 → 323.74] sunset is popping like there are definitely some like high dynamic range colours coming off that image
[323.74 → 330.24] and so when you're using these named colours and hex and stuff you're literally trapped to a tiny
[330.24 → 338.10] portion of what your screen is capable of doing and so what CSS has done is graduated into the HDR space
[338.10 → 344.00] with a bunch of features that allow you as authors to take your website from a SDR website to an
[344.00 → 351.28] HDR website and that is a product excellence thing this is why apple was first they've had display p3 this
[351.28 → 357.72] is a wide gamut colour range since 2016 and all their products, and it makes sense you look at an iPad
[357.72 → 363.18] in the app store you look at an iPad and an app, and you're like the colours on this are beautiful and they
[363.18 → 368.60] they know that they know that a user can't really articulate why, but they will tell you one looks
[368.60 → 373.48] better than the other, so there's an opportunity now for your brand to do this or your colours or
[373.48 → 377.76] whatever it is that you're building to kind of reach into this HDR space and then there are all sorts
[377.76 → 382.10] of goodies for us to talk about like colour manipulation how do you specify colours there's
[382.10 → 387.22] way more than HSL now so I'm sorry it kind of gets more confusing uh it goes into gradients it goes
[387.22 → 391.64] into animations, and we got all that stuff to talk about today so how's that for a high level little
[391.64 → 402.04] intro I have questions me too good I'm here for you first off you mentioned like all of those named
[402.04 → 408.64] colour values like um I forgot deep pink is that the one that you were talking about do those map
[408.64 → 417.06] to like the standard like six character RGB values yep and is there a name for every combination of
[417.06 → 423.56] six character hex values nope they uh originally I don't remember the year who cares, but they're
[423.56 → 429.06] basically the box of crayons someone was like oh we got a because we okay remember web safe 256 colours
[429.06 → 433.32] that's all you had to choose from a lot of those are from the crayon box okay because that's how
[433.32 → 437.54] creative they were when they were writing the spec I wish who cares those are good colours so they like
[437.54 → 444.98] a lot of those are crayon names and those are RGB colours well they're RGB colours, and they are inside
[444.98 → 450.10] that space so yeah they literally map to a RGB colour they literally map to a hex to a HSL all of
[450.10 → 457.96] these colour formats that we've been using today even hub they're all in the RGB range they're in SDR
[457.96 → 463.66] standard dynamic range colour space colours so we have we've had all these ways to reference colours
[463.66 → 469.72] but they're all from the same pool um, and now we have a have new pools to specify colours from
[469.72 → 477.44] so my like 2002 knowledge on those colours was always like oh you shouldn't use those because
[477.44 → 483.36] they could like deep pink could be this on a Mac and this other value on a Windows machine
[483.36 → 489.68] is that the case now still or have they kind of standardized uh they standardized so what's cool
[489.68 → 497.24] about RGB and why RGB has been around for 25 30 years is it is a common denominator basically it's
[497.24 → 503.80] the most common junk that you can find everywhere and everybody has united on this is a healthy
[503.80 → 509.00] baseline it's not junk let's be honest like it's pretty good this is why it survived so long, and we're
[509.00 → 513.82] really only kind of getting nitpicky about bringing them into this HDR colour space, and we were waiting
[513.82 → 518.16] for displays there wasn't a lot of displays that could even show these colours until five or
[518.16 → 524.42] seven years ago so we're we're on this cusp where the capability is there the math is there even for
[524.42 → 530.64] like the downplaying some of these colours so if I ask for some super rad new HDR colour uh on a display
[530.64 → 534.64] that's 20 years old the display is going to be like I don't know what to do, but it can just it'll show
[534.64 → 541.64] deep pink let's say I ask for deepest pink or whatever like the go to the crevices of the pool
[541.64 → 547.06] um the browser and the operating system and the display will all work together to go well my colour
[547.06 → 552.70] profile and my capabilities say I can only go here so I can only reach into this amount of RGB brightness
[552.70 → 557.14] and my little lights that I light up, and you're like cool just give me the maximum pink I don't really
[557.14 → 562.06] care but yeah there's also media queries to help you hand hold this so lets's say you don't want to
[562.06 → 567.34] let the browser and the operating system find something uh you can be like okay well hey I'll
[567.34 → 574.64] just I'll give you a hex value and then if it's a HDR capable display which is the media query at
[574.64 → 581.76] media dynamic range high then you can say inside there then bump up those colours baby we're going to
[581.76 → 589.18] disco town or whatever it is that you're trying to do um okay here's my biggest question as a like
[589.18 → 596.54] as a web developer I have a healthy dose of uh fear of new things right and I want to know
[596.54 → 604.46] what percent of displays people are using can go to disco town right like is this something only 10
[604.46 → 610.12] percent of people are going to be able to use or see yes that's a great question like a metric on
[610.12 → 616.72] how common or uncommon are HD displays yeah this is going to be hard it's like probably depends on
[616.72 → 622.76] your circles I mean every iPhone and every mac is capable, so there's a percentage value for you
[622.76 → 628.20] already many windows laptops are capable you can go into the operating system of windows and say i
[628.20 → 633.16] want HDR windows and windows will be like all right I'm going to start using HDR colours where I can and
[633.16 → 637.36] all those little accent colours you get they're going to be disco town I like that we're calling
[637.36 → 642.52] them disco town colours let's hang on to that um I was just watching Lego masters and that someone did
[642.52 → 646.56] like a disco scene and now I guess that's why it's stuck in my head but yeah you're right like a lot
[646.56 → 651.64] of android phones just a lot of other devices don't have it but where you find it's really common is the
[651.64 → 660.02] TVs people buy um it's like they don't even sell SDR TVs any more you can only get HD super-duper and
[660.02 → 665.66] there's like super high-res ones, and then you have liked your olds which are different because they
[665.66 → 672.00] can turn off the lights to make black which is another thing so a lot of these HDR colours one aspect of
[672.00 → 676.60] them is how black of a black can you make and how white of a white can you make this is like the
[676.60 → 680.60] nits that you'll read you go look at a brand-new Mac laptop, and they're going to be like 10 000 nits
[680.60 → 686.44] and you're like what do I need, I don't know how many nits do I need you know like, and they're like
[686.44 → 692.04] well you want the most nits because it's a couple of hundred extra dollars you know, and you're like I don't
[692.04 → 696.88] know, so anyway that's kind of like some of the factors that are in there I think it's a lot more
[696.88 → 701.12] common now than we think I think that's why the timing is perfect now another like weird little
[701.12 → 708.96] niche detail here is that the web has been capable of HDR in images and videos for many years just not
[708.96 → 717.42] from CSS interesting so how do you enable it in CSS it's its got to be more than RGB or those hex
[717.42 → 723.92] colours right you have to use a new function to specify the colours you have to ask for a colour from a new
[723.92 → 729.44] pool and so that's kind of what these colour spaces are their new pools new opportunities more range
[729.44 → 734.16] which also means things like gradients have less banding because oh here was another reason that
[734.16 → 739.84] like CSS was kind of slow to this is a lot of the browser engines were like hey uh RGB has been
[739.84 → 745.50] really hex that only takes a little bit of memory uh to hold the values for that and these new ones
[745.50 → 750.64] they require double and maybe triple the memory so we're gonna kind of wait on that because we don't
[750.64 → 756.52] want to double every colour in the whole system and there's like this fear about how impactful
[756.52 → 762.96] storing just the values of these colours in memory was going to be, and some genius was just like a few
[762.96 → 769.40] years ago was like how about we only double the make you know if it's in the new range then
[769.40 → 774.88] all that we don't if the site doesn't use any HD colours we don't change the memory and everyone's
[774.88 → 782.64] like why we never thought of that all of a sudden it became like really viable um to just in time
[782.64 → 788.86] upgrade colours to a bigger memory allocation if needed so yeah types dude types it was literally
[788.86 → 794.90] a type issue oh also by the way colours say types I did say types and dude the cut all colours in CSS
[794.90 → 802.66] are typed dude, and they are typed well very intricately typed it's a typed system from the top
[802.66 → 806.72] to the bottom man you call functions you pass parameters they're all typed the ins are typed
[806.72 → 813.26] the outs are typed it is really cool so anyway if you like types uh the new colour stuff is it's
[813.26 → 823.22] very interesting yeah my mind is he's hooked is it like types in CSS then or CSS has always been
[823.22 → 828.96] typed bro it's typed, and it's resilient so it has this like thing where if you put the wrong value
[828.96 → 834.82] into somewhere CSS doesn't crumble and go oh no there's one little wrong thing in my entire application
[834.82 → 841.48] I can't even do anything which is what typescript does um sorry that's what all types do really
[841.48 → 847.54] it's a good reason I know, but it doesn't have to stop the show CSS doesn't stop the show CSS goes
[847.54 → 852.86] oh that's wrong yeah whatever and just keeps going um and so you can pass uh like for example you could
[852.86 → 860.32] pass pixels to um something that needed a colour type, and it would be like all right well nice try
[860.32 → 865.70] and it would just roll on right um, but it is a type so that's how they have type validation is it
[865.70 → 870.60] knows if a length or if a type uh and what all anyway so it's all typed it always has been it's
[870.60 → 875.10] just sort of lesser known because it's not strict about it, I don't know so I don't know how things
[875.10 → 881.48] work in your neck of the woods but if you put something into CSS, and it's wrong, but it doesn't
[881.48 → 888.88] care, and it just stays there that is now part of the legacy of the app that I'm working on like
[888.88 → 894.14] nobody goes back and cleans that up yes seriously I just learned about how many to-dos are in the
[894.14 → 902.84] google code base oh no it's insane I was like oh surely it's just a couple no dude it's
[902.84 → 908.88] so many to-dos, and you're just like, but those are just left hanging yeah that's software we can't
[908.88 → 913.72] get to every edge case and everything all the time it's gnarly anyway that's a rant I think to-do's
[913.72 → 917.96] are just they're just performance art right you leave them there you're like i know I'm
[917.96 → 925.64] supposed to do this I just want you to know that I know funny I'm not gonna so yeah that there's a
[925.64 → 931.60] little mind-blown colour stuff uh yeah where do you want to go next well so you mentioned that it's a
[931.60 → 937.90] new function what does that actually look like to access these new colours awesome question okay so
[937.90 → 944.92] let's start with the most supported one or the one that's historically has support is the colour
[944.92 → 951.56] function so it's literally you call colour you pass in you got two parentheses and the first parameter
[951.56 → 956.86] is the colour space and the one that apple has supported for about six or seven years is the
[956.86 → 964.78] display p3 colour space so you say colour open parentheses display dash p3 space, and then you pass
[964.78 → 970.56] three channel amounts and so it's basically asking for brightness from zero percent to a hundred percent
[970.56 → 975.92] saying how much power should the display put behind those RGB lights that it's going to light
[975.92 → 982.60] up for this colour, and you can say 100 zero and a hundred percent, or you could say one zero one so
[982.60 → 988.80] CSS is very good about um understanding a range between zero and one and zero and a hundred percent so
[988.80 → 992.96] it's on you as an author to kind of pick how you like to work inside there, and it's as simple as
[992.96 → 998.56] that so you say like background is colour open parentheses display p3 one zero one and parentheses and
[998.56 → 1005.80] you got yourself a super hot pink because you maximized the r and the b, and you left the g i
[1005.80 → 1011.50] can't believe I did that in my head wow yeah that's pretty good that was going to be my next question is
[1011.50 → 1017.78] like those the percentages was that r g and b that you're it was r g and b so that's another thing
[1017.78 → 1023.14] that's why the RGBA function here yeah let's just like retract a little bit RGBA was dropped not just
[1023.14 → 1028.50] because of convenience because it was really truly annoying like you're like I need to add alpha you're
[1028.50 → 1032.44] like dang I have to call a different function it's really annoying so what they did is they also
[1032.44 → 1037.86] normalized that all these functions take three channels hex is kind of the odd one out here in
[1037.86 → 1042.94] that it represents the three channels right in like a hexadecimal, and now it's just very blunt it's like
[1042.94 → 1047.14] here are three channels and so moving forward every one of these colour spaces is three channels
[1047.14 → 1052.82] and then you have your alpha with the slash and so it's kind of nice if you're used to HSL there's a
[1052.82 → 1057.44] new one called LCH which is kind of almost like the same letters in a new arrangement it's kind of
[1057.44 → 1063.30] annoying and then there's even one called okay LCH uh which is superior to LCH even though it makes
[1063.30 → 1069.10] it sounds marginally better or marginally compared anyway uh it's just it's like the person that
[1069.10 → 1074.18] came up with okay LCH was just really humble about it, they could have been like rad LCH, or you know
[1074.18 → 1079.70] like doneness LC, but they were like yeah it's okay, and you're like well you really sold that short
[1079.70 → 1084.60] because it's perfect and the okay LCH colour function so instead of calling the colour function
[1084.60 → 1090.16] like we did earlier you can just reference the colour space exactly in a function you say okay LCH
[1090.16 → 1096.22] just like you did with HSL open upper parentheses pass three channels and l is your lightness well
[1096.22 → 1101.46] it's who cares it's it gets more technical than that, but you got an l that's perceptual lightness
[1101.46 → 1107.44] this is lightness per your eyes as a human whereas HSL was lightness in math which was not they're just
[1107.44 → 1114.40] not the same so then you have c and h c is chroma and h is hue, so your hues are pretty similar your
[1114.40 → 1118.96] chroma is about like how much vibrancy it's kind of like saturation, but it's a little bit different
[1118.96 → 1124.28] so anyway each of these colour spaces are unique in that they bring something different
[1124.28 → 1129.82] to the table they're like a utility function that you can call to get access to colours in a way that
[1129.82 → 1135.32] is optimized for one thing over another and so you kind of learn these but okay LCH is a perfect
[1135.32 → 1141.56] first place to start because it both can go into super wide gamut HDR colours, but it also has a
[1141.56 → 1146.84] really, really reliable lightness channel that makes it great for design systems makes it great for
[1146.84 → 1151.54] lightness adjustments and then colour functions like if you want to manipulate a colour like darken or
[1151.54 → 1157.00] lighten something it has reliable results and so yeah there's like a little, so there's how you access
[1157.00 → 1162.32] the colours you call these new functions you either call the colour function and pass a colour space or you
[1162.32 → 1168.56] call the colour space itself directly like ok LCH or lab or LCH
[1168.56 → 1188.96] do you find yourself itching to grow at work, but you're not getting the support you need from
[1188.96 → 1193.36] your manager, or maybe you're at a career transition and trying to figure out what you want and how to
[1193.36 → 1198.52] get it, or you've got a great job but could use an external perspective on some tricky cross-functional
[1198.52 → 1203.84] relationships hi this is ball from js party and these are the exact types of problems I'm helping
[1203.84 → 1208.02] folks with in my new business I think about it as pair programming for non-technical problems
[1208.02 → 1213.24] if you're curious you can learn more and sign up for a free exploratory session at ball.LLC
[1213.24 → 1214.24] slash coaching
[1214.24 → 1232.08] okay here 's's the question I've been wondering since you said the word gradient yes and I've never
[1232.08 → 1237.62] thought about this before but if you define that like say the start and the end colour for a gradient
[1237.62 → 1243.80] in a different colour space will it interpolate differently or is it only for the way you're
[1243.80 → 1250.22] defining those colours this is such a good question it does interpolate differently this is where we
[1250.22 → 1255.12] could even pull up a quick little visual like I know you've seen the RGB cube right all the colours
[1255.12 → 1260.36] packed so nicely into a cube and then imagine you put two little points in there in a three-dimensional
[1260.36 → 1267.00] space and that's your gradient points and then the cube and your function have to go from one to the
[1267.00 → 1271.88] next, and it literally goes in a straight line because that's what math does right it goes straight
[1271.88 → 1276.04] from one colour to the next which means it's going to go through the middle of the cube, or it's going
[1276.04 → 1280.96] to go through different parts of the cube that gather the way that the gradient looks at the end
[1280.96 → 1287.62] HSL is a cylinder so again as you make a gradient in it, you get a different result because the path
[1287.62 → 1292.42] that it took like literally like a journey you could be like this is fun let's make a metaphor out
[1292.42 → 1296.54] of this is a video game you got like a journey different mountains that you have to cross and
[1296.54 → 1300.50] like your little journey person starts here at colour one, and then you have colour two and depending
[1300.50 → 1305.80] on the mountain they take a different path to get there and as they go they collect little colours
[1305.80 → 1310.34] and then in the end you get a whole range of the colours that they went through man I'd play that
[1310.34 → 1315.18] yeah that kind of sounds cool yeah I agree uh and that's colour interpolation, and you can also do this
[1315.18 → 1320.40] with animation if you animate from blue to white it's the same concept instead of you seeing one smear
[1320.40 → 1325.28] of the colour from blue to white like a gradient do you see it change step by step over time so you only
[1325.28 → 1331.60] see one state of the colour interpolation over time and so yeah each colour space has different results
[1331.60 → 1339.90] that's why new gradients use the ok lab colour space by default because it is optimized for vibrancy
[1339.90 → 1345.82] and avoiding the dead zone which is what RGB has notoriously when you go through that middle space
[1345.82 → 1351.16] the middle is white and so you pick up lighter colours on your way sometimes they look gray or muddy
[1351.16 → 1356.28] and these new colour spaces create gradients that are much more vibrant and don't have the muddy zone
[1356.28 → 1360.74] because they're packed different so that when the little journeyman travels across the mountain
[1360.74 → 1368.18] he stays in the bright areas I like that metaphor or analogy so you can't define a gradient with two
[1368.18 → 1374.26] different colour spaces I've never tried it that is correct you can uh well it will interpolate in one
[1374.26 → 1380.36] colour space, but you can put colours from two this is a great like mind-blowing question so you've got
[1380.36 → 1387.40] colour number one is hex something right you're like SDR colour and then the other colour is folk
[1387.40 → 1394.58] something turbo rad cyan the browser there's math in the CSS specs on how to resolve that, and so they're
[1394.58 → 1400.16] they're going to get put into a colour space that is big enough that they both can share a position in it
[1400.16 → 1403.54] and then they're going to get converted into the colour space that the interpolation happens in
[1403.54 → 1409.32] and then the interpolation happens, so there's a conversion and then interpolation and yeah, so this is
[1409.32 → 1414.38] again the colour gets really really complex fast I'm I'm going to hope to make this sound as
[1414.38 → 1419.00] simple as possible throughout this podcast episode, but this is again why it's kind of like working with
[1419.00 → 1425.78] dates or working with money there's a lot that can happen in the math between conversion and interpolation
[1425.78 → 1432.54] and perform yeah it's all math um in the end result you see a colour though I love that also so you
[1432.54 → 1437.68] mentioned JavaScript right where does JavaScript come into play here or are we only working
[1437.68 → 1444.94] in CSS here uh yeah that's a good question CSS has um you know easy access to all these functions but
[1444.94 → 1450.52] from JavaScript you can set colours you can extract colours eventually there's going to be a object
[1450.52 → 1455.62] model for it so that you'll get a rich object back that has the channels already broken out for you
[1455.62 → 1461.20] into RGB or LCH and stuff like that at which point you'll be able to take you'll be able to restructure
[1461.20 → 1466.54] a colour okay we'll have to move into the RCS next the relative colour syntax because you literally
[1466.54 → 1473.14] restructure a colour in CSS put it back together in one line of code and then return it to the browser
[1473.14 → 1478.52] it's super rad but in JavaScript you could do that now you could grab a colour off a element you could
[1478.52 → 1484.88] explore split it by space and find your channels reassemble it put it all back together
[1484.88 → 1490.44] after some math after some math and put it back in um there are also a lot of colour libraries to work
[1490.44 → 1496.26] with there's many of them uh the folks that wrote the specs Leah very and Chris lily have one called
[1496.26 → 1501.30] colour JS I use it all the time and that's very spec compliant for CSS, and you get this really rich
[1501.30 → 1507.04] experience working with colour from JavaScript um it's super fun, and you can make gradients and
[1507.04 → 1510.88] various colour spaces I have all sorts of cool demos I'll share at some point oh here I think I have a
[1510.88 → 1518.48] I have a code pen collection of colour stuff let me send this to you, and it's a mix of CSS and JavaScript
[1518.48 → 1526.44] HD colour and colour functions here put this in the JS party chat book we will include that in the show
[1526.44 → 1532.82] notes as well and yeah um a lot of this stuff is there are tons of utility in each colour space there's
[1532.82 → 1539.12] utility in knowing the JavaScript ways in the CSS just like normal web development right you have
[1539.12 → 1543.22] like this harmony and a relationship in an orchestration that you're going to find the best
[1543.22 → 1548.44] tool for the job and these new colour spaces give you better tools for the job so that's kind of
[1548.44 → 1553.18] what's nice is after this podcast you're going to be like I have new colour tools that help me perform
[1553.18 → 1558.04] my work better I like literally learned new functions that give me better results than what I've been
[1558.04 → 1562.90] working with in the past yeah that's awesome and I love that the fallback is pretty simple
[1562.90 → 1568.76] right like I get really nervous with new tech on the web because I don't know what's going to happen
[1568.76 → 1574.14] when a browser doesn't have access to it or doesn't support it yeah that's and that is an it's a good
[1574.14 → 1579.32] concern there are a few ways to handle like upgrading so you could progressively enhance you know so you've
[1579.32 → 1585.14] already got an app it's already got colours you've got bright blue bright yellow somewhere in the app and
[1585.14 → 1591.80] then you could easily say app media dynamic range is high to target those colours those custom properties or
[1591.80 → 1596.74] whatever and use ok LCH and bump them up and now are you all your yellows and blues are bumped up
[1596.74 → 1601.54] safely there's actually an additional query that you can put in there because there's a difference
[1601.54 → 1607.24] between the display having the capability and the browser being able to parse and so you can also put
[1607.24 → 1611.58] in an ad supports parsing function in there it says hey do you even understand display p3 do you even
[1611.58 → 1616.60] understand ok LCH I don't want to give you this colour unless you can so you can be really handhold with
[1616.60 → 1621.54] it that with like two media queries, or you can just do the cascade you know you just drop it in the
[1621.54 → 1627.52] cascade and just like hey uh here's the colour one is a hot pink and then next one is a hot pink and
[1627.52 → 1631.88] ok LCH and if the browser doesn't know what ok LCH is it goes cool I don't know what it is I'll throw
[1631.88 → 1635.66] it away I'll just take the colour I got before then and there's even another way that you can do this
[1635.66 → 1642.12] an even lazier way which is you just use the new colour functions and if the browser doesn't understand
[1642.12 → 1647.20] it well you wouldn't get a colour so that'd be the bummer but if it does understand it, it will
[1647.20 → 1651.54] automatically adjust it for the display and the capabilities of the device so you can be like I'm
[1651.54 → 1656.02] just going to use these new colours and I'll let the browser and the display and the operating system
[1656.02 → 1661.18] work out how rich it can make this pink how rich it can make that blue and so you have all of these
[1661.18 → 1666.86] options you have graceful degradation you have progressive enhancement you have lazy I'm just going
[1666.86 → 1672.58] to let it be broken on other stuff if I want um yeah it's all there for you speaking of broken on other
[1672.58 → 1678.66] stuff I was looking up ok LCH in MDN, and it looks like Firefox is the only one that doesn't support
[1678.66 → 1684.70] it right now yeah and that recently merged they'll have it so it's in nightly, and it'll be in Firefox
[1684.70 → 1689.10] stable I think that 114 or something like that I don't remember the exact version, but it's soon
[1689.10 → 1695.36] nice so I'm confused I guess the part that's confusing me a little bit is like you know if you
[1695.36 → 1701.06] were going to create a new site, and you wanted you know you're creating a design for it are you
[1701.06 → 1706.86] primarily playing within the standard range colours or like would you have liked your primary
[1706.86 → 1712.74] and secondary colours being in this higher dynamic range with fallbacks into that like when do you
[1712.74 → 1719.34] use what and can you rely on I don't know I'm confused about like you know if Adam is starting
[1719.34 → 1726.62] a site are you do primarily still use RGB in a lot of places or are you dipping into this ok LCH
[1726.62 → 1731.84] and these new colour functions perfect question and I'll like to answer it in kind of two parts i just
[1731.84 → 1738.92] redid my website nerdy.dev have fun check it out it does use HDR colours, but it upgrades to them
[1738.92 → 1743.42] and so I'm using the approach that I mentioned earlier with a media query checking to see if the
[1743.42 → 1748.80] display is capable and checking to see if it understands the parsing that way I safely upgrade
[1748.80 → 1754.62] any vibrant colours like the syntax highlighting is using HDR colours anywhere where we see a nice
[1754.62 → 1760.42] bright colour especially in the dark mode the dark mode got a lot more treatment for the neons that
[1760.42 → 1766.32] you can get out of these HDR colours the other side of this though is that's Adam doing his own design
[1766.32 → 1772.20] I had a third person is always so weird uh that was that's me that's me wearing both hats right I like
[1772.20 → 1777.14] a designer hat and a developer hat and I know what I'm doing now designers though like on teams that
[1777.14 → 1782.06] I've always been in they live in ideal land right they always make ideal comps with ideal layouts
[1782.06 → 1787.78] with ideal users' user really takes great pictures look at that look at that profile page it's amazing
[1787.78 → 1793.06] and then you go to the actual app, and you're like no that user's picture suck anyway so like designers
[1793.06 → 1797.06] supposed to live in this ideal space at least in the beginning of the app who cares but anyway
[1797.06 → 1803.80] they should be using HD colours in my opinion there a bummer is a lot of the design tools haven't really
[1803.80 → 1810.60] caught up it takes I'd say 10 or 15 of the designers that I know even know this stuff exists
[1810.60 → 1817.36] and their work is better because of it, but it's just not popular or I don't know we're still catching
[1817.36 → 1822.50] up I think it's you know like people still or don't even realize why they bought an UHD TV they don't even
[1822.50 → 1826.10] know what they bought they're like I bought a new TV you're like how many colours does it have, and they're
[1826.10 → 1831.18] like I don't know a lot you're like that's that's fine you know like I don't expect everyone to know
[1831.18 → 1837.32] that I didn't even really know it before but I think as designers want product excellence and they
[1837.32 → 1842.56] live in the ideal state they should be using the ideal colours which again they manipulate better
[1842.56 → 1848.66] like you want to make a light variant it lightens better in folk it just does HSL can do funky stuff
[1848.66 → 1855.04] and so they'll eventually be working in these you'll be inheriting them and the relationship will
[1855.04 → 1860.14] change at which point you'll be producing fallbacks at some point or no fallbacks at all as we
[1860.14 → 1866.26] move forward into 2024 and just like everything's HDR or whatever but yeah I feel like I went on two
[1866.26 → 1873.52] tangents and I hope I answered your question yeah I think so in 2024 and beyond when all of this is
[1873.52 → 1880.90] fully supported in every browser uh and works great is there a use case for the older colour syntaxes
[1880.90 → 1889.68] hmm I mean I have friends that work on LCD panels or like kiosks or all sorts of like interesting
[1889.68 → 1896.82] niche industry software on weird screens now they're still going to be in SDR land because
[1896.82 → 1902.60] RGB is just so ubiquitous in that way but I think as we look for product excellence, and we want to
[1902.60 → 1908.60] use the features that someone's got in their hand like a device that's like HDR capable you're going to
[1908.60 → 1914.22] want to give them that colour quality it will look and feel different so yeah I think are just our
[1914.22 → 1918.96] expectations as users might change a little bit as we get there well I have the opposite question
[1918.96 → 1924.90] to what you just asked nick so what are like what's like the best case scenario right we use these and
[1924.90 → 1931.60] like colours pop more gradients interpolate better like what are we getting from this and also
[1931.60 → 1940.04] does it matter evenly across colours right like is a pink way deeper than RGB pink, but yellow is kind
[1940.04 → 1945.64] of the same nice cool okay two parts um the second part is easier to answer is that yeah some of these
[1945.64 → 1951.22] new colour spaces offer way more blues than they do yellows like for example yellow is tough every colour
[1951.22 → 1957.30] space has like a tiny amount of yellow to choose from whereas blues and greens and pinks and reds they
[1957.30 → 1963.08] just go crazy which is also because that's how our eyes are our eyes are like super attuned to
[1963.08 → 1968.40] some of these colours more than others, and anyway it's also the shape of the space but yes some
[1968.40 → 1974.52] hues do offer more than other hues uh the first part of the question though is what is like the main
[1974.52 → 1980.74] benefit here it's its vibrancy it's design system consistency so I have like some demos I can share with
[1980.74 → 1988.12] you that were I've defined 15 custom properties in ok LCH, and you can just change the hue, and you get
[1988.12 → 1993.34] a perfect palette in any hue that you want so you don't have to download the tailwind blue or you
[1993.34 → 1998.40] don't have to download when you like my library open props pink, and you don't have to grab pink and
[1998.40 → 2003.78] green or whatever you don't have to go pick you just grab 15 props and change the hue you can
[2003.78 → 2009.34] also adjust the chroma so if you want a more vibrant colour palette you bump up the chroma if you want it more
[2009.34 → 2016.96] pastel-y you drop the chroma so with 15 props you literally have hundreds and thousands of colour
[2016.96 → 2021.74] palettes to choose from versus the way that we're working today with RGB where we sort of prefix these
[2021.74 → 2027.84] you know nine or 12 or 15 colours, and then we try to work within that that set we can do the same thing
[2027.84 → 2034.70] with 15 props and make it adaptive and dynamic for light and dark and all this sort of stuff so yeah you get
[2034.70 → 2041.44] design systems vibrancy manipulation consistency oh and the gradients are better the gradients do
[2041.44 → 2045.80] genuinely look better like and that's why you've even seen I don't know if you've seen the tools that
[2045.80 → 2051.42] um like Eric Kennedy has a tool where you go and make a gradient on his tool and the output you put
[2051.42 → 2057.66] two colour stops in and the output is eight stops and the reason that he does that is he literally
[2057.66 → 2063.86] has written an algorithm to avoid the dead zone by hand holding the gradient adding additional stops so
[2063.86 → 2068.04] that it never goes through the centre it's like giving the journeyman more positions on the mountain
[2068.04 → 2072.00] to avoid the spots that are dangerous hey that actually worked out pretty good
[2072.00 → 2078.04] that's sweet so yeah so you have like some of these things it's gonna it's going to be smoothness
[2078.04 → 2085.54] vibrancy excellence consistency and reliability of manipulation then yeah, but it is you know more
[2085.54 → 2090.86] confusing in a way like I totally empathize with how heavy this stuff can sound and that's why I'm
[2090.86 → 2095.08] like keep asking the basic questions over and over because everyone who's listening is going to have the
[2095.08 → 2099.40] same questions you all and don't feel bad this crap is somehow confusing you're like colour is supposed
[2099.40 → 2104.84] to be simple, and you're like all of a sudden it's not, and you're like well coding is like that all the
[2104.84 → 2109.90] time you know um but yeah well good I'm glad you're giving me permission because I'm going to keep going
[2109.90 → 2117.16] yeah I'm I'm trying to understand, and it like I'm already terrible at this stuff but I'm terrible with RGB
[2117.16 → 2124.06] and there's just so much more uh but a question I had been so like this folk thing going back to that
[2124.06 → 2130.60] a little bit you set that it's defined it now works in every browser Firefox all of that and i I create
[2130.60 → 2137.94] a site and use that completely but then here I am on a know a nice modern mac but I'm using a really
[2137.94 → 2143.84] old really cheap display with it that doesn't support all of that yeah does that like if I defined like
[2143.84 → 2149.80] some neon blue that's very vibrant does it will that get translated into a more muted blue by my
[2149.80 → 2156.52] display and still show up as some kind of blue or what happens there yes so yeah your uh this display
[2156.52 → 2163.10] I'm looking at right now that you all are on is a poppy SDR display is cheap and whatever the one I have
[2163.10 → 2168.46] over here this is my Mac one that's very nice I can literally take a tab from chrome or safari and drag
[2168.46 → 2172.48] it over and watch them go book and get like downgraded but here's the thing just like we were talking
[2172.48 → 2177.30] about deep pink or the named system colours and those are reaching into the furthest corner that
[2177.30 → 2182.40] that's capable in that SDR RGB colour space that's all the display in the operating system is going to
[2182.40 → 2188.42] do when you ask for super rad you know disco pink when you bring it onto a monitor that can't do it
[2188.42 → 2193.18] the operating system and the browser they all orchestrate and go hey look this display can't do
[2193.18 → 2197.78] that you have to downplay it, and it'll automatically downplay it into the best pink that's possible
[2197.78 → 2203.70] so that's kind of what's nice is you're you're reaching really far and most of the displays won't
[2203.70 → 2208.84] be able to do even some of the stuff folk can do, but it will do the best it can and that's kind of
[2208.84 → 2214.26] one of the fun parts here is you're asking everybody's device to do the best pink that it
[2214.26 → 2219.84] can the best uh vibrant thing that it's possible, and you just let it adapt to all these scenarios just
[2219.84 → 2225.42] like a width of text you know just like a lot of our responsive design and our adaptive design is doing
[2225.42 → 2230.52] where we don't nitpick and pixel perfect everything the same thing's going to happen with colour where
[2230.52 → 2234.36] someone over here is going to have a regular display, so one over here is going to have a super one
[2234.36 → 2239.86] and both their displays are doing the best they can with folk yeah there's a cool site you can go to
[2239.86 → 2246.68] oklch.com it's made by evil Martians the post CSS folks oh well they work on post CSS, and they do lots
[2246.68 → 2252.08] of other stuff, but it's a very good site it's also going to immediately be annoying and confusing
[2252.08 → 2257.84] if you don't do much colour stuff because you're like oh look charts that I don't know what they mean
[2257.84 → 2263.60] but at the same time it gives you a perfect gauge like there's a there's going to be two switches
[2263.60 → 2268.90] there one's for p3 and one's for rec 2020, and you should turn on rec 2020 just to see the additional
[2268.90 → 2274.66] lines that you get there's going to be cutoffs and the cutoffs are going to tell you how dynamic
[2274.66 → 2282.46] is this colour, and you're gonna you can choose to you know reach really far into rec 2020, and it'll
[2282.46 → 2286.42] even show you the fallbacks so it has that little like in the top left there it'll say here's the
[2286.42 → 2290.98] colour you're building here's what that looks like in RGB, and you get like a comparison and that tool
[2290.98 → 2296.00] is really nice for seeing how the colour space folk has some quirks you'll see these curves and these
[2296.00 → 2302.34] cuts and then if you're looking for super bright vibrant you can use their controls to find that peak
[2302.34 → 2307.88] colour that's in there and then put it in your code and it yeah it helps you create folk values
[2307.88 → 2316.34] as like an folk colour picker what is rec 2020 rec 2020 yeah so let's talk about sizes of like sports
[2316.34 → 2323.44] balls you've got like a baseball which is your current uh hex and RGB colour size all the colours
[2323.44 → 2329.30] that it can do fit inside a baseball then you have display p3 let's imagine it's like it's a softball
[2329.30 → 2334.96] maybe yeah it's a softball sure you get like 40 more colours or something like that with um display
[2334.96 → 2340.82] p3 so you literally have a have these two in your hand and there's literally more colours in the
[2340.82 → 2347.10] bigger sized sports ball, and then you have like a basketball which is rec 2020 so rec 2020 uh is a
[2347.10 → 2352.78] recommended its recommendation, and it was recommended in 2020 for like super uh like what's
[2352.78 → 2358.80] the movie theatres we go to that are like crazy rad IMAX yes you got like IMAX colours these are the folks
[2358.80 → 2363.16] that are like real okay uh and then okay here's another one who's the director that did avatar and
[2363.16 → 2369.18] stuff yeah whatever okay anyway like this person's using a camera that's like recording really rad
[2369.18 → 2376.06] colours it's a super raddest maximum that 2020 could do right that's rec 2020 it's a standard space where
[2376.06 → 2381.44] all these things that are capturing and untaking colour can put them into a space that everybody agrees
[2381.44 → 2388.78] on, and then they know what size that is which by the way RGB p3 and rec 2020 are gamuts and that's
[2388.78 → 2393.90] why I referenced the size of a ball like a volume because you have different volumes of colours but
[2393.90 → 2401.78] remember in the gamut of RGB like the baseball you have HSL hex hub and all these different ways to
[2401.78 → 2407.58] access colours from the same pool but in a different shape this is where things this I'm sorry this stuff
[2407.58 → 2414.02] gets Tripp, but you have pools of colours like total number of colours and that's your gamut
[2414.02 → 2420.24] and then to colour space is a shape, and you think about like the RGB cube the RGB cube is showing you
[2420.24 → 2427.30] both its shape and its gamut in one view, but you can separate them you abstract them into two different
[2427.30 → 2432.66] types two different data representations one just being a totality and the other one being a shape
[2432.66 → 2438.78] meant for purpose the HSL cylinder is very handy because we think about colour in a wheel you've got
[2438.78 → 2443.80] that circle you can just easily change the hue and as you go down the cylinder you get darker and as
[2443.80 → 2449.04] you go up the cylinder you get lighter so it made sense for people to interact with HSL in a very
[2449.04 → 2454.18] reasonable humanistic way they think about a hue they change the brightness, and then they change the
[2454.18 → 2460.96] lightness and so these new colour spaces like folk operate in the same sort of accessing language where
[2460.96 → 2464.38] you still say I want a hue and I want some brightness and I want some lightness to change
[2464.38 → 2470.84] but the shape of it is drastically different and so these colour spaces each shape has a superpower
[2470.84 → 2476.56] that's why there's no one true shape right now there's no one true colour space uh and folk just
[2476.56 → 2482.54] came out like a couple of years ago it's crazy it like literally, so inventions will happen we are not done
[2482.54 → 2488.40] with color is we haven't reached our displays haven't reached what our human eyes can do yet
[2488.40 → 2493.16] the code that we write hasn't reached into it doesn't have access to all this stuff yet we
[2493.16 → 2498.54] haven't found the perfect shape that represents the chance of the gamut what the handiness
[2498.54 → 2503.20] of using it like there are problems with the folk even though it's the best one we have there are issues
[2503.20 → 2508.08] in it and people that study it know it they're trying to solve if it's like schools of study trying
[2508.08 → 2516.36] to fix and create the next best colour space it's um very computer science very heavy into math and
[2516.36 → 2524.48] three dimensions and plotting uh it's crazy it's like a totally deep world that spans media it spans
[2524.48 → 2529.56] the movie industry it spans the photography industry, and now it's in CSS where we're getting the
[2529.56 → 2535.26] capabilities that they've had for a number of years it's a whole new world out there do you have
[2535.26 → 2543.22] any like uh tangible explanations for what's changed for monitors like the hardware aspect right like
[2543.22 → 2548.86] how are we bumping up the colours that we can represent within our monitors yeah that's a good
[2548.86 → 2554.44] question one of the one of the best examples is what I was talking about earlier I think it's UHD or
[2554.44 → 2561.52] no it's oled is more expensive because um you know okay we have like black mirror you know when
[2561.52 → 2568.06] your TV is off it's literally black, and it's like reflectively black but if you turn it on, and it's broken
[2568.06 → 2575.22] it's dark gray that's not OLED that's that's your RGB lights at the lowest setting that they have
[2575.22 → 2580.78] and it's just like, but that's not a rich black colour which means if you're watching Game of Thrones which
[2580.78 → 2586.12] I watch Game of Thrones on my crappy TVs all the time and I get tons of bad colour because they're so
[2586.12 → 2591.48] dark in a scene and my screen can't do it that I see these like bands of gray when I know the reality
[2591.48 → 2597.84] is if I was on an OLED display with a really, really rich amount of dark uh range in it, I would
[2597.84 → 2603.44] see richness there and there would be millions maybe more colours just in the dark area let alone
[2603.44 → 2608.26] the light area where the whites are better because of the knits come down to the power of the
[2608.26 → 2614.06] lights how powerful can these things combine to create a white there's literally whiter whites and
[2614.06 → 2618.26] I know we talk about that like painting your home you know like oh there are 10 whites to choose from
[2618.26 → 2621.90] painting walls you're like there are 10 whites come on, and then you see them all together you're like
[2621.90 → 2626.66] oh crap I see the difference that's annoying same thing happens with the display and knits you get
[2626.66 → 2632.74] more whites the whites are wider, and it makes a difference having that darker dark and the lighter
[2632.74 → 2639.30] lights as well as a bigger gamut of colours now you're watching a discovery planet and really getting
[2639.30 → 2645.10] immersed right you're like well the waves are crashing that's good stuff, so there's like some background
[2645.10 → 2650.84] like the displays and the capabilities that are changing that are enabling uh these things to
[2650.84 → 2656.80] be in our homes in our pockets so that makes sense for like the blacks and the whites right the
[2656.80 → 2663.94] the blacks get they can turn the pixels off effectively or eliminate or reduce the glare from other pixels
[2663.94 → 2670.72] close by maybe and then the knits for whiteness but for when it's actually like showing colour is it still
[2670.72 → 2677.62] just RGB colours that it's like RGB LEDs that it's putting together and is there just more of them to
[2677.62 → 2682.76] allow it to that I don't know I'm assuming more powerful and then the colour space it's just the math
[2682.76 → 2689.02] that's built into the hardware is able to do the sub pixel oh it's not sub pixel but like floats
[2689.02 → 2694.40] you know how you now have float values and um you know those might not have been able to be done with
[2694.40 → 2698.78] older TVs they didn't have the compute power, and now we have the compute power so they're doing the float
[2698.78 → 2704.46] numbers, and so they're getting micro adjusted in the water which is why you get possibly a million
[2704.46 → 2713.20] more blues in between two other blues it gets really heavy yeah so we have like are the extra
[2713.20 → 2719.28] colours are they evenly dispersed throughout the luminance or like do we have more just like brighter
[2719.28 → 2725.26] like do we get brighter colours, or we get more colours like evenly throughout the spectrum excellent
[2725.26 → 2730.82] question uh so if you think about the gamuts are the totality of colours possible so if
[2730.82 → 2736.82] you're in the p3 colour space uh there's a certain number of colours that it says I can do this if you're
[2736.82 → 2742.20] p3 gamut compliant it means you can represent everything that's out of there and that it is
[2742.20 → 2746.88] just like flattened out kind of, and you get this view that doesn't feel very dispersed it looks very
[2746.88 → 2751.26] evenly distributed but when you get into the colour spaces where you change the shape of something
[2751.26 → 2758.62] the shape change can heavily impact how many you have there but okay so let's talk about like folk
[2758.62 → 2766.76] if you're in the red hue, and you go from lightness 100 to lightness zero this is a superpower of LCH and
[2766.76 → 2774.98] folk these are called pay lab c-i-e lab colour spaces they're perceptually uniform for human vision they
[2774.98 → 2780.64] were tested in the 70s, and they got you know tons of participants to say what was lighter what was
[2780.64 → 2785.88] darker, and they arranged a colour space based on how we see so that it doesn't matter what hue you're
[2785.88 → 2791.70] in you do get an even distribution from zero to a hundred percent this is why it's a powerful space
[2791.70 → 2796.40] for a design system is if you want to lighten or darken a colour you're literally lightening or
[2796.40 → 2801.30] darkening it based on the way that our eyes perceive colour the noticeable difference that the human eye
[2801.30 → 2806.64] can see not the change in a number in a mathematical colour space shape but literally
[2806.64 → 2812.88] something that one percent will change something visually one percent to humans and so that's
[2812.88 → 2817.40] something special for that colour space other colour spaces might not be that way I did want to mention
[2817.40 → 2822.54] one more thing too is sometimes it can sound like when I'm talking about this stuff like RGB is somehow
[2822.54 → 2828.84] not capable or RGB like the lights aren't or just like the colour concept of three channels that way
[2828.84 → 2836.64] is not good it's very good there's colour spaces that use RGB that are very HDR there's an adobe pro photo
[2836.64 → 2843.82] is a very wide gamut RGB based colour space and even rec 2020 has a RGB mode where you can access
[2843.82 → 2849.26] colours using kg and b because so many of our displays display colour that way so we can specify
[2849.26 → 2855.02] you know how much power to put on each of those lights but yeah who I know this stuff gets gear
[2855.02 → 2861.02] to bring it back to CSS a little bit though like I want to chat about like some colour functions like
[2861.02 → 2866.56] so we'll go beyond colour spaces and gamuts and kind of chat about like usage and stuff that you
[2866.56 → 2871.60] might do inside your application that's handy and how sass helped and how sass is adapted to the
[2871.60 → 2877.32] changes in CSS uh as well yes, yes I went to ask about this unless there are more questions but yeah
[2877.32 → 2883.26] let's do that cool okay so in sass you've had dark and enlightened for a long time those were always
[2883.26 → 2888.12] done in the colour space that they knew best which was RGB they've changed it now actually they don't
[2888.12 → 2892.86] they didn't change it, but they did do you remember when they stopped saying using light and darken
[2892.86 → 2898.30] they said use colour adjust didn't get that memo yeah a lot of people didn't get the memo they gave
[2898.30 → 2902.18] they gave that memo because people were really realizing that darken and lighten would sometimes
[2902.18 → 2909.86] give them weird results and so colour adjust was used to do the same work with a very similar syntax
[2909.86 → 2916.32] but in a better colour space so that the results weren't so weird so now we have CSS which can it
[2916.32 → 2921.42] can lighten and darken colours and so there are two different ways to do it one has great support and
[2921.42 → 2927.26] one is on it's way the great support method is the colour mix function you call the colour mix function
[2927.26 → 2932.90] you pass two colours you can say which colour space to mix them in, and you'll get an output result of
[2932.90 → 2939.02] them you can mix a colour with transparency so to make a colour more or less transparent you can mix a
[2939.02 → 2944.80] colour with white to lighten it if you want to lighten it in a sort of like mixing fashion and
[2944.80 → 2950.28] you can darken things by mixing it with black or another darker version of the hue and that's colour
[2950.28 → 2955.80] mix it's kind of I don't know a little basic in its way because it only out, but there's also one
[2955.80 → 2960.30] called relative colour syntax which allows you to so let's say you have a brand colour that's like
[2960.30 → 2965.76] pound f one zero or whatever right this is again like a designer give you a hex colour, and you need to
[2965.76 → 2969.84] do manipulations on it, you can now say colour so we're going to use the colour function like we were
[2969.84 → 2977.18] talking about earlier with display p3 colour open parentheses from your hex colour and when you
[2977.18 → 2983.08] say colour from well you can even say like ok LCH from you're going to get back a restructured version
[2983.08 → 2989.14] of that colour in the colour space that you asked for it so you could say HSL from hex, and you'd get HS
[2989.14 → 2995.48] and l back you could say uh ok LCH from hex, and you would get LCH back and when you get those values
[2995.48 → 3000.52] you can use the call function to increase or decrease them or divide them or multiply them so
[3000.52 → 3005.34] you could double the amount of saturation you could divide the saturation you could divide the lightness
[3005.34 → 3010.98] you can also just squash it so you could be like hey I got LCH back I don't care about l I want a
[3010.98 → 3016.04] really dark version of this colour and so you set l to five percent or something like that now you have
[3016.04 → 3021.08] a really dark version of that hex colour and so you're getting these new functions that allow you
[3021.08 → 3028.10] to very dynamically build out variants and derivative colours and like derive colours from
[3028.10 → 3034.20] other ones and build entire systems and entire palettes that are very robust and consistent again
[3034.20 → 3039.52] if you're working inside that LCH or ok LCH space you're going to get that consistent lightness
[3039.52 → 3045.12] so if a user chooses they want the theme to be green they get a nice visually consistent green theme if
[3045.12 → 3049.30] they change it to red they're going to get something that's perceptually the same lightness
[3049.30 → 3054.72] across the board just a different hue, and it turns out HSL does not have that power it has a lot of
[3054.72 → 3061.18] oddities in terms of lightness, so yeah relative colour syntax often called RCS and the colour mix function
[3061.18 → 3066.66] are here to save the day for mixing colours making variants and just doing overall colour manipulation
[3066.66 → 3073.00] inside CSS what the heck CSS added all these cool features and I didn't even notice
[3073.00 → 3079.14] this is amazing yeah the sad thing too is like I'm looking I'm googling this stuff as you're like
[3079.14 → 3084.00] saying it and I'm seeing all these like blog posts from 2021 and I'm like wow it's just no idea
[3084.00 → 3090.42] don't worry i if anything everyone is probably in the same seat sitting in their car listening to
[3090.42 → 3096.46] this episode going i just still use hex well I have news for you all there is this is the best time
[3096.46 → 3104.90] to ramp up skip HSL skip hub go straight for folk if you want my recommendation right now go straight
[3104.90 → 3110.50] to folk and go start playing with it in the browser go see the colours that you can get from
[3110.50 → 3115.36] it like maximize the chroma change the lightness and look to see how these things change and go build a
[3115.36 → 3120.72] little colour system with it, I also have convenience things so you can open props has a couple of packs
[3120.72 → 3126.46] that are folk packs ready for you to go, or you just import this one line uh you know it's like
[3126.46 → 3133.54] open props like from unpackaged, and you get 15 folk props from me that you can then go change the hue
[3133.54 → 3138.80] and the chroma of and get entirely new palettes in any hue and any colour that you want you can start
[3138.80 → 3142.82] playing with those right away and I'll put those in the show notes too it's cool stuff we're gonna
[3142.82 → 3148.60] really it's a cool time to start switching um I think by 2024 we're going to see it you know well
[3148.60 → 3153.44] supported in browsers, and it won't be an issue, and we'll be off to the races with wide gamut colours
[3153.44 → 3167.20] in our apps it is now time for a changelog news break the team at sun AI is helping change the game
[3167.20 → 3174.30] in text-to-speech realism by releasing bark a transformer-based text-to-audio model that can
[3174.30 → 3179.58] generate highly realistic multilingual speech as well as other audio including music background
[3179.58 → 3187.56] noise and simple sound effects it can also laugh sigh cry and make other non-word sounds that people
[3187.56 → 3196.18] make crazy right here's an example that includes sad and sighs meta tags my friend's bakery burned down
[3196.18 → 3206.92] last night now his business is toast and here's one more with laughter I don't like pie torch Kubernetes
[3206.92 → 3216.32] or schnitzel and xylophones flummox me you can still hear some digital artifacts and blips here and there
[3216.32 → 3221.98] but we're getting closer to synthesized audio that's indistinguishable from the real thing
[3221.98 → 3230.38] and that's cool slash scary you just heard one of our five top stories from Monday's changelog news
[3230.38 → 3235.92] subscribe to the podcast to get all the week's top stories and pop your email address in at
[3235.92 → 3242.10] changelog.com slash news to also receive our free companion email with even more developer news
[3242.10 → 3247.00] worth your attention once again that's changelog.com slash news
[3247.00 → 3267.74] so that's a great segue into the question I wanted to ask which is like what's the support
[3267.74 → 3275.06] like for this within like design tools because like when I think of like you know doing this i
[3275.06 → 3281.36] usually get like a Figma design from our UX folks and I have to like to translate that into
[3281.36 → 3286.50] the web somehow and I'm looking at you know the exact colours they give me and Figma is usually giving me
[3286.50 → 3294.82] right now it's RGB or hex colours so can these be defined in tools like that or should I go back to
[3294.82 → 3301.42] them and be like I'm going to translate this to folk and watch their faces melt like mine or like
[3301.42 → 3308.04] what's the support like for that yes great question so photoshop has had lab in it which is
[3308.04 → 3313.74] a pay lab colour it's kind of like LCH it's been in there for years people just don't use it they're
[3313.74 → 3319.68] just very accustomed to poking inside the pool of RGB yeah a lot of designers also pick colours
[3319.68 → 3324.44] from their I'm going to say from their heart you know it's its like a subjective thing like they're
[3324.44 → 3328.68] not there doing mathematical computations like we do in code we're like no I want to know it's
[3328.68 → 3333.62] five is it five percent, and they're like it's 5.25 darker, and you're like I'm going to round it, I'm
[3333.62 → 3337.52] going to round that because it don't matter you know uh, and it makes my code look cleaner if I don't have
[3337.52 → 3342.74] the sub anyway um okay so that's off the topic Figma does not have support for these you're right
[3342.74 → 3348.34] it's stuck in RGB it's SDR only they target multi-platforms they're not just web they're not
[3348.34 → 3352.62] just I'm in talks with them right now about trying to figure this out I'm like hey these colours are
[3352.62 → 3356.64] better the gradients are better I know you like product excellence I know that most of your targets
[3356.64 → 3363.52] are iOS and android apps those are HDR spaces and now the web is HDR you can get HDR across the
[3363.52 → 3370.04] board now make that the common denominator and offer hex as an as an export option there is a
[3370.04 → 3374.98] plugin that you can get in Figma Adobe XD does not have wide gamut colours pretty much it's exclusively
[3374.98 → 3379.74] photoshop right now and then web tools there are a bunch of web tools that'll help you make HD colours
[3379.74 → 3384.62] but yeah I'm I'm very much in the same boat as you are I'm like if designers aren't handing these
[3384.62 → 3389.28] off to developers it's probably not going to get done except for those there are a lot of folks that
[3389.28 → 3394.10] spend a lot of time in design systems managing the colours of their application and building robust
[3394.10 → 3400.40] systems they are going to be stoked on folk and these colour functions they're going to get rid of
[3400.40 → 3404.30] all sorts of stuff they're going to build it natively into their CSS, and they're going to get
[3404.30 → 3411.22] awesome results so less code better results, but yeah until designers are handing it off it's probably
[3411.22 → 3417.12] going to be a slow ball to get pushed up a hill yeah so it could be on you to do it, and you could
[3417.12 → 3421.26] honestly I think a lot of we're going to see right now is some bottom-up education happening where
[3421.26 → 3424.96] developers are like I got this new tool and look at these gradients they're sick and the designers
[3424.96 → 3430.66] can be like your gradients aren't better than mine your gradients are better than mine you'll be like
[3430.66 → 3434.76] all right yeah let's talk about it, you know like let's get these in the app let's get you know they
[3434.76 → 3440.92] look fresh anyway so that's what that's going to happen to speaking of gradients can I share my
[3440.92 → 3447.70] tool I want to announce a tool to help people so I mentioned oklch.com which is a phenomenal folk
[3447.70 → 3452.42] colour picker I have been working for the past few months to help enable people into getting into these
[3452.42 → 3458.26] new colour spaces to learning and seeing what CSS colour can do and especially seeing the results that
[3458.26 → 3465.00] you get in CSS gradients you can now go to gradient. Style and that's where I'm building a very
[3465.00 → 3472.46] much it looks like a design tool to help you build these new HDR gradients and see the SDR version
[3472.46 → 3477.56] fallback so I'll generate a fallback gradient for you and I generate the new modern gradient for you
[3477.56 → 3482.96] you can change colour spaces you can do all the stuff, and it's really, really nice really visual
[3482.96 → 3489.06] and you can um even drag it across from a know a SDR monitor to a HDR monitor and kind of see it
[3489.06 → 3493.86] that way as well and just see the change and start to feel out these colours I think there's two main
[3493.86 → 3497.92] things on that tool that are really fun to do well there are a lot of main things to do but the first one
[3497.92 → 3502.84] is use the colour picker so if you see a little colour dot that's one of your colour shops click it and
[3502.84 → 3509.34] you'll get the world's first next gen CSS colour picker where it supports every colour space that CSS
[3509.34 → 3514.16] supports they're even grouped and tell you if they're HD or SDR and stuff like that which is
[3514.16 → 3518.26] really nice, and they give you little control to go play inside there, and it will convert so if
[3518.26 → 3523.48] you have a hex colour for example you can paste a hex colour into the colour stop open up the colour picker
[3523.48 → 3529.82] go to ok LCH it will convert the hex to ok LCH, and then you can go bump the chroma up and be like how
[3529.82 → 3534.20] much brighter can I make this hex you're like oh crap that's a lot brighter, and you can do that
[3534.20 → 3539.04] another fun thing to do is to try on the gradients that are in the bottom left there's some
[3539.04 → 3543.76] presets where I've created some things for you to go explore and try on and then there's a discord
[3543.76 → 3548.38] if you want to join and ask questions and learn more about colour spaces and about CSS colour in the
[3548.38 → 3553.40] top right there's a settings cog click that and go to uh I think it's like help and feedback or
[3553.40 → 3557.76] something like that and that'll pump you out to the discord to come have conversations in there
[3557.76 → 3563.38] there's also uh just above that is a tips and tricks, and you can click that and I put a bunch of hints
[3563.38 → 3568.20] all over the UI to help you learn about what the UI is doing and help you get you the ball rolling
[3568.20 → 3574.16] into building a new gradient in these new colour spaces um yeah gradient. Style I'm gonna probably
[3574.16 → 3578.26] be working on it till the end of the year you can tell some of the stuff's not done it's in beta but
[3578.26 → 3585.48] it's its a really strong place to start as we transition as an industry out of SDR which we've
[3585.48 → 3592.10] been in for 25 years into HDR it's just the future this is so cool I've just been poking around and
[3592.10 → 3599.16] and not listening to you but if you're listening you should go check it out also there's a can
[3599.16 → 3604.96] set the hue path like you can do like the longest path between two colours instead of the
[3604.96 → 3610.28] the shortest yes okay, so this is such a cool one it only works for cylindrical colour spaces it's like
[3610.28 → 3615.70] HSL is a cylinder it only works if the hue is an angle and the way that it works is it's just like
[3615.70 → 3620.68] Zoolander like literally RGB has been like Zoolander this whole time when it can, you know like
[3620.68 → 3624.04] Zoolander could only turn right he'd get to the end of the stage and be like oh wait I can only
[3624.04 → 3632.74] turn right not an Ami turner that's awesome dude now you can tell it to turn the other way so
[3632.74 → 3635.94] basically it would always take the short path right I'd always take the short straight shot
[3635.94 → 3641.22] or to always rotate around the clock the fastest way to get to its destination, and now you can say
[3641.22 → 3647.14] hey go the long way, and you can um there's been people on Twitter making fun demos of this where
[3647.14 → 3651.70] you can say hey I want a gradient from red to red and I want you to go the long way and it literally
[3651.70 → 3656.94] makes a rainbow because it took the long way around it collected every hue all the way around
[3656.94 → 3662.26] 360 degrees if you open up my colour picker, and you see that little hue strip that shows the rainbow you
[3662.26 → 3667.16] know where you're choosing the hue that's literally the colour gradient that I've drawn from red to red
[3667.16 → 3672.08] telling it to do the longest hue or the longer hue interpolation, and it'll take the long way
[3672.08 → 3677.34] it's so cool you used to have to make a gradient with like 12 stops in it to represent all the main
[3677.34 → 3681.74] hue points or whatever and even then it might be a little wrong uh now it's right it's really cool
[3681.74 → 3687.68] yeah hue interpolation it's that's that's a new one to that's getting deep into the weeds of
[3687.68 → 3694.20] colour as well because you have to yeah that's the colour space offering a feature of an angle rotation
[3694.20 → 3700.44] yeah it's cool stuff I'm blowing my mind this is super cool yeah, and it's all typed nick it's
[3700.44 → 3706.70] typed from top to the bottom dude typed you can't break it uh it'll only work if you pass in proper
[3706.70 → 3711.60] you know length percentages or lengths and stuff like that it's its good stuff or angles which
[3711.60 → 3715.00] means you can pass rads to it, you're like that's one of my favourite colours to do is
[3715.00 → 3721.28] two rad oh yeah this colour is two rad dad colour jokes
[3721.28 → 3730.26] this tool is really cool and I'm looking at the CSS that is like you have the modern gradient and
[3730.26 → 3735.62] a classic gradient for each afterwards and like I was just curious because I was looking at some
[3735.62 → 3743.02] other example too and this like English just in the middle of the gradients is blowing my mind
[3743.02 → 3749.36] I don't even know how to search for it, but it's like from zero degrees at centre in okay LCH decreasing
[3749.36 → 3756.02] like it's I don't I don't even know I don't know my brain is shut off no that's that's perfect so
[3756.02 → 3760.76] um no that's a and if you look at the classic one it has a lot of the same English in it one of the
[3760.76 → 3765.74] differences is the in keyword which is new with colour spaces so you have these like definitions
[3765.74 → 3770.24] about the prelude or like the first part of your gradient there is about size and position
[3770.24 → 3775.82] and now we have the addition of which colour space do you want it in and that's where those things are
[3775.82 → 3779.54] coming from and that's sort of what I wanted my tool to also do is because if you go to like
[3779.54 → 3784.72] I don't know some other gradient generator online they don't tell you that there are these keywords
[3784.72 → 3791.32] and some of the keywords are rad like to top right is responsive out-of-the-box like if you said
[3791.32 → 3797.50] 45 degrees it's not responsive it'll stay straight, and you can see that in the tools you resize the box
[3797.50 → 3802.72] you'll see that the degrees stay still but if you do top right it literally takes the first colour
[3802.72 → 3807.34] and make sure that it ends perfectly in the bottom left corner and that the last colour ends
[3807.34 → 3813.12] perfectly at the top right that's why as you resize the box the line the gradient line changes to make
[3813.12 → 3819.10] sure that in the top right is the last colour perfectly ending at the corner's edge and then if
[3819.10 → 3824.68] you go to the radial tool, and you look at things like farthest side or nearest corner my tool now
[3824.68 → 3829.78] visualizes that for you so you can see what it's doing, and it's really rad stuff so some of these
[3829.78 → 3833.84] keywords some of these features that are inside of gradients they've been hidden for years and I'm
[3833.84 → 3838.66] hoping this tool unlocks them for people, and they realize that I can put a gradient in the centre with
[3838.66 → 3843.88] just a keyword like that's awesome and all this stuff so I'm hoping it's like multi-prong here it's
[3843.88 → 3850.54] giving you access to wide gamut colours you know spec compliant colour picker spec compliant wide gamut
[3850.54 → 3855.24] gradients and then just spec compliance in general that the tool is facilitating these things for you
[3855.24 → 3861.54] in terms of the linear conic or radials powers what are its superpowers including double positions
[3861.54 → 3866.58] did you pull it did you pull the second percentage on one of those colour stops such a hidden feature
[3866.58 → 3871.22] of gradients that people don't know exists is double stop you can have a double position gradient
[3871.22 → 3877.46] and you'll see my tool will split the circle in half, and then you'll have two crescents yes I was
[3877.46 → 3882.22] wondering what was going on there and Nick's nodding his head he's like I see the two crescents
[3882.22 → 3888.74] yes um okay so you got like a colour stop you got a colour stop uh that says all right just uh start
[3888.74 → 3892.46] the colour here, and then you add another colour stop, and it says all right and move it from this colour
[3892.46 → 3898.40] to that one to the other stop but if you split it you say I want this colour stop to span a
[3898.40 → 3904.62] range and then transition to the other stop, and it also has superpowers like you can set the second one
[3904.62 → 3910.26] to zero, and it creates a hard stop so you're grading your colour goes you know up to 10 percent and
[3910.26 → 3916.12] then your second position said zero, and it will end there, and you can make hard stop gradients really
[3916.12 → 3922.40] easy by using the double position syntax i also in my tool have transition hints and those are the
[3922.40 → 3928.30] uh sliders in between colour stops which allow you to tell it how to transition between the two which
[3928.30 → 3933.06] of the two colours is more dominant in the interpolation from one to the other and then I visualize that on
[3933.06 → 3937.60] the gradient to you can see the little arrow thing, and you can drag it and see how it changes the
[3937.60 → 3941.58] gradient so it's like there's been hidden superpowers in here it's like specialists have
[3941.58 → 3945.36] only known and I'm like no people need this they need this in their hand so I started building a
[3945.36 → 3951.18] tool to like put all this into one and help folks out this is awesome it's like those uh videos
[3951.18 → 3957.16] of people doing like elaborate tie-dye patterns where they like they're folding things in very
[3957.16 → 3961.74] specific ways, and then you know putting the dye on in very specific ways, and then they get this amazing
[3961.74 → 3967.14] pattern at the end when they hang it up I was watching one of those on Reddit recently and so
[3967.14 → 3970.38] sounds mesmerizing yeah it does
[3970.38 → 3976.86] that's that's kind of everything I mean yeah I mentioned open props has some stuff in there too
[3976.86 → 3981.00] so if you want to start in this like next gen colour stuff there's some good starter packs for you there
[3981.00 → 3985.98] they're they're in beta right now right okay there's no Firefox support so I'm not and I'm just playing
[3985.98 → 3990.80] with this idea but I really like the way that it's headed right now where that you just import this one
[3990.80 → 3995.74] set of 15 custom properties, and then you can just change them however you want, and then you get
[3995.74 → 4002.40] any colour palette of any hue perfectly from light to dark at any amount of vibrancy that you want so
[4002.40 → 4006.76] no longer will you visit a website and be like I've got 12 colours to choose from I can choose jungle
[4006.76 → 4012.82] or grape, or you know lemon uh that's that's gone you're just going to pull in 15 props and be like
[4012.82 → 4018.96] no hue 210 that's our brand hue and now I got an entire palette that's perfectly you know perceptually
[4018.96 → 4024.52] linear lightness, and you go nuts that's really cool this is such a cool tool it's just moving
[4024.52 → 4030.20] those liners back and forth I also love that it's like uh it's encoding it into the URL too so you
[4030.20 → 4034.62] can share what you create yeah as well you can definitely yeah paste it into the chat let's see
[4034.62 → 4040.96] what you made to yeah I was going to say challenge monstrosity challenge gradient. Style and share with
[4040.96 → 4046.78] us on the socials what uh what you come up with totally I'm excited to see them and I had fun
[4046.78 → 4052.58] naming all of them you know I got like sound wave solid to oh here um there's one in the HD example
[4052.58 → 4059.18] it's called solid click that one did you know a gradient can take just one stop and still be valid
[4059.18 → 4064.58] you have to use the double position syntax because you can say hey I want this colour to span from zero
[4064.58 → 4070.12] to a hundred percent, and now it's a single colour stop gradient that goes all the way across the
[4070.12 → 4075.84] canvas and a lot of people would reach for a background colour to do this, and you don't have to so if
[4075.84 → 4080.66] you do a multi-gradient multi-layered gradient you can put solid colours in there that way, and it's
[4080.66 → 4086.48] this tool visualizes it for you which I think is unique yeah this is the best kind of
[4086.48 → 4091.56] learning environment yeah right you're just kind of figuring things out as you go yeah here I'll
[4091.56 → 4097.00] share that one in the chat there I tried some compression algorithms on the URL too so I could fit
[4097.00 → 4103.50] more colour stops in there I was using a base 64 and some other things but I liked the readability
[4103.50 → 4108.46] that you have right now you can kind of parse the URL, and it doesn't look tricky you're not going to
[4108.46 → 4114.04] get sent a URL it's like if I click this what's going to happen I see some obfuscated data that
[4114.04 → 4119.64] makes me feel uneasy and so now it's not obfuscated, but anyway it might as well be straight CSS
[4119.64 → 4126.18] for me at this point yeah svelte kit has been awesome on this tool um I already liked svelte but
[4126.18 → 4131.30] man it's been phenomenal, and then it is typescript but I use a very light amount of typescript I'm like i just
[4131.30 → 4136.32] kind of understand my code I don't want to go nuts with types because it just is a slippery slope for
[4136.32 → 4141.10] me I'm like oh I'll just type this parameter oh I'll just type its return type oh just and then
[4141.10 → 4146.08] it's all of a sudden I'm like oh what did I do my function was already working you know there was no
[4146.08 → 4153.04] bugs what am I doing you're like I'm hardening it you're like yeah I guess I need tests though I do
[4153.04 → 4157.02] need to write unit tests and stuff I don't have those yet oh you have types that's a good start
[4157.02 → 4163.26] light types I'm a light typer these days I've I've been to the dark side of heavy typing and I'm
[4163.26 → 4170.06] like no well I'm a light type yeah there's a balance for sure it's like that uh not now someone's wrong
[4170.06 → 4175.94] on the internet not now there's a type that's slightly incorrect somebody put any in my code base
[4175.94 → 4184.76] well you all feel you like you understand SDR versus HDR now, and you're like I got some new functions to go
[4184.76 → 4189.80] try yeah what's remaining in your mind other than like if it's a very changeable thing your eyes need
[4189.80 → 4193.78] to see it your fingers are going to change numbers in these colour functions, and you're going
[4193.78 → 4199.16] to you know see the results and that's definitely the next step is to go play so yeah hopefully this
[4199.16 → 4205.70] playground is good for that yeah yeah definitely it is it gives you good ideas on how to do these
[4205.70 → 4211.94] things my mind is empty at this point trying to make sense of this but i I definitely see the
[4211.94 → 4220.72] value of these new colour values it's just when to or how to practically apply them is still like
[4220.72 → 4226.06] the difficult part for me, and it mostly comes down to like if i receive a hex colour from my
[4226.06 → 4233.02] from my UX team I'm probably going to use that still, so the tooling needs to come around but yeah
[4233.02 → 4237.62] totally it's its really cool yeah that's it that's why I'll, I'll share my site in the chat there
[4237.62 → 4243.18] just because um yeah you'll open it up, and you'll be like nothing here really looks HD
[4243.18 → 4248.36] but it's me being the designer that in like a subtle way like the background colour is not black
[4248.36 → 4255.58] it is very dark rich cool gray you know it's like and if you open up the colour picker oh Chrome dev
[4255.58 → 4259.26] tools has cool features for this too so does safari by the way like if you're debugging this in the
[4259.26 → 4264.26] browser the Chrome dev tools colour picker is updated now you'll see a cutoff where display p3 is
[4264.26 → 4269.26] kind of like you saw in the oklch.com you can convert in that tool between colour spaces
[4269.26 → 4274.62] but it's really nice to visualize when you're like this colour doesn't feel that bright and then when
[4274.62 → 4280.34] you go see, and you drag the thing down into the RGB colour, and you're like oh okay like when I see it
[4280.34 → 4286.28] downgraded i I definitely feel that, but you might not get that sense immediately uh that it's somehow
[4286.28 → 4289.78] special but I don't know this is one of those things that's why apple has had it for so long
[4289.78 → 4296.16] before everyone else they knew that that subtlety couldn't be articulated by many but that they've
[4296.16 → 4300.62] they would feel it and see its excellence and hopefully that's what you see on my site too like
[4300.62 → 4305.00] if you look at my code snippets on any of my blog posts you'll be like wow those colours are really
[4305.00 → 4310.16] neon it's that's because I'm definitely pushing those to display p3 maximum that's fun stuff I did
[4310.16 → 4317.78] notice that and i I want a vim colour scheme based on that now so yeah how long until VS Code has uh
[4317.78 → 4322.74] HD colour support and all of our colour themes now have better dark colours richer dark colours
[4322.74 → 4327.18] whiter whites and more vibrant neons for all of our highlighting I'm serious we're all going to
[4327.18 → 4332.48] switch to colour themes that are HDR that's going to be amazing well cool yeah we will have all of these
[4332.48 → 4339.16] links in the show notes including um gradient. Style which you heard about here first go share your
[4339.16 → 4345.30] amazing gradients on the socials and with Adam and join the discord Adam anything else you want to add
[4345.30 → 4351.14] no you all's show is so good I really appreciate you having me on and continue the amazing content
[4351.14 → 4356.50] don't stop this it's just you all rock really appreciate if it's just because of amazing guests
[4356.50 → 4362.92] like you, so thank you for coming on and uh Amelia you want to add anything else no I'm I'm stoked to
[4362.92 → 4370.58] try this stuff out same yes i I can't wait I'm going to share a couple of uh gradients and see uh
[4370.58 → 4378.10] how they compare cool well thank you so much for coming on, and we will catch you next time
[4378.10 → 4391.06] one cool thing about our new changelog newsletter is that we don't proxy links like almost everyone
[4391.06 → 4397.56] else does that's awesome because a there's no tracking and b you can hover on a link to see
[4397.56 → 4402.80] where you're headed before clicking I do that all the time if you appreciate direct links as much as
[4402.80 → 4409.06] I do pop in your email address at changelog.com slash news because the software world moves fast
[4409.06 → 4415.40] and we'll help you keep up the easy way special thanks once again to our partners quickly and fly
[4415.40 → 4420.40] for helping us bring you awesome pods each and every week and of course thank you break master
[4420.40 → 4428.30] cylinder these beats are banging next up on the pod DAX rad from SST joins nick and cable to talk
[4428.30 → 4435.18] about open next and open source Next.js serverless adapter stay tuned right here we'll have that
[4435.18 → 4437.24] episode ready for your ear holes next week
[4437.24 → 4442.18] you
