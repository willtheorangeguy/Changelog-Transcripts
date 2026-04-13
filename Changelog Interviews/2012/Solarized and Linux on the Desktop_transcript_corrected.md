[0.00 → 6.40] The Change Log is brought to you by Pusher, and they're looking for a system engineer with experience building scalable messaging systems.
[6.94 → 14.18] If that's you, send your GitHub profile, your cover letter, and your CV to jobsatpusher.com.
[14.18 → 20.76] And also, use the coupon code CHANGELOG for 15% off your first month on any plan.
[21.28 → 23.90] Join the real-time web today at pusher.com.
[30.00 → 41.98] Welcome to The Change Log, episode 0.7.7.
[42.16 → 43.20] I'm Adam Stachowiak.
[43.38 → 44.26] And I'm Won Netherlands.
[44.26 → 45.34] This is The Change Log.
[45.42 → 46.94] We cover what's fresh and new and open source.
[47.38 → 49.92] If you found us on iTunes, we're also on the web at thechangelog.com.
[50.14 → 50.98] We're also up on GitHub.
[51.28 → 52.80] Head to GitHub.com slash explore.
[52.88 → 57.00] You'll find some training repos, some feature repos from our blog, as well as this audio podcast.
[57.00 → 59.42] And if you're on Twitter, follow The Change Log.
[59.88 → 61.06] And I am Adam Stack.
[61.40 → 63.62] And I am Penguin, P-E-N-G-W-Y-N-N.
[64.06 → 64.94] Fun episode this week.
[65.04 → 66.80] Talked to Ethan Schooner from Solarized.
[66.84 → 72.48] Unless you think we talk a full hour about a, I guess, a theme for a text editor.
[72.88 → 74.12] We talked about so much more.
[74.46 → 81.32] Did talk about Solarized quite a bit in the theory behind the colour selection and a lot of the underlying science behind the design.
[81.38 → 83.94] But also talked about Linux tools in general and Arch Linux.
[84.26 → 85.46] He's a bit of an audiophile.
[85.46 → 89.86] So we talked about the full gamut of his seeker.
[90.30 → 91.34] Took a little preview of that audio.
[91.44 → 92.72] His audio sounds pretty good.
[92.98 → 93.96] He sounds better than I do.
[94.10 → 100.30] But I don't want it to sound too good because, you know, the bootleg sound quality gives us some street cred, you know?
[100.38 → 100.88] Sure does.
[100.92 → 101.44] Yeah, it does.
[101.48 → 102.02] That's what I hear.
[102.72 → 103.34] Fun episode.
[103.42 → 103.94] Should we get to it?
[104.18 → 104.74] Let's do it.
[104.74 → 117.54] Chatting today with Ethan Schooner from Solarized.
[117.92 → 120.26] So, Ethan, why don't you introduce yourself for our listeners?
[120.92 → 121.26] Sure.
[121.36 → 123.68] Well, I'm a freelance designer.
[123.68 → 131.78] I'm based here in Seattle and I moved back to the States about four or five years ago to work with a Mac software firm, Omni.
[131.86 → 132.72] I don't work with them anymore.
[132.88 → 133.92] I'm purely freelance.
[134.68 → 140.48] And over the past couple of years, I've been getting more involved on Linux and the open source community.
[140.48 → 148.72] And I guess part of that is my developing, I guess, what you could call a universal colour scheme called Solarized.
[149.20 → 151.36] So I'm happy to go into some more detail there.
[151.48 → 153.46] Do you want to just shoot me some more questions?
[153.68 → 153.82] Yeah, let's jump into Solarized.
[153.98 → 158.74] So 2,200 watchers on GitHub for what is essentially a colour scheme.
[159.14 → 161.28] And a bead of sweat rolls down on the forehead.
[161.76 → 165.20] Give us some background on why you started this project.
[165.20 → 165.68] Sure.
[166.34 → 169.66] Well, this was, I guess, late 2010.
[170.80 → 173.58] I started to get pretty heavily into Linux on the desktop.
[174.34 → 178.18] And so I started to build a couple Linux boxes.
[178.18 → 181.50] I've always been using Debian, Ubuntu for servers.
[181.92 → 185.18] But I'd never really been a very heavy Linux on the desktop user.
[186.36 → 188.14] And so I don't know.
[188.16 → 190.72] I had a couple old ThinkPads lying around.
[190.72 → 197.22] And I started to play around with Arch, Fedora, Ubuntu, and whatever the current releases were.
[198.08 → 200.96] And at the same time, I started to retrain myself in a number.
[201.38 → 204.48] I was still using the Mac pretty heavily.
[204.82 → 214.04] But I felt this urge, as I think a lot of people do and perhaps still do right now, to move away from proprietary systems to more open systems.
[214.18 → 215.60] So I started to use Vim pretty heavily.
[216.46 → 219.16] And I just couldn't find a colour scheme that I liked.
[219.16 → 224.04] So, you know, I noticed also in the terminal I couldn't find a colour scheme that I was very happy with.
[225.06 → 226.66] I started to use Show a lot.
[227.48 → 231.78] So I looked around, and I saw there were some very pretty colour schemes, certainly.
[232.14 → 233.10] I was using Herald.
[233.20 → 235.06] I was using Zen burn for a while.
[235.90 → 238.52] I didn't really like the colours of Zen burn.
[238.52 → 244.44] But, you know, I felt like I liked the strategy they had of being a low-contrast colour scheme.
[245.30 → 247.52] So I thought, well, you know, hey, this is going to be easy.
[247.58 → 250.92] I'll just edit the colour scheme that they have for Vim.
[251.02 → 252.62] And I opened up the Vim Script file.
[252.94 → 265.52] And I think, you know, if you've ever opened up a Vim Script file your first time, and you have this kind of shock of seeing something very alien-looking, which Vim Script is, you know, I realized it wasn't going to be an easy undertaking.
[265.52 → 271.44] And I also realized that the way they had designed the colour scheme wasn't how I would have gone about it necessarily.
[271.64 → 272.54] It's that implementation.
[272.80 → 274.78] And, you know, I'm not faulting Zen burn.
[274.90 → 276.44] It's a very nice implementation.
[277.66 → 279.76] But so I decided I would give it a go on my own.
[279.92 → 283.66] And then, you know, that led – that was sort of the kick, you know, the jumping off point.
[284.48 → 289.26] And I really – you know, it's one of those projects where you only do when you don't know what you're getting into.
[290.42 → 290.82] Right.
[290.82 → 291.10] Right.
[291.90 → 297.08] So – and I kind of like to talk a little bit about, you know, some of the strategy behind it and the way it's structured.
[298.38 → 301.64] Do you have any other questions specifically about how I got myself into this mess?
[302.02 → 302.46] I guess.
[302.52 → 304.12] Did you start with Vim or did you start with the terminal?
[305.18 → 305.48] Why?
[307.24 → 308.10] That's a good question.
[309.26 → 311.14] It was pretty simultaneous.
[311.14 → 318.74] You know, I would say I probably started – I probably started with Vim.
[319.64 → 324.36] At least that's foremost in my mind because I was always really focused on doing the Vim colour scheme.
[324.90 → 328.42] But, you know, for me, I was really using Vim primarily in the terminal.
[329.34 → 334.98] You know, in Arch, I was using RVT or RVT-unicode, however you want to say that.
[334.98 → 343.36] And so, you know, using Vim in the terminal, you really have to be very cognizant of terminal colour issues, which are really legion.
[343.62 → 347.16] It's really terrible implementing colour properly in terminal emulators.
[348.78 → 352.50] So it comes in two flavours, I guess, light and dark.
[352.50 → 353.10] Yeah.
[353.30 → 355.54] So let me talk a little bit about the way it's structured.
[356.56 → 370.42] And for folks listening along on the podcast that are in front of a computer, if you're not familiar with Solarized or if you want sort of a refresher, I'm also going to maybe mention a specific image that's on the Solarized homepage.
[370.62 → 371.88] You can just search for Solarized.
[371.98 → 375.02] It should be in the top hits in Google.
[376.72 → 380.96] But it's also ethanschoonover.com slash Solarized is the official homepage.
[380.96 → 392.14] And you can see on that homepage, I've got a, you know, there's an image right at the very top of that page, which is sort of a yin-yang symbol showing both a dark background and a light background.
[392.64 → 395.90] And then below that, the actual palette itself.
[396.00 → 398.98] And that'll be, those will be useful visual aids as I describe this.
[399.06 → 410.12] But the basic idea is that, you know, the terminal emulators, Vim doesn't have this restriction, but terminal emulators are quite restricted in the number of colours they can display for the most part.
[410.12 → 412.20] Some only display 8, some display 16.
[413.12 → 415.30] You know, some you can display 256.
[416.10 → 420.16] Vim, you have a lot more flexibility depending on whether you're in GUI mode or terminal mode.
[421.22 → 425.76] But regardless, I wanted to support kind of the lowest common denominator.
[425.98 → 431.54] So I designed Solarized to fit within the 16 standard colour slots you'd find in a terminal.
[431.54 → 437.20] And I also want, I realized early on that I wanted something that could work in both a light and dark mode.
[437.32 → 441.94] And so I started to map out light colour schemes and dark colour schemes.
[442.04 → 444.08] So in other words, colour schemes with a light and dark background.
[444.94 → 448.12] And keeping in mind that I wanted to work with contrast.
[448.12 → 452.96] And I realized there was a possibility to kind of fit them together into a single colour scheme that was symmetrical.
[453.20 → 462.38] So if you turned it upside down, so to speak, what had previously been the brightest colour of text would in turn become the bright background.
[462.62 → 465.66] And the darkest, the dark background would become dark text.
[466.28 → 467.68] That's a very simplistic description.
[467.82 → 469.20] There's more detail on the page itself.
[469.42 → 472.68] But that's sort of the symmetric quality to this colour scheme.
[472.86 → 474.74] And it's actually a little bit more complicated than that.
[474.80 → 476.40] In fact, it turned out to be a lot more complicated.
[476.40 → 482.98] It took me all in about six months to design the colour scheme and test it and iterate it.
[483.20 → 486.88] Now, do you have a background in colour theory or was this learning for you?
[488.06 → 490.54] Well, you know, I have a weird background.
[491.54 → 495.60] Right before I moved back to the States, I was working as a photographer full-time.
[495.92 → 499.36] And I also have a background in web development prior to that.
[500.26 → 501.40] So in advertising.
[501.94 → 504.54] But when I was working as a photographer, I started to research.
[504.54 → 506.90] And, you know, my parents are both artists.
[507.08 → 511.46] I do have, I guess, a background just through osmosis in the arts.
[511.88 → 516.10] And I had always worked with colour and with design and, of course, in web design.
[516.24 → 521.66] But when you start to do photography very seriously, you have to be very aware of colour management.
[521.66 → 532.66] And I also became familiar with the CIE L star A star B, or it's often called just lab space, the lab colour space.
[533.08 → 539.88] And that's a very useful colour model or colour space for editing photographs, among other things.
[539.88 → 542.92] Because that's not its original purpose by any means.
[543.26 → 545.40] It's a really fascinating subject in its own right.
[545.86 → 555.62] But that background, that familiarity I had with lab and with colour management really did inform the way that I developed Solarized.
[555.94 → 558.66] So for those that don't know, RGB is, of course, red, green, blue.
[558.80 → 561.14] HS, BSU, saturation and brightness.
[561.28 → 561.90] What is lab?
[561.90 → 565.32] So, well, let me backtrack for just a moment.
[566.56 → 571.60] It's really important when we're talking about these things to kind of understand just even what colour is.
[571.92 → 574.52] And, you know, colour is not an external phenomenon.
[574.76 → 576.66] And we often talk about it as though it is.
[576.72 → 578.80] And we think about, you know, we think about RGB.
[579.60 → 584.96] You know if you're going to throw up a, you know, hex value on a web page, and you want red, you do FF0000.
[585.86 → 589.18] And you think, well, you know, I'm making the monitor display red.
[589.18 → 592.02] But, you know, that's not what is happening at all.
[592.12 → 605.02] Really, colour is a lot more like, you know, poetry or music or cinema even in the sense that, you know, when you watch a sad movie, you have a sense of sadness inside of you.
[605.40 → 607.84] But that sadness is not an external phenomenon, right?
[607.90 → 610.54] That's a – it's an induced phenomenon inside your brain.
[611.34 → 614.90] And the sadness is sort of latent inside the storyline.
[614.90 → 623.00] And just like that, colour is latent inside of wavelengths that are – that we're perceiving that are hitting the back of our retina, our fovea.
[624.52 → 637.80] And when those, you know, when those different wavelengths of light hit our retina, when they hit our fovea, and they stimulate the rod cells in our retina, then – and, you know, I apologize, by the way, if anybody is an expert in colour.
[637.80 → 639.22] And I'm butchering this.
[639.28 → 639.94] I hope I'm not.
[641.14 → 647.36] But when they stimulate, you know, the back of our eye and then that goes into our brain, you know, that's when we're perceiving colour.
[647.68 → 655.10] And because of that, because it's an induced phenomenon and not a purely external phenomenon, there's actually a lot of – I don't want to use the term psychology.
[655.10 → 662.34] But there's a lot of variance in how we perceive colour in terms of the actual external stimulus.
[662.68 → 666.74] So back in the – and I'll describe more about what I mean by that.
[667.28 → 677.96] Back in the 20s or 30s, I think it's the – probably throughout the 20s, there was a lot of colour research that was being done in Europe.
[677.96 → 684.36] And there was a researcher named Wright – I hope I'm getting this right.
[684.92 → 685.66] His name was Wright.
[686.36 → 688.16] And I forget his first name.
[688.86 → 690.18] And there was another fellow too.
[690.52 → 691.78] They were both based in London.
[691.78 → 694.70] And they were both doing similar experiments independent of each other.
[695.18 → 702.90] And basically what they wanted to do is they wanted to figure out basically what I described, how we perceive colour in our brain.
[702.90 → 713.48] And how we can mix together different TRI-stimulus values, red, green, and blue, in order to recreate perceived colour values.
[714.24 → 718.78] So what happened is that this fellow Wright, he was like a colour researcher.
[719.28 → 723.36] And he – it was kind of an ambitious effort, right?
[723.38 → 727.24] I think today if you wanted to do something like this, there would probably be like an fMRI involved.
[727.74 → 732.02] But, you know, 1920s, they still have like horse-drawn carriages rolling around London, right?
[732.02 → 733.16] So it's pretty primitive.
[733.64 → 746.58] So what he does is in order to figure out what's going on in your brain when you see these different RGB values essentially is he set up a screen with a couple holes in the screen.
[746.68 → 751.94] And he set these test subjects in front of the screen, and he made them look through these tiny holes.
[752.54 → 761.18] And the holes were about – two-degree holes are about the same size as the field of view of your fovea, which is the little highly sensitive spot on your eye.
[762.18 → 767.10] And so he had these people looking through the screen at two different spots of colour.
[767.24 → 771.78] And one was being generated by kind of pure light, like a pure yellow light.
[771.96 → 774.60] And the other was a mix of red, green, and blue lights.
[774.80 → 784.18] And then the subject would, you know, fiddle some dials and adjust those red, green, and blue lights until the colour spot, the mixed colour, matched the pure colour.
[784.18 → 795.02] And then they would measure the pure colour, the wavelength of the pure colour, and they would figure out based on that wavelength what values of red, green, and blue light they had to mix to achieve a matching colour.
[795.02 → 800.54] And so that was the start of the CIE colour spaces.
[800.54 → 803.00] That was, I think, CIE XYZ.
[804.70 → 809.50] And so CIE is the International Colour Consortium of – well, no, that's not right.
[809.60 → 810.92] International Colour – I forget.
[811.20 → 815.50] It's a French word, and I'm going to butcher that, so I'm definitely not going to say it, at least not on the air.
[815.50 → 819.16] So that was the first colour space, XYZ.
[819.46 → 827.88] And then years later in the 70s, that same international colour body got together, and they revised it into a couple other colour spaces.
[828.26 → 834.94] And they did specifically in the 1970s, I think 76, they produced CHENAB.
[835.70 → 840.40] And so CHENAB is the refinement of that research in the 1920s and all that data.
[840.40 → 849.80] And it's essentially a colour space that maps all these colour values to a TRI-stimulus value.
[850.02 → 850.84] It's not RGB.
[851.16 → 857.08] It's luminance and then two other essentially chroma values.
[857.92 → 862.48] And luminance, of course, being essentially brightness, and that's the L value.
[862.48 → 884.36] And they're mapped in such a way that a numeric distance, so say from 0 to 10 in terms of luminance, anytime there's a value of a difference of 10, for instance, anywhere along that value, the L value, it's going to be equivalent to the perceptual difference for a human being.
[884.36 → 892.26] And so if I take a value of 0, and I take a value of 10, the perceptual difference will be the same as a value from 90 to a value of 100.
[892.54 → 894.96] That is not true for many other colour spaces.
[895.10 → 896.54] So like HSB, it's not true.
[897.10 → 899.86] HSB, you also have like a luminance value.
[899.94 → 900.80] You have the brightness value.
[900.80 → 915.60] And if you take a value of 0 in HSB, the B is 0, and a B10, and a B90, and a B100, the difference, the perceptual difference between 90 and 100 is not the same as the perceptual difference between 0 and 10.
[915.90 → 916.46] Does that make sense?
[917.20 → 917.52] Absolutely.
[917.76 → 920.16] It's the first time I've heard it explained that thoroughly.
[921.10 → 921.46] Sorry.
[921.58 → 922.60] I hope that wasn't too thorough.
[923.20 → 923.60] I get it.
[924.24 → 927.02] I mean, yeah, you can get a bit deep into the weeds on this.
[927.14 → 928.72] So you just stop me if I do.
[928.72 → 943.50] So you have a table chart, a table colour chart about halfway down the Solarize homepage that basically has, for the lack of a better term, a semantic name and then hex values and terminal colour names and then also lab, RGB, and HSB for each of these.
[943.82 → 948.22] Which of these do you deal with when you're working with Solarize?
[948.32 → 953.04] What's, I guess, the source value that you work out of?
[953.04 → 955.98] Yeah, the source is LAB, the lab value for sure.
[957.14 → 958.58] That's sort of the master value.
[958.72 → 960.28] Even though it's kind of in the middle of that table.
[960.42 → 963.50] So I guess that's perhaps it's not obvious.
[963.82 → 966.14] But that's sort of the canonical value is LAB.
[967.20 → 976.20] The hex values, which are essentially the same as the RGB values, those are simply a single instantiation.
[976.34 → 979.82] So those are a translation from LAB space to RGB space.
[979.82 → 985.44] And RGB is sort of a standardized device-independent RGB space.
[985.44 → 989.94] Did you have any sort of build process that, I guess, translates between these?
[990.50 → 991.24] You know, yeah.
[991.26 → 997.52] I do have a bunch of scripts that I was using, some of which are pretty crufty and not very well written.
[997.88 → 998.86] I'd like to clean those up.
[998.86 → 1016.90] To be honest, one of the goals initially was to create some scripts that would be able to push out not only these values, but also the actual themes for different applications.
[1016.90 → 1024.62] So for instance, I do have scripts that generate things like the BUT colour schemes, although those are notoriously hard to actually get running properly.
[1024.62 → 1030.34] And I have scripts that, of course, will spit out things like the Vim colour scheme.
[1030.44 → 1034.48] So I can update the colours and then push out things like Vim, BUT, et cetera.
[1034.90 → 1044.10] A lot of other terminals, especially when they're just text-based preference files or like X resources files, I can push those out programmatically.
[1044.10 → 1058.42] Some applications, the preference files or the theme files are a little bit harder to parse or, you know, they don't have – the formats are not public or, you know, for whatever reason, I just found them difficult to do.
[1058.54 → 1061.60] And so, you know, I think it's still possible to do something like that.
[1061.68 → 1068.66] I would like to have some sort of master build system that would build out just a huge variety of these themes.
[1068.66 → 1080.44] And I think that there is actually in a way one of the benefits of Solarize and all the ports that have been submitted or which are floating around out there and which I need to pull in because there are a huge number of outstanding pull requests.
[1081.94 → 1085.46] But one of the benefits is that all that work has been done in a way.
[1085.54 → 1088.12] So people have figured out, you know, like here's these 16 colours.
[1088.34 → 1089.94] Here's how they map to all these different themes.
[1090.48 → 1093.24] And it should be doable to create a script like that.
[1093.30 → 1096.18] I mean it's not a small amount of work, but it's doable.
[1096.18 → 1100.58] If you were to build a matrix, I guess, of all the permutations, you have a unified colour scheme here.
[1100.68 → 1103.28] But the amount of variables in this is just incredible.
[1103.50 → 1113.96] So one of those is we talked briefly about the number of tools that it has to cascade across, right, from BUT to Vim to the terminal, all of those different tools.
[1114.06 → 1116.24] We have platform that's a part of that.
[1116.24 → 1130.72] But two of the big variables are font selection within that and also syntax for different languages and what that syntax vocabulary looks like when you colourize.
[1130.80 → 1131.18] Oh, yeah.
[1131.34 → 1132.88] Yeah, that's a huge issue.
[1133.10 → 1133.50] Huge.
[1135.00 → 1141.84] You know, in a way that's a lot like typographers will talk about colour on the page of a specific typeface.
[1141.84 → 1146.18] And they're not actually talking about colour the way that you and I have been here today.
[1146.26 → 1153.74] They're talking about sort of the – they're talking about a purely black and white – say you're printing black text on a white page.
[1154.90 → 1164.24] Type is still said to have colour based on the thickness of the strokes and the way that they all – it coalesces together as a mass, as a body of text on the page.
[1164.24 → 1178.86] And you can say there's sort of an equivalent concept when you have, say, you know, you're looking at a page in Vim, you're looking at a section of Ruby code, or you're looking at a section of Haskell code.
[1178.86 → 1187.40] Like, I was very, very concerned that different – especially, you know, I had control over the Vim theme.
[1188.00 → 1195.04] And I was really concerned that there was a similar – of course, there's some uniqueness, but a similar look to the code in each case.
[1195.30 → 1200.74] So, you know, I didn't want the Ruby code to for some reason look, you know, ugly where the Haskell code looked beautiful or vice versa.
[1200.74 → 1204.02] And that was really non-trivial.
[1204.62 → 1210.64] Just getting things like, oh, in Ruby, you know, I spent a lot of time on Ruby even though I don't code a lot of Ruby.
[1211.52 → 1214.74] I don't know why – because I find Ruby very beautiful to look at syntactically.
[1215.86 → 1216.38] I agree.
[1217.60 → 1221.64] Maybe that's a – you know, maybe I should try to pick it up a little bit more because of that.
[1221.76 → 1223.06] But I also find Haskell very beautiful.
[1223.18 → 1225.90] So I spent a lot of time looking at those two in particular.
[1226.48 → 1229.06] They were sort of my initial test cases and then HTML and such.
[1229.06 → 1232.08] But, yeah, it was really hard to do that.
[1232.14 → 1234.36] And it's still – there's still a lot of room for improvement.
[1235.08 → 1248.88] And it's probably the biggest problem in terms of ports is kind of communicating to people how important it is to have, like, a good mix of colours, to not have any single colour be too dominant, to understand, you know, when is it too many colours in one section.
[1249.00 → 1251.74] Like, you don't want to have it look like a salad, a fruit salad.
[1252.94 → 1256.48] I notice also you include a snippet of SAS for the colour palette.
[1256.60 → 1257.34] Are you a SAS user?
[1257.34 → 1258.20] Oh, absolutely.
[1258.48 → 1258.92] Yeah, totally.
[1259.06 → 1259.60] No, I love SAS.
[1259.70 → 1261.40] In fact, you're SAS, aren't you?
[1261.92 → 1262.26] I am.
[1262.42 → 1267.86] I am writing a book on SAS with Chris Epstein and Nathan Feigenbaum for Manning.
[1267.96 → 1270.96] And we're excited about SAS and Compass and the adoption.
[1271.38 → 1276.00] I was curious, though, dealing with lab, what sort of shortcomings have you found with SAS?
[1277.00 → 1278.44] You mean with a lab colour space?
[1278.60 → 1279.00] Exactly.
[1279.00 → 1282.38] Well, you know, I'm not too concerned.
[1282.48 → 1286.06] Actually, I wouldn't call it a shortcoming with SAS, per se.
[1286.26 → 1289.76] I don't – is there some specific or special support for lab?
[1289.76 → 1290.76] Not that I'm aware of.
[1290.76 → 1291.94] Not that I'm aware of.
[1291.94 → 1292.10] Right.
[1292.10 → 1297.10] I'm wondering if it's just because there's not a foundation of support at the OS level or something.
[1297.30 → 1299.22] Yeah, that's really – well, you know, the crazy thing.
[1299.30 → 1300.16] Here's the crazy thing.
[1300.16 → 1307.32] Is that a lot of operating systems will actually implement colour using lab.
[1307.32 → 1315.30] So, like, you know, OS X, anytime that you're specifying colour values, it's all being translated back to lab.
[1315.30 → 1318.52] So, that's sort of the background space.
[1318.64 → 1320.80] That's the man behind the curtain.
[1321.88 → 1335.34] Now, I would challenge anybody to go out to the Solarized homepage and just with the broad base of support that you've got across operating systems and across tools here to try to guess what your main tool chain would be.
[1335.52 → 1338.36] So, why don't you just tell us where do you camp out?
[1338.40 → 1341.28] Because you can't possibly be an expert in all of these.
[1342.44 → 1344.80] Which you mean expert in all of?
[1344.80 → 1351.12] Your operating system, your editor tools, all of this.
[1351.12 → 1351.44] Yeah, no.
[1351.96 → 1354.70] I'm probably an expert in absolutely none of them.
[1354.82 → 1361.94] I mean, the only thing I can claim to be a certified expert in, I think, is Photoshop, which I actually did my certification in crazily.
[1362.44 → 1363.16] I don't know why.
[1363.32 → 1364.40] It was some kind of challenge.
[1366.10 → 1370.86] You know, and even then, I don't think that means a lot, you know, to say you're an expert in Photoshop.
[1371.06 → 1371.82] It changes so much.
[1372.56 → 1374.82] But, no, I'm not an expert in any of these things.
[1374.94 → 1378.90] You know, in terms of tool chain, I really try to go as deep as possible into all of them, though.
[1378.90 → 1389.90] And, you know, particularly when I started to learn, when I started to go full-time into Linux, you know, I just went as deep as I could, which is one of the reasons I chose Arch, by the way.
[1389.96 → 1391.58] Well, maybe we'll have a chance to talk about that.
[1391.94 → 1392.58] Oh, absolutely.
[1392.58 → 1396.64] I really wanted to understand the system from the ground up.
[1397.26 → 1399.66] And I also try to do that with colour.
[1399.80 → 1403.68] I try to understand as much about what's happening with colour in the operating system as possible.
[1403.76 → 1405.58] But, you know, it is incredibly complex.
[1405.84 → 1412.04] Colour is – you know, right now, actually, Fedora, there's a lot of work with colour being done in Fedora.
[1412.04 → 1421.22] It's probably the most active distribution, Linux distribution, in terms of colour management and trying to create new tools for colour management and make it easy.
[1422.10 → 1423.78] But it's just so complex.
[1423.90 → 1426.60] And there are so many applications which don't support colour properly.
[1426.60 → 1434.10] Like, even among browsers right now, like Chrome, Safari on OS X, they both support ICC version 4.
[1434.38 → 1437.94] And Firefox only supports ICC version 2, if I remember correctly.
[1438.72 → 1448.02] Just small variations like that can really impact the way that, you know, you're preparing colour, the way that you're preparing images, the way that you're embedding ICC profiles.
[1448.52 → 1451.52] So, you know, I'm certainly not an expert.
[1451.52 → 1458.26] I try to be as aware as possible of all the different factors that are going into colour, how the operating system is doing colour management, et cetera.
[1458.34 → 1459.02] But it's hard.
[1459.32 → 1462.38] And, you know, this is – just thinking about OS X, it's hard.
[1462.70 → 1472.06] When you throw Linux into the mix, when you throw, you know, Borg into the mix, which is really kind of nightmarish on multiple levels, colour becomes very hard.
[1473.44 → 1474.38] So 16 colours.
[1475.38 → 1477.08] Why not support 256?
[1478.84 → 1481.18] Well, you know, constraints are good, first.
[1481.52 → 1492.72] You know, really limited – in fact, if you look at some of the examples on the Solarize page, you'll see that there's a – I'm looking about a third of the way down the page.
[1492.82 → 1495.60] There's a 16.5 palette modes example.
[1496.08 → 1499.96] So I actually use Solarize, the Solarize colour scheme on the Solarize homepage.
[1500.70 → 1502.82] And a lot of other people – I've found it all over the web.
[1502.94 → 1505.08] It's – a lot of people are using it on their blogs.
[1505.08 → 1514.18] And I give an example of using kind of like, say, like three of the base colours along with a couple of the accent colours for creating a palette for your website.
[1514.38 → 1520.20] And you can see that in all those examples, I really only use one or at the most two accent colours.
[1520.20 → 1525.50] In fact, I designed it to my own site, this etanschoonover.com.
[1526.22 → 1532.66] And that SAS sample, the example I use there really are – the intent is to use just one accent colour.
[1533.54 → 1536.50] And that's because in design, you know, you don't want to go overboard.
[1536.60 → 1537.76] You want to really limit yourself.
[1537.90 → 1540.24] It's about cutting back and paring away.
[1541.68 → 1542.86] 256 colours is hard.
[1542.86 → 1547.24] I don't think I would have seen the adoption of Solarize if I'd used 256 colours.
[1547.32 → 1548.90] It's really hard to implement that.
[1549.04 → 1550.74] A lot of applications don't support it.
[1551.40 → 1555.60] Almost all applications you can squeeze five, eight, or 16 colours into.
[1556.30 → 1558.04] So that's really it.
[1558.20 → 1562.08] So the background on each side of the spectrum is neither white nor black.
[1562.20 → 1564.46] It's this beige colour or this kind of –
[1564.46 → 1564.72] Oh, yeah.
[1564.88 → 1566.12] No, we haven't talked about that at all.
[1566.12 → 1574.78] It's actually – aesthetically speaking, it's kind of a sea green colour or what I imagine the bottom of the ocean to look like.
[1575.74 → 1577.28] Though, of course, there would be no light there.
[1577.72 → 1582.90] And then the yellow is – the light colour is actually the same as the yellow.
[1583.06 → 1590.20] So the light – that light cream colour is almost the exact same colour as the yellow, just a much higher luminance and lower saturation.
[1592.12 → 1593.72] I find it very easy in the eyes.
[1593.72 → 1596.92] I've always been a dark terminal developer.
[1597.32 → 1601.18] One of the things that I had to get used to was just the use of red.
[1601.84 → 1606.22] And I'm used to saying red in my colour schemes is, you know, danger Will Robinson.
[1606.54 → 1609.96] So that took some adoption to get used to.
[1610.06 → 1613.42] But once I got over that hump, it's been a lot easier in the eyes.
[1613.50 → 1618.28] I think late in the day, my old man eyes aren't squinting as much as they were previously.
[1619.20 → 1619.60] Yeah.
[1619.60 → 1619.72] Yeah.
[1620.08 → 1625.24] This is – it's really important for me to have both modes of light and the dark mode specifically for that.
[1625.52 → 1626.60] My eyes are terrible.
[1626.84 → 1628.74] I have, you know, thick glasses.
[1630.32 → 1636.02] And I definitely will switch about – you know, there's a certain point of the day in which I switch from the light to the dark mode.
[1636.02 → 1637.98] What's your favourite terminal font?
[1639.28 → 1641.22] Oh, I have two of them.
[1642.18 → 1642.58] Terminus.
[1642.60 → 1643.54] I use Terminus a lot.
[1644.44 → 1645.40] I'm a big fan of that.
[1645.50 → 1650.34] Although on the Mac, there's a Terminus port for the Mac, a couple of versions of it.
[1650.34 → 1656.18] And they're not quite as nice as Terminus on Linux or Unix.
[1656.58 → 1658.60] So, no, I really like Terminus.
[1658.72 → 1661.90] But I also – I have a favourite, which is Letter Gothic.
[1661.90 → 1668.56] Of course, today we would say Letter Gothic mono because there are non-monospaced variants that are out there.
[1670.56 → 1673.44] So, Letter Gothic is – I don't know if you're familiar with that.
[1673.52 → 1680.84] Letter Gothic is actually a typeface that was designed for the IBM Electric typewriter back in, like, the early 60s.
[1681.84 → 1684.62] And it looks like a typewriter font.
[1685.26 → 1688.52] And it's actually the font that I use throughout the Solarized webpage.
[1688.72 → 1693.46] So, even, like, at the top on that yin-yang symbol, you'll see that's Letter Gothic.
[1694.04 → 1697.42] And Letter Gothic inspired a lot of other – I think it inspired, like, An dale.
[1697.42 → 1704.22] And there's a lot of DNA from Letter Gothic mono in today's monospaced typefaces.
[1704.62 → 1710.28] I'm testing it out now in myfonts.com, putting it through my rigorous test here of the Dash Rocket.
[1710.28 → 1714.58] I have to put a hyphen with a greater than – I guess it's used in Haskell as well.
[1714.72 → 1716.38] And if those don't line up on that –
[1716.38 → 1717.46] Yes.
[1717.72 → 1718.30] Oh, okay.
[1718.38 → 1718.62] Listen.
[1718.78 → 1723.14] Hey, there's actually – so, Letter Gothic mono is a beautiful typeface.
[1723.46 → 1727.88] But in terms of being a typeface for code, I do use it a lot.
[1728.46 → 1734.18] But I accept and embrace its idiosyncrasies as just part of its beauty.
[1734.18 → 1740.38] If you look at, say, the brackets, the curly brackets, they're really – they're quite squashed.
[1741.04 → 1744.18] And they're not very distinct, particularly at smaller type sizes.
[1746.16 → 1749.94] And the zero is non-slashed, and there's no dot in it.
[1750.00 → 1752.50] So, it looks very, very similar to the capital O.
[1752.84 → 1758.76] Those are really problems in terms of seeing more widespread adoption or popularity for Letter Gothic mono.
[1758.76 → 1774.56] So, one of my side projects is – it's something I've been wanting to do for a while, and I've actually started to do this slowly, slowly, slowly – is to begin a new trace of a Letter Gothic mono-like typeface.
[1774.56 → 1780.26] I think that if you do it from scratch, that it's basically okay.
[1781.18 → 1782.66] I listened – actually, it was interesting.
[1782.80 → 1789.58] You had Micah Rich on recently, and he talked a lot about this, about the creation of fonts and open source fonts.
[1789.84 → 1795.68] And I would – what I'm working on right now is basically an open source implementation of Letter Gothic mono.
[1796.06 → 1798.94] I'm really slow at this, and I'm not a – I'm a type lover.
[1800.26 → 1801.42] I'm a lover, not a fighter.
[1801.60 → 1802.48] I'm a lover, not a designer.
[1802.48 → 1810.32] So, you know, it's – I know that this is not my wheelhouse, but, you know, I can at least start that process.
[1810.60 → 1815.58] And then maybe once the basics are in place, I can stick it up and see if other people are willing to contribute.
[1816.00 → 1816.56] You know, it's interesting.
[1816.64 → 1824.70] You have this appreciation for aesthetics that draws a lot of us to the Mac platform, but you're coding a lot on Arch these days.
[1824.70 → 1832.60] And what's it been like to move over to Linux and see something that's a little bit more bare bones or engineering-driven instead of design-driven?
[1832.78 → 1834.48] And how have you found that transition?
[1835.02 → 1835.10] Yeah.
[1835.30 → 1837.90] Well, you know, I've always had a real split personality in that regard.
[1838.02 → 1842.46] You know, I've always done both code and design, I guess as a lot of web developers have.
[1842.92 → 1846.88] But, you know, it's been exhilarating.
[1846.88 → 1847.90] It's been super enjoyable.
[1848.14 → 1848.76] I love Arch.
[1849.00 → 1850.16] You know, I love Linux.
[1851.04 → 1854.38] And I have high hopes for Linux on the desktop going forward.
[1855.02 → 1860.94] I have strong opinions about what's going on with, like, Ubuntu right now and adoption of Linux on the desktop.
[1862.10 → 1868.04] But it's – you know, it's like I've heard it compared to building your own lightsabre, particularly with Arch.
[1868.04 → 1871.26] And that's, I think, a very apt description.
[1871.68 → 1873.32] It's – you're just building everything.
[1873.46 → 1874.12] You learn it.
[1874.22 → 1875.60] You have to understand it.
[1876.52 → 1882.58] One of the great things about Arch is that it's simple enough that it's all text files, and they're all in, you know, the slash –
[1882.58 → 1883.52] It's a little source distribution.
[1883.68 → 1883.96] Is that right?
[1884.74 → 1885.04] No.
[1885.10 → 1886.44] Well, it's not like Gen2, right?
[1886.48 → 1888.44] Like Gen2, you know, you have to compile yourself.
[1888.64 → 1891.96] Arch, they're binary repositories.
[1891.96 → 1894.58] So, you know, it's not pure source.
[1894.58 → 1901.34] There is also a user repository, which is primarily stuff that gets compiled from source.
[1902.12 → 1909.66] And quite often that's stuff which is either a little bit fresher or, you know, just necessary to run a reasonable system.
[1910.92 → 1912.62] So, it's been great.
[1912.74 → 1913.50] I've really enjoyed it.
[1913.84 → 1915.92] I, you know, I'm not running GNOME on it.
[1916.04 → 1917.26] I like GNOME 3, actually.
[1917.42 → 1919.94] Maybe one of the few people that do.
[1919.94 → 1926.42] Although I have to say that I really only like GNOME 3 because of the new – the web-based installer for the extensions.
[1927.14 → 1929.04] But I'm using primarily Monad.
[1929.16 → 1932.84] And Monad is a beautiful – it's an elegant system.
[1933.00 → 1934.00] It's beautiful on the inside.
[1934.76 → 1937.96] And it's a tiling window manager if you're not familiar with that.
[1938.70 → 1941.40] Like Awesome or some of the other tiling window managers out there.
[1941.80 → 1944.82] And that to me is – it almost feels like the future.
[1944.82 → 1949.44] You know, I realize that tiling window managers are some of the first window managers that were available.
[1949.68 → 1951.90] Like Xerox PARC, I think they were doing a lot of tiling stuff.
[1952.04 → 1953.40] Back to the future with this.
[1953.62 → 1953.92] Yeah.
[1954.24 → 1964.46] And, you know, boy, I tell you that, you know, when I'm working on Arch, and I'm using Monad, and I'm using this tiling window manager, you know, your fingers just fly over the keyboard.
[1964.46 → 1965.92] And you're switching around workspaces.
[1965.92 → 1967.08] And you're bringing up browsers.
[1967.08 → 1969.32] And you're bringing up, you know, terminals.
[1969.32 → 1970.30] And you're bringing up BUT.
[1970.74 → 1972.14] And it's all superfast.
[1972.14 → 1975.74] And then I switch over, and I'm working on my Mac.
[1975.96 → 1978.54] And I feel like I'm going at half speed.
[1979.66 → 1981.66] I really, really miss it.
[1981.78 → 1984.02] I feel like it's a professional interface to a computer.
[1984.64 → 1988.24] Now, I stumbled across Arch, I guess, about a year ago.
[1988.34 → 1989.80] I was getting into Tmux.
[1990.04 → 1994.34] And one of the best resources out there is in the Arch wiki around Tmux.
[1994.42 → 1996.52] Have you used Tmux, the terminal multiplexer?
[1996.52 → 2003.50] Yeah, you know, I have about 100 bookmarks to look at that involve Tmux.
[2003.80 → 2005.14] I have notes about Tmux.
[2005.44 → 2007.14] I think I was looking at something about Tmux yesterday.
[2007.52 → 2009.34] Yeah, I mean, I've played around with it.
[2009.72 → 2012.12] And I haven't really gotten into using it.
[2012.18 → 2016.40] I've been using, like, you know, I use term in multiplex mode on the Mac.
[2016.80 → 2017.60] But definitely.
[2017.60 → 2024.72] And so, I mean, Tmux, if I'm understanding it correctly, is multiplexing your terminal, right?
[2025.00 → 2025.42] That's right.
[2025.54 → 2026.32] Within a single terminal.
[2027.30 → 2029.98] And so, you know, for me, I don't want to say it's a non-issue.
[2030.18 → 2035.60] But when I use, you know, Monad, that's essentially what I'm doing is I'm multiplexing.
[2036.40 → 2037.76] But not just the terminal, of course.
[2037.80 → 2040.08] I'm multiplexing the entire windowed environment.
[2040.38 → 2044.04] It's great if you pair program because then if someone tunnels in your machine.
[2044.18 → 2044.74] Oh, right.
[2044.94 → 2045.16] Yeah.
[2045.16 → 2050.44] No, that's, I don't really, see, I'm such a, I hole up here in my little cave.
[2051.32 → 2051.88] You're a loader.
[2051.92 → 2052.84] I'd love to pair program.
[2053.06 → 2056.58] I'm probably not anywhere good enough to do that with anybody without driving them crazy.
[2057.36 → 2062.18] So I was surprised to see support for term alongside a terminal app.
[2062.24 → 2063.50] Do you have a preference on the Mac?
[2063.94 → 2065.26] No, I use both.
[2065.52 → 2066.64] I still use both.
[2067.28 → 2069.40] I use, like, on the Mac, I use Total Terminal.
[2071.16 → 2073.56] And I use term as well.
[2073.56 → 2076.40] So, you know, it's hard to say.
[2076.46 → 2077.52] I don't really, I don't have a preference.
[2077.64 → 2081.44] I like to keep things as simple as possible on the Mac, unfortunately.
[2081.94 → 2088.98] In order to get the Mac into kind of usable state, approximating my workflow on Linux, I end up having to install a fair amount of stuff.
[2090.84 → 2091.96] But I'm okay with...
[2091.96 → 2093.94] Do you use Homebrew for that or do you roll your own scripts?
[2094.36 → 2094.64] Oh, yeah.
[2094.72 → 2094.90] Brew?
[2095.02 → 2095.68] No, definitely brew.
[2095.80 → 2096.40] Brew, brew, brew.
[2096.58 → 2097.34] All the way, brew.
[2097.88 → 2098.46] Oh, my God.
[2098.68 → 2100.02] Brew's the best thing ever.
[2101.82 → 2111.40] I mean, you know, I know, you know, Mac Ports has been out there and is, you know, that's a great greybeard system for the Mac.
[2111.46 → 2113.20] And I used to use Mac Ports all the time.
[2113.20 → 2121.10] But I really feel like Brew is also the future for, you know, it's sort of the missing repository, isn't it?
[2122.02 → 2122.46] Absolutely.
[2122.72 → 2128.68] It seems like the one missing piece for OS X that Apple's left out.
[2128.84 → 2130.20] And thankfully the community has provided that.
[2130.20 → 2146.60] Yeah, and, you know, I realize, like, they have come out recently with, you know, you can probably specify this in a way that I can't, but with the support for installing the command line tools that you used to have to install Xcode for, now you can download those separately, which is great.
[2146.72 → 2154.86] And I felt like that was a real nod to the brew effort, sort of kind of tacit endorsement and, you know, keep going, guys.
[2155.36 → 2158.78] But it would be great to see more support from Apple in this regard.
[2158.78 → 2164.28] You know, I mean, this is, if you look at brew, and then you look at, I just learned about taps the other day, brew taps.
[2165.74 → 2166.78] I have not seen that.
[2167.02 → 2172.66] Yeah, so brew taps, boy, and hey, brew people, if I'm butchering this, also my apologies.
[2172.92 → 2184.56] But if I understand taps correctly, it's a way, so, okay, it seems to be focused on binary distributions using brew and not just, is that right?
[2184.62 → 2185.32] Is that what taps is?
[2185.94 → 2187.28] Okay, I can see people.
[2187.28 → 2188.94] I can hear them rolling their eyes right now.
[2189.44 → 2198.22] But the other cool thing about taps, if I'm getting this correct, is that I will be able to set up a repository which is named something like homebrew-solarized.
[2198.94 → 2212.20] And then you could then, on the command line, type in brew tap altercation, which is my GitHub handle, slash, or altercation slash solarized, I think is the syntax.
[2212.20 → 2215.40] I guess I pull packages from other users or other repos without going to the canonical source.
[2215.40 → 2216.16] Correct, using brew.
[2216.40 → 2217.74] Yeah, yeah, yeah.
[2217.86 → 2219.02] So forget what I said about binaries.
[2219.04 → 2221.82] The unfortunate part about homebrew is just the naming.
[2222.08 → 2226.74] Every time I try to Google something around homebrew, you have to wait through everybody making their own beer.
[2226.74 → 2229.70] Oh, listen, Wynn, this is a huge issue for open source.
[2229.82 → 2230.54] This goes back to everything.
[2230.64 → 2231.58] This is aesthetics, actually.
[2232.36 → 2233.72] It's not homebrew specifically.
[2233.94 → 2236.26] I think homebrew is just the bee's knees.
[2236.52 → 2237.80] So, you know, they can do no wrong.
[2238.44 → 2241.80] But, you know, it's like, did you see recently that Fresh Meat rebranded?
[2242.34 → 2242.96] I haven't.
[2243.00 → 2244.18] I haven't been out to Fresh Meat in years.
[2244.18 → 2245.52] Yeah, well, nobody has, I think.
[2246.28 → 2248.50] Oh, Geez, Fresh Meat, guys, if you're listening, I'm sorry.
[2248.72 → 2250.40] But it's got to be the truth.
[2250.56 → 2254.60] You know, it's just I think they're, you know, they realized that they needed to rebrand.
[2254.70 → 2255.38] And I can't remember.
[2255.44 → 2257.02] It's like something to do with code.
[2257.16 → 2257.70] I didn't remember.
[2257.82 → 2259.62] It's a more business-y sounding name.
[2260.30 → 2262.18] And I can imagine that what happened is, you know, of course.
[2262.30 → 2262.86] Freecode.com.
[2262.94 → 2263.52] Yeah, Free code.
[2263.60 → 2264.06] That's what it was.
[2264.84 → 2271.62] So, you know, you try to sell services, or you try to pitch like an open source related project or product.
[2271.62 → 2282.86] And if you're going to do it in a business environment, or you want to just get traction on it, at some point, having a really goofy sounding name or a name that you can't Google is a real hindrance.
[2283.12 → 2283.56] Exactly.
[2283.76 → 2284.78] I'm looking at you, GIMP.
[2285.36 → 2286.62] Yes, you, GIMP.
[2288.02 → 2290.02] GIMP makes me sad on a number of levels.
[2290.72 → 2291.98] Are you a GIMP user?
[2293.20 → 2296.28] You know, I really gave it a go.
[2296.82 → 2299.70] And I'm not giving up yet, but I'm not really a GIMP user.
[2299.70 → 2304.14] You know, Photoshop is what keeps me on the Mac, I'll be honest.
[2305.50 → 2307.48] Not just Photoshop, but the entire Adobe suite.
[2307.76 → 2311.44] You know, I do a lot of print work, so I use InDesign pretty heavily.
[2312.60 → 2315.46] I suppose less and less, but, you know, I still use a lot of InDesign.
[2315.64 → 2316.82] Photoshop, of course.
[2317.14 → 2321.36] For me, Photoshop is turning in just the last pit stop on the way out to the browser.
[2321.48 → 2326.66] I usually start in Illustrator and then just copy and paste that smart object into Photoshop and add some layer effects.
[2326.66 → 2328.76] Right, right.
[2328.98 → 2330.56] I definitely do that as well.
[2330.66 → 2339.30] But, you know, one of the differences between Photoshop and GIMP isn't just its integration with the smart objects and Illustrator for me, but it's also the fact that it does 16-bit.
[2340.76 → 2341.92] Still not there with GIMP.
[2342.10 → 2343.26] We're still stuck in 8-bit land.
[2343.66 → 2346.48] And it also does lab colour space.
[2346.48 → 2350.58] So, and CMYK.
[2351.42 → 2356.78] So I noticed your personal website's running Hackle, which I guess is Jekyll for Haskell.
[2357.46 → 2357.70] Yeah.
[2358.00 → 2358.92] You're writing a lot of Haskell?
[2359.94 → 2364.14] Well, you know, I'm cutting and pasting a lot of Haskell, which is a kind of writing, isn't it?
[2365.24 → 2367.30] Yeah, and it's not just cutting and pasting.
[2367.38 → 2368.50] I definitely write.
[2369.70 → 2370.42] Haskell's great.
[2370.42 → 2375.56] One of the reasons Haskell's great is because if it runs at all, it usually runs right.
[2376.56 → 2381.22] And, you know, part of that is just, I guess, the nature of it being functional.
[2381.52 → 2385.34] But it's a really beautiful language to write in.
[2385.74 → 2387.70] For those that don't know, it's functional, yet it's typed.
[2387.76 → 2388.18] Is that right?
[2389.20 → 2389.52] Yeah.
[2389.64 → 2390.20] And you know what?
[2390.42 → 2396.02] I'm going to take a pass in giving you any more details about Haskell because I'm definitely going to screw that up.
[2396.02 → 2399.42] But, you know, my intro to Haskell was actually Monad.
[2400.28 → 2402.62] Again, the tiling window manager that I use in Arch.
[2402.62 → 2412.42] And so Monad is, you implement Monad using essentially what is, you know, your preferences are also the actual runtime.
[2414.30 → 2416.60] So there are other window managers like that as well.
[2417.34 → 2422.56] Boy, what's the one from, oh, I'm drawing a blank here.
[2422.60 → 2423.12] It's not awesome.
[2423.36 → 2424.00] There's another one.
[2424.00 → 2429.78] It's been a while since I've been in that space, probably since Megacity.
[2430.34 → 2431.46] Yeah, yeah, yeah.
[2431.54 → 2431.96] Well, anyhow.
[2432.64 → 2434.70] But, yeah, so the runtime is the preference file, basically.
[2435.08 → 2437.62] And I started to just muck about with that.
[2437.62 → 2443.70] And, you know, Monad, if you're not familiar, I often see people ask, like, what tiling window manager should I try?
[2443.78 → 2444.38] Should I try awesome?
[2444.48 → 2445.32] Should I try Monad?
[2445.46 → 2449.22] And I know a lot of people kinds of freak out because Monad is written in Haskell.
[2449.42 → 2452.86] And Haskell is a really alien experience.
[2453.24 → 2456.00] I mean, functional programming in general is kind of an alien experience.
[2456.52 → 2458.64] But it's not really hard.
[2458.72 → 2466.16] Once you look at a couple examples, and you look at other people's stuff, and you can kind of get a feel for how they're doing stuff, it's super fun to work with.
[2466.16 → 2470.32] Does Monad integrate with GNOME or is it its own deal?
[2470.70 → 2471.06] You can.
[2471.14 → 2475.68] You can run Monad while you're in GNOME.
[2476.08 → 2478.12] So you just run it as your window manager then.
[2478.84 → 2482.82] And you get to keep things like your GNOME widgets, your taskbar, your menu bar and stuff.
[2485.22 → 2491.68] So it was, I guess, Monad that brought you into Haskell and not necessarily any sort of syntactical advantage of?
[2491.90 → 2492.68] No, no.
[2492.68 → 2497.76] I mean, I can understand, and I can appreciate the beauty of Haskell now.
[2497.92 → 2501.42] But it was out of necessity, I guess.
[2502.84 → 2507.22] It was really the only – it was the tiling window manager that I felt I could customize myself.
[2507.48 → 2512.68] For example, there's a great module for Monad, which is the input module.
[2512.68 → 2519.98] It allows you to create like kind of a – if you're familiar with like Quicksilver on the Mac or Alfred or GNOME, there's GNOME Do.
[2520.22 → 2521.96] So it's one of these quick entry tools.
[2522.58 → 2526.42] There's a great feature in Monad, which is called Monad Prompt.
[2526.64 → 2528.88] And you can basically do anything you want with it.
[2529.00 → 2532.94] You can create – it's completely programmable, customizable.
[2532.94 → 2538.62] So back to Solarize briefly, 2,200 watchers, 45 pull requests out there.
[2538.68 → 2539.32] What's the story?
[2539.54 → 2540.94] Do you need help or –
[2541.62 → 2542.42] Yeah.
[2542.68 → 2550.82] You know, I actually – I went to my first Linux meetup the other day, my first face-to-face real-world Linux meetup specifically to chat with some folks about Solarize and sort of the next step.
[2550.82 → 2571.16] But, you know, my decision at this point is – first, it's definitely going forward, but I haven't really been sure whether I should just – there's a whole list of little niggling problems, which I really wanted to solve and solve properly before I started to iterate this any further.
[2571.68 → 2573.50] One of them is terminal colours.
[2573.94 → 2577.10] Terminal colours are really, really tough.
[2577.10 → 2589.42] For example, the way that I have the terminal colour set up right now with the black and the bright black, I basically need to swap those around, and then that's going to impact every other implementation out there that's also doing terminal colour schemes.
[2590.46 → 2593.82] And then the other problem is I wanted to edit the history of the GitHub project.
[2594.56 → 2597.38] Boy, you know, this was like my first big GitHub thing.
[2597.54 → 2600.78] I had done one other big open source project prior to this, which was Kingless.
[2601.64 → 2604.60] And that was also – I had a lot of users, but that was pre-GitHub days.
[2604.60 → 2610.18] And I hadn't – you know, I didn't really know what I was getting into when I did a big kind of GitHub project.
[2610.30 → 2612.20] I didn't know it would be a big GitHub project.
[2613.62 → 2619.18] And I dumped a lot of just garbage in the GitHub history that I shouldn't have.
[2619.32 → 2621.16] There's a lot of like Photoshop files and stuff.
[2621.24 → 2622.80] So I thought, oh, okay, I'll just edit those out.
[2622.94 → 2625.62] Well, that turns out to be kind of non-trivial.
[2625.74 → 2626.66] I don't want to screw it up.
[2626.66 → 2635.46] So I thought about, you know, maybe what I'll do is I'll just kind of – not mothball this, but I'll start essentially Solarize 2 at some point.
[2636.18 → 2638.64] And that gives – I guess there are a couple advantages to doing that.
[2638.74 → 2647.52] One is I can revise the terminal colour schemes and such, and it's going to be very, very clear that people are going to have to update because it will be version 2.
[2647.86 → 2650.00] And also I've got two other colour schemes.
[2650.00 → 2652.78] One is a lot like Solarized.
[2652.88 → 2654.80] It's symmetrical, but it's neutrals.
[2655.12 → 2656.68] So it's not the blues and the yellows.
[2657.60 → 2661.18] And then I have another which is non-symmetrical, and it's a little bit wider gamut.
[2661.28 → 2662.54] It's a higher contrast colour scheme.
[2663.38 → 2667.24] So then I'll be able to build those into that release.
[2669.18 → 2671.38] And that's basically the next step.
[2671.60 → 2679.40] Now, in terms of time frame, you know, I don't want to hold myself to anything, but that's sort of my this year project.
[2680.14 → 2691.26] Do you foresee having some sort of build tool in that repo where folks could test their colours across all of these different tools, or would you split these out into multiple repos?
[2692.48 → 2695.36] Well, that's actually a really – that's a question that I haven't resolved yet.
[2695.48 → 2705.18] That's one of the reasons I was excited about Brew Tap because this whole idea – one of the neat things about Brew Tap is that you'd be able to have the different repositories.
[2705.62 → 2707.10] People wouldn't have to be pulling them in.
[2707.40 → 2709.04] Homebrew wouldn't have to be pulling them in.
[2710.22 → 2717.50] Homebrew could let, you know, different maintainers manage their repository entirely separately, but still have it kind of be accessible via Brew.
[2718.38 → 2720.58] And I thought that's really cool.
[2720.70 → 2725.04] That's one of the things that I've been – not that that's going to map over to Solarize directly.
[2725.04 → 2733.32] But early on when I set up the GitHub repository for Solarize, I really wasn't sure whether I should be using things like submodules.
[2733.96 → 2734.58] You can tell.
[2734.70 → 2739.22] I mean, I still feel like a GitHub newbie in some ways, and I'm relatively experienced with it.
[2739.22 → 2745.82] But, man, there's just a lot I just don't get in terms of, like, best practices, like binary files, for instance, the best way to manage binary files.
[2746.54 → 2752.30] So what I ended up using was something called Git Subtree, which is a non-official GitHub module – or Git module.
[2752.30 → 2754.80] And it's basically just some porcelain.
[2754.90 → 2757.12] It's bash-based Git porcelain.
[2758.06 → 2763.88] And that allows me to include external repositories in my main repository.
[2763.88 → 2770.12] But unlike submodules, you don't have to then run a separate command to import them after you check out the repository.
[2771.08 → 2774.36] Now, I feel like that was a good solution at the time.
[2775.04 → 2776.10] Now I'm not so sure.
[2776.28 → 2784.70] What I would – the ideal situation for me is to have all the different ports for Solarize be completely externally maintained by different people.
[2785.94 → 2792.94] And not have to be pulling them in, not have this enormous, gigantic repository, because it would be huge if I pulled them all in.
[2792.94 → 2796.18] So I'm not sure the best way to do that is, honestly.
[2796.28 → 2797.88] I'm really open to suggestions from people.
[2799.18 → 2803.18] Sounds like you need to fire up IRC and get a hash Solarized.
[2803.98 → 2805.14] Oh, I thought about that.
[2805.26 → 2810.26] I've thought about having a Solarized – a hash Solarized channel for a long time.
[2810.52 → 2812.24] But I don't know.
[2812.38 → 2814.16] I have – you know, I'm on IRC a lot, actually.
[2814.54 → 2815.54] Maybe I should do that.
[2815.70 → 2816.98] I hang out in Vim occasionally.
[2817.32 → 2820.58] But, you know, signal noise is the issue.
[2820.96 → 2822.74] So 222 forks of this project.
[2822.74 → 2827.20] And I'm sure a lot of that is to add support for additional tools and things.
[2827.28 → 2830.06] But when you see folks tweaking the colour scheme, how does it make you feel?
[2830.44 → 2831.20] I'm fine with it.
[2831.34 → 2832.32] I'm okay with it.
[2833.08 → 2835.12] You know, it just means they don't have any taste, right?
[2835.38 → 2835.94] No, no.
[2836.52 → 2840.44] I've got to admit the – and I'm not sure if this is term or what.
[2840.44 → 2846.72] But I had a very early version of Solarized that the red was very, very red.
[2846.82 → 2848.66] I noticed – actually, my –
[2848.66 → 2849.10] That's changed.
[2850.20 → 2850.60] Karthik.
[2851.00 → 2853.28] When I saw it on his screen, I was like, you know, I could live with that.
[2853.34 → 2856.76] But that's not what happens when I go to Solarized and term 2.
[2856.82 → 2859.46] And I think I had a very early version or an old version of it.
[2859.54 → 2864.12] And when I re-downloaded it, I was able to live with the more muted red.
[2864.82 → 2867.84] Yeah, the red – I spent so much time on that red.
[2867.94 → 2871.60] Easily, like, I mean, I think I spent more time on that red than all the other colours combined.
[2872.00 → 2872.98] Red is really hard.
[2873.12 → 2874.96] Part of it is just, like, the human visual system.
[2875.20 → 2875.52] Right.
[2876.32 → 2881.08] Part of it is the way that it interacts with light backgrounds very differently than dark backgrounds.
[2882.20 → 2885.16] Part of it is the way that the display device works with red.
[2885.62 → 2888.44] You know, there's a real – there's a perception of bleed, colour bleed.
[2889.16 → 2891.56] So, yeah, that was really, really hard.
[2891.56 → 2911.70] And, yeah, that's actually – one of the things that I'd like to do is – there's actually a lot of interesting research, CIE-related research and colour space and lab-related research about the way that not just the human visual system works in terms of the nonlinear response to, say, different luminosities,
[2911.70 → 2917.02] but the way that the visual system – our visual system works in terms of contextual contrast.
[2917.80 → 2924.20] So, specifically, the way a certain value of red looks against a dark background versus a light background.
[2924.46 → 2929.80] And I'd like to incorporate some of that research in sort of the next – either the next iteration of Solarized or a different colour scheme.
[2929.80 → 2942.18] Another thing that slowed my adoption of Solarized was just tweaking my Tmux setup to have yet another colour scheme in there because I'd already done that for my dark colour scheme.
[2942.50 → 2945.86] And so, Tmux colours are very lightly documented.
[2946.00 → 2950.10] And I finally found the way to do essentially transparent colours by just saying default.
[2950.28 → 2954.04] I can let the window bleed through from underneath the status bar.
[2954.04 → 2961.04] But do you have some sort of glossary across all of these tools that maps, you know, this is that and this tool and this tool and that tool?
[2961.52 → 2963.56] You mean in terms of, like, transparency of the background?
[2963.78 → 2964.10] Like foreground colour?
[2964.28 → 2969.56] You know, the syntax changes between what you want to pull off in Vim versus the terminal versus BUT.
[2969.98 → 2970.92] No, no, I don't.
[2971.00 → 2975.24] It's – and, you know, even BUT, you can haven Curses BUT and you can have Slang BUT.
[2975.54 → 2979.34] And they're both – they both handle colours slightly differently.
[2979.34 → 2987.46] Those – you know, it's – if there is a Rosetta Stone for this out there, I certainly don't know of it.
[2987.56 → 2994.32] I don't have it other than, like, lots of notes and then the cognitive map that I've developed over time and lots of pain.
[2994.42 → 2995.66] So you haven't automated any of that?
[2995.78 → 2996.84] It's all by hand?
[2997.30 → 2997.52] No.
[2997.78 → 2998.90] Well, it's all by hand.
[2998.90 → 3009.70] And that's one of the reasons that I don't have – I didn't initially roll out support for, you know, just a wide variety of terminals right off the bat because they really do all require a lot of hand-holding.
[3010.12 → 3011.92] So you mentioned BUT a couple of times.
[3012.02 → 3014.76] Any other text mode tools that we should check out?
[3016.24 → 3019.94] That specifically have support from Solarized or that are just awesome?
[3020.26 → 3020.54] Either.
[3020.86 → 3021.12] Either.
[3021.16 → 3022.62] I'm always looking for awesome text mode tools.
[3022.84 → 3025.06] Well, I'm a big Task Warrior fan right now.
[3025.06 → 3030.34] I don't know if you know Task Warrior, but it's a task – command line task management tool.
[3030.54 → 3032.54] They just released version 2.0.
[3033.30 → 3035.12] 2.0 is available via Brew.
[3035.94 → 3043.16] And one of the reasons I'm excited about Task Warrior is not just because it's a CLI tool for doing your task management.
[3043.42 → 3045.18] And they're cognizant of things like GTD.
[3045.26 → 3047.08] It also does have a Solarized Colour scheme built in.
[3047.66 → 3053.74] But it also has a cool server-side component, which is still in development.
[3053.74 → 3055.58] I don't believe that it's available.
[3056.44 → 3061.06] It may be available somewhere in alpha form, but I'm not using it right now.
[3061.36 → 3066.52] But once the server-side component is out, then it's really going to be kind of a distributed device-independent solution.
[3066.92 → 3071.88] And, you know, if you look at the development of that project, they're very active.
[3072.60 → 3078.22] I'm currently using Task Paper Vim just because the Task Paper iPhone client allows me to take it with me on the go.
[3078.42 → 3081.98] How are you handling the mobile aspect of it, if at all?
[3081.98 → 3086.56] Well, for a while I was doing – I was piping stuff in through email.
[3087.94 → 3093.36] I don't do – and pushing stuff back after email, like doing quick, you know, like shopping list exports from Task Warrior.
[3094.72 → 3100.50] But, you know, I do also keep like just text – flat text file lists that are essentially like Task Paper.
[3101.22 → 3102.56] I think Task Paper is pretty cool.
[3103.42 → 3107.58] But, you know, in terms of on-the-go stuff, I'm in my cave all the time.
[3107.66 → 3108.34] I'm never on the go.
[3108.34 → 3121.54] Going back to favourite monospaced font, before I let's forget to ask, Drew Neal of Dim cast fame wants to know about your favourite monospaced font, which we asked about that earlier, but what you would like to do with it.
[3121.74 → 3121.92] Yeah.
[3122.02 → 3130.88] Well, no, it's definitely – what I want to do with it is what I described, which is that kind of open-source retrace of letter-gothic Mona.
[3130.88 → 3131.46] Ah, gotcha.
[3132.30 → 3133.46] It makes total sense now.
[3133.74 → 3137.48] When I got that via Twitter yesterday, I thought maybe it was some sort of inside joke that I didn't know about.
[3138.38 → 3139.02] No, no.
[3139.16 → 3140.48] Ask him what he wants to do with the font.
[3140.72 → 3141.10] Yeah, I know.
[3141.12 → 3142.38] I introduced him to letter-gothic Mona.
[3142.46 → 3145.78] I mean, I think it's – you know, letter-gothic is – it's classic.
[3145.92 → 3146.38] It's beautiful.
[3148.58 → 3150.44] Certainly, you know, I keep coming back to it.
[3150.48 → 3153.02] I'll occasionally leave it for something else, but I keep coming back to it.
[3153.02 → 3157.54] So definitely would like to see it in an open-source format.
[3158.70 → 3164.86] Do you have a Solarized theme for Task Warrior, or is it just what comes from the terminal?
[3165.04 → 3166.26] Somebody else built it.
[3166.26 → 3171.14] They built it, and it should be distributed with Task Warrior 2.0.
[3171.38 → 3174.40] I think it was also distributed with 1.x as well.
[3174.40 → 3183.38] In terms of setting it up, I mean, it's like a single command line to run – operation to run to set your preferences to use that colour scheme.
[3184.68 → 3187.60] And they have both a light and a dark mode, and they're really well done, I should say.
[3187.60 → 3189.08] Which do you use more, light or dark?
[3189.68 → 3192.32] Oh, it's a pretty even split.
[3193.04 → 3194.36] Time of day based, or?
[3194.36 → 3203.62] You know what's funny is I actually started designing and developing the dark mode first, and that was sort of the dominant – you know, cognitively, that was the dominant theme for me.
[3204.40 → 3208.94] And over time, I think I started – I've kind of migrated more towards the light background.
[3209.36 → 3210.96] But it's definitely time of day.
[3211.82 → 3216.26] You know, it's definitely – like if I'm in a dark room, for sure, dark background.
[3218.60 → 3225.28] Before we started recording, you were telling me about – in the move to Linux, audio on Linux was the biggest challenge.
[3225.88 → 3227.50] Yeah, yeah, huge sigh.
[3229.10 → 3230.74] Yeah, you know, it's funny.
[3230.74 → 3234.52] Well, this is just sort of indicative of Linux on the desktop in general.
[3234.96 → 3238.86] And I see so many people ask that same question, and I'm sure you do too, right?
[3238.90 → 3245.44] Which is why, you know, is this – the question we all kind of scoff at and laugh at, which is, is this finally the year of Linux on the desktop?
[3245.44 → 3252.74] And the answer can only be a resounding no for most people, but it's certain – I think developers still do.
[3252.88 → 3254.30] And I mean, I use Linux on the desktop.
[3254.54 → 3256.36] I know a lot of developers that use Linux on the desktop.
[3256.60 → 3263.60] I would be Linux on the desktop full-time for everything if certain conditions could be met.
[3263.60 → 3272.62] And those conditions would be that audio not be a complete nightmare, that I had a decent graphics editing tool.
[3273.70 → 3275.16] You know, I'm not asking the world.
[3275.78 → 3281.28] I don't need – I don't need – I even give up CMYK support, but I just need it to be 16-bit, you know.
[3282.54 → 3284.28] How long have you been using Linux on the desktop?
[3285.44 → 3287.04] Since 2010.
[3288.40 → 3290.14] And prior to that, of course, I used Linux.
[3290.16 → 3291.66] You're relatively noob then.
[3291.66 → 3292.70] Oh, I'm a total noob.
[3292.78 → 3293.46] I'm a total noob.
[3293.52 → 3294.92] But, you know, I mean, I jumped in with both feet.
[3295.00 → 3295.88] I mean, I've released a lot.
[3295.94 → 3296.44] I've written a lot.
[3296.52 → 3302.64] I wrote like an installer for Arch Linux from scratch just to kind of teach myself how to do it.
[3303.68 → 3312.06] You know, I've written – I've done a lot of – yeah, I've really tried to be aggressively engaged and also kind of good citizen of that community.
[3313.44 → 3313.84] So –
[3313.84 → 3317.18] I think I first got into Linux on the desktop in 97 or 98.
[3317.60 → 3318.34] Oh, man.
[3318.44 → 3319.66] And it was so funny.
[3319.66 → 3327.74] Back then, you would spend all this time on your Windows desktop to, you know, trick it out to make it look like Linux just because it had, you know, the cooler look and feel.
[3327.82 → 3329.78] And sometimes you're on Linux, you'd go the opposite direction.
[3329.84 → 3332.34] But lately, I spend most of my time in text mode.
[3333.02 → 3333.34] Oh, yeah.
[3333.54 → 3333.80] Totally.
[3333.80 → 3343.12] I mean, that's for sure, like, you know, one of the reasons that Monad has been so great for me is because, you know, I'm just spawning terminals all the time.
[3344.08 → 3346.96] And having it, you know, be a tiling window manager is ideal.
[3347.06 → 3350.98] But, you know, this is one of my biggest appointments with Linux on the desktop right now.
[3351.02 → 3351.98] And actually, look it.
[3352.28 → 3355.40] You know, Ubuntu – I applaud what Ubuntu is doing with Unity.
[3355.40 → 3359.46] And I'm not a Unity user myself, but they're taking a risk.
[3359.86 → 3360.76] They're experimenting.
[3361.78 → 3371.32] My problem – I shouldn't say my problem with Ubuntu, but my concern, I guess, is that I see them doing things like, you know, they were working on, like, Ubuntu on TV.
[3371.32 → 3377.40] And to me, that is such the wrong direction to be focusing their energies.
[3378.56 → 3380.26] You know, it's a consumer product, I understand.
[3380.60 → 3382.60] And, you know, we have Linux and consumer products today.
[3382.68 → 3383.30] We have Android.
[3383.82 → 3391.56] But I would love to see concerted effort over the next 24 months to solve a couple key problems on Linux and the desktop.
[3391.78 → 3395.64] First, I would love to see these distributions focus on developers.
[3396.16 → 3398.04] I mean, this is the low-hanging fruit people, right?
[3398.04 → 3401.90] I mean, like, developers – right now, if you're a developer, if you're a web developer, what are you doing?
[3402.04 → 3402.66] What are you choosing from?
[3402.70 → 3405.56] You're choosing between Mac and Linux, primarily.
[3405.94 → 3406.34] That's true.
[3406.74 → 3406.98] Right?
[3407.96 → 3410.54] And the Mac is a really appealing platform.
[3410.64 → 3412.18] The Mac has some awesome tools.
[3412.28 → 3416.32] But I am super happy developing on Linux, other than the graphics issue.
[3416.78 → 3424.78] And what's weird to me is I look at the development of things like, you know, the kind of strident response from the GNOME team, where they were like, look, we're not going to allow any customization.
[3424.78 → 3429.52] We're not going to have – they were really adamantly against the web-based extension installation.
[3431.32 → 3442.92] Ubuntu with Unity and this real push to really focus on sort of like consumer adoption, I feel like what's happening is they're forgetting about the fact that they really – they cannot lose the developer market.
[3443.20 → 3447.42] If you lose the developer market before you've achieved the consumer market, you've lost everybody.
[3447.42 → 3453.58] You know, and so that's really – I think, number one, just don't forget about your key market developers.
[3455.24 → 3461.86] And, you know, anything – if you're not focusing on developers first and really making sure that you're at least taking care of them, everything else is a fantasy.
[3462.74 → 3465.44] Number two is they really have to solve the hardware problem.
[3465.72 → 3475.30] You know, like, boy, when I was researching what laptop to buy, I don't know if you have this experience, but, like, I went through probably 16 different wikis before I made a decision.
[3475.30 → 3479.32] That's one reason why I'm on the Mac because it limits my choices.
[3479.64 → 3480.46] What did you end up getting?
[3480.88 → 3484.16] Well, I went with Lenovo, and, you know, I've always been a fan of ThinkPads.
[3484.24 → 3488.90] I've had ThinkPads since they were produced by IBM, and I've always been fairly happy with the build quality.
[3489.92 → 3492.16] My experience has been sort of mixed this time around.
[3492.28 → 3494.56] I have two Lenovo sitting right next to me right now.
[3494.66 → 3495.38] I have two ThinkPads.
[3496.20 → 3501.54] I'm on an X220 tablet with a touchscreen, actually, which is pretty cool.
[3501.54 → 3505.90] I'm excited about the multitouch features that are being put into Borg right now.
[3506.82 → 3518.34] But, you know, I just feel like another great move would be some kind of industry consortium where you had, like, Fedora, Ubuntu, a couple of the other big distributions, Arch, of course.
[3518.34 → 3527.42] But, you know, get these people together and say, like, let's pick for the next 12 months, the next 24 months, three laptops, two laptops.
[3527.56 → 3528.00] Make it two.
[3528.12 → 3528.64] Make it simple.
[3529.06 → 3532.44] You know, one high-end and one kind of very lightweight netbook-like system.
[3532.44 → 3535.76] And have those be baseline gold standard systems.
[3536.08 → 3542.42] You know if I knew that it was as easy for me to go out and get a Linux laptop, and, you know, for certain values of easy.
[3542.56 → 3556.78] But if I could go out and get one of those two gold standard systems and know that Fedora, Ubuntu, and, of course, Arch, the most awesome, that these distributions were going to be supporting that particular model for 12 months.
[3556.78 → 3562.02] I mean, not supporting, but that they would be tested or that it would be sort of a known – and, you know, this is Linux we're talking about.
[3562.12 → 3567.24] I'm not saying that it has to be easy, you know, like just out of the box, everything is working.
[3567.36 → 3576.92] But that there is going to be, like, a dedicated forum for that laptop, that there's going to be, you know, a set of drivers that are tested and that I can get it working, and I can feel comfortable making that choice.
[3577.26 → 3579.92] That right there I think would spur a lot of adoption.
[3580.38 → 3582.76] Have you had any problems getting drivers for Arch?
[3583.66 → 3584.44] No, no.
[3584.48 → 3584.96] It's been great.
[3584.96 → 3586.40] In fact, Arch for me is a lot better.
[3586.40 → 3588.18] I really prefer Arch because of that.
[3588.36 → 3590.52] I mean, the rolling release model is stellar.
[3590.76 → 3591.30] I love it.
[3591.98 → 3599.48] You know, I have not – you know, you always hear horror stories about Arch breaking and I certainly – I haven't had many problems with it.
[3599.54 → 3603.88] I mean, occasionally, once or twice, but it's never been a showstopper for me.
[3605.50 → 3606.98] No, I just love it.
[3607.18 → 3610.82] I feel like it's much easier for me, especially given the weird hardware that I'm running, the touchscreen.
[3610.82 → 3617.40] It's been a lot easier for me to run Arch and get that kind of stuff working, functional, the way that I want it.
[3618.40 → 3625.18] You know, I have multitouch running with Monad right now so that I can swipe using a four-finger swipe on the screen back and forth and have it switch Monad spaces.
[3625.50 → 3627.52] I mean, you know, like that kind of stuff.
[3627.58 → 3628.38] I can't even do that.
[3628.52 → 3631.14] I can barely get, you know, OS X, Lion.
[3631.14 → 3633.16] I can barely get spaces working the way I want.
[3633.38 → 3638.42] You know, this is why Monad is great for me because I can just absolutely customize it down to the metal.
[3638.84 → 3641.76] And spaces is broken on Lion if you have multiple screens.
[3641.90 → 3642.44] It's just –
[3642.44 → 3642.96] Oh, it's terrible.
[3643.10 → 3643.62] It's terrible.
[3644.00 → 3645.66] I mean, it's criminal, really.
[3645.90 → 3649.16] You know, that's UI criminality right there.
[3649.40 → 3650.72] So one last question for you.
[3650.76 → 3652.16] What's on your open source radar?
[3652.32 → 3654.40] Anything out there that you just want to play with?
[3654.70 → 3655.36] Oh, boy.
[3655.46 → 3656.44] That's a good question.
[3658.12 → 3659.34] Boy, I don't know.
[3659.40 → 3660.42] Let me think about that for a second.
[3661.14 → 3661.70] Hmm.
[3663.00 → 3663.80] Thinking, thinking.
[3667.36 → 3667.72] Yeah.
[3667.86 → 3678.60] So things that are open source projects on my radar, I guess there are things that I would like to do, certainly open source projects that I'd like to be involved with.
[3681.14 → 3682.58] I'd like to do a lot more with Vim.
[3683.18 → 3686.90] Vim's always on my radar, but it's great to see that Vim hasn't slowed down at all.
[3687.58 → 3697.22] One thing I would love to do is – and this is not like a particular project on my radar, but I'd love to see some effort in terms of the Vim documentation and the Vim wiki, which is really aging.
[3698.02 → 3700.36] I'm not sure what could be done there.
[3700.36 → 3704.74] And I feel like there's enough smart people in the Vim community right now that something could happen.
[3705.44 → 3707.82] So I'd love to be involved with kind of revising that.
[3708.04 → 3711.14] Vim's one of those tools that your friends tell you about, and then you get into it.
[3711.14 → 3717.98] But it's kind of hard to go somewhere and learn and make an objective decision if you want to jump into this editor.
[3718.42 → 3718.66] Oh, yeah.
[3718.76 → 3726.86] I mean it took me – I really had to like section off about literally a month of my life to learn Vim without exaggerating.
[3727.10 → 3730.78] Like I think I just kind of like hold up for a month and was like, okay, I'm going to learn Vim.
[3730.78 → 3733.84] And it's like touch typing for your brain, right?
[3733.90 → 3739.38] I mean it's – it really just requires a significant remapping of the way that you deal with text.
[3740.26 → 3743.20] I think Dr. Nick called it 1960s video game technology.
[3745.10 → 3745.90] 1960s were awesome.
[3746.14 → 3749.46] He's got a certain – that rings true to some extent.
[3749.60 → 3751.44] Some people ask you, how did you do that in Vim?
[3751.52 → 3752.86] And a lot of times, I don't know.
[3752.92 → 3756.02] I'll have to do it and watch my fingers because it's just muscle memory.
[3756.26 → 3756.84] Oh, totally.
[3756.84 → 3763.12] I mean it's like I have passwords like that where if I think too hard about the password, I'll probably type it in wrong because my fingers remember it pretty well.
[3763.20 → 3764.48] But my brain doesn't.
[3765.88 → 3768.46] Other than that, no, I am still playing with pfSense.
[3768.58 → 3775.26] I have a – I built a router which is running pfSense, which is a BSD.
[3776.18 → 3780.82] And it's just an outstanding firewall and router solution.
[3781.28 → 3783.76] And I did a lot of custom hardware for that.
[3783.76 → 3794.74] So like I had a custom faceplate burnt – or custom faceplate cutout locally here in Seattle and did a lot of custom chassis design for it.
[3794.82 → 3795.94] So that's been a lot of fun.
[3797.52 → 3798.70] Well, thanks for joining us, Ethan.
[3798.84 → 3803.90] It's been fascinating to talk about Solarize and some of the theory behind it and just a wide range of topics.
[3804.30 → 3805.36] Yeah, well, thanks for having me, Won.
[3805.44 → 3806.98] It's been a very enjoyable chat.
[3806.98 → 3836.96] Thank you.
