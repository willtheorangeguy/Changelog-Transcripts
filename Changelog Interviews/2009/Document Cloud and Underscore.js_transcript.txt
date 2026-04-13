[0.00 --> 20.08]  Hello and welcome to the ChangeLog episode 0.0.5.
[20.18 --> 21.32]  My name is Adam Stachowiak.
[21.70 --> 22.62]  And I am Wynne Nutherland.
[22.70 --> 26.42]  We've got a great interview today with Jeremy Aschenkis from DocumentCloud.
[26.70 --> 26.92]  Yeah.
[27.40 --> 28.58]  I think that one turned out really well.
[28.58 --> 30.50]  Some exciting projects coming out of DocumentCloud.
[30.76 --> 33.16]  We're five episodes into this podcast.
[33.96 --> 36.02]  So how close are we to figuring out our format?
[36.84 --> 37.62]  I think we're getting there.
[37.74 --> 44.40]  I think it's an iterative process, but lots of small little tweaks along the way, light little tweaks.
[44.58 --> 51.62]  But I think the format of having the weekly roundup and then also having interviews coupled into that is a nice fit.
[51.70 --> 54.48]  It would be nice to have some guest contributors come on to the show too.
[54.50 --> 56.92]  So we're pioneering Agile podcasting.
[56.92 --> 57.40]  Yeah.
[58.58 --> 62.20]  Who would you like to see come on as a guest contributor, Wynne?
[63.12 --> 64.48]  You know, a lot of names out there.
[64.52 --> 69.92]  I don't want to share probably any of them in case they're too good to come on our little show.
[70.36 --> 71.10]  On our little show.
[71.22 --> 74.58]  Well, I mean, we was – I guess we're somewhat little.
[74.68 --> 78.58]  I mean we got just a little over 100 followers in the last few days.
[78.68 --> 79.10]  I think that's –
[79.10 --> 80.96]  Yeah, zero to 100 in a week is not bad.
[81.12 --> 82.34]  Yeah, that's real nice.
[82.34 --> 89.74]  And certainly the blog article on GitHub.com, their blog, helped us out a lot.
[89.74 --> 95.62]  I really think the podcast will take off when the community gets to embrace it.
[95.98 --> 100.04]  And we get – the news is more than just what we're scouring to find.
[100.12 --> 102.80]  We've got the community crowdsourcing this deal.
[102.90 --> 115.12]  So if you've got a great story out there, what's new and exciting and open source, just submit to submit at the changelog.com via email or just go out to the website, the changelog.com slash submit.
[115.12 --> 118.32]  But we'd love to get that news up on the site.
[119.64 --> 119.92]  Yeah, absolutely.
[120.02 --> 123.34]  I'm looking forward to – we haven't gotten any submissions yet, and that's kind of a shame.
[124.28 --> 133.88]  I really – not that we need people to start contributing, but it would be nice to have somebody alert us besides us just kind of picking up what we find.
[134.82 --> 141.96]  Yeah, I'd like to see what pools of information people are drawing from outside of the ones I'm fishing in.
[142.04 --> 142.38]  How about you?
[142.66 --> 143.78]  Yeah, no, I agree.
[143.78 --> 147.78]  I mean I don't want to be Ruby-centric, and I don't want to be a very language-specific.
[148.64 --> 152.16]  I want to be agnostic about what we're doing here, and I think that's always our approach.
[152.26 --> 156.28]  But you and I tend to just jump in those worlds, and those are the ones that are most fresh to us.
[156.44 --> 161.18]  So if you've got something out there in a different language, let us know.
[162.24 --> 162.56]  Absolutely.
[163.38 --> 166.20]  Well, we've got a great interview today with Jeremy Ashinkos from Document Cloud.
[166.30 --> 170.72]  We talked about three of his great projects, and I think it's a really dynamic interview.
[170.72 --> 174.74]  They're doing some exciting things in the media primary news source space.
[174.92 --> 176.04]  So how about we get to it?
[176.40 --> 177.34]  Yeah, let's get to it.
[177.56 --> 178.10]  Enjoy the show.
[178.10 --> 189.30]  All right, we're here with Jeremy Ashinkos, and Jeremy is with Document Cloud.
[189.44 --> 193.56]  Jeremy, explain a little bit about what Document Cloud is and what it's doing.
[194.10 --> 194.48]  Sure.
[194.48 --> 199.68]  So Document Cloud is a new project that I'm really happy to have started with in August.
[200.22 --> 217.54]  It's a grant funded generously by the Knight Foundation for a two-year project to help make the primary source documents that the New York Times and the Washington Post and the Chicago Tribune and all of these major news organizations are gathering when they're writing their stories.
[217.54 --> 235.22]  To help make these primary source documents that you'd get from the government, you'd get from Freedom of Information Act requests, you'd get from doing good investigative reporting, to make those public and to make them searchable online, to make them able to be embedded alongside news articles for context and to make richer stories.
[235.22 --> 245.82]  And one of the nice perks of this project is that the Knight Foundation has mandated that everything that we produce be open source and be released open source.
[245.94 --> 256.42]  So as we've been going along, I've been trying to split off the sort of atomic chunks of the Document Cloud project as little open source projects and release them.
[256.48 --> 257.82]  And it's gotten a great response so far.
[257.82 --> 276.92]  And we've had a whole bunch of community contribution that has really helped improve the three things that we've released so far being Cloud Crowd, which is a parallel processing sort of framework for Ruby that's a little bit MapReduce inspired, although a little bit more practically oriented, I think, for your day-to-day workflow than a pure MapReduce like Hadoop.
[277.68 --> 283.80]  Jamit, which is an asset packager plugin for Rails that we just launched a couple weeks ago.
[283.80 --> 306.30]  And underscore.js, which is a collection of functional programming helpers for jQuery to give you those Ruby-style map, inject, select, fold left, fold right kinds of array and object functions that you don't always have cross-browser in JavaScript, but that is very nice to have as kind of a standard library base.
[306.70 --> 309.22]  Awesome. Those are three exciting projects to open the gate with.
[309.32 --> 311.36]  How about yourself? What's your role at Document Cloud?
[311.36 --> 316.16]  I'm the – it's kind of my pet project at the moment.
[316.26 --> 329.04]  We're looking actually, which I should mention here in case anyone out there is listening, not necessarily in New York, but we're looking to hire more help both with JavaScript and with Ruby, Postgres, EC2 backend stuff.
[329.14 --> 332.82]  But right now it's just me building out the initial prototype of it.
[334.08 --> 337.84]  And yeah, so I'm the lead developer, I guess, is my technical job title.
[337.84 --> 346.40]  So the Knight Foundation, why did they – I mean I kind of understand why, but do you have some background to why they wanted everything to be open sourced?
[346.84 --> 348.20]  It's part of the mandate.
[348.30 --> 358.98]  So they have this thing called the Knight News Challenge, and the idea is to fund interesting technology slash journalism projects to help figure out what the future of journalism is going to end up looking like.
[358.98 --> 365.22]  So they were the ones who funded every block to the tune of about a million dollars a couple years ago, which is I think their biggest name.
[366.42 --> 372.48]  But they fund five or ten projects, most of which are smaller scale than say a Document Cloud or an every block.
[372.48 --> 381.16]  And then the idea is that you end up producing pieces of technology that can help newsrooms transition to the internet age.
[382.24 --> 386.08]  And so to that end, everything that you do has to be open source code.
[386.26 --> 388.08]  That is in the contract, I think.
[388.20 --> 393.62]  Everything that the grant money is spent on is supposed to be towards the creation of these open source news projects.
[394.44 --> 394.84]  That's wild.
[395.00 --> 396.30]  So every block, too.
[396.30 --> 398.88]  I didn't realize that they supported that as well.
[398.88 --> 402.98]  So that's off topic, but every block is an awesome project.
[403.52 --> 408.92]  Yeah, that's why every block did that big code dump at the end of the project before they sold themselves was because that was the contract.
[409.42 --> 410.12]  I'm behind the news.
[410.18 --> 411.78]  I didn't hear that they sold themselves.
[412.58 --> 416.58]  Yeah, they were bought by MSNBC for an unknown amount.
[416.74 --> 423.90]  Yeah, so that was a nice exit for the team after the grant funding, you know, because this is a two-year grant, and at the end of the two years, we're going to have to figure out how to continue the project.
[423.90 --> 430.40]  So we don't have specific plans yet, but every block's method was to get bought by MSNBC, who's going to continue it.
[431.14 --> 431.24]  Wow.
[431.88 --> 433.76]  So what's your team size like?
[433.88 --> 436.44]  You said, is it just you, or do you have more people in your team?
[436.66 --> 442.70]  Well, we recently hired our second full-time person who's working on the administrative and dealing with all these news organizations who have signed up.
[442.70 --> 454.96]  On the documentcloud.org website, there's a list of partner orgs, but it's many of the major news organizations in the country, along with magazines like The New Yorker and The Atlantic Monthly and things of that nature.
[455.52 --> 460.18]  And I guess the overseas stuff is starting to expand a little bit more as well.
[460.24 --> 462.70]  There's been some interest in the UK.
[462.70 --> 467.70]  So she's our second full-time person.
[467.88 --> 477.66]  There's the three founders, Eric and Scott at ProPublica, and Aaron, who's the editor of the interactive news section at The New York Times, were the ones who got the grant in the first place.
[477.80 --> 482.50]  So they don't have too much time to devote to the project from day to day because they've still got their day jobs.
[483.32 --> 485.70]  But they are the, I guess they're sort of the board.
[486.10 --> 487.60]  Can you tell us about how this project got started?
[487.60 --> 492.62]  I guess I wasn't too much involved in the conceiving of the project stage.
[493.08 --> 497.64]  I got hired after the grant was a sure thing.
[497.82 --> 499.30]  So it's sort of been in the works for a long time.
[499.38 --> 516.42]  I think the three of them originally had the idea to make these primary source documents that are sort of passing through the filing cabinets of The New York Times, for example, to make them public and to make them accessible online and wanted to start a project to make that happen.
[516.42 --> 524.42]  So a big part of this is – I don't know if you guys have seen the document viewer that The New York Times does for a lot of their sources.
[524.90 --> 540.54]  For example, when they had a big Guantanamo project, they released a couple thousand – they started out as PDFs, but they became these sort of JavaScript, HTML web plug-ins on The Times' website where you could search through the court transcripts and the prison records of these inmates.
[540.54 --> 546.54]  And keep track of what exactly was going on on a detainee-to-detainee basis.
[547.28 --> 558.42]  So that particular piece of software, the document viewer that they're using to embed the stories on the web without having to just download PDFs, The Times is donating to this project.
[558.66 --> 562.72]  So part of what I've been working on has been integrating that with the document cloud prototype.
[562.72 --> 567.62]  And there's a new version of it that should be coming out shortly that you'll be able to find on the NewYorkTimes.com in a couple weeks.
[568.04 --> 568.96]  That is pretty cool.
[569.68 --> 575.36]  It's got a Google Books-like infinite scroll kind of a setup for these documents, and it's pretty nicely designed.
[575.86 --> 577.68]  So that should be – that's in the works right now.
[578.14 --> 581.72]  Do you see Document Cloud primarily being involved in the government space or –?
[581.72 --> 585.82]  It's the primary source document space.
[585.82 --> 590.86]  So it's all of these people – all these organizations whose mission is to uncover primary source documents.
[590.98 --> 602.86]  So whether that means it's government records or it's internal corporation memos or emails or anything, I guess, that becomes a primary document of record, I think we're interested in.
[602.94 --> 607.90]  And then beyond that, we might end up opening it up to more things like watchdog groups who are gathering these things.
[607.90 --> 611.32]  And yeah.
[611.90 --> 616.96]  So you mentioned these three projects, CloudCrowd, underscore JS, and Jamit.
[617.22 --> 621.12]  Are all three of these your creation or explain a little bit how each came about?
[621.94 --> 622.12]  Yep.
[622.22 --> 629.06]  They're three direct extractions from the Document Cloud prototype that I've been working on over the course of the fall.
[629.62 --> 637.52]  So one of our first problems was that importing PDFs into Document Cloud is a pretty slow, sort of painful process.
[637.90 --> 640.98]  Because you've got to split apart a PDF into a number of pages.
[641.54 --> 648.06]  And you've got to convert each page into both its full text and its images in different sizes to display it inside of the document viewer.
[648.82 --> 656.72]  And then you've got to – and part of this Document Cloud is that we're actually using the OpenKale web service to do semantic indexing of the documents.
[656.72 --> 662.72]  So we end up knowing what people and what places and what organizations and what terms are mentioned within a document.
[662.84 --> 664.06]  You can search across that kind of stuff.
[664.12 --> 667.92]  So we have to go to OpenKale and get that information back.
[667.98 --> 670.22]  And all of this is a very time-consuming, expensive process.
[670.22 --> 677.90]  So Cloud Crowd, which is our parallel processing framework, is sort of a generic – you have a job you need to get done in Ruby.
[678.26 --> 681.46]  And you can maybe parallelize it to a certain extent.
[681.54 --> 684.02]  And you'd like to do it in as parallel a fashion as possible.
[684.68 --> 688.54]  So the Cloud Crowd primitives are kind of – you write a Ruby script.
[688.62 --> 692.02]  You write a class that has at least a process method.
[692.08 --> 694.24]  And the process method is the parallel part of the computation.
[694.24 --> 697.36]  And it's all sort of web-based.
[697.60 --> 700.46]  So there's a REST API that – it comes as a gem.
[700.54 --> 703.00]  And when you install the gem, you get servers and nodes.
[703.18 --> 706.72]  And the server is the central thing that manages all of the work.
[706.80 --> 711.64]  And the nodes are these – are the actual machines that are performing the work.
[712.00 --> 716.00]  And when you install your action, all you have to do is say, okay, if I'm on a machine that's doing the work,
[716.06 --> 718.00]  what is the parallel part of the work that I'm going to do?
[718.28 --> 722.22]  And then you send it a URL to a file, in our case, a PDF.
[722.22 --> 727.58]  Although it could be a JSON document or some other kind of – or XML document or some other kind of information.
[728.62 --> 731.62]  And then you can do the processing on those documents in parallel.
[731.80 --> 733.42]  So in our case, we're doing the PDFs in parallel.
[734.24 --> 738.78]  And then the MapReduce plays in in that if you define more than just a process action,
[738.86 --> 744.70]  if you define a split and a merge, the split at the beginning will take a single input
[744.70 --> 748.78]  and divide it up into many to all be run in parallel across that process method.
[748.78 --> 752.82]  And then the merge will take back the results of what came out of all of your process calls
[752.82 --> 758.10]  and merge it back into a single result for convenient use consumption back at the other end
[758.10 --> 760.32]  when you get pinged back when your job finishes.
[761.06 --> 764.96]  So in our case, that means you take a PDF, you split it up into chunks of pages using CloudCrowd.
[765.40 --> 770.08]  Each five- or ten-page chunk gets processed in parallel to get the images out,
[770.18 --> 772.66]  to get the text out, to get the entities out through OpenClay.
[772.66 --> 777.78]  And then at the end, merge back together into a single archive that we can import back into the prototype.
[778.50 --> 784.78]  So in that – using this, we can install this gem on many EC2 machines if we need to
[784.78 --> 788.76]  and spin up CloudCrowd nodes very easily and start distributing the workout.
[789.10 --> 791.58]  So this can happen in a reasonably fast fashion.
[792.20 --> 796.76]  Is it EC2 and S3 only, or does it work with any sort of cloud platform?
[796.76 --> 802.06]  It works with any sort of – so it's not – there's actually no dependency on EC2.
[802.18 --> 803.70]  It's only on HTTP and REST.
[803.78 --> 806.28]  So you could install it on whatever kind of box you'd like.
[806.34 --> 809.60]  It's nice on EC2 because you can spin up and down these nodes on the fly very easily.
[810.62 --> 815.72]  There is an S3 file system backend built in because that's what we've been using
[815.72 --> 819.28]  where it will – when it transfers files between different machines.
[819.42 --> 820.62]  This has always been a problem in Hadoop.
[820.68 --> 824.96]  In Hadoop, you have to install this Hadoop FS where there's a common shared file system
[824.96 --> 827.22]  that all of the nodes can write to.
[827.46 --> 833.50]  So the CloudCrowd default file system backend is to use S3 as that sort of common shared file space.
[833.86 --> 835.86]  So when you're done – when they're done with an intermediate work unit,
[835.92 --> 839.90]  it'll save that work unit to S3, and then in the merge step later on,
[839.92 --> 843.40]  it can pull that from S3 and continue the processing without having to worry about transferring
[843.40 --> 846.30]  about which particular node has which copy of which file.
[847.06 --> 848.68]  But there's also a file system backend.
[848.84 --> 851.56]  So if you're just doing it on one box, if you only have one machine that you're doing work on,
[851.62 --> 852.60]  you can use the file system backend.
[852.70 --> 853.12]  It'll be faster.
[853.12 --> 860.40]  Or if you've got something like GFS or GlusterFS set up where you have a shared mounted networked file system,
[860.44 --> 864.18]  you can use that also for a faster than S3 performance.
[866.14 --> 872.14]  This is not technical really at all, but I'm curious to the kind of comments you get about the ASCII art in your readme.
[873.16 --> 874.22]  The CloudCrowd?
[874.32 --> 874.54]  I don't know.
[874.62 --> 876.48]  Not too many comments on the ASCII art.
[876.54 --> 880.32]  People have been more taken with the diagrams that are in the wiki than the ASCII art.
[880.60 --> 881.26]  I missed that part.
[881.26 --> 891.28]  Adam's an ASCII art fan and was convinced by looking at the readme for underscore.js that you had ripped off his signature ASCII art.
[891.48 --> 892.34]  Did I say ripped off?
[892.72 --> 893.84]  I didn't say ripped off.
[894.72 --> 903.04]  No, it's kind of funny though because your underscore.js ASCII art is – if you go and look at – I guess – I wonder if you have any sites out there now that actually do it.
[903.04 --> 908.42]  But at the top of every web document, we put this ASCII art that says handcrafted.
[908.50 --> 913.60]  And I think it was the exact same ASCII art font, I guess if that's what you would call it.
[913.84 --> 914.38]  I'm just kidding.
[914.92 --> 915.50]  I'm just kidding.
[915.62 --> 918.12]  There's this generator page that does it for you where you can just type it.
[918.44 --> 918.46]  Yeah.
[918.84 --> 920.66]  I would use the generator page.
[920.78 --> 922.34]  It's probably the same one.
[922.76 --> 923.26]  Probably is.
[923.54 --> 927.70]  Jeremy, I had not noticed the wikis on these projects because normally I use the GitHub wikis.
[927.70 --> 928.98]  These are beautiful.
[929.80 --> 930.92]  So the art.
[931.18 --> 933.52]  Explain a little bit about where the diagrams come from.
[934.40 --> 935.98]  I guess – so only one of them has a wiki.
[936.12 --> 939.84]  So CloudCrowd has a wiki and Jamit and underscore have pages.
[940.70 --> 944.10]  And I'm still trying to figure out how to document these projects correctly.
[944.18 --> 946.20]  I think I might stick to the plain HTML.
[948.46 --> 951.18]  But in any case – wait, so the art on the CloudCrowd is what you're asking about?
[951.24 --> 951.82]  Sure, yeah.
[952.36 --> 954.46]  The example PDF processing artwork?
[954.46 --> 958.58]  Yeah, so CloudCrowd really needs some hand-drawn diagrams.
[958.82 --> 964.86]  And they're usually a lot nicer than if you spit out a UML or something because you can actually sort of illustrate what's going on.
[965.18 --> 970.78]  And I think that CloudCrowd really needs some explanation because you're talking about a complicated system where you have multiple machines.
[971.02 --> 975.44]  I think at minimum you're kind of talking about three different logical machines.
[975.60 --> 978.04]  You have your application that is making the request.
[978.18 --> 981.96]  You have your central CloudCrowd server and then you have the server where the work's being done.
[982.46 --> 983.98]  So it gets a bit involved.
[983.98 --> 987.22]  And so it's nice to be able to draw it out, sketch it out on paper and to show –
[987.22 --> 988.38]  These are your original drawings?
[988.92 --> 989.14]  Yep.
[989.64 --> 990.04]  Awesome.
[991.26 --> 994.18]  What are you doing to do like the workers, the background jobs and stuff?
[995.00 --> 996.22]  What are we – what's the question?
[996.54 --> 1001.98]  What are you using to do the worker part of it, the cloud nodes, the physical machines with teams of –
[1001.98 --> 1003.94]  So it's all just Ruby.
[1004.10 --> 1017.36]  So the idea is that you install this – for CloudCrowd, you install this gem and it comes with sort of baked in Sinatra servers that are able to listen for work requests and then start doing it.
[1017.62 --> 1020.92]  So what you do is you install your action, which is just a Ruby class.
[1020.92 --> 1023.88]  It's just a script that knows how to do a process method.
[1024.30 --> 1030.46]  And then the node will receive requests to do work and it will run that action if that action is specified.
[1030.64 --> 1032.66]  So in our case, we have an action called process PDFs.
[1032.78 --> 1034.56]  But your action might be called encode video.
[1034.88 --> 1039.00]  And you would have your Ruby script that knows how to do the video encoding and then save that back to S3.
[1039.00 --> 1056.04]  So if you look inside the wiki, there's a page called the job API that details all the sorts of built-in methods when you create an action, the kinds of – or I'm sorry, not the job API page, but the writing an action page.
[1057.22 --> 1059.28]  That details all of the built-in methods that you have.
[1059.46 --> 1064.40]  So you have little – it's a really sort of minimal conveniences.
[1064.40 --> 1072.40]  You have ways to get the input, and if the input looks like a URL, then it will pre-download it for you so that by the time your action starts, it will be ready to go on the local file system.
[1072.50 --> 1073.98]  And you can start manipulating it.
[1074.04 --> 1075.06]  You can start encoding your video.
[1075.22 --> 1076.74]  You can start resizing your JPEG.
[1076.98 --> 1078.20]  You can start processing your PDF.
[1079.32 --> 1082.82]  You can pass an arbitrary JSON hash of options to any action.
[1082.98 --> 1088.12]  I thought that was a convenient way to be able to configure – to make actions a little bit customizable.
[1088.12 --> 1099.92]  So you can imagine if you had an image resizing action that you wrote using, say, graphics magic or image magic to do it efficiently, you could have – in your options hash, you could have the sizes and the image types that you wanted to get back out.
[1100.80 --> 1111.72]  And then the other important method that you get when you're writing a custom action is save, where you call save and you pass it a path on the local file system to your finished video or image or PDF.
[1111.72 --> 1119.84]  And it will save that back to the file system store – or sorry, to the asset store, which is usually S3 but could be the file system like we already discussed.
[1120.70 --> 1124.92]  And then it gives back a URL, which can be used to access it, which then gets sent back to your app.
[1125.92 --> 1130.64]  So is CloudCrowd in the same space as other projects like Delayed Job or Rescue?
[1132.26 --> 1140.54]  Rescue actually, I think, overlaps it to a good extent, which is interesting because I didn't know anything about it when we released it, and CloudCrowd was out for about a month before Rescue showed up.
[1140.54 --> 1148.98]  And I'm not sure if I would have just used Rescue if it had been out before we had started working with CloudCrowd.
[1149.42 --> 1162.00]  The main difference is that Cloud between – well, so Delayed Job and Background Job are both simpler alternatives where you're basically just starting up daemons, but there's not this whole distributed sort of queue thing set up.
[1162.44 --> 1169.04]  Rescue and CloudCrowd both have central queues that then work is parceled out to a whole bunch of workers.
[1169.04 --> 1177.00]  And I think the main difference is that with Rescue, you have an atomic sort of job, and it's more like background job where you're saying do this thing.
[1177.46 --> 1186.10]  And with CloudCrowd, you actually have this kind of built-in MapReduce primitive where you can have a split and a process and a merge, and it'll sort of automatically parallelize the processing to a certain extent.
[1186.22 --> 1188.90]  But that's certainly something that we could contribute maybe to Rescue.
[1188.90 --> 1197.74]  That's why I was asking you about what you were using in that part, like background job or why you went the route of, I guess, writing it all yourself, right?
[1198.34 --> 1198.56]  Yeah.
[1199.30 --> 1200.60]  You mean instead of using background job?
[1200.76 --> 1201.32]  Well, yeah.
[1201.36 --> 1213.78]  Instead of using something that was out there already for – to do queuing, processing, or background jobs, or just job handling in general, why you chose to go the route of writing yourself versus using something that's out there already and able to use?
[1213.78 --> 1228.00]  Well, I mean, it kind of had a funny genesis in terms of how it got started because there was sort of an internal project at the times that was taking the beginning steps towards having a distributed image processing system because they need to do a lot of image resizing.
[1228.22 --> 1230.12]  And this was sort of the generalization of that.
[1230.34 --> 1232.38]  So I didn't actually start it.
[1232.54 --> 1234.58]  I kind of inherited it and then fleshed it out.
[1234.58 --> 1241.26]  But background job I don't think really fits the same niche that Rescue or CloudCrowd do.
[1241.32 --> 1243.66]  And I think that Rescue and CloudCrowd do overlap to a large extent.
[1243.78 --> 1247.86]  And if Rescue had been out, then I might have just used that instead of trying to do this thing.
[1248.62 --> 1249.72]  Well, it's good to have choices, right?
[1250.26 --> 1251.08]  Yep, it is.
[1251.92 --> 1255.68]  Talk to us a little bit about how Underscore.js came about.
[1256.74 --> 1257.10]  Sure.
[1257.44 --> 1259.20]  So Underscore is another extraction.
[1259.20 --> 1268.32]  The idea, I guess, behind it is that it's sort of all the things that, you know, jQuery gives you a great, it sort of levels the playing field.
[1268.46 --> 1270.82]  You know, you're stepping into a naked browser page.
[1270.86 --> 1272.72]  And if you have jQuery, there's a whole lot of things you can do.
[1273.18 --> 1277.00]  And Underscore is kind of finishing off, I think, you know, sort of what jQuery starts.
[1277.14 --> 1288.20]  Like if you, at least in terms of my personal use, if you hand me jQuery, you can start being productive immediately because that's about all that you need to have a solid JavaScript foundation.
[1288.20 --> 1313.84]  And it looks like other people sort of feel the same way because there's been a decent amount of interest in getting Underscore available in the common JS and Node and Rhino and all these sort of back-end server-side JS systems as kind of a standard, I guess, foundation for doing all of the functional array and object and collection manipulation that you need to do so frequently.
[1314.26 --> 1315.30]  I'm a big fan of it.
[1315.30 --> 1328.62]  I implemented a new feature in the footer of my blog to pull in the reading list from Read or Not using jQuery and Underscore to do a lot of the parsing of the JSON that comes back from the service.
[1328.76 --> 1335.82]  And it just felt natural as a Rubyist to drop in and use these methods and use the templating that is built in.
[1336.20 --> 1338.80]  I'm a big fan of this framework.
[1338.88 --> 1339.98]  I think it's going to take off.
[1340.56 --> 1341.16]  I hope so.
[1341.16 --> 1341.44]  Yeah.
[1341.58 --> 1342.70]  I don't think we have enough.
[1343.80 --> 1353.28]  I'd like to think that they're going to take off and they're going to have some kind of enduring support and continue to get contributions.
[1353.52 --> 1361.96]  We don't have the resources to really promote them and to be doing tons of blog posts about how to use it and podcasts and stuff.
[1362.02 --> 1367.50]  Because at the end of the day, you've got to get back to work on Document Cloud proper and making that prototype as solid as you can.
[1367.50 --> 1370.76]  But it's nice to put it out there and to have it be picked up and run with.
[1371.18 --> 1371.66]  Yeah, for sure.
[1372.06 --> 1375.54]  Can you talk about Jamit, where that came about?
[1375.70 --> 1376.66]  Can you give us the backstory?
[1377.74 --> 1382.24]  So Jamit is – it was another extraction.
[1382.48 --> 1386.48]  So in the Document Cloud prototype, I was thinking about how we were going to be packaging assets.
[1386.82 --> 1390.50]  And it had been sort of a problem for me with Rails projects in the past.
[1390.50 --> 1395.86]  So the Document Cloud interface is extremely JavaScript heavy.
[1396.20 --> 1400.80]  It's basically a JavaScript application and Rails is kind of a skinny back end.
[1401.46 --> 1404.58]  And then the database is more significant because you have to do all the searching of these documents.
[1404.72 --> 1406.64]  But the Rails layer is actually very skinny.
[1407.20 --> 1413.98]  And most of the rendering of views and the client-side validation logic, you have to validate in the server too.
[1414.10 --> 1415.36]  But do it on the client first.
[1415.36 --> 1419.72]  And there's actually a full sort of MVC stack in the client.
[1419.88 --> 1427.14]  So we have models of users and of documents and of saved searches and of labels and of metadata.
[1427.38 --> 1434.16]  All of these things are real first-class models in JavaScript in the client using underscore to sort of manipulate them.
[1434.16 --> 1442.32]  And then we have this sort of rich tabbed document searching journalist workspace UI in a client.
[1442.42 --> 1449.42]  Whereas a journalist, you can search through the documents and you can load up the viewer and you can do save searches and you can organize them under labels.
[1449.56 --> 1450.54]  You can visualize them.
[1450.86 --> 1458.02]  It uses Canvas to do some neat little visualizations of the connections between related documents and the people that are mentioned in more than one document.
[1458.18 --> 1463.48]  And so basically at the end of the day, you have a huge amount of JavaScript because it's an entire application getting sent down to the client.
[1463.48 --> 1474.20]  And in the past, I had had some frustrations using the Rails asset packager to try to manage a large number of small JavaScripts into reasonably efficient parcel downloads.
[1474.94 --> 1480.12]  So we had had to customize that a little bit before my previous job.
[1480.34 --> 1483.46]  And I figured that I would just extract that into Jamit.
[1483.60 --> 1489.36]  So Jamit tries to be a relatively comprehensive asset packager for Rails that is easy to configure.
[1489.36 --> 1492.90]  So it uses directory globs instead of having to specify every single JavaScript.
[1493.42 --> 1498.86]  You can just have a specific views directory full of all kinds of tiny 10 or 20 line views.
[1499.34 --> 1503.16]  And then just say in your directory globs, just say views slash star dot JS.
[1503.32 --> 1506.38]  And you'll get all of them included all the time.
[1506.62 --> 1507.26]  So you don't have to worry.
[1507.26 --> 1511.42]  That does increase by asset packagers that you have to specify each individual one you want to.
[1511.72 --> 1512.10]  Exactly.
[1512.10 --> 1516.32]  And then in development, you're trying to make your app.
[1516.40 --> 1520.50]  And every time you change your JavaScript file or rename it, you have to go restart your server and change assets.yaml.
[1520.60 --> 1520.90]  It's a pain.
[1521.18 --> 1521.38]  So yeah.
[1521.98 --> 1525.00]  Or write a reg task that does the packaging for you.
[1525.24 --> 1525.86]  It's a pain.
[1526.42 --> 1527.68]  I mean, you shouldn't have to.
[1527.68 --> 1537.08]  So the idea here is that if you have an ordered unique list of directory globs, so they all get – so if you're talking about a specific package, it's going to expand all of the globs in order.
[1537.22 --> 1538.68]  It's going to take the unique set of files.
[1539.34 --> 1543.62]  And in the end, you can keep things ordered the way you want.
[1543.70 --> 1545.42]  So you can say, first, give me just jQuery.
[1545.92 --> 1546.92]  Then just give me underscore.
[1547.24 --> 1549.74]  And then give me JavaScript slash star dot star.
[1549.84 --> 1551.08]  Give me everything else after that.
[1551.08 --> 1565.06]  It's interesting that you have built-in support for JavaScript templates, and you list a number of options here from John Resick's micro-templating to underscores, built-in templating that we mentioned earlier, prototypes support, and also Mustache.js from Defunct.
[1566.42 --> 1569.20]  Any preference or views on the four of those?
[1570.74 --> 1574.74]  I think there's really good cases to be made for different ones.
[1574.74 --> 1579.66]  As with most things JavaScript, there isn't really a standard, and there's lots of different competing ways to do it.
[1579.66 --> 1599.68]  But I wanted to support JavaScript templates out of the box because that's one thing that if you're using JavaScript templates seriously in your web applications, you need to have good asset packaging support for them because basically every time you load the page, you've got to rebuild all of your asset package – all of your JavaScript templates and send them down as a single JST file, I guess.
[1600.08 --> 1602.38]  So I want a gem to be able to do it conveniently.
[1602.38 --> 1610.68]  But in terms of the actual template method, I don't think that I am too qualified to know about all the different ones.
[1610.76 --> 1611.78]  I know there's really a whole gazillion.
[1611.88 --> 1615.72]  There's pure JS, and there's a whole bunch of different methods out there.
[1615.82 --> 1621.56]  A lot of people like sort of inserting hidden DOM elements onto the page and then using those actual DOM elements as templates.
[1621.56 --> 1632.88]  The ones that I've been more familiar with are more like strings with interpolation like ERB, which is what the micro-templating that we're using and that underscore uses is similar to.
[1632.96 --> 1636.76]  It's a lot like ERB, but with JavaScript instead of Ruby in your tags.
[1638.16 --> 1639.42]  So where do these names come from?
[1639.56 --> 1640.08]  Jamit.
[1640.40 --> 1642.18]  You've got these very unique names.
[1642.28 --> 1644.98]  Are you part of that naming process, or is that something that you inherited as well?
[1646.42 --> 1647.40]  I'm part of it.
[1648.24 --> 1649.36]  Where do the names come from?
[1649.36 --> 1651.32]  Yeah, these are awesome names.
[1651.46 --> 1654.90]  I mean, you look at other people in the space, too, like ThoughtBot.
[1654.98 --> 1657.32]  They've got some really unique names behind their open source projects.
[1658.58 --> 1662.44]  I just wonder where Jamit comes from and kind of the thought process behind these cool names.
[1662.76 --> 1669.64]  You try to find something that's evocative of what the actual app is, but not too clunky or acronymy.
[1670.18 --> 1670.96]  So I don't know.
[1671.22 --> 1676.24]  Spend a couple hours with it kicking around in the back of your head until you find something that sounds appropriate.
[1677.18 --> 1678.52]  I'm not too sure about CloudCrowd.
[1678.52 --> 1681.54]  I keep tripping over it every time I try to say it too many times fast in the road.
[1681.60 --> 1682.34]  It's kind of a tongue twister.
[1682.96 --> 1683.60]  But, yeah.
[1684.14 --> 1692.92]  You know, one of the things that impressed Adam and me when we looked at Jamit and Underscore was just the handcrafted nature of the documentation.
[1693.56 --> 1694.36]  Are these your themes?
[1694.72 --> 1695.68]  Drip this off from somewhere?
[1697.22 --> 1697.90]  The themes?
[1698.40 --> 1699.76]  Drip this off somewhere.
[1700.16 --> 1701.10]  Listen to you.
[1702.76 --> 1703.88]  He's calling you a thief.
[1704.34 --> 1705.52]  I called you a thief with your ass yard.
[1705.52 --> 1706.80]  He called you a thief first, right?
[1707.06 --> 1708.68]  We're late when it was a thief.
[1708.78 --> 1709.44]  He comes on a show.
[1709.62 --> 1711.66]  He's stealing my ass yard and you're stealing.
[1712.40 --> 1712.76]  Jeez.
[1714.22 --> 1718.64]  Well, I don't think the documentation is as much thievery as maybe some of the ideas.
[1718.76 --> 1721.72]  Like, none of this stuff is particularly, you know, is particularly new.
[1721.72 --> 1733.46]  You know, like, Underscore.js has a lot of ideas from Prototype and a lot of, you know, sort of partial implementation sharing of what Prototype and jQuery are doing in terms of their collection manipulation.
[1733.76 --> 1735.90]  And, of course, the idea of having a Rails asset package isn't new.
[1736.02 --> 1743.02]  And the idea of having a Rails or a Ruby distributed job system isn't new either.
[1743.42 --> 1745.58]  But the documentation, I think, is new.
[1745.88 --> 1747.28]  I didn't grab that from anywhere.
[1747.28 --> 1755.16]  Yeah, the reason I say that is most developers, you know, if we write documentation, they tend to not be that pretty to look at.
[1755.30 --> 1759.08]  And both of these sites are informative, minimalistic, and just look great.
[1759.32 --> 1768.48]  And so if this is totally your design, then kudos because it really does a good job of selling the project without having to dig into the source to see how things operate.
[1768.48 --> 1771.82]  Yeah, well, I appreciate that.
[1772.58 --> 1784.62]  I think that has a big, that's a big part of why they're actually, you know, I think we have over a thousand watchers between all of these projects now on GitHub and between, you know, people watching Document Cloud and people watching Document Cloud related projects, which is great.
[1784.68 --> 1788.76]  And I think a lot of that has to do with having solid documentation out of the gate.
[1788.76 --> 1793.12]  And, you know, when people first see a project, what they're going to judge it by is what they start reading about it.
[1793.18 --> 1799.92]  And either that's a blog post explaining it or hopefully it's the official docs and the official docs are good enough for them to get their feet wet and to start messing with it.
[1800.70 --> 1806.96]  So are there any, since you mentioned blog posts, do you have any deep blog posts out there going deeper into some of the stuff that we're talking about?
[1806.96 --> 1821.62]  No, I wish I did. It would be nice to. I think that it'd be good to start putting on DocumentCloud.org some blogs about design decisions as to why things are the way they are in terms of Jamit and how it packages assets or CloudCrowd and how it distributes jobs.
[1822.26 --> 1824.64]  But no, I haven't gotten around to any of that yet. Good idea, though.
[1825.38 --> 1835.50]  I mean, I think that one of the things we cling to jumping into acceptance of an open source project is first, what does it do? Why do I care?
[1835.50 --> 1842.04]  Second is where's the documentation? How deep is it? How informative is it? And three, does it actually solve the problem I'm trying to solve, right?
[1842.54 --> 1844.36]  So need some blog posts.
[1845.58 --> 1850.64]  Yeah, amen to that. If any listeners feel like writing some, that would be much appreciated.
[1851.66 --> 1854.50]  Henry, do you have anything in the scoop? Anything cool coming up that you just have to mention?
[1855.76 --> 1861.70]  Actually, we do. So the next little, it's a bit smaller, I think, in scope than our previous ones.
[1861.70 --> 1874.20]  But the next DocumentCloud open source release, I think, is going to be a project called PDF Pieces coming out in a day or two that makes it easier to take a PDF and to pull it apart into all of its component pieces.
[1874.54 --> 1877.88]  And then, you know, things that you can then index and put on the web and make searchable.
[1877.88 --> 1895.74]  So you'll be able to do, as a command line, you'll be able to do PDF Pieces pages or images or text and explode the PDF apart into its UTF full text or into pings or GIFs or JPEGs of each page or into single-page PDFs if that's what you need.
[1896.42 --> 1903.18]  And it'll also pull out some of the metadata so you can find out, you know, the title and the author and the producer and things like that of the PDF.
[1903.18 --> 1908.80]  So what this is is just going to be a Ruby gem that wraps the excellent Adobe PDF Box Java library.
[1909.32 --> 1917.18]  And so under the covers, it's actually shelling out to special little Java classes that are doing the actual work.
[1917.88 --> 1918.88]  So it's pretty nice and efficient.
[1919.28 --> 1932.50]  And you can pass it, say, a PDF and tell it to give you back all the images for that document in 700 and 1,000 pixels wide as well as both JPEG and ping forms.
[1932.50 --> 1939.62]  And it'll do all that for you in a single JVM loop so you don't have to keep going back and forth between Ruby and Java doing it for every page.
[1940.30 --> 1942.52]  So that's the next thing on our plates.
[1943.40 --> 1944.00]  That's not very interesting.
[1944.94 --> 1949.10]  We normally wrap each show by asking the guests, what's on your open source radar?
[1949.22 --> 1952.90]  So any projects out there other than the ones that are coming out of Document Cloud that excite you?
[1954.24 --> 1955.16]  Yes, absolutely.
[1955.16 --> 1966.88]  So I think the big thing that I'm excited about but that I can't quite see myself getting into yet, which is kind of like a tease, I guess, is all of the server-side JavaScript stuff that's happening.
[1967.10 --> 1973.82]  Because I think we're at the point now with a lot of projects that are more interesting technically on the client side than they are in the server.
[1974.16 --> 1981.98]  And you're doing a lot of great visualization and computation, a lot of great interaction with real MVC stacks, with real models in JavaScript.
[1981.98 --> 1989.94]  And it's really a source of duplication and pain to be duplicating all of these models.
[1990.18 --> 1999.22]  You write it once in Ruby to do the validations and to do the manipulation where you're asking a document what its metadata is and what people it talks about and that kind of thing.
[1999.26 --> 2002.84]  You're doing that both in Ruby on the server as well as on the client in JavaScript.
[2002.84 --> 2013.54]  And to be able to have one language where you can share the models and just send down JSON data and you can have the same operations and the same validations running both on the server and the client I think would be really, really, really useful.
[2013.54 --> 2033.96]  So I'm just kind of waiting for someone to write the complete comprehensive Rails equivalent in one of these server.js platforms, whether it ends up being Node or Narwhal on Rhino or something else on custom V8 that has a complete story of how do you do your parallel processes?
[2034.30 --> 2036.14]  How do you do your file interactions?
[2036.34 --> 2037.22]  How do you talk to a database?
[2037.86 --> 2042.70]  How do you interface with other C or Java libraries, as the case may be?
[2042.70 --> 2052.22]  And once someone has all that figured out and we've got a good server-side platform, I think that it'll become an instant no-brainer to build large-scale web applications in JavaScript end-to-end.
[2052.88 --> 2053.78]  So I'm kind of waiting for that.
[2053.96 --> 2060.34]  I can't justify it for Document Cloud as a project because I don't think it's there yet, but I think it's coming soon, maybe within a year or so.
[2060.90 --> 2064.10]  Anybody wants to get a hold of you, what's the best way to reach out to you?
[2064.18 --> 2064.84]  Are you on Twitter?
[2065.28 --> 2065.92]  What's your handle?
[2066.20 --> 2066.46]  Email?
[2067.22 --> 2068.22]  I'm actually not on Twitter.
[2068.62 --> 2071.38]  People like to message through GitHub, which works pretty well.
[2071.38 --> 2074.18]  Or you can do jeremy at documentcloud.org.
[2075.40 --> 2089.00]  And just to mention the thing that I said at the beginning, if you're a talented JavaScript or Ruby programmer and you are interested in working on projects that have a mandate to be open-sourced, then we'd love to hear from you.
[2089.38 --> 2091.56]  So yeah, you can send me an email at jeremy at documentcloud.org.
[2091.56 --> 2097.66]  And so they can also go to github.com forward slash documentcloud and they can hit you from there.
[2097.72 --> 2099.06]  Is that your user or do you have your own user?
[2099.78 --> 2099.90]  Yep.
[2100.74 --> 2102.08]  I'm pretty much that one too.
[2102.30 --> 2103.12]  So yeah, that'll work also.
[2103.66 --> 2103.90]  Awesome.
[2104.18 --> 2106.52]  Well, it was awesome having you on the show, Jeremy.
[2106.62 --> 2108.74]  Thank you very much for taking the time to chat with us.
[2108.90 --> 2109.86]  Your project was awesome.
[2110.54 --> 2111.04]  Thanks a lot.
[2111.80 --> 2112.56]  It was a pleasure having you.
[2113.38 --> 2114.20]  It was a pleasure being on.
[2114.30 --> 2114.82]  I appreciate it.
[2114.82 --> 2123.06]  Thank you for listening to this edition of The Changelog.
[2123.76 --> 2127.78]  Be sure to tune in weekly for what's fresh and new in open source.
[2128.94 --> 2133.84]  Also visit thechangelog.com to follow along, subscribe to the feed, and more.
[2134.02 --> 2135.08]  Thank you for listening.
[2135.08 --> 2136.08]  Thank you for listening.
[2144.82 --> 2149.16]  Thank you.
[2165.56 --> 2167.92]  you
[2167.92 --> 2168.60]  you
