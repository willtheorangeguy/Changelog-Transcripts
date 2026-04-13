[0.00 → 8.66] Welcome to Practical AI.
[9.16 → 16.78] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[16.78 → 19.54] changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 30.94] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 → 35.44] on six continents, so you can launch your app near your users.
[35.84 → 37.86] Learn more at Fly.io.
[42.80 → 46.36] Welcome to another episode of Practical AI.
[46.36 → 48.28] This is Daniel Whiten ack.
[48.40 → 54.36] I'm CEO and founder at Prediction Guard, and I'm joined as always by my co-host, Chris
[54.36 → 57.12] Benson, who is a tech strategist at Lockheed Martin.
[57.52 → 58.22] How are you doing, Chris?
[58.42 → 59.24] Doing good.
[59.34 → 62.46] It's a beautiful, almost spring day here in Atlanta.
[62.96 → 64.52] I walked my dog before the show.
[65.12 → 66.14] Yeah, the sun is out.
[66.38 → 67.80] It's getting nicer out.
[67.96 → 69.52] I have to start with the weather, of course.
[69.52 → 76.74] Yeah, and spring is breathing sort of new life into various ideas around this podcast
[76.74 → 77.42] as well.
[77.56 → 83.24] And before we hop into our fascinating guest interview today, I wanted to highlight
[83.24 → 85.80] something new that we're trying at Practical AI.
[86.12 → 91.26] We want the show to be practical and useful, and part of that is actually helping you all
[91.26 → 95.14] get live, hands-on help with the latest technologies.
[95.14 → 104.20] And so March 14th at 1 p.m. Eastern, we're going to have our first Gen AI Mastery class or
[104.20 → 106.86] webinar or tutorial or whatever you want to call it.
[106.86 → 113.40] We're going to dive into all things text-to-SQL, data analytics questions with large language
[113.40 → 113.86] models.
[114.02 → 120.34] And we're going to be joined by Chung Shi, who is from Lance DB, the CEO there, who is a
[120.34 → 121.40] recent guest on the show.
[121.50 → 122.60] So it's going to be a lot of fun.
[123.00 → 128.86] Find out more at tinyurl.com slash genai-mastery1.
[129.80 → 132.24] And we'll include the link in the show notes as well.
[132.42 → 133.60] I'm pretty excited about it, Chris.
[133.60 → 134.48] I am too.
[134.56 → 135.44] Looking forward to that.
[135.54 → 140.56] It's a new feature for us to do, and we hope folks in the audience enjoy that.
[140.76 → 144.96] I guess if it's okay, I'm going to dive right into our guest.
[145.08 → 145.66] Go for it.
[145.78 → 150.76] I will say ahead of time, I have been looking forward for years for having this guest come
[150.76 → 151.34] on the show.
[151.50 → 152.48] It's a long time coming.
[152.70 → 157.48] A long time coming because I'm at Lockheed Martin, and we have a lot of don't cross the
[157.48 → 159.08] streams mentality.
[159.08 → 164.30] I had to wait for this guest to retire from his previous position so that there could
[164.30 → 166.54] be not crossing the streams concerns.
[167.26 → 169.52] And so I'd like to introduce Jack Shanahan.
[169.94 → 174.94] He is the only senior military officer who has been responsible for standing up and leading
[174.94 → 179.96] two organizations within the United States Department of Defence dedicated to fielding
[179.96 → 180.82] AI capabilities.
[180.98 → 186.76] One of those was Project Maven, which was also known as the Algorithmic Warfare Cross-Functional
[186.76 → 187.08] team.
[187.48 → 191.78] And the other is the Department of Defence Joint Artificial Intelligence Centre.
[191.98 → 195.44] And he was the founding and inaugural director of that.
[195.58 → 196.54] Jack, welcome to the show.
[196.82 → 199.64] Chris and Daniel, thank you so much for having me on.
[199.70 → 203.98] I just want to, I'll begin by just saying how much I love the title, Practical AI, because
[203.98 → 205.26] I am a practitioner.
[205.50 → 207.40] This is not about research and development.
[207.90 → 213.04] There are a lot of wonderful things happening in the AI R&D world, but that's not my world.
[213.04 → 219.42] My world is how do you take this esoteric technology and turn it into real product for the government
[219.42 → 223.58] or for my case, for the Department of Defence and a little bit for the national intelligence
[223.58 → 224.12] community?
[224.26 → 226.64] Because Project Maven, you talk about crossing streams.
[226.74 → 227.44] We cross streams.
[227.58 → 231.42] It was both what we say, the IC, the intel community and the Department of Defence.
[231.52 → 234.52] But I'm really happy to join both for this podcast.
[234.52 → 235.02] Thank you.
[235.44 → 235.82] No problem.
[235.94 → 239.30] It's, you know, I will note, I follow you on LinkedIn.
[239.30 → 241.68] I encourage our audience to follow you on LinkedIn.
[241.96 → 246.54] You are out there reading the scientific papers as they come out, and you often, when you're
[246.54 → 252.48] sharing posts, will put a spin on the various, you know, papers that are coming out from that
[252.48 → 257.74] AI and national security context, because those papers obviously aren't necessarily in that
[257.74 → 258.00] way.
[258.34 → 259.00] Very insightful.
[259.34 → 260.50] I would encourage people to do that.
[260.76 → 262.84] I wanted to start out as a military professional.
[263.02 → 265.44] How did you get into this particular?
[265.44 → 269.74] I mean, this is, you know, you were the right person at the right place at the right time
[269.74 → 271.02] in the Department of Defence.
[271.02 → 272.86] How did you end up in this?
[273.30 → 274.16] What caught your attention?
[274.16 → 276.06] And how did you get going on this story?
[276.48 → 283.54] Yeah, I guess what I would begin by saying is I spent 95% of my career not working on this
[283.54 → 288.56] because I started in actually fighter aviation for the first 15 years of my military career.
[288.62 → 293.14] I spent 36 years in uniform, retired in the summer of 2020.
[293.14 → 298.58] And then from the flying piece, I was charged to go run an intelligence organization.
[298.80 → 303.50] And then I did a command and control wing and then a flying wing out of Nebraska and
[303.50 → 307.96] then did a command down in San Antonio, which was about intelligence, surveillance, reconnaissance
[307.96 → 311.20] and policy positions and other positions in the Pentagon.
[311.36 → 315.46] So this was not my destiny, my path, as we say, from the beginning.
[315.86 → 320.44] However, when we got to that point where I came back as a three-star into the Pentagon
[320.44 → 326.00] in something we call the Undersecretary Defence for Intelligence, I didn't walk into that job
[326.00 → 329.04] with AI as on my plate, as we say.
[329.04 → 334.96] I left that job with AI dominating everything I did, every single waking moment in most of
[334.96 → 338.70] my non-awake moments, nightmares, dreams, whatever you want to call it.
[338.92 → 343.84] As I say, I cut a long story very, very short by saying we had an intractable problem.
[343.84 → 348.14] And we had intelligence analysts looking at full motion video coming from drone.
[348.70 → 353.18] And there was more drone video than at any point in history, hands down.
[353.50 → 354.94] The intel analysts just couldn't do it.
[354.98 → 356.84] They couldn't spend enough time in a day.
[356.96 → 361.44] As I used to joke about at the time, they would have some sort of energy drink next to
[361.44 → 362.88] them and probably some chewing tobacco.
[363.04 → 366.14] Try to just this mind-numbing work of looking through this video.
[366.36 → 368.52] It was just, first, we're going to run out of people.
[368.52 → 372.64] But two, we were going to get more and more collection, not just full motion video, but
[372.64 → 377.06] from other assets, as we say, to include unclassified open source information.
[377.74 → 379.50] And it was a success catastrophe.
[379.82 → 385.86] More collection from more places at more classification levels than at any other point in history, period.
[386.32 → 387.38] And so what could we do?
[387.44 → 392.74] And we could not find a technology that was ready to be fielded in the Department of Defence.
[393.16 → 397.46] Again, wonderful research and development work that was going on and goes on as we speak today.
[397.46 → 399.36] So we turned to commercial industry.
[399.50 → 401.28] In fact, we turned to Silicon Valley.
[401.42 → 403.94] And they said, yeah, we've got something that could probably help you.
[404.04 → 406.64] And it's called computer vision, natural language processing.
[406.94 → 409.50] And that's where the journey began, to be honest with you.
[409.94 → 412.60] And we formally stood up in April 2007.
[412.72 → 413.34] It's hard to believe.
[413.52 → 415.80] It's been seven years now on that journey.
[416.00 → 417.36] And then we were off to the races.
[417.36 → 419.92] And I did that for just about 18 months.
[420.02 → 426.00] And then I was asked to stand up the Joint Centre or the JAIL, which was to take on everything
[426.00 → 427.62] that we weren't doing in Project Maven.
[427.80 → 429.38] Project Maven was about intelligence.
[429.78 → 435.16] But the entire department needed to start bringing in AI and everything else the department does.
[435.62 → 437.18] And there was no mechanism for doing that.
[437.52 → 440.28] Each of the military services had something going on.
[440.46 → 442.10] But I would call them pilot projects.
[442.46 → 447.08] Small scale pilots that could not cross that valley of death.
[447.08 → 451.12] So the whole point of this new organization was, let's get going.
[451.26 → 452.96] Let's get going at scale.
[453.54 → 455.16] Fast would be very good.
[455.54 → 457.84] Fast and at scale would be superior.
[458.34 → 459.62] And that's what this was all about.
[459.68 → 460.48] It was speed and scale.
[460.64 → 464.82] So that is how I ended up at the JAIL after having done Project Maven.
[465.38 → 466.78] And we had to stand up.
[467.02 → 470.44] As I say, I've decided it's no longer tongue-in-cheek.
[470.54 → 473.68] I actually was the CEO of two AI startups in the Pentagon.
[474.10 → 475.66] But that doesn't make sense to a lot of people.
[475.66 → 476.96] Like the Pentagon does startups?
[477.36 → 478.94] Yes, we did two startups.
[479.20 → 484.70] And all the challenges that you would expect from startups, I lived firsthand with my team
[484.70 → 486.14] in Project Maven and the JAIL.
[486.22 → 490.04] So that's a good starting point to tell you the journey that we took to get to the final
[490.04 → 491.80] 2020 where I walked out the door.
[492.02 → 495.84] But I haven't walked out the door because I'm still very connected to what's going on in government.
[496.88 → 502.06] You mentioned in part of that discussion the words at scale a couple of times.
[502.06 → 508.86] And I know as even now I'm building my own company, you encounter problems at each level
[508.86 → 511.24] of scale that you try to achieve.
[511.36 → 516.92] But when you're talking about at scale at the government level or worldwide where all of
[516.92 → 524.16] these organizations are operating, I'm sure there are things that go beyond the technology
[524.16 → 524.90] element.
[524.90 → 530.20] So choosing saying, oh, this is a great model for this application, right?
[530.44 → 534.86] Whether it's a computer vision or natural language processing or Gen AI now.
[535.14 → 541.40] I'm mostly curious because I don't really have a good window into what does it mean to actually
[541.40 → 550.14] scale one of these applications, AI applications in the national security space versus in an industry
[550.14 → 555.82] context where you might be scaling to, you know, this many users or something within your company.
[556.06 → 562.60] What's different, and what's the same, and what's kind of unique of that at scale component in
[562.60 → 564.16] the national security world?
[564.90 → 567.28] Really all germane points, Daniel.
[567.40 → 569.58] And there's so much to talk about just on that alone.
[569.70 → 573.06] I think I've now spent enough time now that I'm out of uniform.
[573.06 → 577.30] I'm out of the Department of Defence working with venture capital companies, Insight Partners in
[577.30 → 583.34] particular, and I get a chance to go and spend time with CEOs of everything from small startups to
[583.34 → 588.68] pretty big companies that are still in that venture capital business somehow, whatever seed
[588.68 → 590.42] round of funding that they're getting.
[590.82 → 592.54] And the journey is remarkably the same.
[592.66 → 597.76] Actually, surprising to me, I would sit there and cry in my beer, so to speak, and say, oh,
[597.80 → 599.34] nobody understands my problems.
[599.34 → 605.10] And then one day I'm driving into the Pentagon, just despondent about how I'll never get this
[605.10 → 607.92] thing called the Jake Bill, because I have no people, I have no money.
[608.22 → 609.04] How are we going to get there?
[609.06 → 611.20] I'm listening to Guy Ross, how I built this.
[611.48 → 614.70] And I was listening to the CEO, the founder of Belching Routers.
[614.98 → 615.92] It was a fascinating story.
[615.98 → 617.12] It was exactly my story.
[617.20 → 621.26] He says, I built this thing in my parents' garage, and there were days when I was just
[621.26 → 623.14] ready to throw in the towel and give up.
[623.44 → 627.64] And there were other days, 24 hours later, where I would suddenly, some technological breakthrough
[627.64 → 631.30] or some big contract that we got, and all of a sudden it looked bright again.
[631.36 → 631.88] I lived that.
[631.88 → 636.62] I said, well, if he could turn it into that company, then hell, I can do the same thing
[636.62 → 637.72] in the Department of Defence.
[638.06 → 641.62] And I want to come back to something you said, Daniel, because it's so incredibly important
[641.62 → 642.80] to this discussion.
[643.20 → 647.50] The technology, of course, was fundamentally at the centre of what we were trying to do,
[647.74 → 651.98] but everything else was even more important to how do you get to scale.
[651.98 → 658.18] So I would say maybe the differences are, well, they're used for military operations, but
[658.18 → 664.60] I would say that if you look at any big commercial company that was not built as a digital company,
[664.96 → 669.56] it was built as a hardware company in the industrial age, we have the same experiences.
[669.72 → 672.68] I've talked to enough people now and say, oh, yeah, it's the same thing we're going through.
[672.84 → 677.72] It's getting that pilot project scaled and built in a way that you can then put it in
[677.72 → 682.36] one, you know, for a company, let's say for a medical or financial business, it's for that
[682.36 → 682.74] company.
[682.74 → 686.32] But for a lot of other places, it's how do I get this thing scaled to the rest of the
[686.32 → 686.58] world?
[686.94 → 690.52] But in terms of industries, very similar to what we were going through.
[690.92 → 692.88] And I talk about this all the time.
[692.96 → 696.54] I have eight things and I don't have to go through all of them, but they have nothing
[696.54 → 697.66] to do with technology.
[698.08 → 703.82] It's, you know, mandate, vision, alignment, obstacle clears, bureaucratic enablers, resources,
[704.02 → 705.88] authorities, and then sort of talent management.
[706.12 → 710.98] All of those are not technology focused, but they have to exist where you can get there.
[710.98 → 715.60] We all want to focus on, I have this cool new widget, a gadget, and this thing is going
[715.60 → 716.50] to change the world.
[716.90 → 721.46] Well, it might, but if you don't have all those other pieces in place, which if you understand
[721.46 → 725.90] the bureaucracy known as the federal government, you have to have somebody that understands
[725.90 → 727.62] how to navigate in that world.
[727.98 → 732.88] Whatever I didn't know about technology, and that's a fairly long list of things at the
[732.88 → 737.26] time I started all this journey, I sure knew a lot about how to work in the federal
[737.26 → 737.70] government.
[737.70 → 741.40] I had commanded six different levels in the United States Air Force.
[741.80 → 745.68] I had been, you know, in all these places where I had to do this day in, day out.
[745.78 → 747.90] So that part I was very comfortable with.
[748.16 → 752.88] I wasn't nearly as comfortable with technology, so I had to, it was a hockey stick learning
[752.88 → 753.14] curve.
[753.28 → 754.74] No if, ANDs, or bust about it.
[754.90 → 758.86] I still feel like I'm a novice today, by the way, and that's seven years in the past
[758.86 → 759.34] where we started.
[759.42 → 760.02] It's actually eight.
[760.10 → 761.32] We got started in 2016.
[761.32 → 766.38] So I think there are more similarities, there are differences, at least for the non-digital
[766.38 → 772.16] companies, because they have the same problems that a CEO is experiencing today saying, is
[772.16 → 773.20] this AI thing real?
[773.30 → 776.80] Should I really invest millions of dollars of this company's money?
[777.28 → 778.74] What is the return on investment?
[779.06 → 782.34] That return on investment question is an unsettled discussion.
[782.34 → 787.52] And I had lots of those with people very skeptical about what we were trying to do in the joint
[787.52 → 788.10] AI centre.
[788.10 → 790.86] That's actually a point I'd like to extend a little bit.
[791.08 → 796.68] You talked about the federal bureaucracy and the challenge, and the US military is not just
[796.68 → 797.92] a single organization.
[797.92 → 803.20] It's a lot of large organizations with their own structures and their own cultures in each
[803.20 → 803.92] of the services.
[804.58 → 809.94] In a sense, that's almost a much harder thing, I would argue, than a lot of Fortune 500 companies,
[810.26 → 814.80] not only from size, but just you have so many different things at play.
[814.80 → 821.98] When you're taking something as new and as hyped as AI is, so having both the potential of the
[821.98 → 826.66] technologies that are being developed, but with a lot of hype thrown in on top of that,
[826.96 → 832.78] and those skeptical people in different organizations within the larger, how do you navigate that to make,
[832.92 → 837.48] you talked early on about the velocity being so important, velocity at scale.
[837.48 → 840.50] How do you navigate that in a large organization?
[841.02 → 842.90] What are some of the lessons that you learned on that?
[843.04 → 848.24] Because normally we see such slow change, you know, the American people see such slow change in other
[848.24 → 851.44] nations too, in their governments, at least that's the perception.
[851.94 → 854.20] You did a lot in a very short amount of time.
[854.44 → 855.68] How did you navigate that?
[856.18 → 856.72] Very carefully.
[857.10 → 857.84] It was hard.
[858.08 → 859.02] It was hard to do it.
[859.12 → 862.30] But Chris, I'm going to come back to the word that you said.
[862.30 → 866.70] And to me, I would put this at the core of everything I was trying to do, and that's culture.
[866.94 → 870.06] You're trying to change the culture of an organization.
[870.40 → 874.74] And the thing about the Department of Defence, I'm not going to say it's completely unlike
[874.74 → 879.88] a lot of big companies, but I think there are big differences because when you talk about the
[879.88 → 883.32] Department of Defence, there are cultures within cultures.
[883.50 → 885.34] There are military unit cultures.
[885.52 → 886.56] There are service cultures.
[886.78 → 889.06] There's an office of the secretary of defence culture.
[889.06 → 892.40] There is a Pentagon culture, foreign as that culture is.
[892.50 → 897.18] It is a culture unto itself when you walk into that building every morning and leave at the end
[897.18 → 898.78] of the day, dark on both ends.
[899.08 → 903.28] So this culture piece is difficult to figure out how to change that.
[903.60 → 910.14] So what you have to do is just persist for days, months, and years at a time and say,
[910.30 → 912.64] join me, come on this journey with us.
[912.74 → 917.26] And there'll be a lot of resistance to that because, not surprisingly, when you talk about
[917.26 → 921.78] war fighting, the Department of Defence is still largely a risk-averse organization.
[921.94 → 924.06] It has to be because lives are at stake.
[924.44 → 930.02] We're trying to take a culture and change it in a way that people are just not comfortable
[930.02 → 934.54] with because of the hype, because they don't understand what AI really is.
[934.70 → 939.02] To them, they keep hearing miracle whip, miracle, miracle whip, this thing that we're just going
[939.02 → 943.46] to take out of the jar and spread on a couple of pieces of bread and all will be well with
[943.46 → 944.22] the Department of Defence.
[944.22 → 945.50] It just doesn't work that way.
[945.50 → 952.18] So this idea of changing culture from a bottom layer, top layer, middle management layer,
[952.30 → 954.74] it all has to be done simultaneously.
[955.26 → 960.44] And part of this culture is, and this is why when I talked about what you need is not just
[960.44 → 963.14] the bureaucratic enables, but the people who are obstacle clearers.
[963.16 → 964.34] And I put them in three categories.
[964.80 → 969.32] The classic disruptors, which the Marine Corps colonel that ran Project Maven, Drew Zukor,
[969.64 → 972.08] was absolutely positively one of those.
[972.08 → 976.42] You also need the people that clean up the broken glass that comes from the disruptors.
[976.68 → 979.98] And we had a lot of people that were capable of doing that.
[980.20 → 981.80] And then I have the networkers.
[982.10 → 986.28] These are the people that a lot of times are what we would consider middle management.
[986.42 → 987.36] They get disparaged.
[987.66 → 989.28] But to me, they're the key to success.
[989.62 → 992.90] There are the people that know how things get done in the federal government.
[993.10 → 995.46] They go have a cup of coffee with the budget person.
[995.46 → 1000.58] They go have a cup of coffee with a service general officer, and they work the networks
[1000.58 → 1002.56] that they've established over years.
[1002.92 → 1008.74] And if you find somebody that can do that effectively, you're going to do much more than
[1008.74 → 1012.96] people that just think sheer force of will alone will change culture.
[1013.12 → 1016.88] You really need some ratio of all those three types of people.
[1017.10 → 1020.50] And the ratio will change over time, which I found in Project Maven.
[1020.50 → 1021.84] We need the disruptor, period.
[1022.18 → 1025.88] We had to force-feed this down the throat of the Department of Defence.
[1026.20 → 1027.70] Hard, hard, hard to do.
[1028.08 → 1032.04] But over time, as I got into the Jake, I needed more of the people that could do the networking
[1032.04 → 1034.52] and that would do a little bit of disruption.
[1034.70 → 1038.94] But more, it was about cleaning up some broken glass, but really moving faster and faster.
[1039.14 → 1041.44] So culture eats strategy for breakfast.
[1041.60 → 1042.42] It always has.
[1042.48 → 1043.38] It always will.
[1043.48 → 1047.42] You have to put culture at the centre of any technology project.
[1047.42 → 1054.58] Well, Jack, I really love how we're getting into a lot of these culture, strategy, talent
[1054.58 → 1060.72] sort of subjects, which is really key and practical across a lot of organizations that are trying
[1060.72 → 1061.88] to adopt this technology.
[1062.50 → 1066.76] One of the things that you mentioned, which kind of caught my ear is, you know, there's
[1066.76 → 1072.02] people involved in particularly in the context that you've been working in that do have a true,
[1072.62 → 1075.78] valid concern around risk of these technologies.
[1075.78 → 1080.62] Like, hey, people's lives are on the line, and we care about that, which hopefully they should
[1080.62 → 1081.80] care about that, right?
[1082.14 → 1088.28] So after working in these environments for a while and bringing new technology to sort of
[1088.28 → 1095.90] risky situations, for a lot of those people out there that are also navigating, maybe it's
[1095.90 → 1101.28] not people's lives, but maybe it is like real impact to people's lives and integrating AI
[1101.28 → 1107.80] systems around automation or really sensitive subjects like finance and healthcare and other
[1107.80 → 1108.22] things.
[1108.54 → 1115.58] Do you have any learnings or thoughts from your experience of AI in risky situations or
[1115.58 → 1120.84] with sensitive data that you'd like to highlight and how that played out in your situations and
[1120.84 → 1121.90] what you learned over time?
[1122.38 → 1126.72] Yeah, Daniel, I would say this is something we talked about pretty much every day.
[1127.00 → 1129.98] Now, maybe it was a little different because we knew the problem from the beginning.
[1129.98 → 1132.24] That problem could not be solved in any other way.
[1132.32 → 1133.28] So we knew we were going.
[1133.72 → 1137.96] But when I got into the Jake, the conversations we had were generally along this line.
[1138.16 → 1144.66] We're going to start with lower risk, lower consequence use cases, solve those, learn from
[1144.66 → 1149.32] them, and then slowly move up the ladder, maybe even fast up the ladder, depending on what we
[1149.32 → 1151.96] were talking about, to get into those higher risk use cases.
[1152.16 → 1157.12] There is a lot of talk, of course, about the dangers or the risks of so-called killer drones.
[1157.12 → 1161.60] I'll tell you the thing I wasn't working on in the last five years of my career was killer
[1161.60 → 1161.94] drones.
[1162.30 → 1165.62] I had nothing to do with those because they were too high risk, too high consequences.
[1165.96 → 1170.54] And we had to understand how to actually do AI before it started getting to that.
[1170.62 → 1174.96] So we started with things like predictive maintenance, or there were some medical initiatives that
[1174.96 → 1175.86] we were taking on.
[1176.20 → 1181.32] There were some things that we could put on individual intelligence platforms or sensors.
[1181.32 → 1187.80] And so we learned from that, and then based on those lessons learned, began to sort of edge our
[1187.80 → 1189.98] way into more consequential use cases.
[1190.38 → 1194.60] And to me, there would be a clear analogy with any business that's out there.
[1194.72 → 1197.58] Because again, a CEO, the risk will be different.
[1197.70 → 1200.84] It might not be life or death, but it could be tens of millions of dollars.
[1200.94 → 1202.42] And that's very risky for a CEO.
[1202.76 → 1208.02] So the idea of proving success at something, and the reason we stood up to Jake is because
[1208.02 → 1213.00] we showed enough success in Maven, as difficult as it was, we did show real success and put
[1213.00 → 1217.36] AI models out in combat operations within a year of standing up the organization.
[1217.80 → 1219.50] Okay, let's go try some other things.
[1219.86 → 1223.70] And so what you'll see now is, okay, now that we've learned all these lessons, they're going
[1223.70 → 1226.22] to a little bit more consequential use cases.
[1226.72 → 1232.74] Maybe AI enabled autonomous drones, and maybe not lethal drones, but autonomous drones.
[1233.08 → 1234.16] And then you'll start seeing this.
[1234.26 → 1238.00] In fact, you can kind of see some of this playing out in Ukraine as you look at the headlines
[1238.00 → 1240.36] what they're doing with drones on both sides right now.
[1240.52 → 1243.32] So to me, it's like starting with something that's manageable.
[1243.54 → 1244.52] Get your arms around it.
[1244.84 → 1248.00] Learn what it means to build a data management pipeline.
[1248.22 → 1254.02] Because what I've found in the DoD, hands down, what stopped people cold when trying
[1254.02 → 1255.74] to start AI projects was data.
[1256.22 → 1258.44] Much better now than it was seven years ago.
[1258.54 → 1259.30] Much, much better.
[1259.54 → 1260.30] But it's still hard.
[1260.64 → 1264.14] So if you can't get over that data hurdle, then people get despondent.
[1264.14 → 1268.66] They can't reconcile what they're hearing about the hype with the challenges of doing
[1268.66 → 1269.34] it for real.
[1269.76 → 1273.32] And I'll tell you, I've been around long enough now to know when somebody has never done a
[1273.32 → 1277.96] real AI project and just talks about AI, because there's a big difference in those two things.
[1278.54 → 1283.28] One of the things I wanted to share with the audience is that you have recently submitted
[1283.28 → 1288.12] a paper with a lot of guidance to the US Senate.
[1288.12 → 1293.40] They had the AI Insight Forum on National Security, and you submitted your document.
[1294.02 → 1298.32] And this was very recently on Sunday, December 6th of this past year.
[1298.78 → 1306.42] And it's great in that it gives a fantastic kind of oversight into AI in a national security
[1306.42 → 1307.00] context.
[1307.22 → 1311.54] And you offer some recommendations, which I'd love to go through in terms of that.
[1311.72 → 1312.74] But you mentioned Ukraine.
[1312.74 → 1314.60] And you also mentioned that in the document.
[1314.60 → 1319.82] I was wanting to, as a transitional question, kind of, what have we learned that you can
[1319.82 → 1321.16] share from Ukraine?
[1321.34 → 1328.12] So as you're racing through getting AI gradually integrated into our armed services, and we're
[1328.12 → 1332.98] watching and supporting the Ukrainians against the Russians, and we've had this real-time,
[1333.32 → 1338.66] real-life learning process that's come out of that, and seeing what they've done with drones
[1338.66 → 1339.12] and stuff.
[1339.46 → 1344.04] Is there anything that stands out in your mind that was either great learning or something
[1344.04 → 1348.60] unexpected that came from that real-life application that's being developed right now?
[1349.00 → 1353.50] Technology is at the centre of this fight that's going on, this war that's going on between
[1353.50 → 1354.50] Ukraine and Russia.
[1354.72 → 1360.38] And what you've seen in Ukraine in the first year of the war was how quickly they adapted.
[1360.82 → 1361.88] It's an amazing story.
[1362.08 → 1366.68] It's actually an amazing story that what you have is some people that might have been born
[1366.68 → 1369.88] in Ukraine, came to the United States, got educated, went out to Silicon Valley.
[1369.88 → 1375.12] But when the war started, went back over to Ukraine and then focused on how much faster
[1375.12 → 1376.96] they can bring technology to the fight.
[1377.28 → 1381.38] Things that we've been talking about doing in the U.S. Department of Defence for many
[1381.38 → 1383.20] years, they did instantly.
[1383.50 → 1387.56] Like, people don't maybe understand this part of it, moving their entire government to the
[1387.56 → 1387.82] cloud.
[1388.20 → 1390.08] If they had not done that, it would have been a disaster.
[1390.24 → 1391.28] They would have lost everything.
[1391.74 → 1396.42] But then just on the military technology pieces, how quickly they were able to bring in,
[1396.42 → 1400.56] what I say is this really an example of what we've been talking about while software driven
[1400.56 → 1402.68] warfare is moving that fast.
[1402.80 → 1406.98] And it's not to imply that technology, of course, is no longer relevant.
[1407.12 → 1408.44] It's as relevant as ever.
[1408.90 → 1412.26] But technology that is software defined is a different kind of technology.
[1412.74 → 1417.28] And that's how Ukraine has been gaining an advantage is by moving faster than the Russians
[1417.28 → 1418.64] and adapting much faster.
[1418.84 → 1420.66] And the drones are the best example of this.
[1420.80 → 1422.80] It's crazy to see what they've done.
[1422.80 → 1427.60] The idea of bringing in 100,000 drones, some of which are first-person view.
[1427.80 → 1433.08] And you're watching somebody wearing these goggles drive a drone with explosives on it
[1433.08 → 1434.62] into a Russian tank and blow it up.
[1435.08 → 1436.42] So there are a lot of lessons.
[1436.56 → 1438.90] Now, no two conflicts are exactly the same.
[1438.96 → 1441.58] So we've got to be careful about the fungibility of lessons learned.
[1441.64 → 1446.44] But I think there are so many lessons that will apply to conflict for the next 10 to 20 years.
[1446.44 → 1453.06] And this idea of being smaller, smarter, cheaper, attributable, networked, and even swarming.
[1453.24 → 1455.50] It's playing out in Ukraine as we speak.
[1455.80 → 1458.46] Now, is that going to make the difference between winning or losing the war?
[1458.64 → 1460.92] Well, I think it's made the difference in not losing the war.
[1461.26 → 1463.82] It's much harder to win the war because you're up against Russia.
[1463.94 → 1466.06] It's a very difficult fight that they're up against.
[1466.44 → 1470.38] But what we're seeing is technology used in such imaginative ways.
[1470.38 → 1478.68] And it's this weird juxtaposition of World War I-like trench warfare with AI-enabled systems,
[1479.10 → 1484.50] Maven-like capabilities that are being used to find targets, spot targets, and send artillery
[1484.50 → 1485.34] against targets.
[1485.66 → 1490.94] So you're seeing what a lot of us thought was coming, and it did happen, it is happening,
[1491.26 → 1496.50] about how quickly you can adapt to the changing conditions of the battlefield, or I would say
[1496.50 → 1499.10] battle space because cyber is part of this as well.
[1499.10 → 1505.30] Electronic warfare is really, really important right now because it's killing Ukrainian drones.
[1505.44 → 1507.14] The Russians are very good electronic warfare.
[1507.54 → 1510.46] So now the Ukrainians are trying to adapt based on what's going on.
[1510.62 → 1515.28] So we have to listen to those lessons and apply them to the U.S. Department of Defence.
[1515.38 → 1519.40] And I, by the way, and I'll stop here, does I think what you're seeing is the Replicator Initiative,
[1519.60 → 1524.96] which is buying thousands of drones of various sizes and capabilities, is in a large part,
[1524.96 → 1529.18] I think, based on the lessons that they're absorbing from what we see in Ukraine.
[1529.18 → 1532.18] I wanted to go back for a moment to software-defined warfare.
[1532.90 → 1540.00] There is the paper that you just referenced that you wrote with Mr. Molchendani, if I'm getting his last name pronounced correctly,
[1540.44 → 1546.36] who is your CTO at the Jake, and I believe he's the CIA CTO at this point.
[1546.44 → 1546.90] He is.
[1546.90 → 1549.44] That was quite a landmark paper.
[1550.36 → 1555.88] Ironically, for those of us who are in industry and maybe not military-related at all in the audience,
[1556.36 → 1560.74] you're used to Daniel and I always talking about, you know, AI is still part of the software.
[1561.02 → 1562.78] It's all bound together.
[1562.96 → 1570.10] You can't do AI without the hardware and the software and the systems written together to make it practical AI that's usable.
[1570.10 → 1573.48] And you really went there in software-defined warfare.
[1573.48 → 1578.02] It's called Software-Defined Warfare, Architecting the DoD's Transition to the Digital Age.
[1578.20 → 1587.58] And it was quite a landmark paper for those of us in that industry because it really laid out the future of how software needs to be integrated.
[1588.02 → 1596.66] Do you have anything that you wanted to comment on about that, just given I thought it was very important to anybody concerned with AI in the DoD?
[1596.66 → 1602.78] And it was really written by Nan Mulchandani after his experiences in Department of Defence with the Jake.
[1603.16 → 1608.06] Then he left, and before he took the CIA, he had had all these ideas germinating.
[1608.34 → 1610.32] And he said, you know what, I'm going to write about this.
[1610.46 → 1613.24] And we're co-authors, but he's the author.
[1613.38 → 1617.62] I'm the editor, and I placed the operational imprimatur on that report.
[1618.06 → 1625.58] And it's so important because it represents all the commercial software industry best practices that need to be brought into the Department of Defence.
[1625.58 → 1639.52] And what's sad about this, Chris, is to your point, is if you're in commercial tech industry, and you were to read this report, you would be flabbergasted that the department's not already doing all these commercial best practices, which are just the way of doing business.
[1639.64 → 1642.68] You know, microservices, platform as a service, software as a service.
[1642.98 → 1645.28] It's just so foreign to the Department of Defence.
[1645.44 → 1649.04] Getting there, it's come a long way, but that's why he wrote that paper.
[1649.04 → 1659.22] It is a blueprint and say, we can talk about, this is what NAND and I used to have these conversations toward the end of my time there, is that we can talk about AI until we're blue in the face.
[1659.32 → 1661.26] And we will, it's a wonderful conversation.
[1661.42 → 1672.72] But unless you make the Department of Defence modern and digitally modernized, which includes data best practices and do all the things that's in that software-defined warfare report, AI will be meaningless.
[1672.72 → 1674.88] You'll never get there, at least not at scale.
[1675.18 → 1679.98] And by the way, I am now a member of the Atlantic Council's Commission on Software-Defined Warfare.
[1680.08 → 1685.04] So they've taken that mantle and are making it the centrepiece of all these recommendations they're going to have.
[1685.12 → 1686.74] So it's a really important piece.
[1686.88 → 1701.12] And I thank NAND because, as I'll say for as long as I talk about this, NAND changed that organization the day he showed up because he understood there was a different way that we had to be doing business than the standard traditional Department of Defence way.
[1701.12 → 1730.30] One of the interesting things that I think I haven't seen the specific paper you're referencing, Chris, but I like the ideas that are being discussed here because one of the things that I've seen, and I'm kind of trying to parse through and figure out how to put words to, is when I'm on customer sites or interacting with people, it's something about this AI technology that seems to disconnect people's mind from the fact that there's still a need to have error checking.
[1730.30 → 1739.06] Or like, it's not just that you have this AI and you send something over and it kind of automates things, and then you move on.
[1739.26 → 1752.50] There's still the idea of a software application and there's still a call at the minimum to an API that maybe you need like retries around or some sort of health checks or backups or this sort of thing.
[1752.50 → 1757.92] Does that perception hold water in terms of what you've seen, Jack, as well?
[1758.12 → 1760.20] And you were talking a lot about culture.
[1760.42 → 1770.56] Any recommendations for this kind of dealing with this fact of like swapping software for AI versus embedding AI in software?
[1771.36 → 1772.36] Yeah, completely resonates.
[1772.50 → 1778.92] It absolutely resonates because this is, I even say, maybe this is going a little bit too far, but I don't think it is.
[1778.92 → 1781.72] And Ukraine's validating this, by the way.
[1781.94 → 1784.28] The next conflict is going to be an API-driven conflict.
[1784.70 → 1793.32] If you get that piece right, and can update faster than your adversary on this idea of software-driven warfare, you will have a competitive advantage.
[1793.66 → 1800.36] Because the battles, let's face it, you put out an AI model, and you never update it, then you might as well have never done it in the first place.
[1800.36 → 1807.12] The idea of the battlefield is going to change, the battle space will change, but also models will drift and all the other things that happen.
[1807.22 → 1809.26] They get exposed to different data, new data, whatever.
[1809.52 → 1813.52] You're going to have to do a continuous integration, continuous delivery or deployment.
[1813.84 → 1814.84] That's part of this.
[1814.98 → 1824.50] But you can't do that in the traditional way of doing it, which is your have an entire weapon system that you have to pull apart, completely pull apart, rebuild and put back out again.
[1824.50 → 1825.56] That doesn't work.
[1825.66 → 1830.62] You're going to have to break all this apart and just focus on those little bits and pieces that have to be updated.
[1830.76 → 1832.30] You mentioned API calls.
[1832.68 → 1838.80] There is so much more that can and should be done in the department of getting those status updates and two-way fees.
[1838.98 → 1846.38] One, feeding those updates of higher headquarters down, but two, putting all the things that the end user is seeing, feeding that back uphill.
[1846.78 → 1852.64] That's what we have to be thinking a lot more about to be able to handle what I think is going to be a very, very chaotic environment.
[1852.64 → 1862.88] Now, this AI, however great it may eventually become, does not change the fact, as I said in my testimony, that warfare is a very chaotic, nonlinear, dirty, ugly place.
[1862.88 → 1864.88] And it's horrible that we have to go to war.
[1865.16 → 1870.74] But this technology could provide that competitive advantage that makes a difference in a future fight.
[1882.64 → 1897.12] You know, when we started podcasting back in 2009, an online store is just the furthest thing from our minds.
[1897.52 → 1900.42] Now we have merch.changelog.com.
[1900.50 → 1902.82] And you can go there right now and order some T-shirts.
[1902.98 → 1904.46] And that's all powered by Shopify.
[1904.86 → 1905.66] It's so easy.
[1905.78 → 1908.08] All because Shopify is amazing.
[1908.08 → 1914.22] Shopify is the global commerce platform that helps you sell at every stage of your business.
[1914.22 → 1922.44] From the launch your online shop stage to the first real life store stage, all the way to the did we just hit a million dollar stage?
[1923.00 → 1924.56] Shopify is there to help you grow.
[1925.18 → 1933.84] Whether you're selling security systems or marketing memory modules, Shopify helps you sell everywhere from their all-in-one e-commerce platform to their in-person POS system.
[1934.28 → 1937.52] Wherever and whatever you're selling, Shopify has got you covered.
[1937.52 → 1945.30] Shopify helps you turn browsers into buyers with the internet's best converting checkout up to 36% better compared to other leading commerce platforms.
[1945.74 → 1950.42] And sell more with less effort thanks to Shopify Magic, your AI-powered all-star.
[1950.88 → 1956.90] You know, nothing gets me and Jared more excited than when our guests get that coupon code in their email when their show ships.
[1957.08 → 1965.16] Or to everyone out there who loves Change Law Podcasts and can go to merch.changelog.com and get your favourite threads to support our podcasts.
[1965.16 → 1967.66] It is just the best thing ever.
[1967.96 → 1972.32] From stickers to threads, all that is at merch.changelog.com.
[1972.70 → 1977.34] And did you know that Shopify powers 10% of all e-commerce in the U.S.
[1977.34 → 1988.44] And Shopify is the global force behind All birds, Roth's, and Brookline, and millions of other entrepreneurs of every size across 175 countries.
[1988.92 → 1995.04] Plus, Shopify's extensive help resources are there to support you and your success every step of the way.
[1995.40 → 1998.06] Because businesses that grow, grow with Shopify.
[1998.06 → 2005.84] Sign up for a $1 per month trial period at shopify.com slash practical ai, all lowercase.
[2006.28 → 2013.12] Go to shopify.com slash practical ai now to grow your business no matter what stage you're in.
[2013.46 → 2016.68] Again, shopify.com slash practical ai.
[2028.06 → 2044.02] To extend what we were just talking about right before the break, you kind of finished talking about the study of warfare being asymmetric technology advantage.
[2044.02 → 2046.90] You talk about that in your paper and just the challenges.
[2046.90 → 2051.04] And you've talked about integrating in these latest, greatest technologies.
[2051.04 → 2060.38] One of the things that you address a fair amount is you talk about teaming between AI and a human being in the context of national security.
[2060.68 → 2068.36] And adjacent with that, which I know Daniel asked you a little bit of a question about that earlier, kind of having to do with safety and the security of the AIs and stuff.
[2068.36 → 2078.66] Can you talk to us a little bit about, you know, that's obviously a question that many people have in their minds that have nothing to do with this space, you know, the military or the surrounding industry.
[2078.66 → 2081.24] Just concern about what is teaming mean?
[2081.72 → 2085.20] How far in your thinking does autonomy go?
[2085.60 → 2094.78] Is there a point just to infer something that as the pace of warfare speeds up, you know, we have drones, and we have different types of autonomous technologies and stuff.
[2094.78 → 2106.90] But as the pace of warfare speeds up, and you look into the future versus kind of what we're looking at in the near term, how does that change the human AI teaming equation as you're trying to keep up?
[2106.90 → 2113.50] You know, and maybe having humans in the loop can become a problem or a serious logistical issue.
[2114.04 → 2118.84] How are you looking at the future in terms of where we are today and where that's going?
[2119.24 → 2122.48] And what are some of the challenges that we need to overcome to get there?
[2122.48 → 2130.46] I think so strongly about this idea of human machine teaming or human systems integration that if we don't get this right, we're in trouble.
[2130.90 → 2137.04] And what I mean by that is there are people who have been writing about human machine teaming in some form for 50 years.
[2137.04 → 2141.00] No different in terms of the concept of how do you get the post out of human machines?
[2141.00 → 2153.04] But to me, we're at a period where it is changing, and it's changing because the machines are going to be so much smarter than we're used to talking about that it will be a different view of human machine teaming than we're used to.
[2153.28 → 2155.20] So I think there's a whole new research field.
[2155.36 → 2159.72] There are already people working on this, and I'm amazed at some of the work that's being done.
[2160.10 → 2162.86] But we just don't know how good some of these technologies are going to be.
[2163.12 → 2167.62] Let's just take the example, very briefly, the example of sort of ChatGPT or the equivalent.
[2168.10 → 2169.68] There's this idea of prompt engineering.
[2169.68 → 2174.94] I look at that as almost like the elevator operator in the 30s or 40s whenever it was.
[2175.00 → 2177.38] And it goes away eventually because people get comfortable with it.
[2177.48 → 2178.82] But they're not as comfortable with it today.
[2178.90 → 2181.62] You need help figuring out what that interface looks like.
[2181.96 → 2186.80] But the other thing I say, and this is where I come back to, I really do believe there will be situations.
[2186.98 → 2189.62] I call this the bell curve of military operations.
[2190.06 → 2193.56] Some cases, you really do want that human making that final decision.
[2193.94 → 2198.60] Maybe to launch nuclear weapons is the President of the United States and nobody but the President of the United States.
[2198.60 → 2202.32] On the other end, you need the machine to do what the machine does best.
[2202.40 → 2203.94] There is no time to get in the way.
[2204.58 → 2207.08] Everything else in between, I don't know what that is.
[2207.18 → 2211.26] 80%, 90% is human machine optimized for both.
[2211.62 → 2213.14] That centaur idea.
[2213.70 → 2216.20] And that we need a lot more work working through.
[2216.32 → 2219.62] And here's the example I would give from my time in the flying world.
[2220.10 → 2223.28] There were a lot of times the machine did not operate as intended.
[2223.28 → 2227.08] The human was there to make sure that everything went fine with the mission.
[2227.18 → 2228.32] Oh, that broke again.
[2228.56 → 2230.08] We're going to have to pull that circuit breaker.
[2230.32 → 2231.62] I started in the F4.
[2231.74 → 2233.24] Circuit breakers popped all the time.
[2233.66 → 2236.28] You'd piss out hydraulic fluid out the back end or whatever.
[2236.42 → 2239.58] So the human would have to make up for a lot of the machine's mistakes.
[2239.58 → 2242.62] I'm not sure if that's going to be a luxury in the future.
[2242.88 → 2247.52] That you're going to have to let the machine do what the machine does, and the human do what the machine does very well.
[2247.90 → 2248.92] What do the humans do well?
[2249.20 → 2249.90] They do reasoning.
[2250.36 → 2251.34] They do inductive reasoning.
[2251.58 → 2252.52] They do deductive reasoning.
[2252.64 → 2253.72] They do abductive reasoning.
[2253.86 → 2254.88] They put things in context.
[2255.64 → 2257.76] They deal with other human emotions.
[2258.14 → 2259.52] Machines don't deal with emotions.
[2259.64 → 2260.70] They don't understand emotions.
[2260.82 → 2263.76] And I'm not sure, despite what some people claim, they ever will.
[2264.06 → 2265.14] So what does that look like?
[2265.14 → 2267.80] I think there's a lot that has to be done in this area in experimentation.
[2268.50 → 2269.28] Play around with it.
[2269.32 → 2269.98] See what works.
[2270.08 → 2275.60] Because if you don't get it right, and there are a couple of examples where it's went dramatically badly.
[2275.84 → 2278.96] And I think the 737 MAX is one of those examples.
[2279.46 → 2280.92] Well, we're going to put this software in.
[2281.30 → 2281.80] Trust us.
[2281.84 → 2284.22] You don't need to be retrained as a pilot on this.
[2284.44 → 2286.62] Just listen to what it says in the cockpit.
[2286.62 → 2287.48] That was wrong.
[2287.70 → 2291.20] And it's proven that it was dramatically the wrong thing to do.
[2291.34 → 2294.16] So I think this is an area that needs a lot more explanation.
[2294.16 → 2298.20] There are people writing about this and perfect writing in various places.
[2298.20 → 2300.54] But we have to figure out how to get this part right.
[2300.68 → 2306.76] Because the machines are going to be smart enough that they have to be allowed to sort of run when they should run.
[2307.64 → 2313.64] We're seeing both modern models are getting so impressive in certain areas, in certain capabilities.
[2314.00 → 2315.70] There's a lot of hype around them.
[2315.82 → 2316.82] They can't do everything.
[2316.82 → 2325.26] But what they do, they tend to do quite well, recognizing that there are hallucinations and other technical issues to be worked through over time.
[2325.34 → 2330.30] But we're seeing kind of a rapid increase in capability in a lot of these areas.
[2330.30 → 2342.70] So one of the things that I get asked all the time, just kind of on the side with people, is as those capabilities go to some level of increase in the future, whatever that is, and whatever the tasking is.
[2342.70 → 2347.58] And you've kind of alluded to it kind of changes the balance in human teaming.
[2347.66 → 2354.36] Is there a set of metrics or some guidelines that you have in your mind on as you see the technology progress?
[2354.46 → 2359.22] Maybe not today, maybe not this year, maybe not next year, but maybe five, ten years out.
[2359.22 → 2367.24] And you see these capabilities in specific areas increasing far beyond what a human can do for a given task.
[2367.74 → 2369.32] How do you rebalance?
[2369.52 → 2370.64] How do you assess that?
[2370.70 → 2382.18] You talk about assessments in your paper as well, so that you say, this is one of those moments where you let the model do what the model does really well because it does it faster.
[2382.42 → 2386.44] It does orders of magnitude better than a human could do in the same amount of time.
[2386.86 → 2388.20] How do you make those assessments?
[2388.20 → 2395.02] Because I think that for us humans with emotions around technology and warfare, I think that causes a lot of concern.
[2395.14 → 2398.04] It seems to be the foundation of many questions that I get asked.
[2398.46 → 2407.48] How do you make that metric judgment on those adjustments to the culture of how we interact in that way, you know, kind of the way we think about it?
[2407.48 → 2408.88] Yeah, a few thoughts on that.
[2409.06 → 2416.44] And while I remain an AGI skeptic, I do believe these machines, these AI-enabled or smart machines will get so good.
[2416.44 → 2422.66] The human interfering with the machine could be a worse outcome than human-machine together.
[2423.26 → 2428.38] And the example that I've heard, I think it was Gilman-Louis raised this about Alfaro and the Move 37.
[2428.84 → 2432.88] If a human was there to override the machine, it would have lost the game.
[2433.32 → 2435.68] Machines said, no, you really do want to make this move.
[2435.78 → 2436.38] Leave it alone.
[2436.38 → 2437.34] And it won't.
[2437.66 → 2442.62] So that's an example of humans are going to get to the point where they've got to be more comfortable with this technology.
[2442.84 → 2444.30] And they're not necessarily today.
[2444.38 → 2444.76] Why?
[2444.90 → 2451.20] Because just like when I use ChatGPT, whatever version of a large language model, it does get some things still very wrong.
[2451.64 → 2455.44] Maybe the ratio is only 10% versus 20% just a year ago.
[2455.44 → 2461.72] But if that 10% is dangerously wrong, then do you really want that in military operations?
[2461.86 → 2462.88] Not yet, you don't.
[2462.96 → 2463.98] So how do you do that?
[2464.04 → 2465.20] This is the core of your question.
[2465.32 → 2467.48] To me, it is tested and evaluation.
[2468.02 → 2469.00] It's experiment.
[2469.26 → 2479.16] It's putting it into the hands of users as an MVP, a minimal viable product, which again is a little bit different from, or a lot different from the way the Department of Defence has fielded systems in the past.
[2479.16 → 2486.92] Where you fielded a system when it was as close to perfect as you were going to get, which may have not been perfect, but close enough for government work, as we say.
[2487.16 → 2491.02] But in this case, you need to put things in the hands of users sooner rather than later.
[2491.12 → 2492.36] This is why I'm a big fan.
[2492.64 → 2506.00] Despite my reluctance to say we should not be using large language models for putting items in the presidential daily intelligence briefing, you should have all sorts of experimentation being allowed in all these federal government organizations and agencies.
[2506.00 → 2510.48] In fact, the White House executive order on AI says, go try this out.
[2510.74 → 2512.90] It does, it basically says, go do it.
[2513.14 → 2519.52] So I'm a fan of the experimentation, what we'd call sandbox experiments, put it in users' hands because we don't know yet.
[2519.52 → 2522.40] But part of that is core test and evaluation.
[2522.80 → 2525.16] We do not want a short circuit test and evaluation.
[2525.44 → 2526.52] And why is this so important?
[2526.84 → 2530.34] Because I think that's where we're going to see the biggest risk, at least initially.
[2530.88 → 2535.06] Some risks are going to be hard to figure out until you use them in an operational world.
[2535.06 → 2537.22] We just know that, just like in commercial business.
[2537.52 → 2538.96] Some things are going to surprise you.
[2539.20 → 2541.66] But that's why you then update the models because you learn.
[2542.02 → 2553.28] But in that early stages of design and development, before you get to the fielding part, there is this thing that we have done really well in the government for many, many years, especially on the hardware side, it's called test and evaluation.
[2553.62 → 2556.42] That does not go away when we talk about AI.
[2556.58 → 2558.64] In fact, AI is still novel enough.
[2558.72 → 2562.20] I think it's more important than ever to spend a lot of time on the T&E.
[2562.20 → 2566.54] It doesn't mean you're going to go slowly relative to sort of putting out other things.
[2567.10 → 2573.90] But I am a little bit cautious about moving too quickly on some of this because we just don't know what those risks are yet.
[2573.96 → 2580.68] So there's a lot of work going on, including some things I've been working on, on a risk management framework for AI systems in the military.
[2580.92 → 2582.86] Because this risk, it is a hierarchy, right?
[2582.92 → 2585.28] There's one end, there's AI-enabled nuclear weapons.
[2585.40 → 2586.24] Really, terrible.
[2586.24 → 2592.20] On the other end, there's process automation for a finance system that touches nothing having to do with war fighting.
[2592.72 → 2595.06] Negligible risk, move really fast on that one.
[2595.30 → 2601.02] And then a lot of things in the middle, you've got to do test and evaluation, determine how many risks there are, and then come up with risk mitigation strategies.
[2601.70 → 2607.40] I'd love to weave a couple of things together from what you mentioned in your testimony.
[2607.40 → 2615.04] One of those having to do with a concept which I thought was fascinating around techno-economic net assessments.
[2615.42 → 2616.68] And I think there's a lot of people.
[2617.28 → 2619.94] So I'll ask you to maybe explain what you mean by that.
[2620.00 → 2628.86] There's probably a lot of people that see news articles about, oh, this country is ahead of this country and this type of AI, whatever.
[2628.86 → 2637.74] And of course, you see articles about, oh, China, whatever company in China bought up this many GPUs or other things like that.
[2637.86 → 2640.90] And depending on where you're at, you get concerned.
[2641.32 → 2643.34] But it's all sort of very amorphous.
[2643.58 → 2650.76] And it's hard to really grasp where countries are in terms of the AI stack and their capabilities.
[2651.14 → 2657.40] And the other thing that you mentioned in the testimony is encouraging the DoD to take bigger bets.
[2657.40 → 2667.36] And I imagine that that's also connected with sort of making sure that our techno-economic net assessment is sort of on the upward trend.
[2667.50 → 2674.98] Could you talk a little bit about those ideas and maybe how they're connected and how you would love to see this kind of big bets going forward?
[2675.62 → 2682.72] Yeah, if anybody was not in the government and skimmed through my testimony, they probably would have gone past that paragraph and not paid any attention to it.
[2682.86 → 2684.22] There's a reason I put it first.
[2684.28 → 2684.96] It's that important.
[2684.96 → 2686.86] It really is the centre of attention.
[2686.86 → 2695.12] And that is, let me put it in terms of, say, one commercial company competing against another commercial company in the same general business space.
[2695.28 → 2699.94] CEO of one is always looking at CEO of two saying, how much faster are they moving?
[2700.30 → 2704.98] What special sauce are they bringing into their product that threatens our market dominance?
[2705.32 → 2707.46] This is going on every day in commercial industry.
[2707.70 → 2711.14] Well, it's also going on between states, in this case, in AI.
[2711.14 → 2719.62] So the problem is with states is you can get a lot with industrial espionage, but it's a little harder to do when you have a nation state like China.
[2719.62 → 2724.88] And both sides, the United States and China, are talking about how much they're each doing in AI.
[2725.14 → 2727.96] But how much is reality and how much, again, is the hype?
[2728.30 → 2730.18] Well, you need a lot of intelligence assessments.
[2730.18 → 2737.68] And I found this out from my earliest days in Project Maven where I would ask these questions about, okay, and I'll stay very unclassified here.
[2738.06 → 2741.16] The People's Liberation Army, what does their AI stack look like?
[2741.58 → 2747.96] The Intel community is not spending any time collecting, or at least they weren't at the time because nobody told them to.
[2748.36 → 2749.20] What is a GPU?
[2749.56 → 2752.26] Okay, well, we know where we have to start this conversation.
[2752.44 → 2754.36] That is, what does their compute look like?
[2754.60 → 2755.84] What do their models look like?
[2755.84 → 2758.24] Are they using open source, or who's building them for China?
[2758.32 → 2759.86] What does their talent base look like?
[2760.18 → 2769.38] So this idea of not just technology, but then equally important on both sides, U.S., China or U.S., Russia, whatever you want to say, is what are they doing with the technology?
[2770.02 → 2772.12] What are they building new operational concepts?
[2772.30 → 2773.94] Are they actually reorganizing?
[2774.44 → 2778.24] When you start seeing bureaucratic reorganization, they're far along.
[2778.24 → 2779.26] We don't see that yet.
[2779.40 → 2784.40] We don't see it in the Department of Defence because we haven't figured out exactly what this new technology is going to do for us yet.
[2784.40 → 2786.34] So that's what I mean by this.
[2786.38 → 2790.02] And by the way, the U.S. government used to have this thing called the Office of Technology Assessment.
[2790.50 → 2794.28] I think Newt Gingrich managed to kill that as part of the revolution in government, whatever.
[2794.72 → 2797.90] Now there's some serious work to bring something like that back.
[2798.36 → 2808.78] Now I'm just talking about within the Department of Defence and the intelligence community on the classified side, how do I bring in all this information, both unclassified and classified information,
[2808.78 → 2814.84] to give us a relative net assessment, a net assessment, us versus them, where do we stand?
[2814.92 → 2824.26] And it turns out that's pretty difficult to do because technology is not so easy to take a picture from a satellite of a GPU and decide how much farther they are ahead.
[2824.34 → 2832.50] So to me, we've got to do better at understanding vis-à-vis, you know, the United States, vis-à-vis China or Russia or anywhere else around the world, what they're doing in this area.
[2832.50 → 2839.80] And so it's such a big concept to get right, and it's hard because it's just not like collecting against tanks or nuclear weapons or something.
[2840.18 → 2841.24] I can't see it anymore.
[2841.50 → 2847.00] And as I say, there's no fluid coming out of a building somewhere to tell me that they're working on a particular project.
[2847.84 → 2853.60] Well, Jack, we have covered so much material here and time that we've been talking has flown by.
[2854.08 → 2859.96] I think we're going to, if you're willing, we're going to have you back on the show because there's a lot that we haven't been able to address yet.
[2859.96 → 2874.36] But as we finish up, I'm kind of thinking in the background about culture and what you were talking about and just the massive organizational and even national change that we're doing here in the United States in government and military and intelligence.
[2874.70 → 2878.86] It's changing the way that we are looking at the future of war fighting.
[2879.28 → 2887.58] You mentioned in your paper the joint war fighting concept, which I'm very familiar with, and I believe there is an unclassified version out there that we'll add into the show notes.
[2887.58 → 2893.14] But it's changing the way we think about all that we do with the military and intelligence.
[2893.70 → 2895.80] And I think AI is a big part of that.
[2896.12 → 2906.54] As we wind up, do you have any – we often ask guests to kind of take the last question to be whatever you want it to be, paint a picture of the future with whatever you want to be.
[2906.54 → 2924.90] Can you give us a sense of kind of what you're excited about going forward, how you think some of this may evolve, and what that means to the United States military and intelligence community so that the listeners to this, mostly not involved in that directly, have a sense of where things are going?
[2925.02 → 2926.52] Any thoughts you want to finish with today?
[2926.90 → 2927.00] Yeah.
[2927.08 → 2927.52] Thanks, Chris.
[2927.58 → 2930.72] And thanks, Daniel, for allowing me this time with both of you today.
[2930.72 → 2933.32] And it's a big thought, and it's something I've been thinking a lot about.
[2933.52 → 2937.10] And when I retired, I went back and got another master's degree thanks to the GI Bill.
[2937.60 → 2943.70] And I did get a chance to think big thoughts about technology over the course of human history.
[2943.84 → 2953.14] I mean, really, back to the very beginning, I took some courses about looking at what we would call – maybe not technology today, but it was back then – say sugar or tea and how it sort of diffused globally.
[2953.14 → 2964.74] What I say in my testimony, I do believe in my core that we are going to be in the middle of, at some point, the third revolution, sort of agrarian revolution, industrial revolution.
[2965.08 → 2965.70] This is different.
[2965.80 → 2967.24] It's not the fourth industrial revolution.
[2967.38 → 2969.26] It's some kind of digital revolution.
[2969.86 → 2973.66] We don't know what it's going to look like because we just haven't been there yet.
[2974.04 → 2979.42] I say in my testimony, the future is, to a large extent, both unknowable and unpredictable.
[2979.98 → 2980.20] Why?
[2980.20 → 2982.40] Because it's not determinism.
[2982.50 → 2984.10] It is not technological determinism.
[2984.36 → 2993.62] It will be dependent upon the decisions by many, many, many, many thousands of people, from leaders to citizens of countries deciding they like or don't like the technology.
[2993.98 → 2996.96] It's going to take maybe 50 years to 100 years to play out.
[2997.36 → 3002.04] And historians will be the ones that look back and define when this revolution began.
[3002.22 → 3005.52] But to me, it is fundamentally different, which means warfare will be different.
[3005.80 → 3007.66] The character of warfare is going to change.
[3007.66 → 3016.82] I will not say the nature of war is changing because the nature of war is a human-centred decision, like why we fight and why one country fights another country and so on.
[3016.88 → 3018.30] So I don't believe the nature of war.
[3018.44 → 3022.54] But the character of warfare is going to change dramatically as we're seeing in Ukraine.
[3022.54 → 3028.52] And we have a chance to be on the right side of that, as I say in my testimony, asymmetry equation.
[3028.52 → 3030.86] And if we're on the wrong side of it, we risk losing.
[3030.98 → 3032.30] And we're not used to losing.
[3032.72 → 3034.34] And this is a very serious risk.
[3034.34 → 3039.36] So this idea of it's playing out as we speak, get involved in it.
[3039.60 → 3041.10] Don't wait for it to catch up.
[3041.16 → 3047.64] You've just sort of got to dive in and start working these big projects in the government, wherever you are or anywhere else in the industry.
[3048.46 → 3050.44] Well, that's a great call to action to finish up with.
[3050.84 → 3056.30] Jack Shanahan, thank you so much for joining us on the Practical AI podcast.
[3056.30 → 3058.94] Really, fascinating conversation.
[3059.12 → 3060.06] Thank you for your insights.
[3060.50 → 3063.78] And hopefully we can get you back on the show to cover things going forward.
[3064.16 → 3065.24] Really appreciate your time.
[3065.70 → 3065.98] Thanks, Chris.
[3066.08 → 3066.56] Thanks, Daniel.
[3066.68 → 3068.14] And of course, I'll be glad to come back.
[3075.60 → 3076.60] All right.
[3076.94 → 3079.26] That is Practical AI for this week.
[3080.06 → 3081.08] Subscribe now.
[3081.08 → 3086.26] If you haven't already, head to practicalai.fm for all the ways.
[3086.74 → 3092.66] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[3093.24 → 3097.88] Sign up today at practicalai.fm slash community.
[3098.48 → 3104.28] Thanks again to our partners at fly.io, to our Beat Freaking Residents, Break master Cylinder.
[3104.54 → 3105.42] And to you for listening.
[3105.76 → 3107.52] We appreciate you spending time with us.
[3107.88 → 3109.06] That's all for now.
[3109.32 → 3111.00] We'll talk to you again next time.
[3116.30 → 3121.46] proved to be true.
[3121.46 → 3135.50] Law of
[3135.50 → 3137.60] competence.
[3137.60 → 3139.70] We'll talk to you again next time.
[3139.70 → 3144.06] We'll see you next time.
