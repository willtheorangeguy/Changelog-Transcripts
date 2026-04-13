[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
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
[36.88 → 40.22] And all you got to do is go to Rollbar.com slash Changelog, sign up,
[40.60 → 41.84] integrate Rollbar into your app.
[41.92 → 45.92] And once you do that, they'll give you $100 to donate to open source.
[46.30 → 49.14] Once again, Rollbar.com slash Changelog.
[56.96 → 63.12] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[63.28 → 69.72] Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at Changelog.com slash live.
[69.72 → 74.84] Join the community and Slack with us in real time during the show at Changelog.com slash community.
[75.30 → 76.04] Follow us on Twitter.
[76.14 → 77.66] We're at JSPartyFM.
[77.78 → 79.14] And now on to the show.
[79.14 → 84.40] All right.
[84.72 → 85.98] Hello, party people.
[86.32 → 88.66] And welcome to another episode of JS Party,
[88.78 → 92.44] where we are every week throwing a party about JavaScript and the web.
[92.76 → 94.94] I am your host this week, K-Ball.
[95.18 → 97.96] And I am joined by two of our amazing regular panellists.
[98.12 → 99.34] One who is a new panellist.
[99.42 → 100.36] I'm super excited.
[100.62 → 103.62] I've loved all of her episodes so far, but I haven't been on one with her.
[103.72 → 104.42] So welcome.
[104.58 → 106.04] Thank you for joining me, Emma Whitaker.
[106.44 → 106.84] Yay.
[106.94 → 107.84] I'm so happy to be here.
[107.84 → 109.64] I am excited to chat more with you.
[109.92 → 110.12] Yeah.
[110.18 → 111.78] Did I butcher your last name, by the way?
[111.88 → 112.24] I'm sorry.
[112.46 → 113.22] I mean, it depends.
[113.30 → 115.20] Are we speaking it with an American accent?
[115.34 → 116.74] Are we trying out the German version?
[116.98 → 118.92] Because, you know, the American one.
[118.98 → 120.86] But if we're the German one, it's Reticent.
[121.06 → 121.42] Reticent.
[121.76 → 121.96] Okay.
[122.02 → 122.30] Yeah.
[122.58 → 122.84] All right.
[122.88 → 124.12] I will endeavour to do better.
[124.28 → 128.50] And then our other panellists today, Chris Miller, a.k.a. Bone skull.
[128.82 → 129.48] Chris, how's it going?
[129.88 → 130.22] Hi.
[130.46 → 131.46] It's just me.
[132.84 → 133.56] Just you.
[133.88 → 134.16] Yeah.
[134.32 → 135.12] It's just me.
[135.12 → 136.18] Just you.
[136.62 → 137.02] Okay.
[137.02 → 137.50] Hey.
[137.66 → 143.80] So today we are going to do a set of our fun recurring segments, starting off with a segment
[143.80 → 146.20] that got a lot of interest the last time we did it.
[146.42 → 149.72] Our fun Eli 5 or Explain It Like I'm 5 segment.
[149.86 → 153.94] Now, we can take Eli 5 to mean just explain it simply.
[154.24 → 156.90] Or even more fun, you could actually try to do it for a PAW Patrol.
[156.90 → 163.72] I think the last time around we did this, I used the PAW Patrol, which is a thing my five-year-old,
[163.92 → 165.60] now six-year-old, is really into.
[165.96 → 169.72] So you can use actual stuff from kids if you want to, but you can also just make it super
[169.72 → 169.98] simple.
[170.32 → 173.00] So I'm going to start off with my question, since then somebody else will talk.
[173.08 → 176.12] So my question is, explain it like I'm 5 node streams.
[176.12 → 181.18] In particular, like I've done Unix streams for a long time, but somehow when I've tried
[181.18 → 183.48] to tinker around with it in Node, it's always been confusing.
[184.00 → 187.08] Do you mean so like piping stuff in Bash?
[187.58 → 187.86] Yeah.
[188.14 → 188.36] Yeah.
[188.52 → 189.36] That feels normal.
[189.58 → 190.34] I know how that works.
[190.68 → 191.38] Streams in Node?
[191.64 → 193.12] I feel like I should know how that works.
[193.40 → 193.72] Yeah.
[193.88 → 195.46] I feel like it's a little different.
[195.80 → 199.66] I don't really know the guts of how piping works in a shell.
[199.98 → 201.56] So I'm going to take a crack at this.
[201.70 → 202.58] I must apologize.
[202.58 → 208.28] I have explained many things to a five-year-old and I don't think I'm actually any good at
[208.28 → 208.44] it.
[208.56 → 214.70] And, so please stop me if I say something that is in reference to something that you are
[214.70 → 214.98] into.
[215.18 → 216.68] So Node streams.
[216.88 → 221.58] So you can think of a stream kind of like a collection of data, sort of.
[221.78 → 229.90] You can think of it like an array, except not every item in the array is available at once.
[229.90 → 235.24] Maybe a better way to think of it is if you're familiar with an async iterator.
[235.64 → 237.74] So it's this collection of data.
[237.92 → 239.88] The data is not available at once.
[240.16 → 246.52] Typically, when you interact with a stream, you consume each item from that stream individually.
[247.02 → 253.38] So it also means that then that because they're not all available, not the entire data set that's
[253.38 → 255.48] in that stream is in memory at once.
[255.48 → 260.08] And this is great if you are working with very large data sets, especially.
[260.60 → 264.76] But, you know, the use cases for streams aren't limited to very large data sets, but they're
[264.76 → 266.12] very useful for them.
[266.48 → 271.82] So an example I remember, and it's kind of trivial in Python, if you're familiar with
[271.82 → 275.44] Python, there is a built-in function range.
[275.86 → 284.50] And so what that does is it essentially gives you a list of however many numbers, or what have
[284.50 → 285.50] you?
[285.50 → 289.92] And so you say range 10, you get a list with zero to nine or something like that in it.
[289.98 → 292.84] And there's another function called range.
[293.04 → 294.06] And it's different.
[294.28 → 296.70] It essentially doesn't hold the whole array in memory.
[296.92 → 303.24] And so you can say range 50 billion zillion, and Python will just go ahead and go through
[303.24 → 303.42] it.
[303.42 → 309.02] But if you said range, well, then we're going to fill up memory with this huge, huge array.
[309.02 → 316.50] And so it's kind of like if an array in JavaScript is working with a range operator, streams are
[316.50 → 317.34] more like range.
[317.68 → 320.14] So does that make sense so far?
[320.54 → 321.46] Yeah, I think so.
[321.78 → 321.98] Okay.
[322.02 → 326.28] So basically an array that is paged into memory piece at a time for me.
[326.30 → 326.76] Essentially.
[326.76 → 332.44] And so another feature of streams, and this is where this idea of piping comes in.
[332.60 → 334.08] So streams are composable.
[334.40 → 337.66] There are two basic types of streams.
[338.00 → 342.52] One of those is a readable stream, and the other one is a writeable stream.
[342.68 → 347.74] And a readable stream you can think of as a source, a writeable stream you can also think
[347.74 → 348.38] of as a sync.
[348.68 → 351.22] These are interfaces, essentially.
[351.22 → 357.24] So an example of a readable stream might be a process like standard in.
[357.46 → 363.40] So if you're in Node and you want to read some information from standard in, use deadline
[363.40 → 368.18] and whatever, and it's a readable stream, then you can pipe it to some output.
[368.40 → 372.76] And so readable streams have a method pipe, and you'll frequently see this.
[372.86 → 379.12] And maybe another good example is there's a function in the FS module, and that's create
[379.12 → 379.66] read stream.
[379.66 → 385.78] And so instead of calling, say, FS read file, and what that's going to do is it's going to
[385.78 → 388.14] read a file and load its contents into memory.
[388.38 → 391.66] You might want to call FS read, create read stream instead.
[392.10 → 396.08] And so this will give you a stream, and it won't load the whole file into memory and let
[396.08 → 397.42] you process it piece by piece.
[397.70 → 400.60] And so readable streams, again, you can pipe them to some output.
[400.90 → 402.62] A writeable stream, you cannot pipe.
[402.96 → 404.52] A writeable stream goes somewhere.
[404.90 → 409.18] A typical writeable stream is like process standard out or process standard error.
[409.18 → 415.74] So you can read a file with, say, FS create read stream, or maybe it's a text file or something.
[416.34 → 421.46] And because it's readable, you can pipe it to the write stream created by FS create write stream.
[421.82 → 425.40] And so with FS create write stream, you give a file name.
[426.10 → 430.46] And so basically you're reading the file and then writing it out into another file.
[430.66 → 431.84] You do that piece by piece.
[431.84 → 436.10] You can read the file, or you can pipe it to standard out, and it'll just dump the file
[436.10 → 437.32] contents to standard out.
[437.72 → 439.72] So there's readable and writeable.
[439.90 → 441.08] Does that make sense?
[441.54 → 442.74] You can pipe a readable stream.
[442.84 → 444.00] You cannot pipe a writeable stream.
[444.12 → 445.38] The writeable stream goes somewhere else.
[445.64 → 451.10] What makes them composable is that some streams can implement both interfaces.
[451.10 → 454.78] So these are typically transformed streams or duplex streams.
[455.00 → 456.18] There's a bit of a difference.
[456.32 → 461.44] The transformed stream I find myself working with quite often is where you take some sort
[461.44 → 465.18] of readable stream, and then you pipe it through this kind of middleman.
[465.44 → 467.90] And then that finally pipes out to the writeable stream.
[468.12 → 474.76] An example of that might be reading with FS create read stream and then piping it to lib.
[474.76 → 481.08] And so lib will let you like zip up a file or something like that or create a GZIP or whatever
[481.08 → 481.56] archive.
[481.72 → 487.06] And then you could pipe the result out from that to a writeable stream and write the file
[487.06 → 487.30] out.
[487.60 → 492.30] And so you can read a file and like zip it up and write it out without loading the whole
[492.30 → 493.92] file into memory, which is really cool.
[494.10 → 495.96] So that's kind of a transformed stream.
[496.06 → 498.80] A duplex stream I never really have tried to implement.
[499.04 → 501.60] It's essentially a stream that will go both ways.
[501.60 → 504.62] It works as a readable or writeable, but I don't know.
[504.62 → 506.24] It doesn't entirely make sense to me.
[506.30 → 507.18] Don't worry about it.
[507.26 → 510.38] So yeah, the entire data set is not in memory.
[510.66 → 514.96] A good example is something that I've written in the past where I needed to download some
[514.96 → 521.34] huge thing from some website in like maybe a big JSON file or text file and process it
[521.34 → 522.58] and then write it out to a file.
[522.86 → 527.06] Instead of going and fetching the file, I use like HTTP request.
[527.06 → 529.48] And so that will give you a readable stream.
[529.48 → 534.14] And then I could pipe that stream into maybe a transform stream that I implemented.
[534.14 → 536.82] And I don't know, process the data somehow.
[537.22 → 540.44] And then I can pipe that back out to whatever I need to write to.
[540.70 → 542.18] And that's kind of the idea of streams.
[542.52 → 543.84] Streams are all over Node.
[543.98 → 548.30] Many different modules have some sort of stream available in them.
[548.52 → 553.38] I mean, you can work in Node and never really touch streams, but they're perfect for
[553.38 → 559.78] this kind of idea of processing large data sets and kind of composing things.
[559.78 → 560.14] Cool.
[560.72 → 563.06] Seems like a topic we could go a whole segment on.
[563.34 → 563.82] But awesome.
[563.94 → 564.40] Thanks, Chris.
[564.64 → 566.06] Do you want to ask your question next?
[566.14 → 567.80] And then maybe Emma can tackle that?
[568.00 → 570.42] So my question would be, I don't know.
[570.56 → 573.16] I've been trying to get my head around CSS Flex box.
[573.38 → 577.50] Can somebody please explain CSS Flex box to me?
[577.86 → 578.94] Yeah, absolutely.
[579.28 → 584.42] So prior to Flex box and Grid, if you wanted to lay things out on a page, you had to use
[584.42 → 586.40] floats or even worse tables.
[586.40 → 588.00] And things just became a nightmare.
[588.30 → 593.76] Like, I swear I couldn't lay things out in EU basically the first year of my career.
[594.22 → 600.24] So Flex box is now a CSS spec that allows you to lay elements out along one axis.
[600.42 → 602.90] And if I'm explaining this to a five-year-old, they're probably sitting there like, what the
[602.90 → 603.04] heck?
[603.40 → 608.64] So let's say you have, hmm, what's something that would be relevant to a five-year-old?
[608.84 → 609.26] I don't know.
[609.38 → 611.34] Let's say like they have like five cars, right?
[611.34 → 612.78] And they're kind of like all over the floor.
[612.98 → 618.24] And we want to get them all in one horizontal line like they would be if they were going
[618.24 → 619.72] through a drive-through, for example.
[620.16 → 623.20] What you can do is, let's say they're in a container, which is the road.
[623.32 → 627.42] So we set a display of Flex on like this road element.
[627.78 → 634.48] And everything inside of that, all the individual cars, would then be in line along the road.
[634.62 → 635.80] So they're all in a line.
[635.80 → 639.32] And you can lay them out at the front of the road or the back of the road or in the middle.
[639.86 → 641.44] And it makes it really easy to do that.
[641.52 → 645.72] You could even have one car go to the front of the road and the rest stay at the back.
[645.82 → 650.22] But by setting display of Flex on this parent container, it makes it really easy to lay
[650.22 → 651.70] things out along one axis.
[652.18 → 656.92] When you're talking about a two-dimensional axis, that's where things get a little trickier.
[657.12 → 660.96] And so CSS Grid enables you to create these really complex layouts.
[660.96 → 667.54] So let's say we have like a website, and it has a sidebar with a bunch of like navigation items.
[667.54 → 671.70] And then let's say we have a header that spans the whole width of the top of the page.
[671.86 → 673.56] And maybe we've also got a footer.
[674.06 → 676.60] So this is the kind of two-dimensional layout that we're talking here.
[676.74 → 678.68] And it's a little too complex for Flex box.
[678.80 → 681.78] So you could use Flex box, but you'll have a lot of wrapper DIVS.
[681.84 → 684.54] And that can get kind of like semantic and messy.
[684.94 → 689.14] So at this point, you can create a grid of two-dimensional elements.
[689.14 → 691.04] And you can set different grid areas.
[691.18 → 694.16] So you can say, you know, I want this to be five columns wide.
[694.16 → 697.62] And I want the first two columns to be for the aside.
[698.02 → 700.48] And you can just snap elements into a place like this.
[700.56 → 701.48] It's really quite easy.
[701.58 → 704.84] But I think the misconception is that you have to use either or.
[705.04 → 706.62] And that's not true, right?
[706.66 → 708.44] So we can use Flex box and Grid together.
[708.58 → 711.18] It's kind of about identifying the correct use cases.
[711.48 → 715.74] So if you want to lay things out in a line, for example, Flex box is the right tool.
[715.74 → 720.76] And if you need to lay things out, for lack of a better term, in a grid, that's where CSS Grid can come in handy.
[721.32 → 725.80] So I was running into problems because all I had was Flex box.
[726.00 → 728.22] And I was trying to make like a table, right?
[728.50 → 732.34] And so I was like, is this the right tool for what I'm trying to do?
[732.62 → 734.72] And I think that sounds like the answer is no.
[735.24 → 735.60] Yeah.
[735.60 → 737.76] I mean, you can use it.
[737.82 → 740.24] It just won't necessarily match up perfectly.
[740.24 → 747.36] Like you can say Flex Wrap and you can set widths on the children inside, but it's just not the most efficient solution.
[747.78 → 757.92] So it's kind of one of those things if you want to make a table, you know, without using a table element, you would just create this grid and maybe have some rows in there and use Flex box within the rows.
[757.92 → 772.00] Yeah. One of the distinctions that I've heard that I really liked was that Flex box, from the word Flex, it's about like distributing things in space in a way that you want them to sort of be controlled by what's in the content or what's in the elements itself.
[772.12 → 778.60] Right. Like the, the elements sort of figure out together how to distribute themselves, whereas grid is much more command and control.
[778.60 → 787.26] So if you're trying to say, I want these things to be in columns, or I want these things to take exactly the space, grid is much more intended for that.
[787.40 → 793.26] And you can kind of, yeah, as you say, shoehorn Flex box into more exact things, but that's not what it's intended for really.
[793.34 → 794.98] And that's not what it's best at.
[795.44 → 798.52] This has been very, very informative, even just this little bit.
[798.76 → 799.22] Thank you.
[799.34 → 802.98] I wrote a blog post on this about when you should use grid versus Flex box.
[803.06 → 804.74] And I walked through a few examples.
[804.74 → 814.26] It's kind of one of those where when you see it, the more you practice, you'll be able to just look at UI or look at a design and just kind of in your mind chunk, whether it should be Flex box or grid or both.
[814.42 → 821.22] So you should definitely check out that post if you would like to learn more, because I think learning when to use each is definitely a superpower.
[821.78 → 824.18] Awesome. And we'll include a link to that in the show notes.
[824.58 → 828.86] Great. Emma, do you want to ask your question? And I'll try to answer it real quick in the time we have left for this segment.
[829.26 → 833.20] Yeah. Hmm. I don't know what kind of question you want to answer. Hmm.
[833.20 → 834.74] Or a concept to explain.
[835.02 → 844.60] Yeah. So we just talked about Flex box and grid, but sometimes I have problems when I'm writing like my CSS and my properties aren't showing up or my styles aren't being applied appropriately.
[844.94 → 847.50] So could you tell me a little bit more about specificity?
[847.86 → 852.28] All right. Specificity. And I'm going to try to explain it like you're five. So I'm going to go back to metaphors.
[852.38 → 856.62] So my kids are no longer is into PAW Patrol. The latest and greatest thing is Ninja go.
[856.62 → 868.90] Now, Ninja go is a combination word for ninja Legos. They're these ninja characters made up of Legos, and they all have different abilities, but they're kind of we say they're kind of all over the place.
[869.08 → 873.66] The story writing is thin. And so these characters and sometimes one's doing better, sometimes the other.
[873.86 → 876.58] And oftentimes whichever one arrives last is going to hit it.
[876.58 → 882.46] So if we start coming back to CSS specificity, thinking about it as Ninja go and how Ninja go are going to attack problems.
[883.04 → 889.84] CSS specificity, before we go into the metaphor, is essentially a set of algorithms or rules for how styles choose to get applied.
[890.14 → 892.82] And there are two core elements of this.
[892.88 → 898.22] So there's how strong is the thing that we're applying, and there's what order is it that we apply it in.
[898.32 → 901.26] So in the Ninja go world, I might hit something with a punch.
[901.26 → 904.42] That's kind of weak. I might also hit it with a punch and with a weapon.
[904.60 → 907.46] OK, that's a little bit stronger. It's more likely to hit.
[907.82 → 911.26] In CSS, that might be an element selector is the weakest specificity.
[912.00 → 914.20] That might be my punch. I want to go a little bit stronger.
[914.30 → 916.44] I'm going to select based on a class. That's a weapon.
[916.90 → 923.16] So if I've got two different things, the one with the weapon is going to take precedence over the one with just the punch.
[923.16 → 926.58] If I put a punch and a weapon together, ooh, that's going to be both of them.
[926.94 → 929.60] And there's kind of this whole range of different pieces.
[929.60 → 936.86] So in specificity, you have an element, you have a class selector, you have ID selectors, various things.
[937.14 → 942.10] Each one of those is a little bit stronger, meaning if you just have two of them head to head,
[942.48 → 945.14] the stronger one is going to take precedence.
[945.18 → 948.68] And if you combine them, it has the combined strength of the two.
[948.68 → 952.50] And you can add multiple weapons, multiple classes or multiple IDs.
[952.64 → 954.34] The more you select against, the stronger it is.
[954.66 → 958.94] The second piece of this is the fact that it's not necessarily that well thought ahead.
[958.94 → 960.68] So the last one to hit win, right?
[960.74 → 965.30] So if I punch it and the Spinal or Ninjutsu characters are, they've got these ninjas.
[965.48 → 970.36] They have Jay and Cole, and they are all stupid, and they all have their own neuroses, and they're all trying to hit things.
[970.68 → 975.22] Whichever one hits last, if they're hitting the same amount of difficulty, that's the one that's going to take precedent.
[975.80 → 979.44] So the stronger the hit, the stronger whatever it is, it will take precedence.
[979.44 → 987.82] But if you have two things that are the same strength, whatever hits last, which in CSS is literally the order you write the code when it is landing in the file, which everyone hits last will apply.
[988.22 → 996.68] And the final Spinal reference is when all is lost, and they just have to blow something up, they go to what they call Spirits, which is basically they turn into whirlwinds and spin around.
[996.86 → 998.16] And that is the important flag.
[998.16 → 1007.68] So if you have some property that just has to happen, no matter what, you can throw everything in the air, throw your specificity rules out of the way, write important, and that's Spirits.
[1007.94 → 1008.58] It just wins.
[1008.88 → 1013.72] It's not very advisable, either in Ninja go or in CSS, but that's your breakthrough.
[1014.06 → 1014.74] I loved that.
[1014.84 → 1015.78] That was a great analogy.
[1016.30 → 1016.54] Okay.
[1016.68 → 1018.78] And with that, let us close up this segment.
[1018.94 → 1025.96] So we're going to take a short break, and we will be back shortly talking about stories of the week in the JavaScript and frontend space.
[1025.96 → 1040.12] This episode is brought to you by Linde, our cloud server of choice, and we're excited to share they've recently launched dedicated CPU instances.
[1040.12 → 1054.00] If you have build boxes, CI, CD, video encoding, machine learning, game servers, databases, data mining, or application servers that need to be full-duty, 100% CPU all day, every day,
[1054.00 → 1057.04] then check out Linde's dedicated CPU instances.
[1057.64 → 1061.68] These instances are fully dedicated and shared with no one else.
[1061.76 → 1065.70] There's no CPU steal or competing for these resources with other Li nodes.
[1065.96 → 1069.64] Pricing is very competitive and starts out at $30 a month.
[1069.98 → 1073.84] Learn more and get started at linode.com slash changelog.
[1073.96 → 1076.04] Again, linode.com slash changelog.
[1076.04 → 1088.80] All right.
[1089.18 → 1091.34] Welcome back, JS Party people.
[1091.64 → 1095.10] And let us roll into a segment we call Story of the Week.
[1095.10 → 1106.92] So this is each panellist is going to bring a story that they found particularly interesting or salient this week and maybe talk a little bit about what it is, why it was interesting, and any impact it has on the ecosystem.
[1107.16 → 1110.50] So let's go reverse order from what we did last time.
[1110.54 → 1111.46] So let's start out with Emma.
[1111.74 → 1112.02] Awesome.
[1112.20 → 1114.84] So full transparency, this is not a news article.
[1115.04 → 1117.76] However, I find this to be extremely informative and relevant.
[1117.76 → 1125.40] So my story of this week is called Why and How to Use and When to Use Semantic HTML in ARIA.
[1125.78 → 1133.50] And recently, I've been seeing a lot more about accessibility coming up, which is really great because we should all be aware of how to write accessible applications.
[1134.06 → 1137.00] And there were some really key points that I pulled out of this.
[1137.04 → 1140.76] So for reference, this is on CSS Tricks, so one of my favourite sites.
[1141.18 → 1143.70] And so what are the things that I pulled out of this?
[1143.70 → 1155.94] So ARIA provides additional contextual information for your web pages, and they allow people who are blind or have other visual impairments to be able to use your site without trying to discern what is what.
[1156.04 → 1165.16] So if we have a full page of DIVS, like they can't navigate this page versus if we have like a main element, and then we've got a form with an input, this is a lot more semantic.
[1165.16 → 1167.90] And so here's a practical example.
[1168.36 → 1175.62] I've seen people use DIVS, and they've set specific properties on these to style them like as a number, or they use the wrong thing.
[1175.68 → 1180.74] But if I'm trying to input a telephone number, what you should do theoretically is have an input with a type of telephone number.
[1180.86 → 1189.10] And that gives the users the actual like keypad to be able to type in a phone number as opposed to having to use like the full keyboard to type in a number, which is kind of annoying on mobile.
[1189.30 → 1193.36] So it's better for screen readers, and it creates a hierarchy of information on your web page.
[1193.36 → 1201.22] And what I see a lot of is that people try to slap ARIA on as kind of like a band-aid on their non-semantic HTML.
[1201.72 → 1207.16] So like you'll see DIVS with a role equal to checkbox and ARIA checked attribute that they're updating.
[1207.40 → 1208.66] And this is kind of backwards, right?
[1208.74 → 1211.10] ARIA shouldn't be used as a band-aid for things.
[1211.28 → 1214.78] We should definitely be using the semantic HTML where applicable.
[1215.04 → 1219.76] So instead of using this DIV with these ARIA attributes, we should be using an input with a type of checkbox.
[1219.76 → 1223.38] And it's all this stuff baked in so we don't have to worry about updating those.
[1223.70 → 1225.66] So I found this to be quite interesting.
[1225.84 → 1231.48] I'm not sure how familiar you all are with the nitty-gritty of, you know, way ARIA and accessibility.
[1232.04 → 1235.74] But I found this to be really relevant and helpful in getting started.
[1236.56 → 1238.04] Yeah, I have seen that article as well.
[1238.14 → 1246.34] And what I loved about it was this emphasis around ARIA not being the like it being a tool rather than the solution.
[1246.34 → 1247.20] Mm-hmm.
[1247.36 → 1249.26] You need to be thinking about this holistically.
[1249.42 → 1256.36] I saw another kind of related article somewhere that was just highlighting how much we basically get on our own way when it comes to accessibility.
[1256.46 → 1261.72] Because we just keep trying to reinvent the wheel where the browser will do most of this for us if we let it.
[1262.06 → 1262.30] Yeah.
[1262.40 → 1265.52] And I mean, there are certain things that don't exist in HTML yet.
[1265.60 → 1267.62] And that's kind of where ARIA can help fill in the gaps.
[1268.12 → 1270.36] But yeah, it definitely shouldn't be used as a crutch.
[1270.42 → 1271.48] It shouldn't be an afterthought.
[1271.48 → 1277.00] It should be something that we learn how to build our applications from the ground up using semantic HTML.
[1277.30 → 1280.88] And from that ground level, like your app is already more accessible.
[1281.12 → 1284.14] Like writing accessible in semantic HTML is not hard.
[1284.26 → 1285.92] It just needs to be prominent.
[1286.62 → 1286.96] Awesome.
[1287.26 → 1287.54] All right.
[1287.60 → 1289.06] Chris, what's your story of the week?
[1289.48 → 1294.48] So my story is an announcement of a library.
[1295.22 → 1297.24] And that library is called Pastel.
[1297.24 → 1305.16] And Pastel is a framework which wraps essentially yards, which is an argument parser.
[1305.36 → 1308.80] And it helps you build command line apps, essentially.
[1309.08 → 1312.54] So it wraps yards, and it wraps something called ink.
[1312.88 → 1318.52] If you haven't heard of ink, what that is, is it basically allows you to create React components.
[1319.16 → 1321.94] And the renderer is your terminal.
[1321.94 → 1327.14] It's not a browser or a mobile device or Windows 10 or whatever.
[1327.52 → 1330.74] So ink is essentially React in the terminal.
[1331.08 → 1333.32] And Pastel looks like a pretty cool idea.
[1333.52 → 1336.18] So ink is just kind of this React layer.
[1336.44 → 1338.14] It's just kind of this adapter.
[1338.56 → 1346.50] But Pastel ties this together with yards in a way that you can write components in React.
[1346.76 → 1351.48] And these components can essentially look like subcommands.
[1351.48 → 1355.92] And so if you're familiar with git, you would say something like, I don't know, git commit.
[1356.52 → 1362.88] Where if you were going to implement that using Pastel, the commit command would be its own component.
[1363.24 → 1370.22] And I think this is fascinating because it, I mean, there may be a bit of novelty to using React on the command line.
[1370.22 → 1373.34] There are certain applications where it makes a lot of sense, actually.
[1373.56 → 1382.92] But what's fascinating, I think, is that you could package up a command and distribute that as a standalone module.
[1383.32 → 1386.70] And so because it's just a component, it's self-contained.
[1386.82 → 1394.68] And so you could essentially pull a bunch of components down from NPM and then smash them together into your own CLI.
[1394.68 → 1397.54] You could reuse commands from other developers.
[1397.98 → 1399.54] And so that looks fascinating.
[1399.80 → 1401.66] You can't actually do that yet.
[1401.78 → 1404.60] I think there are some barriers to making that happen.
[1404.80 → 1410.20] But I think the potential to be able to compose CLI apps in this way is there.
[1410.52 → 1411.62] And I think that's really cool.
[1411.92 → 1414.86] So I'll be keeping a close eye on Pastel.
[1415.10 → 1416.32] That is fascinating.
[1416.68 → 1423.26] I feel like, yeah, I was having trouble imagining why in the world I would want to use React to do that in my CLI.
[1423.26 → 1425.48] But the composition aspect is kind of interesting.
[1425.72 → 1434.90] It forces this model that we know works well for how to compose independent pieces and have props moving down and that sort of thing.
[1435.36 → 1445.96] It works well for stuff, especially like if you were going to implement top or something, which takes up your screen, and then it updates every couple seconds or whatever.
[1446.18 → 1448.56] I think that would be a really great use case.
[1448.80 → 1449.04] Right.
[1449.14 → 1449.80] That makes sense.
[1449.94 → 1450.10] Yeah.
[1450.28 → 1451.36] There are some others, too.
[1451.36 → 1453.44] It helps with kind of formatting.
[1453.88 → 1458.28] But one of the brought this up earlier, it offers like a flex box model.
[1458.78 → 1462.94] And so I was trying to make it render a table, and it was not having it.
[1463.06 → 1464.62] And so I'll have to look into that.
[1464.96 → 1465.60] That is interesting.
[1465.86 → 1474.00] So, yeah, CLI, but potentially actually using your entire terminal area, more like read line style apps than what I might traditionally think of as a CLI.
[1474.14 → 1476.02] Just interacting one line at a time.
[1476.02 → 1476.46] Cool.
[1476.46 → 1477.02] Cool.
[1477.48 → 1481.78] OK, so my article that I want to bring forward was an announcement by Microsoft.
[1482.24 → 1490.86] We had an episode at the end of last year, I believe, where we were talking about some of the challenges in the reduced diversification of the browser ecosystem.
[1490.86 → 1495.98] And Microsoft going to use a Chromium based edge is something that is very much on our radar.
[1495.98 → 1503.30] But they made a fascinating announcement just recently that they are actually going to build Internet Explorer into that Chromium edge.
[1503.52 → 1504.46] And here's why.
[1504.46 → 1517.38] There are lots of businesses out there that have these old, decrepit internal web apps that they use to run their business and have for years and years and years that were developed 10 or 15 years ago.
[1517.72 → 1518.98] Nobody knows how to modify them.
[1519.08 → 1520.64] And they only work on Internet Explorer.
[1520.90 → 1530.18] And that has been one of the reasons why businesses have continued to force employees to use Internet Explorer and businesses outside the tech industry and why it has refused to die.
[1530.18 → 1537.26] And Microsoft is saying, OK, we're going to give you a browser that for those applications will behave like Internet Explorer so you can use it.
[1537.54 → 1540.12] And for everything else is actually a modern browser.
[1540.58 → 1542.18] And to me, I was like, that's brilliant.
[1542.50 → 1548.38] You know, it's its using technology to solve a very non-technology, very human and stodgy business problem.
[1548.38 → 1558.02] But it's it will be a huge step forward in getting some of the last remaining lingering people using ancient, broken browsers out of that world.
[1558.02 → 1562.52] Does that mean we don't need to test an IE anymore?
[1563.16 → 1564.00] It might.
[1564.42 → 1565.60] That would be a blessing.
[1566.22 → 1566.40] Yeah.
[1566.60 → 1567.72] So we will see.
[1568.14 → 1571.86] Microsoft has been trying to kill IE for years now.
[1572.22 → 1577.70] Basically, ever since Edge came along, they've been trying to kill off an end of life IE and then failing.
[1577.96 → 1580.72] It just keeps lingering and lingering and lingering and lingering.
[1580.72 → 1587.64] And this to me seems to address one of the real use cases why that was happening.
[1587.64 → 1588.60] That's really cool.
[1588.68 → 1593.36] I'm kind of scared to find that there are applications that only work in IE.
[1593.66 → 1595.36] Like what applications are those?
[1595.68 → 1595.84] Yeah.
[1595.88 → 1600.66] I mean, I think it's pretty much exclusively old internal business application, right?
[1600.80 → 1602.30] Where they had a developer, right?
[1602.36 → 1606.12] And it's the same type of things why there are still jobs for COBOL developers, right?
[1606.32 → 1609.04] Some old decrepit thing that was built years ago.
[1609.04 → 1612.42] And maybe one person knows how to maintain it, if that.
[1612.74 → 1615.56] And there's a striking amount of software like that.
[1615.56 → 1619.96] It might have to do with stuff like ActiveX and proprietary APIs, too.
[1620.64 → 1621.08] All right.
[1621.14 → 1624.44] So that, I think, wraps up our story of the week segment.
[1624.56 → 1627.64] Let's take another short break, and then we will come back with some pro tips.
[1627.64 → 1637.60] This episode is brought to you by Gauge.
[1637.82 → 1641.44] Gauge is a free and open source test automation tool by ThoughtWorks.
[1641.56 → 1644.38] The goal of the tool is to take the pain out of test automation.
[1644.80 → 1649.76] And to help with this, Gauge supports specifications of Markdown, which are easy to read and easy to write.
[1649.76 → 1654.12] Reusable specifications to simplify your code, which makes refactoring easier.
[1654.46 → 1657.12] And less code means less time maintaining code.
[1657.50 → 1658.68] And finally, integrations.
[1658.84 → 1662.34] Use Gauge with your favourite tools and your IDEs in the ecosystem of your choice.
[1662.80 → 1671.16] Selenium, Sci Heap Pro, CIC and CD tools like Good, Jenkins, Travis, and IDE support for Visual Studio, VS Code, IntelliJ, and more.
[1671.48 → 1674.26] Head to gauge.org slash js party to learn more and give it a try.
[1674.52 → 1676.92] Again, gauge.org slash js party.
[1676.92 → 1687.48] Okay, welcome back.
[1687.80 → 1689.70] Last segment of today's JS Party.
[1689.82 → 1692.08] We are going to share some pro tips.
[1692.48 → 1694.66] Talking about how you can make your life better.
[1694.76 → 1698.88] Whether it's how you do your development, debugging, just general life tips.
[1699.00 → 1700.24] Anything along that dimension.
[1700.74 → 1703.68] I know we've expanded the gamut before, and we probably will again today.
[1703.78 → 1705.32] So let's start off with Chris.
[1705.32 → 1707.74] Chris, what are your pro tips to share with our audience?
[1708.22 → 1712.18] So I've worked remotely for the better part of a decade.
[1712.40 → 1717.52] So I have some pro tips around working from home.
[1717.78 → 1721.48] Some of these are probably kind of obvious, but you'll need a home office.
[1721.78 → 1729.30] So you need somewhere where you can shut the door and just essentially separate yourself from the rest of your family.
[1729.44 → 1730.50] You need this home office.
[1730.50 → 1734.84] You don't always have to work in the home office, but it needs to be available.
[1735.18 → 1740.24] One thing I found, and this is kind of like a recent upgrade for me, is an adjustable desk.
[1740.40 → 1741.62] So I can sit or stand.
[1741.88 → 1742.22] Yes.
[1742.54 → 1743.16] That's great.
[1743.30 → 1743.60] Yes.
[1743.96 → 1744.34] Love it.
[1744.44 → 1752.54] And another thing that keeps the work-life balance for me is having a computer for work and having a computer for not work.
[1752.54 → 1756.04] And so I'm on my work computer during the day.
[1756.18 → 1758.36] At the end of the day, I shut the work computer.
[1758.80 → 1763.70] And if I want to do something else, like play video games or something, I will get my other computer.
[1763.94 → 1767.14] But that work computer doesn't get opened up again until the next day.
[1767.14 → 1768.48] I need to do that.
[1768.62 → 1770.90] I have that problem where I'm really lazy.
[1771.46 → 1777.10] I got a new computer, but I haven't set up the same settings on there for like my dev environment and whatnot.
[1777.40 → 1783.30] So if I want to do like play around with coding, I'll just do it on my work computer, which I shouldn't do.
[1783.30 → 1786.04] Yeah, I will do that.
[1786.20 → 1792.36] Kind of have been doing most of my coding if I'm coding in the evenings, which is not that often anymore.
[1792.58 → 1797.24] I'll probably just use my work computer because, again, I don't have everything set up on my other one.
[1797.34 → 1800.54] But mostly I'm just like playing games on that other machine.
[1800.92 → 1801.10] Yeah.
[1801.52 → 1802.48] So another thing.
[1802.56 → 1806.96] Oh, invest in a decent microphone and some headphones.
[1806.96 → 1815.94] If your computer doesn't have a webcam, get a good webcam because you're going to be video conferencing or on Skype or whatever a lot.
[1816.26 → 1817.66] So make sure people can hear you.
[1817.74 → 1820.62] Make sure your stuff works every time.
[1820.86 → 1824.60] You don't want to be screwing around trying to get your audio set up right.
[1824.86 → 1833.76] It would be really helpful to make sure that you plug in instead of Wi-Fi because that helps with video conferencing and such.
[1833.76 → 1837.88] You don't have to dress up, but you should be presentable.
[1838.30 → 1838.42] Get dressed.
[1838.92 → 1840.46] Yeah, you should get dressed.
[1841.04 → 1841.44] Yeah.
[1842.22 → 1845.14] I wear comfortable clothes around the house.
[1845.46 → 1849.64] I wear this like I like go through slippers like they're essentially disposal.
[1850.34 → 1855.34] Like I just wear the hell out of slippers because, you know, I just want to be comfortable around my house.
[1855.64 → 1862.76] And when I'm working, I just want to be comfortable, not have to fuss with my clothes or maybe like, I don't know, just wear comfortable clothes.
[1862.76 → 1863.70] Be presentable.
[1863.94 → 1866.18] Do things like shave and take a shower.
[1866.44 → 1870.16] This is stuff that, I mean, I've forgotten to do in the past.
[1870.28 → 1874.16] And it's something you have to remind myself, oh, I should probably, you know, shave.
[1874.42 → 1875.64] And so I don't look like a bum.
[1876.12 → 1881.80] But yeah, video conference when you can, it helps you take care of yourself essentially.
[1881.80 → 1886.94] So that's funny because like every time I work from home, I sit in a fluffy bathrobe.
[1886.94 → 1890.58] And then when I have to get on my go-to meetings, people are like, why don't you turn your video on?
[1890.60 → 1894.22] I'm like, you really don't want to see this like dumpster fire of a look right now.
[1894.68 → 1894.86] Yeah.
[1894.90 → 1895.76] I mean, I've been there.
[1895.94 → 1897.74] It's something you have to work at for sure.
[1897.74 → 1906.80] And then another thing is if you have issues with sleep or don't get enough sleep, you will find working from home, your bed is very nearby.
[1907.32 → 1912.74] And it can be tempting to use your bed for sleeping during the day.
[1912.92 → 1917.44] I find that if I make the bed, I'm less likely to go try to lay in it.
[1917.64 → 1918.22] Make your bed.
[1918.50 → 1919.52] So that's my tip.
[1919.94 → 1921.26] How often do you get out of the house?
[1921.26 → 1926.20] Because I feel like if I were to work from home, it would be my fortress that I would never leave.
[1926.30 → 1927.84] Like my husband sometimes doesn't leave that.
[1927.92 → 1930.08] Like he wouldn't leave the house if it weren't for me.
[1930.18 → 1932.06] I don't think he would go outside for like a fortnight.
[1932.34 → 1934.80] I mean, honestly, I don't leave the house that often.
[1935.20 → 1942.56] But it's more to do with kind of my personality as such that I'm kind of a recluse.
[1942.80 → 1949.76] I do go outside and that sort of thing, especially after the workday is over and on the weekends.
[1949.76 → 1952.84] But during the workday, I'm pretty much always at home.
[1953.02 → 1958.02] I don't like to go and work from a coffee shop because I find that it really affects my productivity.
[1958.30 → 1962.18] I like to be in my comfortable space and just totally zone out.
[1962.36 → 1963.26] That's how it works for me.
[1963.60 → 1966.82] I don't think I could do like the digital nomad thing.
[1967.06 → 1971.04] I need my comfort and my familiar space and my control over my environment.
[1971.42 → 1973.36] I also work from home all the time.
[1973.50 → 1978.22] And on exactly that getting out thing, there's a habit that I've adopted that I now like advocate to everyone.
[1978.22 → 1985.86] And it wasn't my intended pro tip, but it is an amazing tip, which is I try to once a day go for a walk outside.
[1986.36 → 1993.74] And during that period, I'm living in a place with beautiful weather or the place, but find something to be grateful for and reflect on that as I walk.
[1993.82 → 1998.90] So I'll walk outside and be like, oh, my gosh, I'm so lucky to live in such a beautiful place with beautiful weather or whatever it is.
[1998.90 → 2006.88] And the thing with this is it actually there's science behind this, which it activates two things that make you feel better.
[2007.32 → 2008.68] One is just moving your body.
[2008.94 → 2010.68] Being more active will make your body feel better.
[2010.78 → 2012.48] Like there's just the physical reaction.
[2012.92 → 2017.70] And two is it's shown that gratitude and practicing gratitude will make you feel happier.
[2017.70 → 2024.78] And it's one of the things like if people are struggling, keeping a gratitude journal and various other things and working from home, it's like I get outside the house.
[2024.94 → 2027.94] So just making this something and I usually do it.
[2028.08 → 2031.52] I'll go walk somewhere for lunch or if I eat lunch, and I'll take a walk after lunch.
[2031.52 → 2036.26] But go for a walk, find something on that walk that I feel grateful for and reflect on it.
[2036.54 → 2042.66] And it is just like when I started this practice, it totally shifted my emotional well-being along a number of dimensions.
[2042.94 → 2045.22] Plus, working from home, it got me out of the house.
[2045.22 → 2048.18] Yeah, that sounds like a brain science episode.
[2049.08 → 2049.68] Could be.
[2049.76 → 2051.10] I have a lot of those hacks.
[2051.20 → 2055.10] I'm going to tell about one in a little bit, but I want to hear your pro tip first.
[2055.46 → 2060.30] Yeah, I changed my mind like four times, but I finally settled on one that's quite relevant.
[2060.58 → 2066.22] So I recently spoke at my first technical conference, which was simultaneously terrifying and also just thrilling.
[2066.76 → 2071.04] So I have a few tips around how to give your first technical talk.
[2071.04 → 2075.50] So oftentimes people think that you have to be an expert on something to give a talk on it.
[2075.50 → 2077.80] And I would say that's just not true, right?
[2077.80 → 2081.04] Use it as a chance to learn a new skill that you've been wanting to learn for a while.
[2081.20 → 2082.56] And you don't have to be an expert.
[2082.84 → 2086.30] People come to hear your point of view on something.
[2086.52 → 2091.18] And even if they are familiar with the topic, often they'll walk away having learned something new.
[2091.42 → 2093.84] So my biggest thing was I forget to breathe.
[2093.84 → 2097.38] So I would recommend breathing when you give a talk because it could be really useful.
[2097.80 → 2105.94] And having water, I actually had to stop talking a couple of times and go take a drink of water, which wouldn't have been so painful if the table was closer.
[2106.06 → 2109.54] But like I literally had to stop and like walk over and take a drink.
[2109.58 → 2111.80] And the whole process took like a solid 20 seconds.
[2112.20 → 2114.22] It was fine, but recommend having some water.
[2114.72 → 2116.58] Also, it's really important to make eye contact.
[2116.58 → 2118.44] So don't just stare at your computer.
[2118.54 → 2121.02] Make sure that you're engaging with the audience a little bit.
[2121.02 → 2131.86] And then going back to the brief discussion we had on accessibility, make sure that your slides have big font and enough colour contrast, you know, with the projector to be accessible for everyone.
[2132.12 → 2132.94] And then just two more.
[2133.06 → 2136.78] So one is not talk too quickly because I have this problem a lot.
[2136.80 → 2141.20] And especially if you're giving an international conference, you'll get people from all over the world.
[2141.20 → 2145.64] So make sure you don't talk too quickly, which it might be hypocritical.
[2145.98 → 2148.60] It might be hypocritical because I'm sitting here talking really quickly.
[2148.78 → 2150.12] But yeah, try to talk slowly.
[2150.12 → 2155.54] And lastly, just don't put a lot of words on your slides, especially if your content is really technical.
[2155.86 → 2158.02] Make sure that you use images.
[2158.14 → 2159.90] Mostly images are just a few words.
[2160.10 → 2162.32] Don't pack your slides full of content.
[2162.50 → 2165.74] But if you're interested in giving a technical talk, go for it.
[2165.82 → 2167.10] What's the worst thing that happens?
[2167.20 → 2172.28] Honestly, like I think you'll get more out of the experience than, you know, if you were just too afraid to do it.
[2172.34 → 2174.34] So I highly recommend everyone try it out.
[2174.82 → 2174.94] Yeah.
[2175.06 → 2176.28] Speaking is a great hack.
[2176.78 → 2178.80] Can you talk more about breathing?
[2178.80 → 2179.86] I have that problem.
[2180.14 → 2181.48] Yeah, it's really hard.
[2181.92 → 2187.56] I'm the kind of person that like if I know my subject material, I kind of want to just get through it as quickly as possible.
[2187.56 → 2191.74] Or like I'm just my brain is like two steps ahead of my breathing.
[2191.74 → 2199.46] So after each slide, or after I made like a statement, I would kind of pause for like two seconds and kind of let them digest what I had just said.
[2199.56 → 2202.18] It also kind of makes you seem more like important.
[2202.40 → 2207.34] Like I find that like pausing for effect, like while it lets me catch up, people don't know that.
[2207.40 → 2209.60] They think I'm just like pausing for like dramatic effect.
[2209.66 → 2212.30] I'm like, no, I'm seriously just trying to like to live over here.
[2212.30 → 2213.40] That's awesome.
[2213.58 → 2217.94] Speaking is a great hack for introverts because like you go to a conference, and you want to meet people.
[2218.08 → 2219.42] But if you're like me, you're kind of shy.
[2219.62 → 2224.46] I mean, you wouldn't think that I'd be shy with the speaking that I do, but I am.
[2224.66 → 2225.70] And a lot of folks are.
[2225.70 → 2227.88] But if you're a speaker, people want to talk to you.
[2228.44 → 2236.46] So you don't have to put yourself out there any more than just getting on stage, which as scary as it is, I find less intimidating than going up to people.
[2236.60 → 2241.44] I have no idea who they are and say or that I am excited to know, but I don't know and be like, hi.
[2242.00 → 2244.66] And if you're a speaker, like, yeah, then they'll come and talk to you.
[2244.84 → 2252.72] It's easy to connect with other speakers because you're a speaker, and they're a speaker, and you're going to have the speaker's lounge, and you can just tweet at them beforehand and say, hey, I see you're speaking.
[2252.82 → 2253.58] I love your stuff.
[2253.58 → 2254.62] I'm going to be there, too.
[2254.62 → 2256.36] You know, it's great.
[2256.78 → 2259.48] But no one will ever shut you down if you try to talk to them.
[2259.68 → 2261.70] We're all there to learn and to get to know people.
[2261.86 → 2264.22] And the last conference I was at was React.js Girls London.
[2264.38 → 2267.90] And I've got to say it was the most inclusive and friendly environment I've ever been to.
[2268.06 → 2270.10] It wasn't just women who were there.
[2270.22 → 2272.54] It was women speakers, which is pretty neat.
[2272.64 → 2274.62] But the environment was so inclusive.
[2274.84 → 2277.14] And what was terrifying is I was the first speaker.
[2277.22 → 2282.00] So I got up on stage and like the React and React Native core teams were sitting in the front row.
[2282.00 → 2283.72] And I had no idea that they were coming.
[2283.72 → 2288.62] And so I just got up on stage, and I'm like, OK, so Danny, I'm sitting in the front row watching me give a talk about React.
[2288.72 → 2289.96] Like what could possibly go wrong?
[2290.06 → 2293.78] So if I can live through that, anyone can live through any conference experience.
[2294.02 → 2294.18] Awesome.
[2294.62 → 2295.10] All right.
[2295.18 → 2296.98] So I think I'm the last one with a pro tip.
[2297.22 → 2300.18] And I sort of teased this because I said I have a lot of like brain hacks.
[2300.18 → 2301.90] So this is also kind of a brain hack.
[2302.04 → 2306.68] And it comes from personal growth guru that I follow because I'm into that kind of stuff.
[2307.02 → 2308.42] Both woo-woo and not woo-woo.
[2308.70 → 2310.92] I actually prefer the not woo-woo that's backed by science.
[2311.06 → 2312.28] But take from it what you will.
[2312.54 → 2314.50] Anyway, so there's this guy named Brendan Bur chard.
[2314.74 → 2315.94] And he has this thing that he says.
[2316.02 → 2319.80] He says, if you think about a power plant, a power plant doesn't have energy.
[2319.88 → 2320.96] It generates energy.
[2321.32 → 2323.38] You take that and think about it for your own life.
[2323.52 → 2323.68] Right.
[2323.68 → 2329.14] If you're one of the biggest things for me in terms of my productivity, in terms of what
[2329.14 → 2332.82] am I getting done, in terms of being able to get out and interact with people and do
[2332.82 → 2334.62] things is like, where's my energy?
[2335.22 → 2340.16] And when I heard this and started thinking about it, it completely shifted my mindset
[2340.16 → 2340.82] about this.
[2340.98 → 2345.56] I should not expect my environment to give me energy or other people to give me energy
[2345.56 → 2347.92] or the project even necessarily to give me energy.
[2348.06 → 2353.48] I need to think about how do I internally generate energy and bring it to whatever scenario.
[2353.48 → 2354.26] I'm going to be in.
[2354.86 → 2357.40] And this can apply to more than just energy, right?
[2357.46 → 2362.60] Like I now have this like self mantra of the things that I want to bring into everything
[2362.60 → 2363.36] that I do.
[2363.54 → 2367.06] And for me, those things are curiosity, joy, and love.
[2367.18 → 2372.48] Like I want that when I show up in my best self, it's because I brought those things to
[2372.48 → 2372.92] the table.
[2372.92 → 2378.10] And this concept shift of whatever it is that is your best self, and that's hard to figure
[2378.10 → 2382.36] out sometimes, like it's very personal, but whatever it is, focusing on the ways that
[2382.36 → 2387.10] you can generate that and bring it to the table rather than expecting other people in
[2387.10 → 2390.34] your environment and whatever else to bring it to you.
[2390.76 → 2392.74] And that has been revolutionary for me.
[2392.92 → 2394.44] And so I wanted to share that as an idea.
[2394.70 → 2395.60] I love that idea.
[2395.72 → 2400.58] I think in one of the JS Party episodes, we talked about books, like favourite books, and
[2400.58 → 2402.08] one of them was the originals.
[2402.20 → 2406.72] And I believe it was in that book where they discussed if you're unhappy, you've got two
[2406.72 → 2407.12] options.
[2407.12 → 2410.70] You can just walk away, or you can actually like to bring something to the table and try to
[2410.70 → 2411.24] fix it.
[2411.50 → 2413.36] And I'm a huge proponent of that as well.
[2413.48 → 2417.68] Or it's like you can't just expect the universe or expect people to give you think, especially
[2417.68 → 2419.98] if you don't tell them that you have these expectations.
[2419.98 → 2424.98] Like you should bring things to the table and things will happen upon you in return to
[2424.98 → 2425.32] those.
[2425.56 → 2426.58] Yeah, 100%.
[2426.58 → 2428.46] And this is not to say stuff doesn't happen.
[2428.66 → 2429.76] Bad stuff happens.
[2430.16 → 2433.10] And if you've had bad stuff happen to you, that can be really rough.
[2433.10 → 2437.48] There's nothing I'm not trying to say that you can or should be able to generate these
[2437.48 → 2438.90] things in yourself all the time.
[2439.10 → 2443.72] However, what I'm saying is for me, the mind shift of going from this is stuff that happens
[2443.72 → 2444.04] to me.
[2444.12 → 2447.08] Somehow I was a perfect energy today, and somehow I was not to.
[2447.20 → 2451.44] This is something that I at least have partial control over and can like work on myself and
[2451.44 → 2455.50] iterate and figure out what are the things that I do that that help me generate energy
[2455.50 → 2459.56] and joy and curiosity and all those things like that was very empowered.
[2459.56 → 2462.16] So yeah, stuff does still happen to you.
[2462.16 → 2467.26] But it's how you choose to handle those situations that kind of defines you and shapes your future.
[2467.76 → 2469.04] So yeah, I fully agree.
[2469.28 → 2469.68] All right.
[2469.76 → 2471.90] That wraps up our pro tips.
[2472.20 → 2475.48] And this wraps up another episode of JS Party.
[2475.78 → 2477.08] So thank you all for joining.
[2477.32 → 2478.10] Thank you for listening.
[2478.46 → 2480.00] Listen live every Thursday.
[2480.30 → 2483.34] I guess they tell you that in the after episode, but I'm going to say it to listen live Thursday
[2483.34 → 2486.74] because it's so much more fun when you all are hanging out with us and chatting in the
[2486.74 → 2488.20] Slack room and everything like that.
[2488.20 → 2489.60] Thank you, Emma and Chris.
[2489.78 → 2491.98] And we will see you next week.
[2492.16 → 2492.48] Yay.
[2492.54 → 2493.16] Thank you.
[2495.02 → 2495.56] All right.
[2495.62 → 2497.46] Thank you for tuning in to JS Party this week.
[2497.58 → 2500.52] Tune in live on Thursdays at 1 p.m.
[2500.56 → 2500.92] U.S.
[2501.06 → 2503.60] Eastern at changelog.com slash live.
[2504.02 → 2506.60] Join the community and Slack with us in real time during the shows.
[2507.00 → 2508.42] Head to changelog.com slash community.
[2509.04 → 2509.70] And do us a favour.
[2509.84 → 2511.02] Share this show with a friend.
[2511.32 → 2512.22] We're just going to have a podcast.
[2512.72 → 2514.30] Go into Overcast and favourite it.
[2514.30 → 2517.04] And thank you to Vastly, our bandwidth partner.
[2517.40 → 2518.90] Head to fastly.com to learn more.
[2519.30 → 2521.90] And we move fast to fix things around here at changelog because of Rollbar.
[2522.10 → 2523.84] Check them out at rollbar.com.
[2524.08 → 2526.16] We're hosted on Leno cloud servers.
[2526.52 → 2528.14] Head to leno.com slash changelog.
[2528.20 → 2529.58] Check them out and support this show.
[2530.04 → 2532.02] Our music is produced by Break master Cylinder.
[2532.40 → 2535.46] And you can find more shows just like this at changelog.com.
[2535.60 → 2536.58] Thanks for tuning in.
[2536.58 → 2537.60] We'll see you next week.
[2544.10 → 2544.54] Congratulations.
[2545.32 → 2547.84] You've listened all the way to the end of the show.
[2548.24 → 2548.96] And guess what?
[2549.24 → 2550.24] Got a little surprise for you.
[2550.58 → 2554.22] Here's a preview of Brain Science, our upcoming podcast coming out very soon.
[2554.52 → 2561.02] The easiest way to subscribe is to subscribe to our master feed at the changelog.com slash master.
[2561.02 → 2564.18] Get all of our podcasts in one single feed.
[2564.18 → 2568.64] Plus some extras that only hit the master feed, including Brain Science.
[2569.04 → 2571.46] Brain Science is a podcast for the curious.
[2571.70 → 2575.82] We're exploring the inner workings of the human brain so we can understand things like behaviour change,
[2576.26 → 2580.38] habit formation, mental health, and this thing we call the human condition.
[2580.66 → 2585.82] It's hosted by myself, Adam Stachowiak, and Meryl Reese, a doctor in clinical psychology.
[2585.98 → 2588.90] It's brain science applied, not just how does the brain work,
[2589.12 → 2592.74] but how do we apply what we know about the brain to better our lives?
[2593.28 → 2593.68] Here we go.
[2594.18 → 2602.34] As humans, one of the things that separates us from any other animal out there is the fact that we have language.
[2602.56 → 2603.40] We have words.
[2603.88 → 2608.14] And we have super powerful words that truly change how we feel and how we make other people feel.
[2608.68 → 2614.62] If the words we say have so much potential to influence ourselves and the world around us,
[2614.64 → 2616.66] how do we begin to understand the power of words?
[2616.66 → 2626.40] So words really are the thing that separates us from all other animals because, right, sharks, bats, dogs, lizards, they don't talk.
[2626.40 → 2633.68] And this is really critical when it comes to managing our moods and our feelings.
[2633.68 → 2644.88] One of the things that I sort of talk about, even I mentioned earlier about the way in which we file things in our mind according to feelings, this is exactly how we differentiate it, too.
[2644.88 → 2650.16] Thinking about an example like with professional athletes.
[2650.16 → 2657.04] You might say that they get anxious, like before a race or before a run or a dive.
[2657.48 → 2661.32] But using that word, it's not really a threat, right?
[2661.32 → 2666.48] But their brain would be like, oh, I'm nervous, and now I start this whole sequence of events in my body.
[2666.68 → 2679.00] Whereas if I just change the word to like I'm anticipating, or I'm excited, it creates a different sort of rollout of emotions as well as physiological responses.
[2679.52 → 2684.36] I mean, I'm anxious about going to Disneyland is not usually what we say, right?
[2684.56 → 2685.10] I'm excited.
[2686.34 → 2686.90] Exactly.
[2687.50 → 2687.88] Exactly.
[2687.88 → 2695.40] So it then puts a lid on or files things differently in our mind, which then changes how we feel about it.
[2695.76 → 2700.34] So in my field in psychology, I would say name it to tame it.
[2700.46 → 2705.86] The better I can name different feelings, the more I can tame whatever emotion that is.
[2706.34 → 2712.76] And so then I'm not really stuck living in this sort of mammal and reptile lane where I'm always just flipping my lid.
[2712.76 → 2713.64] I'm reactive.
[2713.94 → 2715.66] I'm angry, or I'm sad.
[2715.66 → 2725.24] But rather I can go, I recognize this is how I'm feeling or like I'm afraid of some other threat like losing my job.
[2725.24 → 2737.24] And I can go, you know what, here are the words I can use to talk to myself about that fear so that I'm not just stuck feeling afraid of a possible threat, which has never occurred yet.
[2737.82 → 2740.92] You use this concept to say customized thinking.
[2742.34 → 2745.26] I'm not sure if I fully understand what you mean by customized thinking.
[2745.34 → 2746.02] What do you mean by that?
[2746.02 → 2753.74] Well, because we are human, we do have the power of choice, which is super powerful.
[2753.92 → 2756.98] Like nobody has to tell you how you need to think or how you need to feel.
[2757.30 → 2757.72] Right.
[2757.80 → 2766.66] And like your version of success might be very different from mine, which is going to impact my choices and the direction I'm headed.
[2766.66 → 2774.76] And so when you think about customized, right, I mean, you can customize a car, you can customize your order at a restaurant.
[2775.12 → 2782.18] Like it really is tailored specifically to you and going, how do I want to think, and how do I want to feel?
[2782.18 → 2791.30] One example I consider is I want to always, I want every day of the week to feel like I do on the weekend.
[2791.94 → 2793.98] Because to me, the weekend feels great.
[2794.16 → 2795.40] I'm with my family.
[2795.72 → 2799.86] I'm not sort of running things with such a tight timeline.
[2800.54 → 2805.06] And there's just a different sort of ethereal vibe to the weekend.
[2805.72 → 2808.46] And I think, why does that only have to exist on the weekend?
[2809.54 → 2809.72] Yeah.
[2809.86 → 2810.78] I want that every day.
[2810.80 → 2811.36] Why is that?
[2811.36 → 2812.94] I want that every day too.
[2814.78 → 2818.52] Well, and I think part of it is really our attitude and our expectations.
[2819.22 → 2829.80] I mean, there are legitimate threats all around us, but it doesn't help me do me or do my life any better if I am only focused on threats.
[2830.10 → 2836.54] So I want to practice changing the channel in my mind that says, hey, yeah, I see that potential job loss.
[2836.70 → 2839.64] But I also see I'm with my family right now.
[2839.64 → 2846.96] And right now, nobody can take sort of what I've been through and how I feel away from me.
[2846.96 → 2848.54] I'm in charge of how I feel.
[2848.54 → 2853.00] So I'm going to do things that actually contribute to feeling better.
[2853.00 → 2857.50] So how do we apply this name entertainment idea to this model then?
[2857.50 → 2863.56] Because maybe if you name the week, can you change how you feel about it?
[2863.56 → 2864.90] Because that's really what it's about.
[2864.98 → 2874.76] How do we take the labels we apply things to things, the names we give things, the words we use, the choices, what I think we might call nuance.
[2875.02 → 2879.20] I'm not really sure how you put that into play with the power of words.
[2879.20 → 2887.54] But the difference between, like you said before, being anxious or being excited, fundamentally, it's almost the same feeling.
[2887.86 → 2890.86] But from a nuance level, it's very different.
[2891.28 → 2897.90] It's one direction or the other of excitement, negative excitement potentially or positive excitement.
[2898.20 → 2900.00] How do we apply that to customized thinking?
[2900.64 → 2902.84] Well, I think that's a great way to say it, Adam.
[2902.84 → 2911.44] I really like that nuance because what we're looking for, even as I talk about the different brains, we want a symphony.
[2911.84 → 2916.12] I mean, I'm not going to fire the woodwind section because I don't like a violin, right?
[2916.14 → 2919.48] So I don't want to fire a certain part of my brain like, you're not really helpful.
[2919.80 → 2920.92] I don't need to see that.
[2921.58 → 2925.70] But what we need is a sense of congruence.
[2926.56 → 2930.78] And so, sure, not every day of the week can feel exactly like the weekend.
[2930.78 → 2934.84] So I'm not going to say this is how I feel.
[2934.98 → 2944.16] But I have to actually believe it for it to impact my mind, my brain, and my body in the way in which I desire it to.
[2945.00 → 2955.30] And so I might use the words like, I strive for everyday to have a feeling that reminds me of exactly how I feel on the weekend.
[2955.30 → 2962.98] So that I don't lose sight that like every day really is a gift and I get to enjoy every day of my life to some degree.
[2963.86 → 2969.06] And so another example might be I'm living out in the Pacific Northwest.
[2969.34 → 2972.14] A lot of people have negative feelings about the weather.
[2972.84 → 2973.50] Imagine that.
[2973.50 → 2982.88] But so if someone were to say that they just need to learn to love it, that's going to create what we call cognitive dissonance.
[2982.94 → 2983.72] It doesn't fit.
[2984.16 → 2987.92] So it doesn't matter how much I'm like, oh, I do love the gray.
[2988.10 → 2989.30] I do love the clouds.
[2989.50 → 2991.62] It's not going to jibe with me.
[2991.70 → 2992.76] And so it won't stick.
[2992.76 → 2999.88] So instead, I can say I love the way in which the rain creates the green.
[3000.04 → 3002.98] And in the summer, when it is green, it is amazing.
[3003.68 → 3005.68] This idea of learning to live with it, though.
[3005.84 → 3006.66] Get over it.
[3007.18 → 3008.52] It is what it is.
[3008.66 → 3013.20] There are so many phrases we use to say just that, like just learn to live with it.
[3013.50 → 3014.22] What is it called again?
[3014.84 → 3015.94] Cognitive dissonance.
[3016.28 → 3017.68] And what does that mean when you play it out?
[3018.20 → 3019.34] It doesn't go together.
[3019.34 → 3023.52] So if you're like, oh, just do it.
[3023.58 → 3024.66] You just need to get over it.
[3024.96 → 3032.14] Like that really isn't helpful either because your body is giving you a signal and your brain is telling you, I don't like this sensation.
[3032.40 → 3033.94] I don't like how this feel.
[3034.04 → 3039.12] I mean, a lot of people will say, oh, I just hate the gray and the gray is just overwhelming.
[3040.26 → 3044.08] And so we have to go, well, what's my emotional buy-in?
[3044.50 → 3046.60] Like what do I like?
[3046.60 → 3051.06] How does that even allow me to enjoy something else?
[3051.18 → 3055.38] And so I'm going to look at going, you know what?
[3055.42 → 3062.50] I really like that I get to wear warm clothes, or I really do love my coffee because it's for such a long time.
[3062.54 → 3063.32] It's gray and rainy.
[3063.42 → 3065.70] I want to be inside by a fire drinking my coffee.
[3065.70 → 3066.14] Right.
[3066.34 → 3068.94] And so how can I look for going, you know what?
[3069.28 → 3075.58] If I do these things I might not want to do, I do get some more of what I do want to do.
[3075.58 → 3084.54] And so it's really almost like a bartering system in your brain of saying, if you do this thing you don't like, you get this thing you do like.
[3084.54 → 3097.14] Or, you know, I know you don't have to make yourself do this thing unless you can see a way in which it actually benefits you or speaks to you emotionally.
[3098.00 → 3101.40] Everything, Adam really has to have this emotional buy-in.
[3101.40 → 3110.48] And if there's no good emotion, no really the primary Euro neurochemical in our brain is dopamine for feeling good.
[3110.66 → 3112.54] I don't get some hit of dopamine.
[3113.06 → 3115.10] My brain's going to be like, it's not worth it.
[3115.10 → 3116.38] And I'm not going to do it.
[3116.70 → 3117.18] Period.
[3120.58 → 3122.58] That's a preview of brain science.
[3122.70 → 3130.14] If you love where we're going with this, email us to get on the list to be notified the very moment this show gets released.
[3130.14 → 3133.60] Email us at editors at changelog.com.
[3133.70 → 3139.14] In the subject line put in all caps, brain science with a couple bangs if you're really excited.
[3139.66 → 3143.94] You can also subscribe to our master feed to get all of our shows in one single feed.
[3144.06 → 3149.84] Head to changelog.com slash master or search in your podcast app for changelog master.
[3149.96 → 3150.58] You'll find it.
[3150.90 → 3155.02] Subscribe, get all of our shows and even those that only hit the master feed.
[3155.12 → 3157.16] Again, changelog.com slash master.
[3160.96 → 3161.28] Challenge.
[3163.42 → 3167.86] Customers.
[3178.22 → 3179.50] academicisms.
[3179.76 → 3181.08] Amazon.
[3181.60 → 3185.00] Tune in October
[3185.24 → 3187.88] Rem ужас
