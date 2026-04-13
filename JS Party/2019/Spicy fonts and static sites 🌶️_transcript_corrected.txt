[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.96] Check them out at Rollbar.com.
[10.18 → 12.40] And we're hosted on Linde cloud servers.
[12.74 → 14.74] Head to Linode.com slash Changelog.
[15.48 → 18.54] This episode is brought to you by our friends at Rollbar.
[18.66 → 21.62] Move fast and fix things like we do here at Changelog.
[21.62 → 24.38] Check them out at Rollbar.com slash Changelog.
[24.60 → 26.96] Resolve your errors in minutes and deploy with confidence.
[26.96 → 30.14] Catch your errors in your software before your users do.
[30.52 → 33.16] And if you're not using Rollbar yet, or you haven't tried it yet,
[33.30 → 36.78] they want to give you $100 to donate to open source via Open Collective.
[36.88 → 40.20] And all you got to do is go to Rollbar.com slash Changelog, sign up,
[40.60 → 41.84] integrate Rollbar into your app.
[41.92 → 45.92] And once you do that, they'll give you $100 to donate to open source.
[46.30 → 49.14] Once again, Rollbar.com slash Changelog.
[56.96 → 63.12] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[63.28 → 69.72] Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at Changelog.com slash live.
[69.72 → 74.84] Join the community and Slack with us in real time during the show at Changelog.com slash community.
[75.30 → 76.04] Follow us on Twitter.
[76.14 → 77.66] We're at JSPartyFM.
[77.78 → 79.12] And now on to the show.
[79.12 → 87.14] Hello and welcome to another exciting adventure with the JS Party.
[87.54 → 91.60] I'm your host today, Nick Needed, and I'm joined today by Divya Sassidaran.
[91.78 → 92.04] Hello.
[92.24 → 92.74] Welcome, Divya.
[92.96 → 93.40] Thanks.
[93.84 → 97.36] And we have a special guest this week, Mr. Zach Leatherman.
[97.54 → 97.90] Hello.
[98.22 → 98.54] Hello.
[98.66 → 99.82] How are you all doing?
[100.36 → 102.14] Welcome to the party, Zach.
[102.54 → 103.84] Do you want to tell us a little bit about yourself?
[104.50 → 105.02] Yeah.
[105.02 → 105.18] Yeah.
[105.98 → 112.14] So I actually live in Iowa in the middle of the U.S., kind of in the middle of nowhere.
[113.44 → 120.48] I am a web developer for Filament Group, which is a're a completely remote design and development
[120.48 → 121.28] consultancy.
[121.74 → 125.52] Used to be based out of Boston, but we're kind of just spread all over now.
[126.04 → 126.40] Yeah.
[126.44 → 128.14] And we basically make websites for people.
[128.14 → 134.30] So I've been with the company, with Filament Group for, I think, almost six years, six or
[134.30 → 135.02] seven years now.
[135.24 → 136.66] So, yeah.
[137.16 → 137.82] Very cool.
[138.32 → 144.66] And you are also an organizer of Nebraska JavaScript Conference with Jared and me.
[145.20 → 145.50] Correct.
[145.76 → 145.92] Yeah.
[145.92 → 147.46] We have another one coming up in August.
[147.76 → 153.30] So we are reviewing talks for that tonight, reviewing the CFP stuff for that tonight.
[153.48 → 154.18] So, yeah.
[154.44 → 154.94] Yeah.
[155.34 → 157.72] I'm actually really excited about this year's theme.
[157.72 → 164.16] I keep talking about it because I'm more curious, like, what each of you, which character
[164.16 → 167.82] each of you will be matching that.
[168.32 → 168.56] Yeah.
[168.56 → 169.28] That's a good question.
[169.34 → 172.18] We'll have to get some dye for Nick's beard.
[172.70 → 173.12] Oh, yeah.
[173.24 → 173.48] Of course.
[174.00 → 175.16] It's getting there on its own.
[175.24 → 176.66] I don't have to worry too much about it.
[177.72 → 178.12] Yeah.
[178.12 → 182.38] So we are going to talk to you about a couple of topics this week.
[182.68 → 184.48] The first one is fonts.
[184.66 → 187.76] Now, when I think of fonts, your name immediately comes to mind.
[187.92 → 192.40] And I think if you say font enough on Twitter, you just kind of swoop in, right?
[192.76 → 195.62] I may or may not have a saved search set up.
[195.62 → 200.90] This is something that is always perplexing to me because I don't have an eye for design
[200.90 → 201.44] at all.
[201.64 → 203.92] And so I'm always amazed that you can change the font.
[204.04 → 209.28] And then I have no idea what to change it to beyond, you know, Comic Sans, which is terrible.
[210.20 → 212.90] But you can really pick some cool fonts.
[212.98 → 216.28] And I think that sites look a lot better with cool fonts.
[216.36 → 219.20] I just don't know how to determine what those fonts are.
[219.76 → 224.40] But what would you say is the state of the art for font loading today?
[224.40 → 226.98] Yeah, I mean, there are a couple of different levels.
[227.20 → 229.82] It really depends on how deep you want to jump in.
[230.16 → 235.18] Like there's the easiest thing you can do is sort of just add a font display descriptor
[235.18 → 240.04] to your font face block to let the text be visible while it's loading.
[240.76 → 245.14] And kind of the neat recent thing that happened there was that Google Fonts added support for
[245.14 → 245.66] that too.
[245.78 → 253.10] So if you use Google Fonts, you can add this display URL parameter to your Google Fonts URL.
[253.10 → 256.78] And it will actually add this font display descriptor for you.
[257.60 → 262.26] And that's sort of like the entry level font loading thing you can do.
[262.36 → 266.30] That's like the easiest thing you can do to sort of improve your font loading behaviour.
[266.82 → 270.68] And there are some caveats with that specifically around like icon fonts.
[270.78 → 277.04] If you're using icon fonts, it doesn't really work great because with an icon font, you basically
[277.04 → 279.66] don't ever want your fallback text to show.
[279.66 → 284.82] Like you never want the text to be visible while it's loading because you don't really
[284.82 → 287.06] know what's going to show or what's going to render.
[287.62 → 290.60] Yeah, because that could be overwriting anything, right?
[290.72 → 294.34] Like it could be overwriting the letter A or just some invisible character.
[294.34 → 301.30] Yeah, and a lot of times like the best practice is to use this Unicode area called the private
[301.30 → 301.98] use area.
[302.54 → 306.94] But operating systems sometimes dump who knows what in there.
[307.10 → 308.70] There'll like to be some emoji in there.
[308.78 → 310.42] I know iOS has emoji in there.
[311.22 → 320.48] And so a lot of times you'll see like icon fonts sort of showing emoji fallback when the
[320.48 → 325.02] glyph, like the fallback glyph has nothing to do with what the actual icon is going to
[325.02 → 325.24] be.
[325.74 → 331.98] Yeah, there's not really a good font display descriptor value for icon fonts.
[332.06 → 334.46] And I have a blog post on my website about that.
[334.56 → 336.12] I think I just launched that last week.
[336.42 → 340.08] So yeah, icon fonts are just kind of outside the font loading mainstream.
[341.14 → 343.76] There's no good way to really do it without JavaScript.
[344.72 → 346.24] But this is the JS party, right?
[346.44 → 348.02] So use all the JavaScript.
[348.02 → 354.22] Can we maybe take like a step back and talk a little bit about like the overall problem
[354.22 → 358.28] of fonts loading on the web for people who are not familiar with that?
[358.74 → 358.94] Sure.
[359.12 → 359.30] Yeah.
[359.42 → 366.92] So when you add a web font to your code, basically there are a couple of different things that happen
[366.92 → 368.08] when the font loads.
[368.56 → 374.78] The biggest problem primarily is that browsers will hide any text using that font for up to
[374.78 → 376.58] three seconds while the font loads.
[376.58 → 381.76] And then if the font hasn't loaded within three seconds, it will show your fallback text.
[381.90 → 386.28] It will render sort of your system font fallback in your font family stack.
[386.88 → 391.04] And then it will re-render after the font has loaded successfully.
[391.34 → 396.52] So you kind of have like this up to two different stages of rendering that can happen.
[397.28 → 398.56] You have invisible text.
[398.64 → 399.94] Then you could have fallback text.
[399.94 → 401.14] Then you get your web font.
[401.86 → 407.02] And so that's really problematic when it comes to web fonts because not just the perceived
[407.02 → 409.84] performance of you want your text to render.
[410.44 → 415.40] Like you want your text to be visible and readable as soon as like the page renders.
[415.64 → 418.24] On first render, you want readable text.
[418.24 → 424.30] But when you have multiple fonts interacting, you get some weird race conditions that can happen.
[425.10 → 432.78] So like when you have a web font for a title and then a different web font for like your italics
[432.78 → 438.28] of that same font family, you can get some weird like partially visible text.
[438.28 → 442.94] Like each web font has its own loading cycle.
[444.04 → 447.20] So and they all can finish at different times.
[447.72 → 453.50] So it's really kind of a weird resource that isn't really treated in any other way like any
[453.50 → 454.76] other resource on the web.
[455.10 → 457.16] It's kind of has its own unique problems.
[457.84 → 462.30] Yeah, I really like your I think you've given you've showed this example in like multiple
[462.30 → 468.50] talks you've given where there's like an example of a news site that's like Mitt Romney is running
[468.50 → 472.12] for president because the not like didn't load.
[472.26 → 477.88] Yeah, they like italicized not because he was not running for president.
[478.24 → 481.56] But the not italic web font hadn't loaded yet.
[481.64 → 487.30] And so this person, James, I think his name was James Muskrat, took a screenshot of this
[487.30 → 492.98] site he was reading, and it said the exact opposite of what the title was trying to convey.
[493.42 → 495.10] And it's kind of a huge problem, right?
[495.12 → 502.54] Because the web font introduced like basically a reliability issue with their content because
[502.54 → 507.12] they conveyed the exact opposite of what the news article was trying to say.
[507.74 → 510.02] Yeah, that's crazy and an extreme example.
[510.38 → 515.60] So that was an example of what would you call that flash of invisible text or void?
[515.60 → 517.54] Yeah, that's so that's invisible text.
[517.72 → 518.12] I don't know.
[518.16 → 522.80] I've kind of started to move away from using foul and void and just sort of saying invisible
[522.80 → 524.44] text and fallback text.
[524.62 → 527.66] But because I just think it's more understandable.
[527.66 → 531.64] Like those initialisms are I don't know, they're confusing to people.
[531.64 → 535.58] Like every time I launch a blog, like a new blog post, I'll get like someone saying what's
[535.58 → 536.80] a foul or what's a void.
[536.98 → 540.80] And so I think it's just easier to say invisible text and fallback text.
[541.40 → 542.58] And so I might have missed this part.
[542.58 → 548.36] Is it based on how you load it or where you could have that invisible text or unstyled
[548.36 → 548.62] text?
[548.72 → 552.46] Or is it up to the browsers, like browser implementation details?
[552.86 → 555.46] Well, I mean, different browsers used to do it differently.
[556.10 → 563.00] But they've all kind of settled on this invisible text default sort of edge and Internet
[563.00 → 563.50] Explorer.
[563.70 → 570.20] Microsoft browsers have historically been a huge fan of just making the text invisible or visible
[570.20 → 572.92] by default from right when it starts to load.
[573.74 → 576.58] They sort of opted out of invisible text altogether.
[576.58 → 581.04] But with the new Chromium Edge, that's changing.
[581.24 → 584.98] And they're going to standardize on this three second invisible text.
[585.20 → 590.22] As far as I know, I did actually download the Mac version of Chromium Edge to test it
[590.22 → 590.40] out.
[590.50 → 593.50] And yeah, they're using this three second invisibility timeout.
[593.76 → 596.42] So I would say, yeah, it used to be more diverse than it is.
[596.42 → 598.70] But it's certainly standardized.
[599.38 → 599.72] Very cool.
[600.02 → 601.64] What problems still exist, though?
[602.06 → 602.26] Yeah.
[602.30 → 606.32] So the kind of the thing that I'm super excited about, and this is something Jason
[606.32 → 614.18] Mental has written about on his blog, is the ability to load a partial font and sort of
[614.18 → 616.60] combine fonts on the client.
[616.76 → 618.88] He's calling it incremental transfer.
[618.88 → 625.34] And I think this is really, really, really important, especially because variable fonts
[625.34 → 628.42] are going to be sort of ballooning file sizes.
[628.90 → 629.94] Fonts are going to get bigger.
[630.10 → 631.44] They're going to take longer to load.
[631.98 → 639.24] We need the ability to partially load a font and then sort of delta in more of that font later
[639.24 → 640.68] and combine it on the client.
[640.68 → 647.50] And I think that's going to be a huge, huge win, especially for international fonts that
[647.50 → 649.88] have like a huge character set.
[649.98 → 652.14] Like the Latin character set is not that big.
[652.64 → 657.92] But when it comes to sort of other languages, this problem is like a big, big, big one.
[658.30 → 661.22] So yeah, I think that's a very, very exciting new development.
[661.40 → 666.74] And they're working on, I think they have a sort of standards group, standards body established
[666.74 → 667.26] around that.
[667.30 → 668.86] And they're sort of working through that right now.
[668.86 → 670.34] So it's very, very cool.
[671.30 → 676.12] Isn't there also the ability to load fonts via JavaScript?
[676.58 → 680.92] So you could use like, there's a font loading API that you can use in order to make sure
[680.92 → 683.76] that your font gets loaded and there's like priority given.
[684.16 → 684.40] Yeah.
[684.52 → 691.00] I mean, the big sort of win, because the CSS font loading API is a JavaScript API, just
[691.00 → 694.68] as you said, to sort of have more control of your font loading.
[695.12 → 698.10] And it actually predated the font display descriptor.
[698.10 → 704.14] So historically, a lot of people use that to use the CSS font loading API to do some of
[704.14 → 706.76] the things, the same things that font display does now.
[707.16 → 711.62] So some of that usage or some of the benefit that you get from the CSS font loading API
[711.62 → 717.72] is sort of minimized and made easier with this new font display browser support, which is
[717.72 → 719.78] really, yeah, it's really great.
[719.78 → 724.70] The real benefit you can get from the CSS font loading API is that you can actually make
[724.70 → 727.62] all of your web fonts render at the same time.
[728.12 → 731.78] So you can sort of group your repaints so you don't get a bunch of bank.
[731.94 → 740.58] Like if you have four or five web fonts on your page, you can find out when those render and
[740.58 → 746.36] then render them all at the same time, which is much better than sort of having five different
[746.36 → 750.88] reflows that happen at different parts of your waterfall on your page.
[751.24 → 754.82] So yeah, I find that I've used that a bit before.
[754.82 → 759.66] And it's really nice because like each of it's basically like whenever you use that API,
[759.66 → 760.30] it's a promise.
[760.30 → 765.36] And so you can just like wait for everything to like resolve and then load your content,
[765.48 → 766.52] which is super nice.
[766.90 → 767.86] Yeah, it's super slick.
[768.44 → 771.56] It's really set up to be perfect.
[771.64 → 772.14] I don't know.
[772.18 → 773.38] I really appreciate that.
[773.50 → 779.58] I wish that Edge and Internet Explorer had like jumped on that support bandwagon, but I guess
[779.58 → 781.42] we're going to get that with Chromium Edge too.
[781.96 → 783.28] It's new modern APIs.
[783.46 → 784.34] They're fascinating.
[784.90 → 785.10] Yeah.
[785.18 → 788.28] I mean, CSS font loading API has actually been around for a few years.
[788.28 → 792.54] It's kind of, I don't know exactly when it was introduced, but yeah, it predated font
[792.54 → 794.00] display by a couple of years for sure.
[794.52 → 798.54] So where do you think something like preloading comes in?
[798.60 → 804.34] Because there's the ability for you to preload assets via like, let's say like using preload
[804.34 → 806.68] or you can use like HTTP2 push or something.
[807.14 → 809.00] Like, is that recommended as well?
[809.38 → 810.32] Yeah, I mean, absolutely.
[811.04 → 815.92] So I would say that there's, so we kind of mentioned like the introductory font loading
[815.92 → 817.54] is the font display descriptor.
[817.54 → 825.08] I would say level two is like preload and maybe the higher level is the CSS font loading
[825.08 → 825.36] API.
[825.52 → 829.66] So maybe we skipped over preload, but so if you're going to do, if you're only going
[829.66 → 834.04] to do a couple of things, I would say use font display and use preload together because
[834.04 → 838.74] preload sort of lets you say to the browser, hey, I'm going to use this font.
[838.94 → 842.78] So load it as high up in the waterfall as you can.
[842.78 → 849.60] And I don't know what sort of like the nuance of font loading is that you're kind of racing
[849.60 → 857.36] to get your web fonts to finish loading before first render, or at least as many of them as
[857.36 → 857.84] you can.
[857.84 → 866.40] And there is a small like first render penalty that comes with preload if you use it too much.
[866.98 → 873.06] Like if you're preloading four or five or six web fonts, you're going to see a delayed first
[873.06 → 873.46] render.
[874.12 → 876.68] Like your page is going to render slower altogether.
[877.22 → 878.12] Don't overdo it.
[878.12 → 882.82] But I would say just like if you're going to preload like one or two web fonts, you can
[882.82 → 884.76] really get great benefit out of that.
[885.84 → 889.52] Also with fonts, this is something that I've always struggled with.
[889.60 → 891.02] There are so many different formats.
[891.20 → 896.72] So there's like WAS and then there's TTF and which is like the recommended file.
[897.42 → 902.24] Yeah, there's kind of the true type format and the open type format, which is, I don't know,
[902.24 → 907.82] that's like the standard, like the standard baseline fonts that you'd get, and you can install
[907.82 → 908.96] on your local device.
[909.74 → 916.28] And WAS is mostly just a container format that adds compression around those formats.
[916.28 → 922.94] So it's not really anything more than sort of wrapper around true type and open type
[922.94 → 923.48] fonts.
[923.98 → 928.96] So you get compression for free, so you don't have to add any sort of like server configuration
[928.96 → 929.76] for that.
[929.76 → 933.70] And then WAS 2 is just a newer version of WAS that makes the compression.
[934.00 → 937.04] I think it's on average like about 30% better.
[937.30 → 941.78] So I would say you can get away with just using WAS 2 and WAS formats now.
[942.58 → 946.00] We'll probably get to a point where you can only use WAS 2.
[946.26 → 948.56] That's probably coming within the next couple of years.
[948.78 → 954.96] But it's a lot easier than it used to be because sort of back in the beginning of web fonts,
[955.08 → 959.46] there used to be like these six or seven or eight different formats you had to list together.
[959.76 → 963.74] And they were all sorts of, I don't know, it was complicated.
[964.00 → 965.22] It was much more complicated.
[966.24 → 969.14] So yeah, it's kind of nice to only have to use two different ones now.
[969.70 → 969.92] Yeah.
[970.26 → 974.80] Also alongside, I think you mentioned this a little earlier with like the fact that fonts
[974.80 → 981.12] sometimes can take longer to load because like some glyphs are, some like glyphs are more
[981.12 → 984.38] than others, like for different languages and so on.
[984.68 → 989.66] Is there an ability, let's say if you, you need it, like specific characters in a font
[989.66 → 991.50] file and not everything else.
[991.64 → 995.68] Is there a way to like to specify, I want just these and like, I don't want to load everything
[995.68 → 996.20] else.
[996.50 → 998.96] Because sometimes that is a concern.
[998.96 → 1002.22] Like you're like, I just want to use this font italic thing.
[1002.22 → 1005.94] And I only for these particular characters and nothing else.
[1006.40 → 1006.96] Yeah.
[1007.14 → 1014.56] So you can, that's, that's what you call subletting, sort of modifying the font file to only include
[1014.56 → 1015.80] what you want to be in it.
[1015.80 → 1022.12] Um, and I maintain a tool called Glyph Hanger, which lets you sort of programmatically say,
[1022.30 → 1026.72] Hey, I want these font files to be subset to these specific characters.
[1027.20 → 1030.92] And it'll output WAF2 and WAS files for you.
[1031.50 → 1036.80] Um, and another thing Glyph Hanger does is it will actually spider URLs that you feed into
[1036.80 → 1040.28] it to show you what glyphs are used on that specific page.
[1040.42 → 1045.78] If you feed it a URL, it can actually go out, uh, parse the page, find a URL.
[1045.80 → 1048.22] All the glyphs that you're using on the page.
[1048.44 → 1054.18] If you have a static site, and then it can, it will write like the font files that you
[1054.18 → 1054.88] need for you.
[1054.88 → 1059.72] Like it will transform those or create new subset font files for you.
[1059.72 → 1063.98] So yeah, it's kind of useful to create the smallest font files that you can.
[1064.58 → 1067.84] What kind of fonts or glyphs would be missing from that?
[1067.86 → 1071.52] Cause it, it seems like maybe I'm not getting my head around this.
[1071.80 → 1075.78] Would it be specifically looking to see you used an uppercase X and a lowercase?
[1075.80 → 1077.96] Uh, so I'll include those.
[1077.96 → 1079.86] And then same thing with all the other letters.
[1080.22 → 1081.94] Yeah, it does go down to that level.
[1082.04 → 1087.50] But so, so most, I guess from a higher level perspective, most fonts include multi-language
[1087.50 → 1088.48] support built in.
[1088.58 → 1093.44] They aren't, they aren't usually segmented or if they are segmented, they're not segmented
[1093.44 → 1095.32] as granular as you'd want them to be.
[1095.32 → 1101.36] So it's, it's kind of typical for a font that you'd download to be like 50 or a hundred or
[1101.36 → 1106.70] even a couple of hundred kilobytes, uh, for, for sort of larger font file.
[1107.02 → 1113.68] And when you subset down to like a one specific language that's used on a site, I've seen fonts
[1113.68 → 1116.52] go down to even like five kilobytes compressed.
[1116.52 → 1123.02] So yeah, you can get a lot, a lot quicker rendering, uh, with a lot smaller file.
[1123.76 → 1128.02] So with dynamic content, that becomes a harder problem.
[1128.30 → 1134.02] And that's kind of gets into the more incremental transfer, uh, thing we talked about earlier,
[1134.02 → 1140.00] which sort of allows you to combine those subsets into a single font file in the client.
[1140.00 → 1140.28] Yeah.
[1140.94 → 1145.08] So could you technically use glyph hanger in your build?
[1145.38 → 1150.32] Let's say if you have like a single page app or whatever, and you have a build script
[1150.32 → 1155.74] that like builds it to, to like static HTML, could you like put glyph hanger in the middle
[1155.74 → 1161.52] somewhere in the build process so it can like scan all the HTML once it's been rendered?
[1161.94 → 1163.42] Yeah, you can certainly do that.
[1163.42 → 1169.94] Uh, when I was working on the font loading for filament group.com, which is our company website,
[1170.00 → 1175.16] actually built, uh, like a little thing on top of glyph hanger that would go through
[1175.16 → 1180.78] all the different pages on our site and find all the different glyphs on every single
[1180.78 → 1181.32] page.
[1181.48 → 1186.00] Now for a small, like a small site, uh, like ours, you could do that.
[1186.06 → 1190.22] We can sort of get away with that, uh, because there isn't more than like, I don't know, like
[1190.22 → 1195.26] 20 different, uh, well, we have a bunch of different blog posts on there, but, um, there
[1195.26 → 1197.58] isn't a ton of content on the site.
[1197.58 → 1200.76] It's not like thousands of pages that we have to go out and spider.
[1201.32 → 1207.66] Um, so if you're, if you are willing to tolerate the sort of the build time performance hit to
[1207.66 → 1209.34] do that, you can absolutely do that.
[1209.52 → 1215.50] Um, but I don't know that that scales super well, uh, to like a thousand site page.
[1215.74 → 1216.16] Yeah.
[1216.30 → 1222.68] And the idea is that like, this won't work for, let's say a dynamic application or not dynamic,
[1222.68 → 1227.80] but like, let's assume you have an application that like just loads JavaScript to switch
[1227.80 → 1228.46] out the content.
[1228.60 → 1231.58] Then like glyph hanger might not work as well.
[1231.70 → 1232.82] Is that correct?
[1233.16 → 1239.06] Well, glyph hanger uses, uh, puppeteer, which does run JavaScript.
[1239.52 → 1242.42] So it can't find glyphs on JavaScript content.
[1242.90 → 1246.58] That's sort of a newer thing that I think we've added within the last couple of years, but,
[1246.80 → 1251.58] uh, originally it used to use something like JS DOM, which was just sort of like a fake,
[1251.58 → 1257.02] fake DOM implementation, but now it uses puppeteer, which allows us to sort of spider JavaScript
[1257.02 → 1257.88] stuff as well.
[1258.06 → 1258.44] Yeah.
[1258.46 → 1258.96] That's really cool.
[1259.50 → 1259.70] Yeah.
[1259.72 → 1260.24] It's yeah.
[1260.26 → 1260.74] I like it.
[1260.94 → 1261.68] It works well.
[1262.20 → 1267.54] So Zach, if people want to learn more about font loading or, um, to catch some of your,
[1267.54 → 1273.02] your wonderful jokes, what, uh, you have some talks that we can point people to, right?
[1273.58 → 1273.86] Yeah.
[1273.90 → 1277.90] So I have a couple of different talks that I've done, uh, in the past couple of months that
[1277.90 → 1279.76] I think are probably useful to look up.
[1279.76 → 1287.30] Uh, one was at the performance now conference, uh, in Amsterdam last, last, the end of last
[1287.30 → 1287.54] year.
[1287.62 → 1294.30] And I sort of went through, uh, and this was a more like technical talk about how to sort
[1294.30 → 1300.00] of improve the default web font loading of the WordPress theme, the default WordPress
[1300.00 → 1300.38] theme.
[1300.38 → 1302.76] When you go to create a new site on wordpress.com.
[1302.76 → 1309.54] Um, and I think if you're looking to sort of improve the font loading of a site, then
[1309.54 → 1313.36] that sort of gives you, gives you like a bunch of different tools that you can use.
[1313.36 → 1318.80] And it goes through the performance characteristics of those tools, how to implement those tools,
[1318.80 → 1323.62] uh, the different performance profiles that you'll get when you use those tools and sort
[1323.62 → 1325.32] of the trade-offs, um, there.
[1325.32 → 1331.52] So I think that that's probably a really useful talk if you're trying to sort of look for pragmatic
[1331.52 → 1333.60] wins that you can have in your font loading.
[1334.10 → 1338.72] And then another one is, uh, the Beyond Tolerant conference a couple of weeks ago, I gave the
[1338.72 → 1342.34] Scoville scale of, uh, font loading opinions.
[1342.82 → 1350.48] And that sort of went through a bunch of different, uh, just, I guess, spicy hot takes I had on web
[1350.48 → 1354.24] font loading, um, and things that you should do and shouldn't do.
[1354.36 → 1361.56] And it was more of a higher level, like, I don't know, more of a fun talk and not necessarily
[1361.56 → 1366.00] as like deep dive technical, but I, I don't know.
[1366.04 → 1371.66] That was the intention, but just in terms of how I write talks, I always seem to get lost
[1371.66 → 1373.18] in the deep dive technical stuff.
[1373.18 → 1375.26] So there's certainly some of that in there too.
[1375.64 → 1376.62] Did that answer your question?
[1377.62 → 1378.02] Yeah.
[1378.42 → 1378.54] Yeah.
[1380.48 → 1391.80] This episode is brought to you by Algeria search technology to power your business trusted by
[1391.80 → 1394.10] Twitch, Stripe, Adobe, and many more.
[1394.40 → 1394.92] Even us.
[1395.06 → 1399.40] Yes, we use them to power our search, and we love the way they obsess over that developer
[1399.40 → 1400.00] experience.
[1400.18 → 1404.28] They let us fine tune the index for the best results and report back what people are searching
[1404.28 → 1404.62] for.
[1404.88 → 1408.40] Even servicing search terms that get zero results, which we love.
[1408.40 → 1412.84] Check the show notes for a link to get started for free or head to algolia.com to learn
[1412.84 → 1413.14] more.
[1413.14 → 1430.66] So Zach, the other thing that you're pretty well known for at this point is a fun project
[1430.66 → 1431.76] called Eleventh.
[1432.06 → 1432.46] Woo!
[1433.32 → 1433.80] Yeah!
[1434.46 → 1435.02] Eleventh!
[1435.26 → 1435.58] Woo!
[1436.04 → 1436.30] Yeah.
[1436.30 → 1438.56] So we're taking this all the way up to Eleventh.
[1439.40 → 1443.96] I'm so glad that you said that joke, Nick, because I have never heard that one before.
[1444.38 → 1448.04] It's a completely new exclusive to the podcast.
[1448.42 → 1449.52] So tell us about Eleventh.
[1449.56 → 1450.02] What is it?
[1450.88 → 1455.16] Eleventh is, I guess, at its core, a static site generator.
[1455.60 → 1458.04] It was sort of inspired by Jekyll.
[1458.04 → 1461.20] And yeah, so it's written in JavaScript.
[1461.56 → 1462.54] It runs a node.
[1464.50 → 1468.06] And yeah, it's just basically a static site generator.
[1469.28 → 1474.40] And it's sort of, I don't know, yeah, it's kind of taken off and a lot of people are using
[1474.40 → 1474.68] it.
[1474.78 → 1481.36] And it's been a really, I don't know, I've been super delighted and humbled to see the
[1481.36 → 1483.06] different things that people have built with it.
[1483.12 → 1484.12] It's kind of great.
[1484.12 → 1492.08] And in some respect, it's, I don't know, I feel like it's been really awesome to see
[1492.08 → 1498.84] just people say, I don't really have very much coding background, but I've tried out
[1498.84 → 1500.74] Eleventh, and now I have my own website.
[1501.72 → 1508.10] Like, that's like, has been super meaningful to me just to hear those stories of people
[1508.10 → 1514.08] that maybe didn't have a website before and maybe even didn't really know how to
[1514.08 → 1515.30] write very much code before.
[1516.04 → 1521.18] But they tried out Eleventh, and they were able to get it working and were able to deploy
[1521.18 → 1523.98] their own website using it, which is just amazing.
[1524.32 → 1525.16] Amazing to me.
[1525.68 → 1526.42] Yeah, that's really cool.
[1526.64 → 1530.16] And that makes it sound like it's really simple to get started with.
[1530.46 → 1531.58] What makes it simple?
[1532.10 → 1534.96] You know, that's a very, very interesting question.
[1534.96 → 1541.88] We try and like to make the default, like config list behaviour of the tool to be kind of intuitive.
[1542.38 → 1544.78] It will work without a configuration file.
[1545.84 → 1550.86] It basically only, all it needs to operate is, is content.
[1550.86 → 1556.18] So if you feed it a markdown file, it will transform that markdown file into HTML.
[1556.64 → 1559.44] If you feed it a liquid template, it can do that.
[1559.54 → 1562.28] If you feed it a non-U template, it can do that.
[1562.38 → 1567.34] And I think there's like eight or nine different template languages that we support right now.
[1567.98 → 1568.20] Yeah.
[1568.26 → 1573.88] So I really, really have focused hard on trying to make sort of the beginner experience something easy.
[1574.34 → 1574.78] Nice.
[1574.78 → 1578.60] So is that done via like a plugin system, like supporting multiple templates?
[1579.42 → 1580.62] Not yet.
[1580.84 → 1589.12] So that's the next big ticket item on the Eleventh docket is sort of democratizing the emulating language support
[1589.12 → 1595.96] so that I'm not like the arbiter of the template languages that go into the tool.
[1597.46 → 1602.36] We have like eight or nine, as I said, that we support right now.
[1602.36 → 1611.04] And people have asked for like more to come, but I'd rather just sort of create a plugin system built into Eleventh.
[1611.36 → 1618.96] I mean, there is a plugin system set up right now, but it doesn't let you, there aren't hooks to add your own emulating language into it yet.
[1619.16 → 1624.62] So supporting template, new template languages is our next big release.
[1625.62 → 1626.14] Nice.
[1626.24 → 1631.34] It supports quite a few template languages at the moment, but it'll be cool to, yeah, like you said,
[1631.34 → 1636.02] have more of an agnostic way of loading a template.
[1636.52 → 1641.36] Yeah, because, I mean, you could kind of see, I mean, there are benefits and downsides to both.
[1641.44 → 1651.16] I think that certainly there's ease of use benefit in having them bundled because anyone could download it and get started
[1651.16 → 1657.52] without having to sort of add additional plugins, which is kind of a bummer when you're just getting started.
[1657.52 → 1660.92] So I think we'll always have like a stock set that we support.
[1662.72 → 1669.52] Yeah, so Markdown, Liquid, Nubucks, Handlebars, Moustache, EPs, Hall, and Pug.
[1670.32 → 1678.56] And then sort of like the big one that I've sort of gravitated towards lately is just like raw JavaScript templates.
[1678.56 → 1685.30] So you can write a JavaScript class or a JavaScript function that returns a string, and that's your template.
[1685.74 → 1687.46] You don't need to really do more than that.
[1687.94 → 1689.32] The string is just HTML?
[1689.72 → 1691.90] Well, you can feed it, yeah, just a string of HTML.
[1692.16 → 1695.98] You can feed it any sort of template language that will output a string.
[1696.34 → 1699.24] You can do that as well inside this JavaScript templates.
[1699.38 → 1703.96] Anything you can do in JavaScript, you can do in Eleventh within a JavaScript template.
[1703.96 → 1711.10] So the tool itself, you install from NPM, as you said, and then that gives you an Eleventh command that you can run.
[1711.34 → 1713.42] And is that like the main part of it?
[1713.66 → 1722.62] Does that consist of a server and a tool for compiling or working with one format and translating it into another?
[1723.36 → 1727.78] Yeah, so basically Eleventh is just a command line tool.
[1727.78 → 1730.74] We do include like browser sync.
[1731.82 → 1743.38] If you want to run a local like hot swapping web server or whatever to preview your code and reload automatically, all of that is built into.
[1744.40 → 1746.86] But really Eleventh is at its core.
[1747.06 → 1753.14] It's just a command line tool to let you transform templates into HTML.
[1753.14 → 1762.30] Okay, so the output of this, something that you would actually like to put on to a website is just static files, like static HTML files.
[1762.42 → 1762.82] Correct.
[1763.62 → 1765.12] Okay, very cool.
[1765.26 → 1770.16] That makes it nice and simple, but still powerful because you can utilize tooling.
[1770.28 → 1778.62] I'm comparing, or I'm thinking of tools that I've used in the past, like Jekyll, that let you do a very similar thing.
[1778.62 → 1783.32] The one downside of Jekyll that I've always had is its Ruby dependency.
[1784.14 → 1788.32] But it sounds like this is much more up my alley because it's just JavaScript.
[1788.78 → 1797.10] Yeah, we've actually gotten a lot of people that have migrated from Jekyll with the sole reason that they didn't want to maintain Ruby stuff.
[1797.18 → 1798.60] They wanted to just do JavaScript.
[1798.60 → 1807.30] And I definitely hear that complaint too because I'm a little bit familiar with Ruby, but I'm not like an expert at Ruby.
[1807.42 → 1810.24] And I'm definitely more familiar with JavaScript than I am Ruby.
[1810.90 → 1818.20] So yeah, it just feels like more at home to be an Eleventh project than it does a Jekyll project for me.
[1818.80 → 1818.98] Yeah.
[1819.22 → 1825.14] Also just like being able to work with just like plain JavaScript is so nice.
[1825.14 → 1829.20] Because a lot of statics like generators out there have some kind of dependency.
[1829.56 → 1834.84] So like I've used Hugo a lot and that requires Go, which is really, Hugo is really great.
[1835.04 → 1845.50] But if the moment you want to update your templates and change like themes, you have to like dive into the weeds of whatever Go uses for emulating, which is kind of annoying.
[1845.50 → 1860.38] And with Eleventh, it's really easy to just take whatever boilerplate and then change it, change the styles, the theming and so on without having to really like to understand like the entirety of Eleventh because it's so lightweight.
[1861.00 → 1861.22] Yeah.
[1861.40 → 1872.50] I mean, the sort of the interesting thing about Eleventh, which is a little bit different from a lot of other static site generators, is that you can actually use all of these different emulating languages together.
[1872.72 → 1873.92] You can mix and match them.
[1873.92 → 1881.88] So for example, you can use like a liquid layout, but your content can be in Moustache.
[1882.54 → 1897.72] So you can sort of mix and match the different emulating languages together, which I think is very powerful, especially if you're using it for a client where you may or may not know what emulating languages they wanted support or use.
[1897.72 → 1909.22] So you can sort of develop code and then modify just the sort of as little as possible to the client specifications, but still use the same tool.
[1909.60 → 1910.92] We have a question in the chat.
[1911.16 → 1914.50] How do we get GitHub Pages to switch from Jekyll to Eleventh?
[1914.64 → 1916.84] Is Eleventh something you can use with GitHub Pages?
[1916.84 → 1919.20] It is.
[1919.20 → 1938.02] The examples that I've seen use sort of like a CI approach, like Travis CI to like to run a build or run your compiled, sort of run your Eleventh build on the server and then deploy that output to GitHub Pages, you know, like your GitHub Pages branch.
[1938.02 → 1942.30] I know GitHub came out with this new like, what is it called?
[1942.42 → 1943.02] GitHub Actions?
[1943.92 → 1944.52] No, GitHub.
[1944.92 → 1945.52] Is that what it's called?
[1946.74 → 1951.04] And I feel like that there could be some overlap there, but I haven't played around with that yet.
[1951.04 → 1964.98] But I think that's sort of their counterpart to what Netlify does, which is just lets you run like a build of your own choosing on their servers and deploy it.
[1965.76 → 1971.78] And we've actually had a lot of good overlap between people that have used Eleventh and people that have used Netlify.
[1972.80 → 1976.66] Just it's super easy to get a site up and running.
[1976.66 → 1985.56] Again, like I mentioned, like people that don't really know very much about coding have used Eleventh and Netlify together to deploy their own website.
[1986.50 → 1988.82] And it's been just really awesome to see.
[1989.64 → 1995.68] I think Phil is like the leading that charge of like Eleventh and Netlify, pretty much.
[1995.96 → 1998.90] Because every time, yeah, he's always like, why do you use a framework?
[1999.10 → 2000.16] Just use Eleventh.
[2000.16 → 2012.46] Phil has been, I don't know, is like, I first met Phil last year at Smashing Conference, like when Eleventh was just in its infancy.
[2012.90 → 2015.72] We were just like a couple versions in.
[2016.22 → 2018.46] And I had talked to him about it just a little bit.
[2018.56 → 2021.28] And he ended up trying it after the conference, I think.
[2021.46 → 2026.40] And he ended up being one of our very first cheerleaders, like from the beginning.
[2026.40 → 2035.98] I would even go far as to say that Eleventh would not exist in its current form without Phil's like early adoption and cheerleading, Phil Hawks worth.
[2036.72 → 2046.72] So huge thank you to Phil because he has been like a huge part of Eleventh's sort of origin story, if you will.
[2047.54 → 2051.04] Yeah, I'm sure he'll be chuffed to hear that, whatever he says.
[2051.58 → 2053.82] Whatever he said, chuffed, chuffed.
[2053.82 → 2056.82] But yeah, so it's been really cool to see.
[2056.98 → 2063.96] And we've actually had a bunch of sorts of bigger name website launches, too, using it, which has been really awesome.
[2064.68 → 2070.40] So web.dev, which is like Chromium Dev's website, is using Eleventh.
[2071.10 → 2078.88] V8.dev is using Eleventh, which is Matthias Bones actually was another very early adopter of Eleventh.
[2079.40 → 2081.58] And so he's using that on V8.dev.
[2081.58 → 2088.52] I think they used it at CERN for the World Wide Web rebuild, which was super awesome to see.
[2089.28 → 2091.78] And I know CSS Tricks has used it a little bit, too.
[2092.18 → 2094.28] I think the conference website that they have set up.
[2094.78 → 2099.30] So yeah, yeah, it's been awesome to see what people are building with it.
[2099.80 → 2100.44] That's really cool.
[2100.44 → 2100.48] Cool.
[2101.78 → 2109.28] So I wanted to ask you why you went out and built a static site generator.
[2109.82 → 2112.14] That is a very good question.
[2114.60 → 2115.84] I'm not really sure.
[2116.60 → 2118.86] I have a very good answer for it.
[2118.86 → 2125.40] So the original impetus, there's kind of two different things that I wanted when I first started the project.
[2125.72 → 2134.40] I kept seeing all of this sort of JavaScript frameworks coming out that were sort of touting performance and touting all these different things.
[2134.56 → 2136.20] Like their developer experience was great.
[2136.20 → 2143.40] And I kept trying them out and looking at the output that would be generated from these files or from these tools, excuse me.
[2143.88 → 2147.36] And they always had runtime JavaScript attached to them.
[2148.14 → 2153.38] And I don't necessarily think that when you're building sites that you all, like every site needs runtime JavaScript.
[2153.58 → 2154.90] You may add it on later.
[2154.90 → 2161.76] But I don't want my tool to inject a bunch of stuff that maybe is unnecessary for my use case.
[2162.20 → 2165.98] And I'm not saying they aren't useful things for different style of sites.
[2166.60 → 2174.08] But I think that there is a definite place for a tool that doesn't have runtime JavaScript built in.
[2174.18 → 2176.68] And it only outputs what you put into it.
[2176.68 → 2191.04] And so I think that Eleventh has sort of occupied that space between your classical static site generators and sort of your more JavaScript-y JavaScript frameworks.
[2191.38 → 2194.20] You get a lot more control of what the output of your site is.
[2194.92 → 2198.10] Yeah, that's kind of the reason I started building Eleventh.
[2198.10 → 2210.54] And the other sort of reason that I haven't necessarily talked about a ton was that I actually started building a site to showcase web fonts and web font loading.
[2211.18 → 2221.66] And Eleventh sort of started as a tool to help me build that site, which is kind of funny to think back on because that project got shelved almost immediately.
[2223.46 → 2227.04] Because Eleventh sort of took over because it's sort of taken off.
[2227.04 → 2240.70] But I think once I start to get more of these bigger ticket items into Eleventh and development starts to maybe calm down a little bit, I'll go back to that web font loading site and use Eleventh to deliver that.
[2241.06 → 2244.08] So, yeah, that's kind of, I guess, the origin story of it.
[2244.38 → 2249.30] It's always nice to, like, when projects spin out of something that you've wanted to build.
[2249.84 → 2254.68] So you want to build something and then you, like, generalize it, and then you open source it, which is super cool.
[2254.68 → 2255.48] Yeah.
[2255.48 → 2261.28] Because then it's, like, you're super invested in it rather than, like, oh, whatever, I built this thing, and then I don't really care about it.
[2261.44 → 2266.50] Because it shows, like, just the fact that this is, like, a passion project, like, totally shows.
[2266.74 → 2272.56] Because Eleventh is one of those where I'm, like, oh, if you ever have an issue and you, like, post it, you're going to get a reply.
[2272.70 → 2275.30] And, like, automatically it will be, like, we're fixing it.
[2275.62 → 2276.38] And so on.
[2276.48 → 2277.36] Oh, nice.
[2277.46 → 2277.80] Thanks.
[2277.88 → 2279.22] Yeah, I really appreciate that.
[2279.22 → 2284.12] Yeah, I have, like, all my websites are using it, basically.
[2284.46 → 2286.20] So, yeah, I'm super invested in it.
[2286.34 → 2294.22] So I think I am really delighted to hear that you think that we're responsive to fix issues.
[2294.22 → 2297.70] Because I've been really busy with conference stuff the last couple of weeks.
[2298.66 → 2302.48] And I owe some open source maintenance for sure.
[2302.48 → 2308.54] I usually think when I have an issue with it, I just, like, ping Phil and be like, hey, Phil, can you help me with this?
[2309.66 → 2311.00] He's, like, de facto.
[2311.66 → 2320.72] Yeah, I mean, yeah, it's been super helpful just to have other people that have, like, our cheerleaders of the project sort of answer questions, too.
[2320.82 → 2322.32] That's been very awesome.
[2322.32 → 2331.58] Because it kind of lets me or frees up more of my time to sort of work on new features and bigger ticket stuff that I want to add.
[2331.80 → 2334.50] Yeah, because it's pretty much just you're working on it.
[2334.66 → 2337.94] Or do you have anybody else who's actively contributing?
[2338.64 → 2344.18] No, I mean, it's basically me in my limited spare time.
[2344.18 → 2349.86] So, like, after the kids go to sleep at night, I'll sometimes fire it up and work on it.
[2350.54 → 2356.84] And then in the morning, sometimes I'll get, like, a couple of hours before work after the kids go to school.
[2357.12 → 2360.52] So, yeah, it's kind of just been here and there.
[2360.80 → 2364.20] But, yeah, I really have, like, a clear vision for what I want it to do.
[2364.30 → 2370.46] And I've been able to sort of stick to that and not get too bogged down by issues so far.
[2370.46 → 2376.32] Because I know a lot of open source maintainers sort of get, I wouldn't say, maybe bogged down isn't the right term.
[2376.60 → 2382.58] But the scale of the project, yeah, the scale of the project sort of outgrows your free time.
[2383.00 → 2387.90] So, yeah, it's been really helpful to have people sort of chime in to answer questions.
[2388.82 → 2390.42] How can people contribute to 11T?
[2391.10 → 2392.24] That's a very good question.
[2392.36 → 2396.12] I would say the easiest thing you can do is just try it out.
[2396.92 → 2400.18] And if, like, a part of it confuses you, tell me.
[2400.46 → 2404.48] Because if it's confusing to you, I'm sure it's confusing to someone else.
[2404.90 → 2408.68] And, yeah, just give me as much of your feedback as you're willing to.
[2409.02 → 2416.32] And I think that the biggest metric of success for the project is how easy and intuitive it is to use.
[2416.32 → 2423.26] So I'm always open and receptive to people's just, like, general confusion about why it did something.
[2423.26 → 2430.18] Because that really helps me sort of think of better ways to solve problems inside the framework.
[2430.98 → 2432.92] So, yeah, just try it out.
[2433.08 → 2434.96] If you like it, let me know.
[2435.02 → 2436.70] If you don't like it, let me know.
[2436.90 → 2439.84] But maybe tell Phil first and then let me know.
[2440.78 → 2443.46] Yeah, just give me your feedback and let me know what you think of it.
[2443.56 → 2445.12] So that's probably the easiest thing.
[2445.12 → 2448.36] Yeah, is there anything else you wanted to convey about Eleven, Zach?
[2448.92 → 2451.30] Oh, no, I don't think so.
[2451.36 → 2452.80] I mean, we do have an open collective.
[2453.20 → 2456.08] I was actually going to bring that up because I see the...
[2456.08 → 2462.50] This is one of the first sites that I've seen that has a very pretty sponsor button on GitHub that links to the open collective.
[2462.82 → 2464.30] Yeah, I saw someone...
[2464.30 → 2464.72] I don't know.
[2464.76 → 2467.56] I saw someone had talked about that on their Twitter.
[2467.72 → 2469.34] And it's very easy to set up.
[2469.34 → 2472.20] It's not like a trial thing.
[2472.78 → 2476.96] The sponsor button is different from like GitHub sponsorships, which is like...
[2476.96 → 2478.62] A long waiting list or whatever.
[2479.10 → 2480.66] Yeah, basically.
[2481.02 → 2482.74] Are you on GitHub sponsorship?
[2483.20 → 2484.56] No, I did.
[2484.90 → 2487.78] I'm on the wait list to try it out, but I haven't heard anything.
[2488.34 → 2490.04] I don't know if I'll actually use that either.
[2490.04 → 2494.22] But yeah, we're on open collective now, but maybe GitHub one will be better.
[2494.32 → 2494.76] I'm not sure.
[2495.08 → 2496.32] Try it out and see what happens.
[2499.34 → 2506.40] This episode is brought to you by Gauge.
[2506.62 → 2510.24] Gauge is a free and open source test automation tool by ThoughtWorks.
[2510.36 → 2513.18] The goal of the tool is to take the pain out of test automation.
[2513.60 → 2518.56] And to help with this, Gauge supports specifications of Markdown, which are easy to read and easy to write.
[2519.02 → 2522.92] Reusable specifications to simplify your code, which makes refactoring easier.
[2523.28 → 2525.92] And less code means less time maintaining code.
[2526.30 → 2527.48] And finally, integrations.
[2527.48 → 2531.14] Use Gauge with your favourite tools and your IDEs and the ecosystem of your choice.
[2531.66 → 2539.96] Selenium, Cheapo, CIC and CD tools like Good, Jenkins, Travis, and IDE support for Visual Studio, VS Code, IntelliJ, and more.
[2540.30 → 2543.08] Head to gauge.org slash js party to learn more and give it a try.
[2543.32 → 2545.76] Again, gauge.org slash js party.
[2545.76 → 2549.94] All right.
[2549.94 → 2554.78] All right.
[2554.84 → 2560.52] So for our next segment, the topic is I'm excited about X where X is literally anything.
[2560.52 → 2565.16] And this is the panellists' chance to tell you about things that we're excited about.
[2565.16 → 2570.98] And this doesn't necessarily have to be in the JavaScript font loading or static site generation world.
[2571.40 → 2572.34] It can be anything.
[2572.78 → 2575.90] So with that, Divya, do you want to start us off?
[2576.04 → 2576.98] Yeah, I can go first.
[2577.36 → 2578.76] I'm really excited about Vue.
[2578.88 → 2580.90] I feel like I'm always excited about Vue.
[2580.90 → 2584.44] And that's mainly because I use it a lot.
[2584.70 → 2586.64] And it's like my framework of choice.
[2586.94 → 2591.92] I've used a couple of frameworks and I find that it's like one of the ones that resonates the best with me.
[2591.98 → 2592.88] Because I get to write.
[2593.10 → 2596.24] It's still like you get this idea of single file components.
[2596.24 → 2601.54] But you still get to write HTML, CSS, and JavaScript in pieces, which I like a lot.
[2603.00 → 2607.56] Because for me, sometimes writing in JSX can be frustrating.
[2607.56 → 2612.42] And this is not a slight on other frameworks, obviously.
[2612.60 → 2613.60] It's just a preference thing.
[2613.72 → 2616.80] Because I like to think in different pieces.
[2617.46 → 2619.50] So I can be like, how do I want my page to look?
[2619.54 → 2620.62] And then I can focus on that.
[2620.68 → 2624.68] And then I can focus on the interactivity afterwards rather than kind of putting them together.
[2625.34 → 2627.86] And that's just the way I think about things.
[2628.00 → 2631.56] And also, alongside that, I didn't think I would be excited about this.
[2631.70 → 2635.40] But I've been watching videos and reading a lot about Svelte.
[2635.40 → 2638.40] And I feel like I have to learn it now.
[2638.82 → 2640.84] Because it's super cool.
[2641.48 → 2648.12] And Rich talks about it with such enthusiasm that I was like, you know, maybe there's something to learn here.
[2648.26 → 2650.98] And the syntax is also really Vue-like.
[2652.28 → 2655.00] Because I think it takes a lot of pages from Vue.
[2655.34 → 2660.86] And so as a Vue developer, I think I would get it slightly better, maybe.
[2660.98 → 2661.36] I don't know.
[2661.36 → 2664.66] And so I just kind of want to dive into that.
[2664.78 → 2667.58] Because Svelte 3 came out, was it a month ago?
[2667.78 → 2668.46] I don't remember.
[2668.60 → 2669.80] It's like one of the conferences.
[2669.82 → 2670.60] Within the last month.
[2670.68 → 2670.96] Yeah.
[2671.52 → 2676.38] When Richard Harris, who created Svelte, pretty much like accidentally released it or something.
[2676.52 → 2677.82] Where he was like, I didn't mean to.
[2679.42 → 2679.82] Whoops.
[2680.44 → 2680.82] Yeah.
[2681.22 → 2683.18] And just talked about just like reactivity.
[2683.32 → 2687.54] I think the whole point of that talk, which was, I think it was called like something reactivity.
[2687.54 → 2697.14] But the whole point was just the idea of how frameworks, the goal is to act very much like Excel spreadsheets, where it updates automatically.
[2697.50 → 2699.32] And you don't have to like to do a lot of finagling.
[2699.50 → 2706.64] And it's very easy to understand without you having to get in the weeds of understanding like JavaScript and scope and inheritance or whatever.
[2707.26 → 2707.98] You have to learn.
[2708.52 → 2709.56] So that's really cool.
[2709.66 → 2714.86] I think framework from the framework side of things like Vue and Svelte are pretty exciting for me.
[2714.86 → 2720.42] And then in terms of just general things, I'm currently learning Spanish and that's pretty exciting.
[2720.70 → 2722.04] But also like frustrating.
[2722.64 → 2725.36] Exciting because it's like a different part of my brain.
[2725.74 → 2731.60] Because I don't think, I think learning languages is, to me, it seems different from learning a programming language.
[2732.02 → 2734.18] Even though it sounds like it should be the same.
[2734.80 → 2740.98] But learning a language is like very hard and to me very frustrating because half the time my brain works.
[2740.98 → 2744.44] It's like it refuses to like to learn things.
[2745.06 → 2750.76] And I find it so useful to just like get into a beginner's mindset so much.
[2750.90 → 2758.72] Because especially when I'm programming, I like, you know, if you've done this for a while, you have your assumptions of how things should be.
[2759.14 → 2761.92] And how things should be worded, how to teach someone and so on.
[2762.08 → 2765.32] So you assume someone has knowledge that's obvious to you.
[2765.32 → 2771.90] And so like learning a language kind of takes me out of that frame because I'm like, oh wait, I have no frame of reference.
[2772.78 → 2780.68] Because like if you're like me, I know like a couple of languages, but I never went down in the weeds with grammar.
[2781.50 → 2787.04] And so trying to learn grammar and a new language at the same time.
[2787.08 → 2789.24] Because a lot of the times they're like, do you know how this works in English?
[2789.24 → 2795.02] It's based on like this subjunctive grammar, and you're like, I don't know what subjunctive is.
[2795.22 → 2800.96] And then you kind of have to like figure out like, oh, okay, in English, like this is the rule and then translate that into a new.
[2801.08 → 2805.72] So like that learning process has been fascinating, and I've learned a lot about myself.
[2806.00 → 2811.36] It can be hard when you hit a wall and just like wanting to give up immediately.
[2811.36 → 2816.60] Because you're vulnerable, like all of your, I don't know, alarm bells go off.
[2816.76 → 2819.66] When you're like learning something, and you don't know something, you automatically shut down.
[2819.78 → 2821.10] I think that's pretty normal.
[2822.18 → 2833.28] And so like trying to get past that, I think is like a great exercise in just like learning about how I deal with things, how I learn and being better about that, which is neat.
[2833.66 → 2834.40] I'm also learning.
[2834.56 → 2834.76] Yeah.
[2834.80 → 2835.68] I'm also learning Spanish.
[2835.80 → 2836.20] Nice.
[2836.70 → 2838.60] And yeah, it's a lot of fun.
[2838.74 → 2841.04] I'm learning it alongside my almost three-year-old.
[2841.04 → 2848.08] But it's much harder for me, I think, because I'm constantly, my wife is fluent in Spanish, and I'm constantly asking, why is it like this?
[2848.16 → 2851.70] Why is this male and this is female, like ending with O and A?
[2852.18 → 2853.90] And my three-year-old doesn't care.
[2853.98 → 2854.32] Yes.
[2854.52 → 2856.30] And is just kind of going along with it.
[2856.36 → 2859.72] And native, if you speak a language natively, you don't think about those rules.
[2859.80 → 2864.26] So like if you talk to someone, and you're like, hey, you speak Spanish, like why is it this way?
[2864.26 → 2865.96] And they'll be like, because it's that way.
[2866.52 → 2866.88] Right.
[2867.04 → 2868.10] And you're like, why?
[2868.10 → 2871.36] And it's also annoying because you speak like a child.
[2871.54 → 2875.56] Like I currently speak like a child when I speak Spanish, and it's really frustrating.
[2876.06 → 2877.92] I'm just like, I'm actually like intelligent.
[2878.56 → 2885.62] I just speak like a person who doesn't know much and hasn't lived very long.
[2886.00 → 2886.64] But yeah.
[2886.96 → 2892.56] My neighbours speak Spanish, and they speak, they have two kids and they're very fluent.
[2892.56 → 2896.84] And I kind of feel judged every time I try to speak.
[2896.94 → 2899.10] I'm just like, it's fun.
[2899.48 → 2900.04] That's really great.
[2900.12 → 2904.28] I really like the point that you made about just sort of learning a new language and getting
[2904.28 → 2909.46] out of your comfort zone to sort of question your, I don't know, your preconceived notions
[2909.46 → 2911.08] about things and how they should work.
[2911.42 → 2918.92] I feel like just being a parent, I feel like does a lot of that for me because you're sort
[2918.92 → 2925.76] of seeing your child learn something new for the first time, and they have sort of no rules
[2925.76 → 2931.28] or sort of, I don't know, biases attached to them already.
[2931.46 → 2936.28] And so they're learning something from scratch, and you get to see them learn something from
[2936.28 → 2936.66] scratch.
[2936.78 → 2942.84] And it really, I don't know, it takes me out of that sort of comfort zone, or I already know
[2942.84 → 2943.68] how everything works.
[2943.84 → 2947.12] So all of those biases established with that.
[2947.78 → 2949.50] Yeah, that's, that's totally true.
[2949.62 → 2955.56] I still think it's really fascinating that humans have a short gestation cycle and in
[2955.56 → 2961.60] general, the baby, like baby humans are completely useless compared to most mammals.
[2961.66 → 2966.50] Like I was at the Smithsonian recently because they have different exhibits, and I was walking
[2966.50 → 2967.08] through them.
[2967.28 → 2972.24] And one of the curators was just like, yeah, human babies are just really like, if you put
[2972.24 → 2976.78] a bottle of milk and a baby, like the baby will die because it wouldn't know to like
[2976.78 → 2977.92] drink the milk.
[2978.64 → 2983.30] So yeah, it makes me think a lot about like humans and our species.
[2983.68 → 2984.62] Bottles are complicated.
[2985.30 → 2989.38] Human babies do, do know how to drink milk via other means.
[2989.38 → 2995.02] But still like the entire, at least the entire first year is just this, this child, they went
[2995.02 → 2997.88] to hurt themselves and your job is to prevent them from doing that.
[2998.00 → 2998.52] That's true.
[2998.52 → 2999.08] Yeah.
[2999.26 → 3005.04] So if it's, if anything, I totally understand the like trying to learn, relearn things that
[3005.04 → 3007.62] you think are obvious because a child doesn't know it.
[3008.02 → 3008.14] Yeah.
[3008.14 → 3010.16] I never thought about that, but that's, that's a good point.
[3010.64 → 3010.76] Yeah.
[3010.78 → 3017.36] I kind of wonder how much of that sort of affected just like how I build software too, because
[3017.36 → 3022.72] you're like, I saw my daughter learn something, learn all these things for the first time.
[3022.72 → 3024.98] And now my son's learning all these things for the first time.
[3024.98 → 3030.46] And it sort of puts you in that more of like a friendly to beginners mindset.
[3030.96 → 3036.14] And how can I make this more user-friendly to someone that has like none of the knowledge
[3036.14 → 3038.08] that I may have accumulated over time.
[3038.82 → 3042.04] So some things that I'm pretty excited about are Eleventh.
[3042.78 → 3045.88] Just, I am excited to, to check that out.
[3045.90 → 3047.34] And I just wanted to tell you that.
[3047.34 → 3051.98] Uh, and I really get excited every time I get a new let's encrypt email about my certificate
[3051.98 → 3054.40] expiring and then me having to go figure out how to do that again.
[3054.56 → 3058.50] And I'm like, I should just rewrite everything and throw it on Netlify, right?
[3059.50 → 3061.66] And be done with this whole charade.
[3061.66 → 3067.88] Because I don't actually know how to manage a server as it is obvious by me having to shut down
[3067.88 → 3070.58] a Bitcoin miner that started up on mine at some point.
[3070.66 → 3071.18] Oh no.
[3072.24 → 3074.32] But yeah, so I'm excited to check that out.
[3074.32 → 3077.70] Uh, another thing is, uh, Neovim 0.4.
[3077.94 → 3080.44] Uh, I think that's the one that's going to introduce floating windows.
[3080.72 → 3086.58] Uh, I'm just really excited about that because it, uh, is going to add a whole new level of
[3086.58 → 3093.22] interactivity to Neovim and Vim in general, just like my workflow will, will get better
[3093.22 → 3093.82] with that.
[3093.88 → 3094.68] So I'm excited.
[3094.68 → 3100.20] And that's like just the ability to float windows around your text and, uh, show things
[3100.20 → 3100.38] there.
[3100.58 → 3100.86] So it's.
[3101.14 → 3104.28] Do you have to, uh, quit each window individually or?
[3104.68 → 3105.54] Uh, I don't think so.
[3105.58 → 3111.00] I think it can just pop up like, like for example, you know, you GUI users take this
[3111.00 → 3115.12] for granted, but like popping up completion stuff or documentation about something that
[3115.12 → 3116.42] you're, you're using.
[3116.82 → 3119.94] That was just a low brow Vim quitting joke.
[3120.02 → 3120.26] Sorry.
[3120.68 → 3121.12] Oh yeah.
[3121.26 → 3121.88] I got you.
[3123.80 → 3124.50] Good one.
[3124.70 → 3125.18] Nice one.
[3125.44 → 3126.88] It's so, it was so funny.
[3126.96 → 3128.02] I had to explain it.
[3128.18 → 3129.98] That's how, you know, a joke's hilarious.
[3130.26 → 3130.78] For sure.
[3130.78 → 3131.02] Yeah.
[3131.68 → 3134.34] It's like an ultimate dad, dad joke level.
[3134.64 → 3138.02] It takes a joke, and it makes it a dad joke when you have to explain it.
[3139.30 → 3140.02] I don't know.
[3140.18 → 3141.26] Anyway, go ahead, Nick.
[3141.32 → 3141.56] Sorry.
[3141.94 → 3142.22] Yeah.
[3142.30 → 3143.24] Uh, that's it.
[3143.24 → 3147.36] And then the, the other thing, uh, that I'm excited about now that I have to, to fill
[3147.36 → 3151.30] the void, uh, that was the disappointment of the Game of Thrones finale.
[3151.64 → 3158.08] Uh, I started watching Chernobyl on HBO and, uh, that got me excited to look into like how
[3158.08 → 3163.82] nuclear reactors actually work and, uh, how, like why that one failed and, uh, reading and
[3163.82 → 3166.22] watching stuff about, about that whole incident.
[3166.58 → 3170.00] Um, so my search history has been pretty interesting with that.
[3170.54 → 3174.72] Um, but yeah, it's, it's been really fun learning about all of that and learning about
[3174.72 → 3176.32] what happened and what could have happened.
[3176.36 → 3178.16] And, uh, and the show's pretty good too.
[3178.22 → 3179.06] So, yeah.
[3179.12 → 3180.58] So Zach, what are you excited about?
[3180.94 → 3185.10] Uh, we kind of talked, talked about this a little bit earlier, but I'm super excited
[3185.10 → 3189.74] about Indie Web, I don't know if the Indie Web dev or Indie Web camp that I went to a couple
[3189.74 → 3190.32] of weeks ago.
[3190.86 → 3195.48] Um, it's sort of all around having your own website and owning your content and not letting
[3195.48 → 3202.16] sort of social media companies dictate who sees what and when, um, sort of rising above
[3202.16 → 3205.96] the algorithms that try to dominate our social media existence.
[3206.30 → 3211.50] So yeah, I'm super excited about sort of Indie Web stuff like web mentions and putting
[3211.50 → 3214.84] your own likes and retweets and all this stuff on your own content.
[3214.84 → 3216.50] So yeah, I don't know.
[3216.64 → 3222.56] I'm really, I really feel like at home in that community when I went to that Indie Web camp
[3222.56 → 3224.40] a couple of weeks ago.
[3224.50 → 3225.98] That was just really cool to see.
[3226.22 → 3229.30] And the other thing I guess is, is overlap with what Divya said.
[3229.34 → 3231.06] I want to try out Svelte.
[3231.30 → 3236.80] I think it's a really cool, the sort of like compiler approach that they're taking to JavaScript
[3236.80 → 3242.56] code, uh, rather than sort of having a giant deliverable, like a library deliverable that
[3242.56 → 3243.94] they serve to a client.
[3244.36 → 3250.28] Uh, they sort of only serve up the JavaScript that's actually used by the page, sort of,
[3250.28 → 3253.36] uh, a more like compiler based method.
[3253.94 → 3257.60] Uh, so for that reason, yeah, I'm kind of super excited for Svelte.
[3257.60 → 3263.84] And I would actually really like to see the crossover between, if there is any crossover
[3263.84 → 3269.06] between Svelte and Eleventh, maybe we can get Eleventh to compile Svelte templates as well.
[3269.36 → 3270.78] Would be really cool to see.
[3271.30 → 3277.22] And then, yeah, just, I guess all the movement around serverless and Netlify is, uh, really
[3277.22 → 3277.82] cool to see.
[3277.90 → 3283.30] Just getting more people, uh, having their own websites and owning their own content just
[3283.30 → 3287.32] to sort of circle back to the Indie Web stuff I talked about earlier.
[3287.94 → 3291.92] Yeah, just really excited to see more and more people making their own websites, having
[3291.92 → 3298.12] their own blogs and, uh, controlling their existence instead of letting social media companies
[3298.12 → 3299.34] control that for us.
[3299.46 → 3301.34] So yeah, I'm very excited about that.
[3301.74 → 3301.82] Yeah.
[3301.92 → 3305.92] The Jam stack is really fascinating, and I'm excited about that.
[3306.10 → 3310.78] And, and related to algorithms running your lives, I think this has been a recommendation
[3310.78 → 3316.38] on this, on the show before, but, uh, the, the book Weapons of Math Destruction, uh, I'm
[3316.38 → 3318.54] about three fourths of the way through that.
[3318.60 → 3319.30] It's perfect.
[3319.44 → 3319.60] Yeah.
[3319.64 → 3320.30] I read that.
[3320.38 → 3325.70] It's, it's really, really well written, and it's very accessible to, for someone.
[3325.82 → 3330.08] I think the author is like incredibly accomplished, and it's like a mathematician.
[3330.60 → 3332.18] I was able to understand it.
[3332.48 → 3336.64] So it was, it was just like a perfect breakdown of everything.
[3336.88 → 3337.10] Yeah.
[3337.62 → 3337.96] Yeah.
[3338.82 → 3339.70] It's terrifying too.
[3339.70 → 3340.14] Yeah.
[3340.14 → 3340.54] Yeah.
[3340.80 → 3342.40] It was like, I was like, Oh my God.
[3342.70 → 3342.82] Cool.
[3342.94 → 3346.74] Well, thanks so much, Zach, for coming on and talking to us today about fonts and about
[3346.74 → 3347.26] Eleventh.
[3347.66 → 3353.36] And, uh, where can people follow you on these web mentions or indie web places?
[3353.76 → 3354.04] Yeah.
[3354.12 → 3357.88] So Zachley.com Z-A-C-H-L-E-A-T.com.
[3358.54 → 3363.58] Uh, it's just the first four letters of my first name and then the first four letters of
[3363.58 → 3364.28] my last name.
[3364.48 → 3366.88] And then, uh, you can find my Twitter.
[3366.88 → 3369.32] It's like the same except the .com.
[3369.48 → 3369.88] Oakley.
[3370.08 → 3370.74] That's really cool.
[3371.10 → 3371.90] I do the same thing.
[3371.94 → 3374.60] The first four of my first and last name, but that's everything.
[3374.92 → 3375.02] So.
[3376.02 → 3378.20] It works out more conveniently for you.
[3379.20 → 3380.06] A little bit.
[3380.36 → 3380.88] It does.
[3381.54 → 3382.62] Uh, yeah, I think that's it.
[3382.68 → 3390.02] There's a if you want to check out Eleventh, it's a one, one T Y dot I O or one, one T Y dot
[3390.02 → 3390.80] dev.
[3391.04 → 3395.44] We're migrating domains for political reasons, but yeah.
[3395.60 → 3395.96] So.
[3396.48 → 3396.84] Cool.
[3397.24 → 3397.48] Yeah.
[3397.62 → 3397.96] Awesome.
[3398.10 → 3398.28] Yeah.
[3398.28 → 3399.10] Thanks for having me on.
[3399.50 → 3401.50] This was a really cool to talk about Eleventh.
[3401.58 → 3405.52] I haven't been like on a podcast or even at a conference to talk about Eleventh yet.
[3405.52 → 3407.78] So it was really kind of neat to talk about it.
[3407.78 → 3408.34] Yeah.
[3408.72 → 3415.66] I'm really excited about, really excited to play with it and to see like if I can, I don't
[3415.66 → 3415.80] know.
[3416.04 → 3420.36] I'm wondering if I can like to do some kind of like emulating or something with like Dojo,
[3420.82 → 3421.70] having Dojo output.
[3421.92 → 3422.38] Oh yeah.
[3422.40 → 3425.44] Are there any Dojo static site generators out there or no?
[3425.58 → 3427.20] We're working on some build time rendering stuff.
[3427.26 → 3429.52] It's not in its own project yet.
[3429.52 → 3436.02] Uh, but the, the new Dojo site, uh, is all built with Dojo and then just rendered to regular
[3436.02 → 3436.40] HTML.
[3436.76 → 3437.28] Very cool.
[3437.28 → 3437.72] Yeah.
[3437.78 → 3442.96] Let me know how that works or if it doesn't, maybe we can figure something out.
[3443.64 → 3450.72] I was just, um, it's funny cause yesterday someone reached out about like Elixir templates
[3450.72 → 3455.96] not working on Netlify, and I was like, I have no idea how Elixir templates anyway.
[3456.62 → 3456.90] Yeah.
[3456.90 → 3458.42] I haven't heard of that one before.
[3458.76 → 3463.64] I don't actually know a lot of Elixir people who use static site generators, but apparently
[3463.64 → 3469.26] they have a static site generator or a way of like building stuff, but they have like a
[3469.26 → 3472.56] separate dependency system I think called Hex or something, whatever.
[3472.90 → 3477.44] I don't, clearly don't know anything about Elixir, but yeah, I guess that's not, yeah,
[3477.44 → 3480.64] it's not popular enough for that to be a use case, but.
[3480.98 → 3481.16] Yeah.
[3481.16 → 3482.10] I've never heard of this.
[3482.66 → 3483.78] What language is it?
[3484.28 → 3485.12] Like Erlang.
[3485.60 → 3486.42] Oh, Erlang.
[3486.52 → 3486.72] Okay.
[3487.10 → 3487.26] Yeah.
[3487.26 → 3489.68] I mean, we're, we're kind of like, I don't know.
[3489.68 → 3492.56] We only use stuff that's available in node.
[3493.44 → 3494.22] So if there is.
[3494.36 → 3494.88] Yeah, exactly.
[3495.20 → 3500.24] Cause if it's something else you have like different dependency system, and then you have
[3500.24 → 3504.80] to figure out, I haven't, I don't even know which thought or like, yeah.
[3504.96 → 3507.08] Or if you wanted to use like Python, I don't know.
[3507.48 → 3507.98] That's weird.
[3508.62 → 3509.84] Well, I wish you luck.
[3509.84 → 3510.40] Yeah.
[3513.58 → 3513.98] Yeah.
[3513.98 → 3521.12] I, I know people who like use, um, template, like, because you can do, uh, templates using
[3521.12 → 3525.08] Django, and it's always, I'm just like, why?
[3525.50 → 3526.56] It's horrible.
[3527.00 → 3527.24] Yeah.
[3527.28 → 3529.24] I think Django is still pretty popular, isn't it?
[3529.26 → 3529.56] Or no.
[3529.76 → 3530.72] Django is really popular.
[3530.86 → 3531.08] Yeah.
[3531.40 → 3536.78] The best use case I've had for that is using Django as like a REST API.
[3536.78 → 3541.30] So like you'd build your backend and Django and then your front end is like whatever,
[3542.04 → 3543.16] whatever you want to use.
[3543.26 → 3546.60] And then you could still access Django through like an endpoint.
[3547.12 → 3549.96] So Django is just exposing like endpoints.
[3550.16 → 3550.40] Yeah.
[3550.44 → 3553.08] Kind of like the, like the WordPress API or whatever.
[3554.00 → 3554.44] Exactly.
[3554.64 → 3554.94] Yeah.
[3555.00 → 3558.18] Which I think is like, I guess, jams tacky.
[3559.20 → 3561.68] I'm more of an am stack person myself.
[3562.14 → 3562.42] Yeah.
[3562.86 → 3564.14] Oh, we didn't get to talk about amp.
[3564.62 → 3565.64] Amp stack.
[3565.64 → 3565.72] Amp stack.
[3566.14 → 3566.92] Thank God.
[3567.04 → 3568.50] It's like a huge slide on amp.
[3568.68 → 3569.08] What?
[3569.48 → 3570.94] I think it was, was it Jeremy Keith?
[3571.00 → 3571.90] This is totally separate.
[3572.20 → 3575.94] It's funny cause Jeremy Keith calls it, no, what does he call it?
[3576.14 → 3576.62] Madge.
[3576.82 → 3578.02] What's a Madge stack?
[3578.22 → 3580.62] It's like jam stack, but put backwards.
[3580.78 → 3582.30] Oh, because he wants markup first.
[3582.44 → 3582.54] Yeah.
[3582.86 → 3583.86] Markup first.
[3584.34 → 3584.60] Yeah.
[3584.78 → 3584.94] Yeah.
[3584.94 → 3585.52] I could see that.
[3585.68 → 3586.60] I'm on board with that.
[3587.06 → 3590.16] That's even more awkward to say than jam stack, but.
[3590.48 → 3591.34] Yeah, it's true.
[3591.70 → 3591.90] Yeah.
[3591.90 → 3595.10] I've been, uh, there's been a lot of amp stuff flying around this week.
[3595.10 → 3597.30] Is there anything new that came out from amp?
[3597.54 → 3599.90] I don't know if it's anything new specifically.
[3600.16 → 3604.18] I think that, I don't know, just more and more people are, I've been talking about it.
[3604.64 → 3606.44] That's another round of amp hatred.
[3606.94 → 3613.02] It's been kind of interesting to see just how much overlap there is between like the sort
[3613.02 → 3617.88] of people that are anti-amp and people that attend Scoff EU.
[3618.40 → 3620.34] So are you for or against amp?
[3620.54 → 3622.12] I'm fine with amp the framework.
[3622.12 → 3627.72] I think most people that are anti-amp would say that they're against the amp carousel.
[3628.24 → 3631.66] So like prioritization of amp results and search results.
[3631.66 → 3637.20] Cause in terms of just like making it optimized for mobile and basically that what the amp
[3637.20 → 3638.80] framework does is interesting.
[3639.20 → 3639.34] Yeah.
[3639.36 → 3645.12] I mean, that's just a standard, like your standard JavaScript UI framework or whatever.
[3645.44 → 3647.28] I mean, it's, I don't think they'd call it a job.
[3647.38 → 3651.96] They call it like an HTML framework because it isn't technically, you're not writing in
[3651.96 → 3653.80] JavaScript, but it's still running JavaScript.
[3653.80 → 3654.86] So it's the same.
[3655.22 → 3656.64] So yeah, I don't know.
[3656.64 → 3661.22] I wish, I wish they would sort of fix the problems that they had, like there's been a
[3661.22 → 3665.34] ton of like feedback about it, and it doesn't seem like there's been a ton of progress made.
[3665.64 → 3668.80] Just show up to all the amp roadshows or conferences or whatever.
[3669.42 → 3672.82] Make my whole existence to be just the amp hater.
[3673.08 → 3674.06] You could be one of those.
[3674.20 → 3679.20] Like I, I actually heard about this where there are people who travel to like, so if you're
[3679.20 → 3683.46] like for or against a specific, like, I don't know, it's basically like being a lobbyist.
[3683.46 → 3688.58] So if you find like, oh, there's like legislation like going on in specific places that are,
[3688.58 → 3693.12] is going to change a law that you care about, then you would just like travel and like protest.
[3693.72 → 3695.06] Did you hear about this on Facebook?
[3695.54 → 3695.94] No.
[3696.14 → 3698.66] Is this the paid protester thing that is?
[3699.56 → 3701.08] No, I actually heard about it.
[3701.16 → 3701.68] What was it?
[3702.12 → 3709.48] There's like a moving company, moving, like this moving app thing in Chicago that I use.
[3710.16 → 3712.38] And I forget what it's called.
[3712.38 → 3714.88] It's like hip and cool, whatever the kids use.
[3715.64 → 3717.44] And I used it once.
[3717.44 → 3724.10] And the driver was, I learned as a also like the whole situation was kind of weird.
[3724.10 → 3731.06] But anyway, so the driver of the truck was anti-circumcision.
[3731.54 → 3732.68] I learned.
[3733.04 → 3734.94] Also conspiracy theorist.
[3734.94 → 3739.10] And he showed me all of his like banners that he had created.
[3739.50 → 3739.94] Yeah.
[3740.00 → 3744.60] I had a very similar encounter with a repair person that came over to my house and started
[3744.60 → 3749.48] talking to me about all these conspiracy theories for, yeah, it was a disaster.
[3749.94 → 3755.74] Sometimes it is fun to just like, it's like, oh, tell, tell me more just purely for like
[3755.74 → 3759.56] the story that you can tell at like parties.
[3759.72 → 3759.92] Yeah.
[3759.92 → 3760.48] Like these.
[3760.64 → 3760.88] Yeah.
[3761.24 → 3762.06] Jazz parties.
[3762.48 → 3763.16] Yeah, exactly.
[3763.48 → 3767.94] You're like, tell me more so I can tell how, tell other people how crazy this is.
[3768.22 → 3768.46] Yeah.
[3768.62 → 3770.80] There's no point saying that they're wrong.
[3770.88 → 3773.68] Because I'm like, that's not a fun discussion.
[3773.68 → 3776.44] Versus being like, oh, why do you think that?
[3776.48 → 3781.80] And then kind of just like eking out all the details and like the logical gaps.
[3782.12 → 3784.34] I've definitely done that in cab rides for sure.
[3784.80 → 3787.68] The cab driver starts talking, and you're like, oh really?
[3787.84 → 3788.96] Why, why is that?
[3789.30 → 3793.54] You just keep asking why and why and why and just see how much they can see how much crazy
[3793.54 → 3794.72] they'll reveal to you.
[3794.90 → 3799.32] And then you'll also get like recommendations on YouTube things you should watch.
[3799.54 → 3800.84] They're like, watch this.
[3801.20 → 3802.16] It'll tell you.
[3802.16 → 3806.90] I think the one he was telling me about, he was like, oh, did you know that earth used
[3806.90 → 3810.26] to be an alien mining ground?
[3810.56 → 3814.90] And I was like, he was like, yeah, they found these like giant tree stumps.
[3814.98 → 3818.70] And it's, it's obvious that like, who cut them down?
[3818.82 → 3819.76] They're too big.
[3819.76 → 3821.34] And trees like, don't grow like that.
[3821.42 → 3822.62] So they must have at some point.
[3822.72 → 3824.70] And someone must have been around to cut them down.
[3824.78 → 3825.68] And I was like, whatever.
[3825.68 → 3826.12] Yeah.
[3826.34 → 3826.74] Yeah.
[3826.90 → 3830.98] I mean, for real, I think that there is a huge problem with this sort of algorithms
[3830.98 → 3835.90] sort of encouraging people to believe extreme things like this.
[3836.14 → 3842.86] I know on YouTube, if you watch like one thing, you can get recommended some pretty gnarly stuff.
[3842.86 → 3848.42] And then you go down a rabbit hole of like, oh, wait, I, I actually, I think there's a Netflix
[3848.42 → 3852.74] show called Flat Earth, like about Flat Earth.
[3853.70 → 3859.72] And like, it was a documentary where they just talk about Flat Earth theorists or people who
[3859.72 → 3861.02] believe in Flat Earth theory.
[3861.02 → 3865.92] And some of them were like people who are like, oh, yeah, I didn't believe in this.
[3866.10 → 3867.92] And then I watched a couple of YouTube videos.
[3867.92 → 3869.04] And I was like, you know what?
[3869.10 → 3870.10] This is so true.
[3870.68 → 3875.58] Yeah, it's a huge problem because you can't even really talk about it without, I
[3875.58 → 3877.24] don't know, spreading their message.
[3877.74 → 3883.22] I mean, you can't even like talk it down without giving them the network effects of talking about
[3883.22 → 3884.52] their messages.
[3884.52 → 3886.14] Like, yeah, it's terrible.
[3886.14 → 3892.24] Like I did a, I did just like a joke talk at Bar Camp a few years ago about Flat Earth
[3892.24 → 3893.90] and why Flat Partners exist.
[3894.36 → 3900.46] And I recorded the video and I decided not to even put it online just because during the
[3900.46 → 3905.24] talk, there was like people tweeting at me wanting the information that I was putting
[3905.24 → 3907.40] out because they were like real Flat Partners.
[3907.92 → 3909.12] That might have been my fault a little.
[3909.28 → 3911.24] I tagged them in a tweet, I think.
[3911.60 → 3915.18] Well, no, it's, I mean, I learned quite a bit just from that.
[3915.18 → 3921.60] Just like, even if you tell a joke about something, it can sort of platform these people into something
[3921.60 → 3922.78] that you don't want to spread.
[3923.60 → 3923.82] Yep.
[3923.92 → 3927.78] And then you become the like accidental spokesperson.
[3928.62 → 3933.10] Yeah, that's a real problem when you have, I mean, you have to be really responsible when
[3933.10 → 3936.84] when people sort of get like these big followings, what they even joke about.
[3937.06 → 3938.18] You have to be very careful.
[3938.80 → 3939.92] Yeah, it's a big responsibility.
[3940.52 → 3940.68] Cool.
[3940.92 → 3941.10] Yeah.
[3941.30 → 3942.68] Thanks again, both of you.
[3942.76 → 3943.22] It was a lot of fun.
[3943.22 → 3944.32] Thank you guys for having me.
[3945.18 → 3946.52] All right.
[3946.60 → 3948.42] Thank you for tuning in to JS Party this week.
[3948.54 → 3951.50] Tune in live on Thursdays at 1 p.m.
[3951.52 → 3951.90] U.S.
[3952.06 → 3954.58] Eastern at changelog.com slash live.
[3955.06 → 3957.58] Join the community and slack with us in real time during the shows.
[3957.84 → 3959.40] Head to changelog.com slash community.
[3960.00 → 3960.68] And do us a favour.
[3960.82 → 3962.00] Share this show with a friend.
[3962.28 → 3963.48] We're just going to have a podcast.
[3963.64 → 3965.28] Go into Overcast and favourite it.
[3965.76 → 3968.02] And thank you to Vastly, our bandwidth partner.
[3968.36 → 3969.86] Head to fastly.com to learn more.
[3970.26 → 3972.88] And we move fast to fix things around here at Changelog because of Rollbar.
[3972.88 → 3974.82] Check them out at rollbar.com.
[3975.06 → 3979.10] We're hosted on Leno cloud servers at the leno.com slash changelog.
[3979.18 → 3980.56] Check them out and support this show.
[3981.02 → 3982.98] Our music is produced by Break master Cylinder.
[3983.46 → 3986.44] And you can find more shows just like this at changelog.com.
[3986.64 → 3987.54] Thanks for tuning in.
[3987.80 → 3988.58] We'll see you next week.
