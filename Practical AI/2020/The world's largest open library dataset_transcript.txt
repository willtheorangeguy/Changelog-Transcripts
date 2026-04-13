[0.00 --> 15.96]  Our original kind of vision for it is, wouldn't it be cool if this was a two-way process in terms of we open up the data and then people who are much smarter than us are able to contribute back things built with that data, which then can be used by more researchers and it becomes this product in itself that continues to grow.
[16.24 --> 21.20]  And we just kind of provide the inputs to photos and whatever we're kind of doing on our side.
[21.40 --> 24.68]  The V1 was like, let's get it out there and let's see what people start using.
[24.68 --> 30.08]  Because, you know, Tim and myself, we're not, as you can probably tell, too well-versed in machine learning.
[30.48 --> 34.20]  So we have no idea really how people are going to use this and what fields are going to be valuable.
[34.48 --> 38.20]  But get it out there, get some feedback on it, see what people are using.
[38.32 --> 42.88]  And then if in the future we have that opportunity to make it a two-way process, we'd love to do that.
[45.08 --> 47.48]  Bandwidth for Change Log is provided by Fastly.
[47.80 --> 49.68]  Learn more at Fastly.com.
[49.92 --> 52.20]  Our feature flags are powered by LaunchDarkly.
[52.20 --> 54.30]  Check them out at LaunchDarkly.com.
[54.30 --> 56.38]  And we're hosted on Linode cloud servers.
[56.72 --> 60.26]  Get $100 in hosting credit at Linode.com slash Change Log.
[60.94 --> 62.06]  What up, friends?
[62.16 --> 66.10]  You might not be aware, but we've been partnering with Linode since 2016.
[66.44 --> 67.40]  That's a long time ago.
[67.60 --> 72.76]  Way back when we first launched our open source platform that you now see at ChangeLog.com,
[73.26 --> 76.86]  Linode was there to help us, and we are so grateful.
[77.08 --> 82.18]  Fast forward several years now, and Linode is still in our corner, behind the scenes,
[82.18 --> 86.36]  helping us to ensure we're running on the very best cloud infrastructure out there.
[86.84 --> 87.62]  We trust Linode.
[87.84 --> 90.22]  They keep it fast, and they keep it simple.
[90.54 --> 93.72]  Get $100 in free credit at Linode.com slash Change Log.
[93.88 --> 99.74]  Again, $100 in free credit at Linode.com slash Change Log.
[99.74 --> 121.08]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[121.48 --> 122.42]  and accessible to everyone.
[122.70 --> 126.82]  This is where conversations around AI, machine learning, and data science happen.
[126.82 --> 131.54]  Join the community and Slack with us around various topics of the show at ChangeLog.com slash
[131.54 --> 133.18]  community, and follow us on Twitter.
[133.34 --> 134.92]  We're at Practical AI FM.
[141.24 --> 144.66]  Welcome to another episode of Practical AI.
[145.06 --> 146.70]  This is Daniel Whitenack.
[146.82 --> 153.44]  I am a data scientist with SIL International, and I'm joined, as always, by my co-host, Chris
[153.44 --> 158.44]  Benson, who is a principal emerging technology strategist at Lockheed Martin.
[159.04 --> 160.08]  Happy Thanksgiving, Chris.
[160.12 --> 160.46]  How are you doing?
[160.66 --> 161.50]  Hey, happy Thanksgiving.
[161.66 --> 162.34]  Doing very well.
[162.42 --> 165.66]  I guess by the time this goes out, it will be just after Thanksgiving.
[165.66 --> 167.76]  Just after American Thanksgiving.
[168.12 --> 168.30]  Yeah.
[168.50 --> 168.86]  That's right.
[168.92 --> 171.66]  We haven't stuffed ourselves yet at this moment, so we're lively.
[171.96 --> 172.50]  Lively today.
[172.50 --> 179.24]  Although I heard there was a general surplus of turkeys because people are at home and they're,
[179.24 --> 181.12]  you know, smaller groups, right?
[181.20 --> 184.68]  Of course, you and I, I don't know if you're, you go for the tofurkey.
[184.90 --> 189.08]  For our listeners that don't normally listen, Chris and I both don't eat meat.
[189.32 --> 193.04]  We always have a tofurkey, and that's about the right size for us this year, I think.
[193.10 --> 194.56]  We're not going to have that many people around.
[195.02 --> 198.68]  Yeah, it's good because my wife is really into like making sure that we have all the,
[198.86 --> 200.82]  so we have the tofurkey and all the little things.
[200.82 --> 202.16]  But yeah, it's all vegan.
[202.62 --> 204.00]  And so, yeah, it's delicious.
[204.10 --> 209.02]  I got to say, turkey, if you're a vegan, you know, five years ago, it sucked to be a vegan
[209.02 --> 209.56]  on Thanksgiving.
[209.94 --> 210.64]  It really did.
[210.70 --> 211.16]  It sucked.
[211.42 --> 212.76]  But now, it's good stuff.
[213.08 --> 217.58]  As far as like general meat substitutes, I would say it's pretty good.
[217.70 --> 218.60]  They've gotten a lot better.
[218.94 --> 219.12]  Yeah.
[219.20 --> 219.70]  They really have.
[219.80 --> 219.96]  Yeah.
[220.02 --> 225.20]  I don't know if they're using AI to like analyze the recipes and get it right, but.
[225.34 --> 229.30]  I was going to say, I have no idea what this has to do with AI, but you know, there we go.
[229.30 --> 230.32]  We're coming into the holidays.
[230.32 --> 231.08]  It's time to eat.
[231.60 --> 231.64]  Yeah.
[231.80 --> 232.10]  Yeah.
[232.20 --> 234.94]  Well, I'm pretty excited today about our conversation.
[235.18 --> 240.56]  You know, Chris, we've had a number of people come on the show and mention various opinions
[240.56 --> 244.12]  or ideas about opening up data sets.
[244.12 --> 245.18]  So open data.
[245.56 --> 245.72]  Yep.
[245.72 --> 247.68]  Whether that be image data or speech data.
[247.76 --> 251.00]  We had a conversation with Mozilla Common Voice about that data.
[251.46 --> 255.52]  But generally, a lot of times when we get into these conversations, it's more from the
[255.52 --> 261.26]  perspective of consuming that data for some purpose, not from the perspective of people
[261.26 --> 263.84]  that have actually worked to open up data.
[263.84 --> 270.92]  So I'm really excited today that we have a couple of people from Unsplash with us.
[271.42 --> 277.58]  And Unsplash has released a huge, actually the world's largest open library data set.
[278.26 --> 283.52]  And today we've got with us Luke Chesser, who's co-founder of Head of Product at and Head
[283.52 --> 284.88]  of Product at Unsplash.
[284.90 --> 288.98]  And we've got Tim Carbone, who is data engineer at Unsplash.
[289.10 --> 289.66]  Welcome, guys.
[290.34 --> 290.68]  Hey, guys.
[290.68 --> 291.38]  Thanks for having us.
[291.60 --> 292.38]  Hey, thank you.
[292.52 --> 292.64]  Yeah.
[292.76 --> 293.00]  Yeah.
[293.06 --> 298.98]  So before we jump in, why don't we just go into a little bit of each of your backgrounds
[298.98 --> 304.46]  and how you got interested in doing what you're doing now and eventually ended up at Unsplash.
[304.56 --> 305.50]  Do you want to start us out, Luke?
[305.80 --> 306.24]  Yeah, for sure.
[306.34 --> 313.18]  So my background was originally as a designer and I joined two friends to start a company,
[313.18 --> 318.02]  which was at the time an open marketplace, like a marketplace for hiring designers and developers.
[318.02 --> 323.96]  And by necessity over the years, I ended up having to learn engineering and kind of worked
[323.96 --> 327.12]  my way into building products completely.
[327.42 --> 330.82]  And one of the side projects we started building inside of that company was a company called
[330.82 --> 331.34]  Unsplash.
[331.44 --> 335.66]  And it was just this little image kind of repository that we open sourced.
[335.84 --> 340.14]  And that eventually turned itself into a full company, which is its own entire story.
[340.32 --> 343.80]  And now I get to oversee this team of really talented people.
[343.80 --> 348.68]  So I'll pretend that I know a lot about coding and design and everything, but really, they're
[348.68 --> 350.04]  the ones that make me look really good now.
[350.34 --> 353.80]  And before we go on, I got to ask, because the listeners only hear the audio.
[354.00 --> 355.82]  We're all on a Zoom call right now.
[355.90 --> 357.92]  And I see the guitars hanging behind you on the wall.
[358.00 --> 361.58]  So you must be a musician, I guess, or just a fan or what?
[361.74 --> 364.10]  Let's say my coding is even better than my guitaring.
[364.28 --> 367.28]  So I don't know how good I would say this guitar is.
[367.36 --> 369.46]  This is purely for show, I think.
[369.80 --> 370.40]  It looks good.
[370.50 --> 370.68]  Okay.
[370.72 --> 371.40]  I make myself look cool.
[371.56 --> 371.82]  Cool.
[371.82 --> 373.12]  Well, Tim, what about you?
[373.24 --> 376.86]  What's your background and how did you end up working with Luke at Unsplash?
[377.20 --> 382.24]  So for my background, I have a classic computer science master that I did in France.
[382.86 --> 387.02]  And for the final master internship, I was led to Montreal, essentially.
[387.48 --> 389.82]  And that's when I started working in data.
[390.40 --> 395.42]  A couple of years later, I had a great opportunity to join Crew at the time, working remote.
[395.72 --> 399.26]  Went back to France for a couple of years and then went back to Montreal.
[399.26 --> 402.30]  So now I'm working for Unsplash since the transition.
[402.72 --> 406.32]  I've been working there for four to five years now.
[406.76 --> 412.62]  And I'm working as a data engineer, essentially building the whole data architecture, trying
[412.62 --> 418.94]  to get some stats in front of our contributors and get some useful insights for our business
[418.94 --> 419.68]  needs.
[419.68 --> 420.28]  Yeah.
[420.34 --> 424.78]  And also, Tim's going to be humble here, but Tim's the only person working on data inside
[424.78 --> 425.36]  of our company.
[425.52 --> 426.70]  And there's a lot of data.
[426.70 --> 432.30]  We have a whole stats analytics system that serves our 200 something thousand contributors.
[432.84 --> 434.70]  We have a massive search system, all these things.
[435.04 --> 436.54]  All of it's powered basically by Tim.
[436.80 --> 439.98]  So he's going to be very humble, but he's very good.
[440.06 --> 442.12]  You got some weight on your shoulders there, my friend.
[442.32 --> 442.48]  Yeah, Tim.
[442.56 --> 442.98]  Thank you.
[443.10 --> 443.90]  And same thing.
[443.90 --> 448.94]  I'm not a machine learning engineer, so AI is very foreign to me.
[449.26 --> 453.32]  So yeah, mostly focused on data architecture, warehouses and things like that.
[453.60 --> 453.76]  Yeah.
[453.82 --> 455.94]  So you probably know more than me on AI.
[456.62 --> 458.20]  Well, I think we're all learning.
[458.42 --> 463.24]  And it sounds like from what you're already doing, you probably have a good bit of knowledge
[463.24 --> 464.14]  in a lot of areas.
[464.14 --> 465.44]  So that's great.
[465.72 --> 467.00]  I'm curious a little bit.
[467.26 --> 472.92]  You mentioned a bit about how Unsplash came about and this data set came about.
[472.92 --> 478.00]  Could you give us a little bit of a history of just where this data originated and the
[478.00 --> 478.60]  nature of it?
[478.82 --> 483.32]  What's included in your data and why does it exist in the first place?
[483.92 --> 484.04]  Yeah.
[484.08 --> 489.22]  So going back to, I guess, the fundamentals, the data exists because Unsplash is this
[489.22 --> 493.54]  repository of images that are contributed by a community of photographers all over the
[493.54 --> 493.74]  world.
[493.92 --> 498.16]  And they open up their images and say, hey, anyone can use these images for whatever they
[498.16 --> 498.88]  want to use them for.
[498.88 --> 503.12]  And traditionally, that's been, okay, I'm going to download these images and I'm going
[503.12 --> 505.34]  to use them in a creative project.
[505.34 --> 507.12]  I'm going to make a graphic.
[507.26 --> 508.38]  I'm going to use them in an article.
[508.74 --> 512.16]  But there's so much more to images than just what they look like.
[512.32 --> 517.22]  And with 2 million images now in this community, we've been talking about for a while the idea
[517.22 --> 523.10]  of opening that up to AI researchers or really just anybody who wants to use it in a different
[523.10 --> 523.38]  way.
[523.38 --> 527.52]  And we've had this API traditionally where developers can come in and pull in images
[527.52 --> 528.72]  for different applications.
[528.72 --> 530.42]  So we power Medium's images.
[530.64 --> 531.42]  We power Google's.
[531.54 --> 532.80]  We power BuzzFeed.
[533.08 --> 536.28]  A whole bunch of different companies use the images via the API.
[536.64 --> 542.64]  But the API wasn't set up to be used for the kinds of data-intensive projects where you
[542.64 --> 544.18]  need to pull in a lot of information.
[544.78 --> 549.04]  And so Tim and I have had this conversation a handful of times over the year.
[549.04 --> 553.28]  Wouldn't it be cool if we could open up our data set and make it available to people who
[553.28 --> 555.62]  just want to play with the data and make cool things?
[556.30 --> 560.34]  And it was earlier this year, during lockdown, where we didn't have a lot going on.
[560.38 --> 561.58]  We were like, let's do something.
[562.08 --> 565.66]  And Tim took it upon himself then to think about what would be useful, what would be good
[565.66 --> 567.84]  for a V1 and how could we get that out there?
[568.24 --> 572.02]  And Tim's probably the best person to talk about what data we actually expose in it.
[572.68 --> 572.86]  Yeah.
[573.00 --> 577.94]  And I should mention too that one of the reasons why we're having this conversation is our editor
[577.94 --> 582.96]  at ChangedLog, Adam Stachowiak, one day in our messages during, like you're saying, during
[582.96 --> 586.96]  lockdown, he messaged me and said, hey, look at what was just released from Unsplash.
[587.04 --> 588.54]  And this would be a cool conversation.
[588.54 --> 591.32]  So thanks, Adam, for forwarding that along.
[591.84 --> 592.00]  Yeah.
[592.10 --> 598.36]  Let's maybe then kick it over to Tim just to talk about what is actually in this data
[598.36 --> 598.60]  site.
[598.68 --> 601.22]  So you mentioned images that people contribute.
[601.90 --> 602.90]  Is it just images?
[603.24 --> 607.08]  You know, what's the sort of domain of these and how are they represented?
[607.08 --> 607.60]  Yeah.
[607.78 --> 610.42]  So the data set doesn't actually contain the photos.
[610.64 --> 616.12]  It's basically a couple of CSV files in which you will find the link to download the photo.
[616.30 --> 620.18]  So you could potentially parse the data set and mass download everything if you want.
[620.80 --> 624.92]  And for each photo, you have a bunch of associated data and metadata.
[625.44 --> 628.94]  So you would have, for example, exif data from the camera.
[629.24 --> 631.42]  You would have photographer details.
[631.42 --> 633.70]  You would have geolocation for the photo.
[634.10 --> 636.26]  You would have Unsplash stats.
[636.70 --> 643.00]  And you would also have things like tags and keywords data that were collected from third
[643.00 --> 648.14]  party AIs, including like Google AIs and Amazons and things like that.
[648.26 --> 652.92]  You will also get some data about the colors that are present in the photo.
[652.92 --> 657.94]  And we're trying to include a bit more of Unsplash content.
[658.10 --> 660.10]  So we added the notion of collection.
[660.36 --> 663.38]  So on Unsplash, when you go on Unsplash, you can create collections of photos.
[663.94 --> 665.08]  And that could say a lot.
[665.40 --> 670.52]  I'm guessing that could say a lot to researchers as to which photo is related to another one
[670.52 --> 670.92]  or whatever.
[670.92 --> 674.96]  So we're including that collections data inside the data set.
[675.26 --> 681.02]  And we're also including search conversion data that could be very interesting, I think,
[681.18 --> 681.36]  too.
[681.82 --> 687.04]  So you'd have people who search on Unsplash, who click on photos, who download photos.
[687.28 --> 689.66]  And that is also representing the data set.
[690.28 --> 690.68]  Very cool.
[690.86 --> 693.24]  I guess as you were saying that, something came to mind.
[693.40 --> 696.64]  I was really wondering, and I'll probably throw it back to Luke for this.
[696.98 --> 699.14]  How is your business model accommodating that?
[699.14 --> 704.46]  Because what you're describing is wonderful to hear as a practitioner and a user or consumer
[704.46 --> 704.86]  of that.
[705.26 --> 709.38]  But how is your company organized so that you can support this kind of work?
[709.84 --> 710.94]  And what's the benefit?
[711.08 --> 712.30]  How does all that work in your world?
[712.76 --> 712.88]  Yeah.
[712.92 --> 719.16]  So the data set isn't released in any way to be this commercial product.
[719.30 --> 726.68]  There is a potential for it to have a commercial business behind it in the sense that right now
[726.68 --> 729.92]  it's under a license where we've released in two data sets.
[730.10 --> 734.20]  The smaller data set is able to be used for commercial and non-commercial uses.
[734.40 --> 738.10]  The bigger data set is more restricted in terms of commercial uses.
[738.32 --> 741.38]  So there is a possibility that it could eventually commercialize in that way.
[741.38 --> 745.50]  We're not necessarily banking on that or that's not the reason why we're doing it.
[746.34 --> 750.20]  Unsplash itself, though, has in its DNA this idea of sharing and openness.
[750.20 --> 756.16]  And, you know, we as a business get to benefit from the fact that people are opening up their
[756.16 --> 760.62]  images and sharing them and believing in this bigger kind of cause of when I share something
[760.62 --> 763.58]  out and it gets used, that's, you know, helping other people and that's great.
[764.00 --> 766.12]  So we wanted to do something similar, you know.
[766.70 --> 771.80]  Traditionally, in terms of the history of Unsplash, we have always started with this idea of if we
[771.80 --> 776.10]  create value for people, we can find ways to commercialize it later and run a business on top
[776.10 --> 776.36]  of that.
[776.80 --> 782.74]  The way Unsplash makes its money is through brands uploading at images to Unsplash that
[782.74 --> 786.58]  then get this massive amount of distribution through all of our API networks through the
[786.58 --> 788.74]  site and end up in all these different kinds of places.
[789.12 --> 793.18]  So the data set doesn't need to be something where we make money directly off of it.
[793.68 --> 794.50]  And yeah.
[795.12 --> 795.24]  Got it.
[795.28 --> 795.90]  That's very helpful.
[796.04 --> 800.04]  So kind of in the DNA, but I was wondering because that's always an issue that we run into
[800.04 --> 803.52]  because there's lots of companies that have different models for sharing.
[803.74 --> 805.70]  And I love the fact that sharing is part of your DNA.
[805.70 --> 809.04]  But you also have to maintain a company and do that.
[809.12 --> 812.36]  So it's always an interesting question to find out how people are approaching it.
[812.84 --> 813.16]  Absolutely.
[813.28 --> 813.44]  Yeah.
[813.48 --> 814.16]  I think we're lucky.
[814.28 --> 817.26]  And we're still a small enough company in terms of, you know, we're 25 people.
[817.68 --> 821.66]  We can make decisions that are, you know, long term and don't need to directly impact
[821.66 --> 823.22]  the company, you know, tomorrow or something.
[823.34 --> 827.02]  And, you know, a lot of times we do things because we just want to do it and we think it's
[827.02 --> 827.78]  a cool thing to do.
[827.82 --> 831.54]  And I think the data set has, you know, a handful of different motivations behind it.
[831.56 --> 834.10]  And one of them was just, wouldn't it be cool if we could do this?
[834.10 --> 837.42]  And when it's small enough, you get to kind of make some of those decisions.
[837.92 --> 838.04]  Cool.
[838.18 --> 838.48]  Thanks.
[838.94 --> 839.18]  Yeah.
[839.46 --> 845.36]  It's interesting to me that there's been this progression in companies kind of built around
[845.36 --> 847.36]  open source software.
[847.36 --> 853.96]  So like open core companies or other companies that are built around some open source toolkit,
[854.40 --> 856.32]  at least on some level.
[856.84 --> 862.10]  It seems like there's not that many pre-existing examples of companies that are really built
[862.10 --> 864.60]  around like open data models.
[864.76 --> 865.48]  Is that true?
[865.54 --> 867.64]  Or am I just like sort of missing that?
[868.20 --> 873.64]  As far as I'm aware, I think, you know, if this ever has any commercial benefit, that'd
[873.64 --> 874.02]  be great.
[874.14 --> 877.44]  But at the same time, I think, you know, our primary motivation is, you know, let's
[877.44 --> 878.20]  see what gets out there.
[878.28 --> 879.10]  Let's see what gets used.
[879.26 --> 883.82]  And there's a reinforcing idea of, you know, if a lot of different researchers are using
[883.82 --> 888.14]  Unsplash images, it reinforces the idea that Unsplash is the place for images.
[888.14 --> 889.34]  It's the place where you get images.
[889.34 --> 893.64]  And it's one more benefit for our contributors who open up their images where they can say,
[893.76 --> 898.62]  hey, I contributed to these models that help, you know, self-driving cars or, you know, I
[898.62 --> 901.80]  have no idea how it's going to be used, but they can say, you know, there's one more benefit
[901.80 --> 904.68]  of me opening up my work and making it available to people.
[919.34 --> 924.08]  All right.
[924.14 --> 929.92]  So I'm kind of interested, I guess, maybe we can kick it over to Tim.
[930.02 --> 935.54]  I'm kind of interested in terms of like the just some general stats in terms of the data
[935.54 --> 939.56]  set size and the types of images that are included.
[939.68 --> 941.62]  And also maybe like, how is that growing?
[941.62 --> 945.32]  Like you mentioned a lot about people uploading their images.
[945.32 --> 951.00]  What's the sort of trajectory of that and what's being added most and some of those sorts of
[951.00 --> 951.34]  stats?
[951.82 --> 951.96]  Yep.
[952.10 --> 957.92]  So the data set, I think the light data set is about five gigabytes and the full size
[957.92 --> 961.86]  data set is more about 20, 25 gigabytes, something like that.
[962.24 --> 965.76]  And that's the metadata about it, not the images themselves.
[965.96 --> 966.40]  Exactly.
[966.56 --> 966.72]  Yeah.
[966.74 --> 967.70]  That's just the metadata.
[967.70 --> 970.58]  So we have about 1.3 million photos right now.
[970.94 --> 973.98]  And you mentioned which kind of photos are included.
[973.98 --> 980.30]  So at Unsplash, we have a manual curation process for every single photo that comes in.
[980.94 --> 984.38]  And so the photo can end up in kind of like different buckets.
[984.62 --> 986.84]  So you'd have photos that are featured.
[986.98 --> 992.60]  You'd have photos that are approved and because they just match the guidelines or they fit the
[992.60 --> 993.04]  guidelines.
[993.68 --> 996.36]  And so that distinction is also presented in the data set as metadata.
[997.10 --> 1001.86]  But in the light data set, for example, only featured photos are showing up.
[1001.86 --> 1003.96]  It's a subset of featured photos.
[1004.24 --> 1007.28]  And I think they only concern nature photos.
[1008.00 --> 1010.30]  And in the full data set, everything's in there.
[1010.44 --> 1013.32]  So approved photos and featured photos.
[1013.68 --> 1013.88]  So yeah.
[1014.04 --> 1015.60]  So that's what's in the data set.
[1015.98 --> 1018.70]  I'm not sure I remember the rest of the question.
[1018.78 --> 1019.10]  I'm sorry.
[1019.94 --> 1021.06]  No, it's all good.
[1021.14 --> 1024.90]  Also, in terms of the trajectory of how the data set is growing.
[1024.90 --> 1030.34]  And obviously, that's also tied to, you know, the main part of your business and people uploading
[1030.34 --> 1031.60]  photos and that sort of thing.
[1031.94 --> 1032.28]  Absolutely.
[1032.54 --> 1038.70]  So yeah, we definitely want to make the Unsplash data set some kind of a product of Unsplash
[1038.70 --> 1041.38]  and not just like a single time dump of data.
[1041.96 --> 1047.16]  So it's something we want to keep improving, upgrading, getting feedback on and kind of like
[1047.16 --> 1048.34]  iterating over it.
[1048.34 --> 1052.02]  So we're getting thousands of new submissions every day.
[1052.22 --> 1058.50]  And I think the plan is to kind of like put those new submissions and those photos inside
[1058.50 --> 1060.42]  the data set from time to time.
[1060.42 --> 1063.78]  So we haven't decided on the frequency yet.
[1063.88 --> 1069.64]  But I'm guessing that every couple of months, maybe, or a couple of quarters, we'll be releasing
[1069.64 --> 1073.42]  a new version of the data set with new photos and maybe some improvements.
[1073.42 --> 1078.70]  Couple of days after the release, we started getting some feedback and we've pushed directly
[1078.70 --> 1081.68]  like a V1.1, a new version of the data set.
[1081.80 --> 1085.06]  So yeah, and we've been improving a couple of fields, improving data quality.
[1085.22 --> 1088.46]  So right after that, because we started getting feedback.
[1088.84 --> 1090.94]  So yeah, we'll be reacting to feedback pretty quickly.
[1091.26 --> 1092.18]  That's pretty cool.
[1092.38 --> 1097.92]  Is there any kind of thought for the future about like, since you have these open source
[1097.92 --> 1103.06]  projects and stuff that will be pulling the data set down and running ML processes on it
[1103.06 --> 1103.58]  and stuff?
[1103.86 --> 1107.60]  Maybe there's a feedback loop where some of those open source practitioners can help
[1107.60 --> 1111.16]  you do, like you mentioned manual curation and stuff like that.
[1111.16 --> 1115.26]  Any thoughts toward automating that curation with ML going forward?
[1115.58 --> 1116.16]  Yeah, absolutely.
[1116.34 --> 1119.12]  I think that's something that we talked about with Luke.
[1119.56 --> 1124.82]  It's also the fact that we have this massive data set and we don't have the skills to leverage
[1124.82 --> 1125.36]  it properly.
[1125.82 --> 1130.42]  So if we put it out there, maybe it can help the research and we can leverage that research
[1130.42 --> 1131.52]  that was just made.
[1131.52 --> 1133.88]  Yeah, that's part of being a startup, really.
[1134.06 --> 1134.74]  I mean, that's normal.
[1134.92 --> 1139.40]  You're always trying to find the skills for the next thing to go along and fund it.
[1139.48 --> 1140.48]  I totally get that.
[1140.70 --> 1140.94]  Exactly.
[1141.14 --> 1141.72]  So yeah, totally.
[1142.18 --> 1146.98]  And also, I think that it can also be a feedback loop in the sense that some researchers can
[1146.98 --> 1152.00]  create kind of like new metadata for each photo that would be the result of a model.
[1152.38 --> 1156.82]  And we could include that result in the data set so that it can be helpful for other
[1156.82 --> 1157.24]  researchers.
[1157.36 --> 1159.14]  So it can be a feedback loop in that sense as well.
[1159.14 --> 1160.40]  That's exactly it, Chris.
[1160.76 --> 1166.14]  Our original kind of vision for it is, wouldn't it be cool if this was a two-way process in
[1166.14 --> 1171.18]  terms of we open up the data and then people who are much smarter than us are able to contribute
[1171.18 --> 1175.64]  back things built with that data, which then can be used by more researchers.
[1175.64 --> 1179.02]  And it becomes this product in itself that continues to grow.
[1179.02 --> 1184.28]  And we just kind of provide the inputs to photos and whatever we're kind of doing on our side.
[1184.74 --> 1188.02]  The V1 was like, let's get it out there and let's see what people start using.
[1188.10 --> 1193.44]  Because Tim and myself were not, as you can probably tell, too well-versed in machine learning.
[1193.64 --> 1197.16]  So we have no idea really how people are going to use this and what fields are going to be
[1197.16 --> 1197.56]  valuable.
[1197.84 --> 1201.80]  But get it out there, get some feedback on it, see what people are using.
[1201.80 --> 1206.88]  And then if in the future we have that opportunity to make it a two-way process, we'd love to do that.
[1207.36 --> 1210.70]  Just now, at the point where this is released, you have thousands of listeners who just heard
[1210.70 --> 1210.94]  that.
[1211.18 --> 1215.98]  So we should consider that to be a call to action to take advantage of the data set,
[1216.04 --> 1217.56]  but also contribute back there.
[1217.90 --> 1218.16]  Perfect.
[1218.40 --> 1218.58]  Yeah.
[1218.84 --> 1223.44]  It would definitely be cool to see out of this some examples that pop up on Google Colab or
[1223.44 --> 1228.36]  something of people pulling in some of that data and doing something and making that work
[1228.36 --> 1229.30]  itself open.
[1229.30 --> 1234.98]  And I'm curious, as sort of a follow-up to that, it sounds like you have started to get
[1234.98 --> 1237.64]  some feedback on this and some usage of it.
[1237.64 --> 1241.98]  So I guess one question is just like, how has that gone so far?
[1242.12 --> 1248.32]  And like, you know, what sort of influx of usage and downloads have you seen just as a
[1248.32 --> 1249.92]  result of this work?
[1250.98 --> 1251.16]  Yeah.
[1251.70 --> 1256.06]  So far, I'm not 100% sure on the numbers we should have checked before we came on.
[1256.14 --> 1257.98]  I think it's done about 3,000 downloads.
[1257.98 --> 1260.02]  That's of the light set.
[1260.24 --> 1264.38]  I think for the full data set, it's probably done about 1,000 downloads, probably.
[1264.90 --> 1267.04]  So it's been out for three, four months now.
[1267.16 --> 1269.04]  So that's, you know, it's a good start for us there.
[1269.24 --> 1272.06]  We haven't really been doing much marketing or talking about it.
[1272.08 --> 1274.88]  So hopefully something like this, we'll get it in front of some more people as well,
[1274.92 --> 1275.56]  which will be helpful.
[1276.10 --> 1280.42]  The kind of couple uses that I'm aware of that were cool and, you know, surprising for
[1280.42 --> 1280.58]  me.
[1280.80 --> 1283.12]  I mean, you can never predict how people are going to use this.
[1283.12 --> 1286.32]  And I think there was obvious things of, you know, people are going to train vision
[1286.32 --> 1288.34]  models, you know, and tagging models with it.
[1288.40 --> 1291.88]  But it's been cool to see some of the kind of more out there uses.
[1292.02 --> 1297.96]  One of them being, for example, somebody trained a model to detect human faces in, you know,
[1298.04 --> 1299.18]  everyday objects, essentially.
[1299.30 --> 1301.68]  So like clouds and textures and stuff like that.
[1301.94 --> 1304.92]  And you could have given me like a million guesses and I never would have guessed that
[1304.92 --> 1306.62]  that was something people would do with the data set.
[1306.62 --> 1307.96]  So that was cool to see.
[1308.36 --> 1310.46]  And then you've got more serious kind of uses of it.
[1310.50 --> 1313.72]  So there's some researchers out of Cornell that are, they've written a paper.
[1314.08 --> 1318.04]  I don't think it's fully released yet, but it's basically trying to quantify and understand
[1318.04 --> 1320.58]  why people post to social media.
[1321.12 --> 1325.38]  So with everything going on in politics and across different social networks, one of their
[1325.38 --> 1330.44]  main focuses was understanding and detecting kind of the different motivations between why
[1330.44 --> 1333.88]  people post and trying to, I guess, find some authenticity in that.
[1333.88 --> 1337.26]  And so they've been using the unsplashed data set to try and inform that.
[1337.66 --> 1339.42]  So that's been, you know, really cool as well to see.
[1339.58 --> 1343.86]  You know, it'd be really interesting to see as practitioners use these, you know, for some
[1343.86 --> 1346.80]  of these use cases you're talking about and others going forward, they're gonna have to
[1346.80 --> 1351.38]  go through the process of labeling the data in a lot of cases, you know, for any kind of
[1351.38 --> 1352.24]  supervised learning.
[1352.76 --> 1356.40]  And so it would be interesting to see if some of those might contribute back some of the
[1356.40 --> 1360.60]  labeling for some of the photos to add to the data set just to make future users
[1360.60 --> 1360.90]  easier.
[1360.90 --> 1364.82]  So that would be an interesting way for somebody to contribute back, I would say.
[1365.32 --> 1365.66]  Yeah, absolutely.
[1365.76 --> 1369.66]  I know the Cornell researchers were talking about contributing it back because they spent
[1369.66 --> 1371.66]  a bunch of money labeling.
[1371.96 --> 1375.02]  And so I think it'd be, I think they're open to that, which would be cool to see.
[1375.26 --> 1375.66]  Fantastic.
[1375.82 --> 1375.94]  Yeah.
[1375.96 --> 1380.86]  There's another use case that we have is people using the data set as kind of a, to
[1380.86 --> 1385.22]  get out stats for the photography industry in general, because there's actually a lot of
[1385.22 --> 1386.56]  information in there.
[1386.56 --> 1393.16]  If you look at, for example, Exif data, you have camera model, camera brand, stuff like
[1393.16 --> 1393.40]  that.
[1393.48 --> 1396.42]  And that can give you a lot of information about the state of the industry.
[1396.70 --> 1401.98]  And we've seen a couple of articles writing about that and leveraging the data set to get
[1401.98 --> 1404.54]  some insights about the industry already.
[1404.80 --> 1405.40]  So that's great.
[1405.40 --> 1405.96]  Yeah.
[1405.98 --> 1409.10]  And I think what was cool about those data sets is, you know, people have done that already
[1409.10 --> 1411.56]  with Flickr data sets and 500 pixels.
[1411.56 --> 1415.96]  But what's different about the data set with Unsplash is people aren't going and bulk uploading,
[1416.12 --> 1420.18]  you know, every photo that they take, which can skew the data set in a certain way.
[1420.24 --> 1424.68]  You know, if I go and I upload every photo of my family to Flickr, that skews the data
[1424.68 --> 1426.02]  set towards whatever I have.
[1426.02 --> 1430.40]  But with Unsplash, it's this different thing, which is kind of what are the best photos being
[1430.40 --> 1430.96]  taken with?
[1431.08 --> 1434.34]  So is the mobile industry really like mobile photography?
[1434.54 --> 1438.72]  How much is that impacting professional or high end photographers?
[1439.12 --> 1443.76]  And we're seeing different results when you analyze it with Unsplash versus, you know, a
[1443.76 --> 1448.48]  different story that you would get with Flickr where the iPhone and, you know, Android smartphones
[1448.48 --> 1451.54]  are just completely dominating the camera industry.
[1451.54 --> 1457.70]  Yeah, it's interesting to me on that front, a lot of image data sets that you can download
[1457.70 --> 1464.68]  in sort of typical AI sort of tutorials, initial computer vision work and that sort of thing
[1464.68 --> 1466.94]  are actually fairly low resolution.
[1467.48 --> 1473.98]  So, you know, we're talking like maybe 227 pixels where, you know, something like that.
[1474.10 --> 1480.56]  It sounds like the data set from Unsplash is definitely that sort of higher quality in terms
[1480.56 --> 1486.14]  of the actual photographs, but then also, you know, scrutinized according to, you know,
[1486.20 --> 1489.36]  people not just uploading everything, but there's a curation process.
[1489.80 --> 1492.08]  There's photos coming in that are validated.
[1492.60 --> 1498.04]  Could you speak a little bit to that in terms of, you know, the properties, generally speaking,
[1498.16 --> 1504.48]  the sort of properties of the photos in terms of resolution and then also like just the scrutiny
[1504.48 --> 1508.94]  that people give in terms of what they upload and the thought that goes behind that?
[1508.94 --> 1509.50]  Yeah.
[1509.68 --> 1514.74]  So I think that's the central, if we're going to start, what is the major difference between
[1514.74 --> 1517.76]  Unsplash's data set and some of those other ones which exist out there?
[1517.80 --> 1521.38]  Because obviously there's a ton of, you know, image data sets that already exist and some
[1521.38 --> 1523.94]  of them have more photos in them than Unsplash.
[1524.68 --> 1529.44]  Fundamentally, the quality of these photos from just a pure technical perspective, every
[1529.44 --> 1532.12]  image I think has to be a minimum of five megapixels.
[1532.36 --> 1535.90]  On average, I think the real size is above eight megapixels.
[1535.90 --> 1540.42]  You probably see like a cluster of images at like eight megapixels and then a cluster
[1540.42 --> 1542.34]  at like 12 or 15 roughly.
[1542.66 --> 1547.14]  So it's right away, every image is high definition and can, you know, and contains a lot of pixel
[1547.14 --> 1548.54]  information in it.
[1548.92 --> 1554.36]  Then as Tim hinted at before, we use a curation process where a human actually reviews every
[1554.36 --> 1555.52]  single image that comes in.
[1555.74 --> 1562.22]  So right away, you filter out all the, let's call it spam images from it.
[1562.22 --> 1567.78]  And then you also have a thing where on Unsplash, people don't upload photos, you know, that
[1567.78 --> 1568.92]  look exactly the same.
[1568.98 --> 1572.54]  They don't go and upload their entire camera roll where they've taken 20 photos of the
[1572.54 --> 1574.28]  same thing from slightly different angles.
[1574.70 --> 1577.70]  It's really, you know, they upload the best of what they have.
[1578.08 --> 1584.08]  And so you're getting a potentially smaller data set in terms of the number of images,
[1584.08 --> 1589.08]  but a much more broad data set in terms of the types of photos you're going to see and
[1589.08 --> 1590.24]  the quality of those photos.
[1590.24 --> 1594.98]  And so we think right away, that's something unique and can provide a different perspective.
[1595.60 --> 1599.44]  Especially, you know, if you're interested in looking at the idea of what makes a good
[1599.44 --> 1604.58]  photo or what makes something beautiful or how to help people take better photos, this
[1604.58 --> 1606.34]  is a great data set right away for that.
[1607.06 --> 1612.20]  You know, it occurs to me that you're almost creating a niche market and that you started
[1612.20 --> 1617.14]  Unsplash for the purpose of kind of offering creative assets, you know, out there that are
[1617.14 --> 1623.72]  very high quality and maybe, you know, initial users were creatives who were looking for those
[1623.72 --> 1627.08]  amazing photos to include in their websites or whatever it is they're working on.
[1627.54 --> 1632.84]  But now that you're making this available for ML and you develop a community around the
[1632.84 --> 1636.28]  ML use cases, it might push the creative side as well.
[1636.28 --> 1642.84]  And that you now have the potential of saying, if you move into, you know, AI based curation
[1642.84 --> 1647.70]  and stuff, then you have with this somewhat unique data set, as you just were discussing
[1647.70 --> 1654.46]  like that high end high quality imagery, then you could actually curate from a website level,
[1654.46 --> 1658.70]  for instance, that wants to refresh constantly to where every time you're there, you're getting
[1658.70 --> 1659.28]  new things.
[1659.28 --> 1663.86]  And you could, you could have a model that's trained to pick out certain types of images
[1663.86 --> 1668.30]  and download those directly for there so that you can have refreshed creative.
[1668.50 --> 1674.00]  It may be a human that starts it off, but then you have ML kind of driving a user experience
[1674.00 --> 1677.94]  that's ever refreshing, which is a really interesting idea to me.
[1678.08 --> 1682.26]  And that, you know, you could, instead of just randomly picking something, you can have something
[1682.26 --> 1686.12]  that is curated at that level for, you know, a really nice website.
[1686.12 --> 1686.98]  Yeah, absolutely.
[1687.10 --> 1688.42]  Chris, you got to come join our product team.
[1688.56 --> 1692.28]  You've been, I've had like two, two, two of our ideas right away on this podcast.
[1693.50 --> 1694.38]  You're quicker than us.
[1694.42 --> 1695.52]  It took us months to get there.
[1695.78 --> 1695.90]  Yeah.
[1695.90 --> 1699.62]  We've got a review team who would love for us to be able to make their jobs a bit easier
[1699.62 --> 1701.50]  and, and do some stuff like that for sure.
[1701.64 --> 1703.56]  I think that's in the future for us, for sure.
[1703.56 --> 1718.48]  Changelog++ is the best way for you to directly support practical AI.
[1719.00 --> 1724.74]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer
[1724.74 --> 1729.40]  to the metal and help sustain our production of practical AI into the future.
[1729.40 --> 1736.14]  Simply follow the Changelog++ link in your show notes or point your favorite web browser
[1736.14 --> 1738.46]  to changelog.com slash plus plus.
[1738.46 --> 1742.70]  Once again, that's changelog.com slash plus plus.
[1744.00 --> 1746.42]  Changelog++ is better.
[1759.40 --> 1771.48]  So because this is practical AI, and as Chris knows, I'm always probably prone to jumping
[1771.48 --> 1775.96]  into details because I'm thinking there, there may be other people listening to this that
[1775.96 --> 1780.88]  are at companies that have sort of a wealth of, of data.
[1780.88 --> 1787.54]  And, you know, I'm even thinking at, at SIL, we have so much data in our archives.
[1787.54 --> 1793.66]  That's like so valuable for so many reasons, but it's definitely not, you know, available
[1793.66 --> 1794.46]  in this way.
[1794.46 --> 1797.60]  And the access patterns are not similar to what you were saying.
[1797.68 --> 1802.68]  Traditionally, you had certain access patterns for your data on Splash that weren't like downloading
[1802.68 --> 1804.46]  a million images at a time.
[1804.46 --> 1811.34]  I'm curious about maybe this one is for Tim in terms of thinking about, okay, we're going
[1811.34 --> 1813.36]  to open up a bunch of this data.
[1814.14 --> 1820.36]  How do we deal with the side of things about, you know, what if a bunch of people all of a
[1820.36 --> 1824.06]  sudden start to want to download millions of images at a time?
[1824.06 --> 1831.98]  And, you know, how do we support this sort of bandwidth and storage and infrastructure that's
[1831.98 --> 1839.12]  going to be required to provide this data in a reasonable way while not jeopardizing the
[1839.12 --> 1841.84]  sort of main functions that we do as a business?
[1841.98 --> 1842.64]  Any thoughts there?
[1842.98 --> 1843.76]  You want to take this, Luke?
[1844.62 --> 1849.96]  I should probably take this one just because, yeah, I mean, I think our thing to start with
[1849.96 --> 1855.66]  is, is we always try to release things as broadly as possible and then work backwards to restrict
[1855.66 --> 1856.52]  it if we need to.
[1856.68 --> 1860.02]  You do get a lot of bad actors out there, unfortunately, especially at scale.
[1860.02 --> 1863.74]  And we've, we've seen that over the years with Unsplash is it's, you know, our API start
[1863.74 --> 1865.88]  out as broad as we could make it.
[1865.96 --> 1869.12]  And then we've had to put in place certain restrictions in terms of, you know, don't
[1869.12 --> 1874.20]  use it to create competing products where you just, you know, resurface these images or
[1874.20 --> 1874.56]  whatever.
[1874.90 --> 1878.98]  The data set, you know, has that potential where people could go out and potentially,
[1879.18 --> 1882.60]  you know, spam it and download it a ton of times.
[1882.76 --> 1886.00]  You're going to get access to all the image URLs that we have.
[1886.00 --> 1890.24]  And you could, you know, try and mess with our CDN and stuff like that.
[1890.38 --> 1894.82]  But fundamentally, we've seen over the years that those number of people that, you know,
[1895.20 --> 1898.64]  they make up a really small percentage of the community that's out there.
[1899.00 --> 1903.74]  And so we try and focus on the good of it and starting with that and trying to make sure
[1903.74 --> 1906.90]  we, we don't restrict the good uses as much as possible.
[1906.90 --> 1911.78]  So in terms of how we got it through, in terms of, you know, how do you convince people inside
[1911.78 --> 1913.20]  your company to open up data?
[1913.54 --> 1917.46]  I think we're lucky in a lot of ways in the, you know, as I was saying, we're a very small
[1917.46 --> 1917.80]  company.
[1917.90 --> 1920.80]  And so it really is a conversation where it's like me and Tim are like, wouldn't that be
[1920.80 --> 1921.04]  cool?
[1921.18 --> 1922.34]  Yeah, let's do it kind of thing.
[1922.56 --> 1925.52]  So I get in, you know, other companies, it's a lot harder.
[1926.14 --> 1930.20]  But we do deal with that, you know, from an image standpoint is we work with a lot of big
[1930.20 --> 1933.82]  institutions who want to make their archives open and accessible.
[1934.46 --> 1938.34]  And getting that through the higher levels is hard.
[1938.54 --> 1941.82]  People want to hoard onto data in whatever form it is.
[1941.90 --> 1947.40]  And I think we're making progress as a, you know, as a society towards this idea that openness
[1947.40 --> 1954.28]  can have second or third order effects that are harder to project and put right in the bottom
[1954.28 --> 1954.94]  line right there.
[1955.04 --> 1959.86]  But they can have this greater effect on your goodwill, on your community, on,
[1960.20 --> 1962.16]  a whole bunch of different things about your organization.
[1963.00 --> 1964.34]  And we're getting there.
[1964.64 --> 1967.90]  It's, I think we're still, you know, there's a lot of people that want to lock it down and
[1967.90 --> 1968.58]  hoard stuff.
[1969.36 --> 1975.00]  But I've yet to see, you know, people always talk about the advantages of data and how,
[1975.10 --> 1976.86]  you know, they're building a data advantage over people.
[1976.98 --> 1980.32]  I think for a lot of companies, there isn't really actually a data advantage.
[1980.32 --> 1986.76]  You can hoard onto that data, but there's not a ton of value, at least commercially in that
[1986.76 --> 1987.20]  data.
[1987.20 --> 1991.26]  And so opening it up to other people can, can have a second or third order effect on
[1991.26 --> 1991.78]  your business.
[1991.78 --> 1992.88]  And so they should consider it.
[1992.88 --> 1997.46]  I was just going to say, and it's not a question, just to comment to what you just said, is that
[1997.46 --> 2003.60]  working in a large industry for large companies, as I do, I'm seeing companies like yours with
[2003.60 --> 2008.08]  the cultures that you're just now talking about having that impact in larger companies and
[2008.08 --> 2015.04]  companies that have typically been very large and very closed are looking at what kinds of
[2015.04 --> 2016.68]  work companies like yours are doing.
[2016.90 --> 2021.12]  And they're starting to make those changes, not only in industry, but also in government,
[2021.24 --> 2021.56]  actually.
[2021.78 --> 2025.54]  So you are collectively having the impact that you're striving for.
[2025.62 --> 2026.52]  I just wanted to note that.
[2026.88 --> 2027.94]  I really hope so.
[2028.04 --> 2031.42]  And there's a lot of people out there doing a lot of work.
[2031.52 --> 2032.98]  And we're just one small piece of that.
[2032.98 --> 2036.78]  But I've noticed that with governments is governments, I think, are coming around to
[2036.78 --> 2036.90]  it.
[2036.96 --> 2041.12]  And you're seeing it, you know, I think probably led first and foremost by open source software,
[2041.12 --> 2046.32]  like we've seen over the last 20 years or something, how roughly, you know, every major
[2046.32 --> 2047.84]  company now contributes to open source.
[2047.94 --> 2050.68]  And there's a selfishness to why they're actually doing it as a company.
[2050.68 --> 2055.58]  But the fact that we were able to get these companies to that point is, you know, testament
[2055.58 --> 2057.42]  to the work that people did back then.
[2057.42 --> 2061.14]  And I'm hoping that, you know, if you fast forward 10, 15, 20 years, you're going to
[2061.14 --> 2065.10]  see people being in a similar position from data where they can actually say, hey, if we
[2065.10 --> 2069.30]  do this, which is beneficial to everyone, it also has a benefit to us.
[2069.52 --> 2072.82]  And if we have to be the guinea pigs for that, we're happy to be the guinea pigs.
[2072.82 --> 2079.42]  And it sounds like that you are instituting some sort of like versioning aspects to the
[2079.42 --> 2080.90]  data set that you're releasing.
[2082.04 --> 2085.32]  Tim, what was your thought process around that?
[2085.32 --> 2089.86]  And then maybe also like there's all sorts of different formats that you could release,
[2089.86 --> 2092.04]  you know, data sets in.
[2092.16 --> 2099.58]  You could just, you know, put up some archive files on S3 and have people download like a
[2099.58 --> 2108.28]  big thing where the decisions around how you release this data related to how your infrastructure
[2108.28 --> 2112.42]  had, you know, in the past supported people downloading images.
[2112.64 --> 2114.62]  What was your thought process around that?
[2114.62 --> 2115.26]  Yeah.
[2115.26 --> 2115.32]  Yeah.
[2115.46 --> 2122.60]  So regarding the archive versus the links in the CSV, I think it's mainly because as
[2122.60 --> 2125.28]  a data engineer, I'm not directly working.
[2125.86 --> 2130.46]  I mean, because I'm not working in AI, I'm not directly working with the image itself.
[2130.96 --> 2133.74]  And so I'm working mostly with the metadata.
[2134.50 --> 2140.36]  And so the closest thing I can see from the image or the easiest thing accessible is just
[2140.36 --> 2140.86]  its link.
[2140.86 --> 2141.28]  Right.
[2141.76 --> 2148.16]  And we currently have the infrastructure that allows us to basically power thousands of
[2148.16 --> 2149.58]  integrations on the internet.
[2149.58 --> 2155.72]  And so we might as well leverage that for people to download every single photo through
[2155.72 --> 2156.58]  the link in the CSV.
[2156.90 --> 2157.02]  Right.
[2157.02 --> 2159.86]  So I think that was the main thought process.
[2160.30 --> 2166.70]  Regarding versioning, I think that's also kind of a way to stay flexible.
[2167.26 --> 2173.28]  So if you add the image to your archive, then it's kind of like frozen in time and you have
[2173.28 --> 2174.14]  that thing.
[2174.14 --> 2180.12]  Like, whether if you have a link, then it's much easier to say, I don't know, maybe today
[2180.12 --> 2184.06]  you're restricting a certain amount of pixels and tomorrow you don't want to do that anymore.
[2184.28 --> 2185.32]  You have that flexibility.
[2185.96 --> 2188.84]  And we can find that flexibility all across the data set.
[2189.38 --> 2189.50]  Yeah.
[2189.58 --> 2194.68]  And I've mentioned that we want to keep adding more info, adding more things.
[2194.68 --> 2197.60]  And that's why versioning is kind of essential.
[2198.00 --> 2204.10]  It's super essential in like, if we have that feedback loop model where we have new contributions
[2204.10 --> 2207.32]  coming in, we need to have some kind of versioning in place.
[2207.86 --> 2209.14]  So yeah, that's the thought process.
[2209.22 --> 2211.80]  Kind of like always staying the most flexible we can.
[2212.32 --> 2213.30]  And yeah, that's the idea.
[2213.30 --> 2219.64]  I noticed you have like the GitHub repo that talks about the data set from the people that
[2219.64 --> 2225.72]  are making those downloads to access your data in a new sort of way or for new purposes
[2225.72 --> 2226.86]  and training models.
[2227.02 --> 2234.48]  Have you got feature requests in terms of the image metadata or like new access patterns or
[2234.48 --> 2240.24]  other things that maybe you didn't expect or fundamentally different from the ways that
[2240.24 --> 2245.58]  your users that are just accessing one image at a time or browsing or requesting?
[2246.08 --> 2250.82]  So right when we published the data set, I think it gained a bit of like traction and
[2250.82 --> 2252.52]  people started using it directly.
[2252.70 --> 2254.64]  So we quickly had feedback essentially.
[2255.22 --> 2258.82]  Mostly it was about some data quality points.
[2259.16 --> 2264.00]  So, hey, you should watch this field because there's an unexpected value over there that we
[2264.00 --> 2265.12]  didn't find essentially.
[2265.56 --> 2267.76]  And so the feedback is really nice in that way.
[2267.76 --> 2275.16]  Regarding unexpected uses, I think for V1, we tried to provide with kind of like our vision
[2275.16 --> 2278.06]  of what could be useful for machine learning and AI.
[2278.76 --> 2283.64]  So yeah, colors, keywords, geolocation, things like that.
[2283.76 --> 2290.56]  And the data requests that we had, I don't think there was anything super surprising at the
[2290.56 --> 2291.60]  time currently.
[2291.60 --> 2298.14]  But we had some feature requests, including data that we actually have and we didn't put into the
[2298.14 --> 2298.62]  data set.
[2298.98 --> 2303.08]  Things like pixel density or color or things like that.
[2303.20 --> 2306.82]  Some very specific data that we didn't plan to add.
[2307.40 --> 2310.88]  And so that gave us insight into, hey, the community might want this.
[2310.98 --> 2313.28]  So we might add that into the next version.
[2313.28 --> 2318.12]  And so we're trying to expose the versioning into our GitHub repo as well.
[2318.38 --> 2322.50]  And we're trying to expose the information of what's going to be in the next feature and
[2322.50 --> 2323.74]  what's going to be in the next release.
[2324.30 --> 2330.54]  And so if you have any suggestion, any feedback, you can just go on the GitHub repo and ask for
[2330.54 --> 2330.72]  it.
[2330.78 --> 2333.34]  And we'll try to answer and plan it for our next release.
[2333.72 --> 2334.14]  That's awesome.
[2334.34 --> 2338.96]  I think that kind of leads into a natural next question, which is it's kind of the creative
[2338.96 --> 2339.42]  question.
[2339.42 --> 2340.58]  And so I'm going to add it.
[2340.62 --> 2341.44]  I want to ask both of you.
[2341.52 --> 2343.72]  I'm curious from both a business and a technical perspective.
[2344.36 --> 2349.50]  And I want you to wax poetic just a little bit and kind of like when you're sitting around
[2349.50 --> 2353.22]  talking together, what are some of the aspirations on where you want this to go?
[2353.58 --> 2355.04]  What are some of the cool ideas?
[2355.16 --> 2356.18]  And you're not committed to it.
[2356.24 --> 2357.94]  Nobody in the audience is holding you to this.
[2358.06 --> 2362.70]  But what are cool things you can think of that you would like to see at any time frame
[2362.70 --> 2367.32]  down the road going forward, whether you're able to do it, whether that's a practical
[2367.32 --> 2368.80]  thing or not even a practical thing?
[2368.80 --> 2371.42]  I just love to hear what the creativity about how you see the future.
[2372.00 --> 2376.84]  The one that I'm really excited about or the data that I think is really unique, again,
[2376.88 --> 2377.82]  with this data set.
[2377.90 --> 2380.92]  And it's I think the data that we have in there is a good start.
[2381.30 --> 2383.46]  We still have some ideas for where we want it to go.
[2383.94 --> 2389.46]  Specifically, the data around search conversions and the collections, I think is really unique.
[2389.96 --> 2391.98]  There are data sets, again, out there that do this.
[2391.98 --> 2396.78]  But at the volume that we're going to get to, especially in the second or third releases
[2396.78 --> 2402.18]  of the data set, I think it starts to become really a unique data set there.
[2402.50 --> 2408.30]  And what's cool about it is people search on Unsplash for very abstract things.
[2408.60 --> 2413.54]  It's really, you know, when you look at the types of images that are on Unsplash and what
[2413.54 --> 2416.96]  they're downloaded and used for, it's not, you know, find me the dog photo.
[2416.96 --> 2420.48]  Find me the photo of the cup or the coffee cup in this image.
[2420.62 --> 2426.78]  It's like, you know, it's very abstract stuff like love or happiness or depression or like,
[2426.84 --> 2431.64]  you know, a whole bunch of things which are harder, I think, at the current stage, at least
[2431.64 --> 2434.68]  for vision models to really understand and quantify.
[2434.98 --> 2439.22]  But we're getting this real time feedback of millions of people going on Unsplash,
[2439.30 --> 2443.18]  searching these things, scouring all the different photos, collecting them into these different
[2443.18 --> 2446.94]  collections in different groupings, and then interacting with them in different
[2446.94 --> 2447.24]  ways.
[2447.86 --> 2452.82]  And we've exposed that data in kind of a V1 version, but we have, you know, a lot more
[2452.82 --> 2454.98]  internal data that we want to expose around that.
[2455.06 --> 2459.90]  And I think if we can expose that in the right ways, and again, I'm no machine learning expert,
[2459.90 --> 2460.68]  so I have no idea.
[2460.68 --> 2466.96]  But my hope is that that can start to improve the models that are out there around understanding
[2466.96 --> 2467.26]  that.
[2467.82 --> 2471.90]  And that would be, you know, a huge win, I think, because we experience that ourselves is
[2471.90 --> 2479.08]  when we upload on, you know, images to Unsplash, the quality of the tagging for them is quite
[2479.08 --> 2483.16]  limited in terms of it can recognize what's in the images, but can't represent what does
[2483.16 --> 2484.22]  this image actually mean.
[2484.74 --> 2486.90]  And so if we can help improve the industry there,
[2487.46 --> 2489.32]  kind of semantic meaning in that sense.
[2489.52 --> 2490.04]  Yeah, exactly.
[2490.18 --> 2491.76]  Like abstract semantic meaning.
[2491.84 --> 2494.90]  Like, I think that's the next step in vision learning.
[2494.90 --> 2496.34]  And I understand why it's super hard.
[2496.34 --> 2499.44]  But our hope is that maybe we can contribute back in some way to that.
[2500.00 --> 2500.26]  Very cool.
[2500.58 --> 2500.94]  Awesome.
[2501.24 --> 2503.84]  Tim, any thoughts in addition to that?
[2504.06 --> 2505.80]  I think that sums it up pretty well.
[2506.00 --> 2506.60]  I think that's fine.
[2506.68 --> 2507.10]  I think that's fine.
[2507.14 --> 2511.08]  I was going to go on, like, go far back on a previous subject.
[2511.36 --> 2513.08]  Let's not do that.
[2513.20 --> 2513.88]  All good.
[2513.98 --> 2514.88]  I stole your answer, Tim.
[2515.16 --> 2515.38]  Sorry.
[2516.20 --> 2516.74]  All good.
[2516.98 --> 2521.74]  I'm very excited that you took the time to join us on the podcast.
[2521.74 --> 2526.60]  I hope and I anticipate that you'll get some usage out of this.
[2526.74 --> 2532.02]  And I hope that it connects with the AI community and they start investigating those more subtle
[2532.02 --> 2538.82]  things that are included in the data set and other things that none of us on this call probably
[2538.82 --> 2542.34]  can even predict or expect that people will use it for.
[2542.80 --> 2548.16]  We'll include in our show notes a link to the data set and a link to Unsplash other resources.
[2548.82 --> 2549.66]  Please check it out.
[2549.66 --> 2552.56]  And yeah, let us know in our Slack channel.
[2552.70 --> 2556.44]  You can join our Slack at changelog.com slash community.
[2556.82 --> 2561.10]  And let us know in our Slack if you're downloading the data set and what you're using it for.
[2561.30 --> 2563.42]  And yeah, we're excited to hear.
[2563.66 --> 2566.58]  So thank you, Luke and Tim, for joining us.
[2566.62 --> 2567.52]  Really appreciate it.
[2567.60 --> 2572.18]  And can't wait to see what happens with this data set in the future.
[2572.70 --> 2573.36]  Thanks for having us, guys.
[2573.78 --> 2574.30]  Thank you, guys.
[2574.30 --> 2584.36]  Come hang out with Daniel, Chris, and hundreds of other AI practitioners in our community Slack.
[2584.52 --> 2585.70]  It's a cool place to be.
[2585.80 --> 2586.76]  Not a lot of noise.
[2586.94 --> 2587.88]  Some great signal.
[2588.06 --> 2589.70]  And best of all, it's totally free.
[2590.08 --> 2592.42]  Check it out at changelog.com slash community.
[2593.02 --> 2597.56]  And don't forget to follow the show on Twitter for AI news and links, highlights from past episodes,
[2597.64 --> 2598.24]  and more.
[2598.24 --> 2600.36]  We are at Practical AI FM.
[2600.58 --> 2601.76]  We'd love to have you following along.
[2602.10 --> 2605.94]  Thanks to Daniel and Chris for hosting Practical AI week in and week out.
[2606.10 --> 2610.40]  To the mysterious Breakmaster Cylinder for the excellent beats you hear on all changelog podcasts.
[2610.72 --> 2614.82]  To our sponsors who have our back, Fastly, Linode, and LaunchDarkly.
[2615.06 --> 2615.96]  And to you for listening.
[2616.26 --> 2617.88]  We appreciate your time and attention.
[2618.40 --> 2619.70]  That's all we have for you today.
[2620.12 --> 2626.56]  On the next episode, Chris and Daniel chat with the team at Microsoft all about their new research to product milestones.
[2626.56 --> 2630.18]  That's coming at you, so stay tuned next week.
