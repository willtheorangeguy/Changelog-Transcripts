**Adam Staravia:** Let's come closer to centre, right? We're podcasters, we do audio pretty much for a living, and why not talk about the thing that sort of powers the metadata of -- not sort of, but totally does power the metadata of the mp3 that we famously ship around the world for people to listen to. The ID3 tag. So Lars is here. Lars, hey. Good to see you. Good to have you back on one of our shows. You've been on Ship It recently, now on the Changelog, talking about this dive into ID3v2, and v3, and v1, and VX, I guess with your... What is -- is it a plugin? What is what you created called?

**Lars Wickman:** So for your needs to ship chapters, I built out a library for decoding and encoding ID3 tags. And we focused on the 2.3 spec. I can enumerate the specs that you could possibly deal with; it's ID3, also known as ID3v1. It was the first version, before they had a versioning scheme. Then you have ID3v2.2. I haven't seen 2.0 or 2.1, so I don't know if they ever shipped.

**Jerold Santo:** Hm... It may have been quick iterations, maybe while they were drafting.

**Lars Wickman:** Then there's 2.3, and 2.4 being the most recent one. And I get the sense that it didn't get the full-on adoption of 2.3. So 2.3 Seems like the gold standard now.

**Jerold Santo:** That's the one that we're using?

**Lars Wickman:** Yeah.

**Adam Staravia:** 2.3.

**Jerold Santo:** It's kind of like Star Wars. Remember Star Wars Episode Four, A New Hope. When George Lucas first released Star Wars Episode Four, it was just called Star Wars.

**Lars Wickman:** Well, they didn't call it ID1...

**Jerold Santo:** That's right. ID3v1. So was there an ID2? Was there an ID1? These things are -- we'll never know. We'll never know the answer to these things.

**Adam Staravia:** It was always challenging for them to start, I guess, four episodes into a six-episode non-trilogy. Mixology? I don't know what would you call it? Sept ology? That would be seven, sept ology. Right?

**Jerold Santo:** It ended up being three trilogies. But I'm not sure what you'd call that either... Ideology, that's what I'd call it. It's kind of like Scientology, only different.

**Adam Staravia:** Let's not all do that. But hey, ID3 is this, I guess, interesting and non-interesting thing that has unique takes... You wrote a blog post titled "What ID3v2 could have been." Very good deep dive. We tasked you with running this library, so that we can finally have chapters, which - Jerold, you've got a blog post pending. I don't know if it's going to go out before or with this episode; we don't know. But check the show notes there, there might be a link there. Worst-case, follow --

**Jerold Santo:** It should be out by the time this goes out, unless something goes terribly wrong.

**Adam Staravia:** So we tasked Lars -- Lars... With -- since I'm having to say his name correctly, since I'm American; we get lazy. We say Lars, instead of Lars... But ID3v2, what could have been; but before this task, you had not looked into the spec. Had you messed with audio at all, really? I mean, I know you've done some stuff behind the scenes with Sonic Pi, and stuff like that... But at this level, messing with a file, writing its metadata - had you like looked into ID3 at all, ever, before this task?

**Lars Wickman:** \[05:48\] So I was familiar with the format, because growing up in the '90s and 2000s, it's like "Oh, this mp3 file doesn't show the right artist title." So I'd try to go into Properties in Winamp or whatever, and it's like this ID3... But I can set artist, and the title, and if I set those, they will be shown instead of whatever's in the file name. That was sort of where I started with ID3. And after a while, Winamp started to support more fields in two different tabs. That was ID3v2.

**Jerold Santo:** Yeah, it got complicated.

**Lars Wickman:** And that was probably the extent of my use of it. I didn't really spend any time with the binaries of it up until this point, really.

**Adam Staravia:** I had a similar path too, with Winamp, and then also iTunes. I've done a lot of fuzzing with -- back in the day, when we used to have iTunes, and actually have mp3, or potentially actual WAV files that you've... I would rip my own CDs to digital so I can listen to them anywhere. This is when you had your own CDs, basically, that you would swap out like -- I don't even know what I'd call myself then, but like this manual process. Who wants to do that, right? To have this digital file and take it anywhere with you.

**Jerold Santo:** To be clear, ripping our own CDs that we purchased legally is the only way that any of us ever acquired any sort of audio files back in the 90s.

**Adam Staravia:** Truth. Truth.

**Lars Wickman:** Yes, because there was not a widely spread practice of carrying computers to other people's houses and downloading a sort of wandering MP3 collection, that for some reason had disproportionate amounts of Enya in it.

**Jerold Santo:** \[laughs\] Everybody loves Enya. You got a love Enya. Here's what was interesting about that for me... I had the exact same introduction to ID3 tags, through wanting a more pristine music library, but having gathered said library from the four winds...

**Adam Staravia:** Friends, friends...

**Jerold Santo:** Yeah, wherever that you get them... And if there was any sort of discrepancy, for instance, in the album title, between two mp3s that are on the same album, they would list duplicate in my player, whether it was Winamp, or even iTunes in the same way. But there was a satisfying moment when you took those duplicates, and you reconciled to a single album title, without whatever punctuation or whitespace at the end, or you got rid of that weird Unicode character that wouldn't render properly anyway... That they would like to collapse down and be considered part of their own album, instead of being two separate albums. So that very much tickles the nerd in my body... Weird sentence... And my completions body as well. Just like, "I've got to do this for all my mp3." So I spent lots of time inside those editors just tweaking ID3 tags, and just trying to get them all to be awesome.

**Lars Wickman:** I am not a completions, nor a perfectionist...

**Jerold Santo:** \[laughs\] You're not a completions... Adam?

**Adam Staravia:** Very much so, yeah. Very much. I guess the ones that drove me most nuts was when it was a compilation.

**Jerold Santo:** Yeah.

**Adam Staravia:** Like, it was multiple artists, so you couldn't group by artist. You had to go by album. And then when you want to listen to -- it was just a mess. So I would always be tweaking albums, artists, songs... It's just a never-ending battle. And I guess that's the beauty of the cloud, really, the music in the cloud, because it kind of does it for you, and you never have to do it again... Because I haven't done it since, pretty much...

**Jerold Santo:** Right.

**Lars Wickman:** But it also takes away the possibility of having a correct music collection, because Spotify will not give you the correct thing. It's like, "Oh, this is a great playlist I used to play." And now that I play it, they have a weird live cover of this entire band, instead of the original songs, because they lost them. Oh, Spotify doesn't have this track anymore. They'll just substitute something...

**Adam Staravia:** \[09:52\] A small tangent on that note... How interesting is it that we could be having a conversation here, we can remember a song from back in our heritage, our young years, or whatever, 20 years ago, and for the most part, we can probably pull up Spotify or some version of Spotify out there, iTunes Music etc. and we can probably play that song in a matter of seconds. Like, you would have to go out and own that music, which isn't like bad or good for the artists, but you'd have to have owned the thing, maybe have to go traverse and find the disc, put it into the disk player you don't own anymore, using old RCA cables, plug... Like, now it's all digital. It's HDMI, it's optical, digital etc. to plug these components in together... In a moment's notice, we can play Offspring from back in the day, right now.

**Jerold Santo:** That's hilarious, because that's the exact band I thought of when you said that... I was like, "You could play an Offspring track" and you just went to the exact same place.

**Lars Wickman:** Offspring was my first cool album. I had some cool ones before, but Smash... That was a good album.

**Jerold Santo:** Oh, can we play this? Why not... \[sample 00:11:10.19\]

**Adam Staravia:** You got a love self-esteem, right? I mean, in a moment's notice, we can play that. Ain't that crazy?

**Jerold Santo:** Well, go back even further, and they had to wait for songs to come on the radio. And if you wanted to hear a certain song, you had to call in and ask them to play it for you.

**Adam Staravia:** And sit there all day and listen to the radio.

**Jerold Santo:** \[laughs\]

**Lars Wickman:** With a tape deck ready.

**Adam Staravia:** Exactly. And you'd have like a little bit of the previous song, the DJ, some sort of bit, and then the song. Wow...

**Jerold Santo:** Same -- Now looping back to Star Wars - it was the same thing. When I was a kid, to see Star Wars we had to wait for it to come on. Or we had to have a friend who had like a -- not even a DVD. They had a...

**Adam Staravia:** Laser disc?

**Jerold Santo:** No, not laser disc. What was the previous -- not Betamax? VHS tape.

**Adam Staravia:** VHS tape, yeah.

**Jerold Santo:** Right? Their parents were wise enough to tape it when it came on at one time that year, and have a recording of it...

**Lars Wickman:** That particular family that daddy knew -- that had two VHS players.

**Jerold Santo:** Yes. \[laughs\]

**Adam Staravia:** That's right.

**Lars Wickman:** It's all piracy...

**Jerold Santo:** It's piracy all the way down, yes. So times certainly have changed. Well, let me get back to changing things... This spec change - we talked about ID3v1, which we all have nostalgic 90s memories of. There's an aspect of it which plays into this conversation, which is it being a fixed width format, right? Like, it's 128 bytes, and only so much is going to fit inside those bytes. And inside of that, there's a specific number of bytes allocated for each field. So I think the album title could only be like 30 characters, or something. Or it maybe depends on --

**Lars Wickman:** 30 bytes.

**Jerold Santo:** Okay, 30 bytes.

**Lars Wickman:** Each. Yeah. So 30 bytes, 30 characters.

**Jerold Santo:** Yeah, exactly.

**Lars Wickman:** Each. For title, artist, album and comment. And that also means that a bunch of characters was off limits, because I think everything was Latin one or ISO88591.

**Jerold Santo:** Right. Yeah, no UTF8 back then for that particular thing. So if your album title was too long, you just had to decide where you were going to truncate it. So you have a bunch of just partial titles. The titles for a lot of our episodes, Adam, wouldn't fit in ID3v1. You'd have to just truncate it, and maybe throw the ellipses in there at the end...

**Adam Staravia:** Total sadness.

**Jerold Santo:** Total sadness. So there are obvious limitations. That being said, pretty cool how simple it is. Lars, maybe you remember, or you know why it's at the end of the file, though. It's like 128 bytes at the end of the mp3 file.

**Lars Wickman:** I'm pretty sure that was done to avoid tripping the MPEG parsers. I recall having seen something about why it was there, but I don't recall -- yeah, okay, [Wikipedia tells me](https://en.wikipedia.org/wiki/ID3#ID3v1)... "Some players would play a small burst of static when they read the tag". So yeah, probably not have it at the start.

**Jerold Santo:** \[14:02\] So the first second of your song is like \[static 00:14:02.23\] and you're like, "What?!" and then it starts.

**Adam Staravia:** It's not an ideal listening experience, that's for sure.

**Jerold Santo:** So that's kind of like a backwards-compatibility thing.

**Lars Wickman:** Yeah. But more modern players will correctly skip it. And that's good, because IP3v2 moves it to the start of the file... Which makes it better when you're streaming the audio, for one thing, which means you can read all the metadata, and then start playing it. And I think that's what most pocket mp3 players that existed for a long while, but no longer do - they don't keep the whole song in memory, I don't think. They're very, very dumb little machines. But they can probably read the ID3 tag to show the title and keep that in memory. But yeah, if we were only supporting ID3v1, this would have been a two-day project, I think...

**Jerold Santo:** Maybe less... \[laughs\]

**Lars Wickman:** I mean, tests, and then documentation...

**Jerold Santo:** So one part of this -- so we hired Larsen to do this work, and he did a great job over the summer of getting this done. This is so that I wouldn't have to do a much slower, much worse job of trying to accomplish the same thing and never actually get it done, which is historically what we had done with chapters. And part of that was like me being your customer, right? So you got to do all the standard consultant customer relations... It's fun for me to be the customer, because I can ignore you for a long time, and then suddenly be like "Let's work on this!" and you're supposed to be nice to me anyway, and be like "Yes, sir. Let's work on it right now, when you want to, because I'm the customer." So maybe we can talk about that dynamic.

But part of this was like me saying, "Well, our specific needs are important here", and one of the tiny little things that I wanted to do was when we mix down a WAV file into a mp3 file inside of Adobe Audition, which is our workflow, Audition adds some lame ID3v1 stuff. And then when you throw that through some sort of parser, such as a command line tool like the ID3v2 command line tool that we're using to test, it will display that stuff even after we've written our own good ones. And I was "Can't it just also strip that?" And you're like, "Well, it's at the end of the file. Does it really matter?" And I was like, "No, not really..." And then the nerdy completions in me was like "Yeah, but I really do want it to be out of there..." So I wrote this little function - you can see it in our mp3 kit - that just removes v1 tags. And it's like seven lines of code, and it took me like 25 minutes... And sure, I'm just removing them, I'm not writing them. But it was like literally a 15-minute deal. And so I think if that was the goal, I think a) we probably wouldn't have hired you. But b) you probably would have accomplished it in like the time it takes to eat lunch.

**Lars Wickman:** I mean, it's one pattern match in Elixir... Since it's a static length, it's always 128 bytes. So that's one line in Elixir.

**Jerold Santo:** Yeah, it really is nothing in Elixir. Elixir is really well suited for this kind of work. Maybe you can speak to that as well at some point.

**Lars Wickman:** Yeah.

**Adam Staravia:** Does a mp3 have to have one of these tags? So if Adobe Audition takes a WAV file and mixes it down to a mp3 and puts this lame ID3v1 version in, does a mp3 have to have ID3 at all?

**Lars Wickman:** No. The mp3 MPEG standard has no metadata system. That's why ID3 was introduced by some enthusiasts...

**Adam Staravia:** So why? I mean, we don't ask that there'll be to put anything in there.

**Jerold Santo:** Well, they just want to...

**Lars Wickman:** No, I think there'll be -- Audition writes two things. So it probably does an ID3v1, that Jerold removes, but it also does an ID3v2...

**Jerold Santo:** Correct.

**Lars Wickman:** ...with proper, the more likely metadata. But you can have both. So it probably adds both for safety.

**Jerold Santo:** It does. And then your library overwrites theirs on the v2, but it'll let the v1 be a dangling 128 bytes...

**Lars Wickman:** \[17:59\] Yeah. And the library can overwrite both the 2.2 and 2.4, because it's very easy to parse the parts that are required, to sort of capture the tag and strip it out. But there's a bit more nuance when you start parsing version 2.4, and then what's in -- since you didn't need it, it wasn't worth putting the time in. Welcome contribution though, since it's open source.

**Jerold Santo:** It is open source. You can go out, and you can install it in your mix file, and it's out there on hex. Pm, and it's also out there on GitHub for the source code... So I encourage people to use it.

**Lars Wickman:** And I think that's a very classy approach of you all, to actually hire someone to do the job, but turn it open source and take on maintenance.

**Jerold Santo:** Yeah. Well, it's basically just replacing me with you on the bootstrap, like on the parts that you're good at, and I would be less good at, and then just like treating it like it's our own thing, which is exactly what we would have done without you. I would have built a library, released it open source and maintained it. And so happy to just bring you along for the ride, get a better library than I could have written, faster, while I'm also working on other stuff... You get some business out of it, so that's good for you and your consulting firm... And we all get the benefit. I mean, why not?

**Lars Wickman:** Yeah, I think it's a classy move.

**Jerold Santo:** Yeah, I try to keep it classy around here. I appreciate that.

**Lars Wickman:** But we all only mentioned sort of titles and albums and artists.

**Jerold Santo:** True.

**Lars Wickman:** ID3v1 only had that, and some genre, and a comment of 30 bytes, I guess... But ID3v2 added so much more. And a bunch of the things are just very reasonable things like "Oh, the year it was released and published, and who the publisher was, and who the composer, and the writer, and the lyrics by... sort of things... So just more metadata that you could add, that were simple text fields. But then you start getting things like artwork; you can bring some artwork in there. Pictures, URLs... But as you go into implementing this stuff, you find the fun and weird tags. And that's sort of what prompted this blog post. Because it's absolutely fabulous stuff in there.

**Jerold Santo:** Yeah, there is fabulously interesting stuff in there. And I wish we were like a fly on the wall of the meetings of the spec writers... Because it seems like to me, as I read your posts, I'm like, "This seems like almost like maybe ID3v1 was just written maybe in a weekend, by some enthusiasts, and then like serious business people came along." And I'm just completely making this up. I don't know the history.

And then I was like "You know what we need is everything and the kitchen sink." And it's almost like, all these different frames or tags, these specific types of frames you can put in your tag - each one seems like somebody's pet project. Like star ratings - isn't that in there?

**Lars Wickman:** Well, if we want to talk ratings, we should probably first talk about the play counter...

**Jerold Santo:** Okay.

**Lars Wickman:** ...because the ratings build on the concept of the play counter, and the play counter is--

**Jerold Santo:** The play counter is actually the funniest one. Tell us more.

**Lars Wickman:** So that's the PCNT frame. So every field in ID3v2 is a frame, and you can have an arbitrary number of them, up to like 256 megabytes of tag...

**Jerold Santo:** Wow.

**Lars Wickman:** ...which will outstrip most audio files you've ever seen.

**Jerold Santo:** I was going to say, if you had like 192 chips song, how long would that song have to be 256 megabytes? Like, five, six hours, maybe.

**Lars Wickman:** It'd be a chunk of a song. That's a decent podcast.

**Jerold Santo:** Maybe like a Grateful Dead concert.

**Adam Staravia:** Sure.

**Jerold Santo:** Like a whole concert from the Grateful Dead... I don't know, just guessing.

**Lars Wickman:** \[21:54\] Yeah. But the play counter frame is a very, very short frame. It has the identifier that is the play counter, and then it has a number. And the idea was that the player you use to play your file would increment that with one, when you've started playing the song... Changing the file forever.

**Jerold Santo:** Changing the file forever. Yeah, so this is like when you almost feel violated; like, "This thing changed me." Shouldn't an audio player be like read-only on a file? I just feel like that's just classy; talk about keeping it classy... It's just weird; like, you're going to change the actual thing that you're --

**Lars Wickman:** But it was also a different time.

**Adam Staravia:** Yeah. I was going to say, what's the timeframe of the implementation of this? Because this was probably back in the day when I was managing my iTunes library, and it was mainly me listening to my mp3s.

**Lars Wickman:** And if you look at those types of libraries, they would have like a SQLite, or other metadata database where they kept their play counts. I don't think iTunes wrote the ID3 play count. It might have, but I doubt it.

**Adam Staravia:** I doubt it, yeah. But you got a wonder where the spec was trying to go, what it was trying to solve. Somebody put this out there... Like you said, Jerold, there are some businesses -- maybe some programmers initially, and maybe businesses thinking "How can we put our composer in there, and give everybody credits? And how can we get credit for the record label? How can we get all our names in this file so that we get marketing?" This may have been like the old -- not so much social network by any means, but like how do you distribute who you are to the world? And you embed it in these mp3 on the internet.

**Lars Wickman:** Yeah. And it's clear if you read through the spec that they considered this metadata to be sort of a significant thing that would communicate a ton of information, and potentially carry data. This play counter is a weird one, because almost no one can see how that would be good... I speculate in the blog post that it might turn out to be sort of a cool, hipster thing if this had caught on, so that all the mp3 files out there had play counts. Could you find that Enya song really close to the source? Could you find an OG? Like, is it 2 play count? Then it's probably close to the rip, right?

**Jerold Santo:** Or just somebody didn't like the song very much.

**Lars Wickman:** Yeah.

**Jerold Santo:** They listened to it once and bounced. Accidentally had it on repeat.

**Lars Wickman:** It definitely feels like sort of like a silly frame. But then we have one that is actually used when reading songs. I think Windows File Explorer preview can actually show the popularity meter stars.

**Jerold Santo:** Is that how you say that? I've been reading that, and I've been reading it the polarimeter...

**Lars Wickman:** Polarimeter... I don't know. Popularity meter is what I'm going for.

**Jerold Santo:** I liked the way you said it, polarimeter.

**Lars Wickman:** It allows storing an arbitrary number of up to the max frame size of 16 megabytes, probably, email and rating pairs. So this is personally identifiable information.

**Jerold Santo:** Oh, it's your email alongside with your rating. I didn't realize it till your email. Wow...

**Lars Wickman:** So we can get a Jerold rating, we could get an Adam rating, a Lars rating... And that's fantastic.

**Jerold Santo:** That's fantastic... \[laughs\]

**Lars Wickman:** And it also bundles in a personal play counter. So you can know, was this rating all BS? Have they even played the song?

**Jerold Santo:** Oh, they never even actually played it...

**Lars Wickman:** I mean, you'd care more what someone who plays the song 100 times has to say about it, I think...

**Jerold Santo:** That's similar to like the Amazon reviews certified purchaser tag. You know, like, "Well, this person reviewed it, and we can verify that they purchased it", which is a nice little added information. Here it's like this person rated it five stars, but they never actually listened to the song.

**Lars Wickman:** Of course, there's nothing to stop Winamp from showing a UI where you can just edit your play count...

**Jerold Santo:** Right. My favourite part about this whole thing is it relies upon this concept, I guess -- like, if this was going to finally make its way back around to the record label, or the artist, it assumes that it had some sort of mechanism by which they could collect all of these mp3 files, right?

**Lars Wickman:** \[26:14\] So I don't think this is signal back. I don't think this is feedback. I can only imagine it being a sort of trading thing, where files are passed around.

**Jerold Santo:** Yeah, but you can just write whatever you want into the -- you can just download Lars' open source Elixir library and just change the values.

**Adam Staravia:** Yeah, because there's nobody saying you can't change the value. If you can edit the thing, the metadata, you can--

**Jerold Santo:** Well, if it makes it more collectible, why wouldn't I just do that?

**Jerold Santo:** Right. Well, I mean, I can change your rating. You could have put a five-star rating, or whatever the... Is it zero through 255?

**Lars Wickman:** Oh, yeah. 0 to 255. That's a good rating system... \[laughs\]

**Adam Staravia:** That's a massive range... If you have rated it 100 out of 255 - like, is that good or bad? I don't know... \[laughs\]

**Lars Wickman:** Like, this song is clearly a 143...

**Jerold Santo:** Right. Like, "Well, I disagree. It's more of a 144." \[laughs\]

**Adam Staravia:** It's a wide range, that's for sure. Don't get Brett Cannon on that range. He'll be upset.

**Jerold Santo:** I was going to say, we need somebody who can formalize what each value means, so that we can actually have an objective measure.

**Adam Staravia:** You've really got to think about what the idea was though, because if this can be edited by anybody... If in the spec process - and this is before the times of ubiquity of Spotify, and streaming music versus shared files via unknown places to share files, etc... What was the idea? Like, what were they trying to solve for, really? I mean, it seems to have no utility in retrospect.

**Lars Wickman:** So I imagine this is a speculative feature, a hundred percent, where they figured, "Oh, if something like Winamp implements this..." Because this was probably launched around the heyday of mp3 exchanging in the more manual sense... Then, if Winamp displayed these things, or you could build a way of exchanging these and seeing these ratings... Like, let's say Napster would show these ratings; then suddenly you'd actually see -- you get some signal; you could index some of this and see, "Oh, I only want five-star songs, essentially." Or 255 rating songs, you know?

**Adam Staravia:** That's right.

**Jerold Santo:** So just to pin this to a timeframe - because we're kind of guesstimating around... According to ID3.org, the version 2.3 was authored in February 1999.

**Adam Staravia:** Oh, yeah.

**Lars Wickman:** In 1999.

**Jerold Santo:** So even maybe older than I was thinking. Maybe it wasn't at that point being used yet, maybe it was just finalized, and the people had to start implementing it... But it goes way back. We're talking 25 years.

**Lars Wickman:** Yeah, so it's not new. So it is really predating a lot of our conceptions of what an audio file should act like, I think.

**Break:** \[28:56\]

**Adam Staravia:** So the correlation to a well-known exchange of mp3 platform was June 1st, 1999. So timeframes were pretty close; maybe they were both speculating on where this file format could go/would go. I don't know.

**Lars Wickman:** And a lot of the frames that are slightly unusual in this spec are also pretty decent web citizens. So in many cases, they are required to reference either a URL where you could find a contact email, or directly a contact email, when there is a source that they want to reference. You know, "Go here, because we can really just include a ton of information in this... But over here, this is where you find the information about whom this is from."

For example, the commercial frame -- and this should be interesting to you. Monetization - this is something that podcasts work hard at.

**Jerold Santo:** Okay, now you're talking my language.

**Lars Wickman:** The commercial frame. This frame enables several competing offers in the same tag by bundling all needed information. So every offer has a price, specified in any number of currencies...

**Jerold Santo:** Oh, wow. \[laughs\]

**Lars Wickman:** A date for how long this offer is valid...

**Adam Staravia:** Wow...

**Lars Wickman:** A contact URL for reaching the seller, and a "Received as" field that can indicate if it's delivered -- for example a standard CD with other songs, a file over the internet, or a stream over the internet, or a ton of other things.

**Adam Staravia:** They had some high hopes for this file format, this spec. I mean, there were some far-fetching ideas here.

**Jerold Santo:** So this is definitely where the business guy came in and decided he needed his frame...

**Adam Staravia:** Yeah. This made me think a little bit, like, could the mp3 format and this ID3v2.3 be used to share information under the radar? Like, "Ship mp3s around this world where people are exchanging mp3s." Maybe there's a Trojan horse in there, maybe there's a virus in there, maybe that's espionage, maybe it's corporate secrets... I don't know. Could you shove information in what you think is a mp3, but it's not -- it is a mp3, and you can play it as a mp3, but it's really meant to deliver something else?

**Lars Wickman:** So you have, for one thing, attached file as a frame. And you can go up to 256 megabytes.

**Adam Staravia:** Yeah. "This is a huge mp3. Wow." Does the length of the mp3 suit the file size of the mp3?

**Lars Wickman:** "How many mp3s can we nest?" That's an interesting experiment...

**Jerold Santo:** That'd be a good way of smuggling. You could smuggle a whole album by just putting all the other songs into the one song's attached files.

**Lars Wickman:** That's true. You could probably fit -- you could definitely fit a whole album into a song.

**Adam Staravia:** But how would you extract an album out of the tag, the frame? Well, you need to use a library, wouldn't you?

**Jerold Santo:** Yeah.

**Adam Staravia:** So you'd have to have some programming skills, or some access.

**Lars Wickman:** Or a tool that parses for that particular tag... But I don't think anyone uses that for anything. There's also custom comments, which you could use and abuse for many things, custom URLs...

**Adam Staravia:** Wow.

**Lars Wickman:** So you could ship anything in this.

**Adam Staravia:** So you could do a lot, really. You could do a lot. You could put a database in there... I think you said an SQLite database can go in there...

**Lars Wickman:** Oh, yeah. That would be convenient...

**Adam Staravia:** An mp3 file... An ISO... Could you put an ISO in there?

**Lars Wickman:** Yeah. I mean, it's an arbitrary file. You could do anything.

**Adam Staravia:** As long as it's under that file size, you're good to go.

**Jerold Santo:** 256 megabytes... Yeah, I guess it's small enough--

**Lars Wickman:** And I wonder if many parsers actually enforce that... Because there's no reason to enforce the file size of the tag you're trying to read.

**Jerold Santo:** Right. All you want to do is get to the part that you're interested in, right? That's a parser.

**Lars Wickman:** \[34:10\] Yeah. And you read the fixed -- so when you're parsing these frames, you look for a frame header. And in that frame header, you have "Oh, what kind of frame is this? How big is this frame?" So if it's a frame you don't understand, you can just skip that number of bytes from the frame header, and then you're at the next frame, you can read that instead.

**Jerold Santo:** Gotcha. You can get to the next one.

**Lars Wickman:** So I think any parser implemented for this would honestly just look at those sizes, and probably not care about the size of the actual tag. There's nothing fundamentally stopping it.

**Adam Staravia:** You could break the rule then.

**Lars Wickman:** I would expect most parsers break the rule, because there's -- "Oh, I wonder if it's actually the size field of... This is probably the size field of the tag header." So the first piece of the ID3 tag indicates how big is this tag.

**Jerold Santo:** Which lets you skip the whole thing if you're not interested in it.

**Lars Wickman:** Yeah. So that's what we do when we're parsing. We know that we don't need to read more than that length of file. I don't think we actually read the full file, because we just start looking at frames and then read as much as we need... But we use it, for example, when we need to replace a tag, because then we can see, "Oh, how far do we need to skip? How much do we need to throw away?"

**Jerold Santo:** To slice off the front, yeah.

**Lars Wickman:** But this commercial frame also lets you include the seller's name and an embedded logo...

**Jerold Santo:** \[laughs\] I love it.

**Lars Wickman:** And -- I mean, I could see this as a use case, if there was a mp3 player that really respected this, where "Oh, we're selling mp3s online." I mean, there have been a ton of businesses that do that. "Oh, here's the sample." So you can get a sample of the song. And then you embed this commercial data in it for buying the full thing. And then you could get that offer right in your client, right? I don't think anyone ever implemented this, but I hope someone did.

**Jerold Santo:** Yeah.

**Lars Wickman:** And then when you've bought the song, you could get offers for the shirt.

**Jerold Santo:** Ooh... An upsell.

**Lars Wickman:** Yeah. I mean, you could get current offers. You could get at-the-time-of-purchase-relevant offers... But at least there's an expiry date.

**Jerold Santo:** You, you'd be able to expire that sucker. It's interesting that we don't even think about -- just kind of going back to Adam's thing with his immediate access to a song from the '90s... Except for maybe some of us nerds and people in the audio world - like, we don't think about the files so much anymore when it comes to listening to music, or listening to podcasts. I mean, we wouldn't even care if our job wasn't to write mp3s out and ship them around the world as podcasters, right? That makes us care. And we wouldn't care about any of this stuff, except for that it's just interesting intellectually, if we didn't want to add chapters to our podcasts. Like, we don't want to add chapters to our mp3 files; we couldn't care less. But we do want chapters in our podcasts, which means we have to add them to our mp3 files. It's a means to an end, for us even. But most people don't even think about like "Oh, my new episode of Beam Radio showed up. I'm so glad that I downloaded the mp3..." I mean, even inside podcasting, they're not all mp3 ease. You can ship AAC, you can ship mp3... It depends on what the players support. You can probably ship FLAC...

**Adam Staravia:** Ogg Vorbis.

**Jerold Santo:** Ogg Vorbis... Many of our listeners probably exclusively listen to Ogg Orbit-based podcasts. I guess -- that can't be true, because they're listening to this one here. So that's a bad speculation. But point being is we've kind of -- at least when it comes to audio, to a certain extent, culturally, we've kind of transcended the file paradigm.

**Adam Staravia:** \[37:54\] Isn't that the case for most things though, really? I mean, you take pictures all day long on your phone, and you don't think of them as files necessarily. You think of them as an image. You upload it to whatever platform you prefer, or share it via iMessage, or AirDrop, or whatever... Furthermore, you don't think of it as a file, really. I think the file paradigm really is like becoming erased.

**Lars Wickman:** I think files exist for PDFs.

**Jerold Santo:** Yeah, I was going to say, business stuff. I was kind of thinking like, where is it that you still think about files? It's like, "Will you send me the attachment to that Word doc, or to that PDF?" And now we're thinking files, aren't we? But I agree with you, images - you kind of don't think about it that way very often.

**Lars Wickman:** Yeah, it's really getting lost, the whole idea of a file... At least the file you edit. Because a PDF is typically still a file, still a document, but you don't edit it. And edited documents are getting rarer with things like Google Drive, and Office 365, and the cloud. DOCX is still a thing, but it's less of a thing than it has ever been before.

**Adam Staravia:** I love it when people send me a DOCX file which is editable, and say "Fill this out." It's like, "Well, I don't have the fonts you had... You're going to get it back all jacked up." Plus, I'm on a Mac, you're on a PC, or something like that... Like, did you think this through? I can add my signature in my PDFs via Preview, which is -- I love that feature. Like, you scribble your own signature, and you drop it on any PDF you want... It's mainly contracts, PDFs, the occasional DOCX file, where they're like "Fill this out", and it's like, "Why? Just give me a PDF? Or send me the DocuSign." Who in this world sends somebody a file and says, "Take this thing and sign it, and then send the file back to me signed."

**Lars Wickman:** I had a background check run on me by a client at some point, and they needed me to send a release to the Swedish police authority... They're a fintech, so it was sort of normal. But I had to print a form, sign it, stick it in the mail... It's like, them and the Swedish IRS are the only people that get me to do that these days. And the IRS my wife takes care of, thankfully. The best CFO I could imagine.

**Adam Staravia:** I love it when they see "We need real ink on this thing." Really? Like, what?! I mean, I guess, if you can't prove I did it... Like, real ink.

**Jerold Santo:** Back in the day weren't there people that actually would forge other people's signatures? And maybe it was just in the movies. Like, you'd hire somebody who would -- they would study a signature, and they would forge it, and you could compare it... The judge or the jury or whatever always compared the signature, and be like "Is this really Adam Staravia's signature?" And it's like, "Well, here's a comparison." That always struck me as weird, because my signature is never the same. Every time I sign it, there's like these subtle differences... And we're getting to the point where I have it saved inside of Preview, and so I can just slap it on stuff... It's like, it's never been less representative of a person than a signature, and yet we still -- at least here in the States, we're still asked to sign for stuff if we don't have Apple Pay or whatever on a credit card deal... Usually at restaurants, because they want a tip, so you've got to write the tip, then add your signature... And it's like, you can just do squiggly marks. It doesn't matter.

**Adam Staravia:** And I do.

**Jerold Santo:** Is forgery dead?

**Adam Staravia:** It's never my real signature. It's always some sort of scribble.

**Jerold Santo:** Can you not be a professional forger anymore? Has that business gone by the wayside?

**Lars Wickman:** I think they get into NFTs now.

**Jerold Santo:** \[laughs\] That's funny... I mean, there is NFT vibes here, isn't there? I mean, going back to the spec... Isn't there NFT vibes going on?

**Lars Wickman:** Yeah. So this is actually something we could pitch for your subscribers, because I've seen that in my Changelog++ subscription it says "For Lars Wickman." Oh, nice. And you could also additionally tag my mp3s with the ownership frame.

**Jerold Santo:** Oh...!

**Lars Wickman:** Then you could put the name in there.

**Jerold Santo:** We could make you the owner of that particular mp3.

**Lars Wickman:** \[42:04\] Yeah. You could even ship a user frame, which is the Terms of Use...

**Jerold Santo:** Hah! A EULA. Do you have to sign it before it'll play? "Before you listen to this podcast, please click you agree to these terms in the..." There's a terms frame... Okay. Owner frame is kind of cool. Like, what if we do that, just because?

**Lars Wickman:** I don't think you want extra copies of your mp3s for every one of your subscribers though...

**Jerold Santo:** Right. But if we're doing dynamic ad insertion style moves - you know, there's people that are actually stitching their mp3s live on request; we could certainly do that. I agree, we do not want to do this, but you can get it done if you're serving a new mp3 for each Changelog++ member. That would feel concierge, wouldn't it, Lars?

**Lars Wickman:** Yeah. I just wish we could get the parsing into all the pod catchers...

**Jerold Santo:** Yeah, true.

**Lars Wickman:** ...so it would show your mp3.

**Jerold Santo:** Yeah, you could even match it with like your SSH public key, and be like "Wow, this really was signed, sealed and delivered."

**Adam Staravia:** Actually, that's a good idea, Jerold. If you put the public key in there, you could ensure that only Lars could listen to the file.

**Lars Wickman:** So there are cryptographic mechanisms for encrypting the entire file using ID3. There's also methods for just signing a group of frames, or part of a file to ensure that the ownership, for example, hasn't been tampered with... And I guess that's sort of where you get into NFT territory, aside from not being uploaded anywhere.

**Jerold Santo:** \[laughs\] I love how we can make up ridiculous things and Lars is like "Actually, there is a frame for that." Everything that we think of, they've got it covered.

**Lars Wickman:** More useful maybe would be synchronized or unsynchronized lyrics, which you could use for your transcriptions... Like, unsynchronized probably. I don't know if you have timestamps in your transcripts.

**Jerold Santo:** Not as granular as we'd want. We have timestamps that are just like every once in a while, but they're not like phrase by phrase, or word by word.

**Adam Staravia:** Yeah.

**Lars Wickman:** I think you could probably use synchronized then. You probably want to use both... But yeah, I'm not sure anyone uses these.

**Adam Staravia:** But there is room then in there for a transcription?

**Lars Wickman:** Oh, yeah.

**Jerold Santo:** Oh, yeah. \[laughs\] That's just text. There's plenty of room.

**Lars Wickman:** Yeah. I think there's an extension spec that covers more accessibility features, and I think that one has specifically captions. So maybe that's what you'd want to go for. Chapters is an extension chapter. Chapters and table of contents - those belong together. And those are an extension of the ID3v2 series of specs.

**Adam Staravia:** But all this assumes there's a client, or a parser or library, something out there that can consume it. Like, it's one thing to put it in there, but it's another thing to make it useful by having software that can render it, use it... You know, make smarts around it.

**Lars Wickman:** Yeah. Almost all these frames are dead in the water.

**Jerold Santo:** You know what would be a really cool hack project? It's like, build a cross-platform -- like use Kauri, or something; build a cross-platform mp3 player that just supports every ridiculous frame in the ID3v2 spec. And it has all the features. That would be so cool.

**Lars Wickman:** I've been so keen to try.

**Jerold Santo:** Yeah. I would use it for 10 minutes, for sure.

**Adam Staravia:** 10 minutes... \[laughs\]

**Lars Wickman:** But listen, my idea is even more grand, because--

**Jerold Santo:** Okay...

**Lars Wickman:** ...it could be backed by mp3 files that are only on the server. And this mp3 would be the database for ratings, for play counts... So you get this single source of truth. And it would, of course, be able to show the commercial options, so you can monetize this player.

**Jerold Santo:** \[45:57\] Okay...

**Lars Wickman:** And you could even add -- so there are audio events. So there are ways to embed cues in the metadata like this; for example, "Fire the fireworks here" effects... I think that might be used in certain types of staged productions. I'm not sure. The capability is there, at least.

**Adam Staravia:** Wow. So much.

**Lars Wickman:** So much...

**Adam Staravia:** Just so much. You just said fireworks...

**Jerold Santo:** "You just said fireworks..." \[laughs\] Completely straight-faced, too.

**Adam Staravia:** I mean, a mp3 having an event that fires fireworks.

**Lars Wickman:** So I think that frame has wide use it, and it also has some very simple uses, like "This is the chorus. This is the bridge. Oh, guitar solo." Like, you can specify things that happen in the audio. But you can also add cues if you want to provide cues for something else. And this is where monetization really comes in... Because then you can actually decide which commercial frames -- and this is not in the spec, but I see no reason why you couldn't sort of build a slightly ad-hoc solution for this... But you could queue up your advertisements from the commercial frame based on these events throughout the file.

**Adam Staravia:** Is this the best place for this data? I'm thinking like --

**Lars Wickman:** In the mp3 file?

**Adam Staravia:** Yeah. Because --

**Jerold Santo:** Well, of course. That's why they've put the frame in there for it.

**Adam Staravia:** Well, I guess I'm thinking -- maybe this is wrong... Spotify is obviously the most ubiquitous place you can listen to music; that and Apple Music, of course, because Jerold's an Apple Music person and every time I say Spotify he's like "Cringe. I don't use that. I use Apple Music." Anyway... Platform aside, would they be interested in using these frames in those ways? Because wouldn't their individual mp3 somewhere on disk be what you say, which is their database? Is that the best place to store the data to do these things? Or is that even a good use case for them? I'm just trying to find, like, how could you actually provide usefulness around this?

**Lars Wickman:** I would probably assume on Spotify every song is backed by one single mp3 on one disk somewhere... And the play count and everything that's used to calculate how much they owe artists and all of that - that's just stored in ID3. I assume that's the case. And that sounds like the optimal --

**Adam Staravia:** No way... Do you think they're doing this?

**Jerold Santo:** \[laughs\]

**Lars Wickman:** No, I absolutely do not think they're doing this. And it would be absurd.

**Adam Staravia:** Exactly. Like, this is the worst place to put the data, right?

**Lars Wickman:** One of the things I find delightful about the play count is that if you have a practice of hashing your file to keep track of whether it bit rots, or if anything's wrong with it - I mean, it would change the hash every time you add one to the play count.

**Jerold Santo:** Yeah. That's why I was going back to like "You don't mutate my files. You're just a mp3 player", right? Just read-only, please;  don't change my MD5 sum, or whatever.

**Lars Wickman:** But maybe Winamp wants to add some commercial offerings into your mp3 files...

**Adam Staravia:** He's really on this commercial kick, isn't he, Jerold? He's just really pushing this commercial kick...

**Jerold Santo:** He is. He's trying to find a way of making this viable.

**Adam Staravia:** Yeah.

**Jerold Santo:** I actually like the idea of Spotify/Apple Music backing their entire play counts and ratings by modifying their mp3 files... Because what they're doing is they're introducing bloat into their network fees... Because they're actually increasing the size of the audio by modifying the ID3 tags each time. I mean, once you hit that 255 limit - where are you going to go from there? You've got to create another frame, or I don't know; I don't know how it works, but...

**Lars Wickman:** Yeah, you have to stream 256 megabytes before you get to the audio...

**Jerold Santo:** Exactly. So that is, to me, I think the best place to...

**Adam Staravia:** So is this a combination of just failed dreams on the ID3 spec writers? Like, they had a lot of vision for where it could go, and they were just way off? The usefulness of these features is just not there?

**Lars Wickman:** \[50:07\] Many of the frames are perfectly useful. So the absolute majority of frames are text frames, which is just a general -- like, this can be a string, and from ID3 version 2.4 it can be multiple strings. So if for some reason you suddenly support multiple titles, which is either great or terrible... Any number of titles.

**Adam Staravia:** "We really couldn't choose the right title, so we just gave it two." I can see us doing that one time, Jerold... Or you could A/B test it, which one gets played more.

**Jerold Santo:** I do like that they have a frame for mood now... So not only can you apply a genre, like blues, but you can apply a mood... Like blues... I don't know, sad.

**Adam Staravia:** I've got the blues. Not listening to the blues.

**Jerold Santo:** Right. So that's cool. But yeah, most of them are just text, and most of them are -- I mean, I guess the interesting one that isn't just text... We talked about attached a picture; so that's what people use for putting their cover art, or their album art, shipping that with the file, which is nice... That's useful. But really, chapters is the one that actually is like -- people use this. This is cool.

**Lars Wickman:** A lot of clients or a lot of encoders also add some kind of comment, like "This was encoded using blah-blah-blah."

**Jerold Santo:** Isn't there an actual field for that?

**Lars Wickman:** Well, there is a comment you can add, and then there's probably also one for the tool. I don't remember. But I bet there is.

**Jerold Santo:** I think we're doing that one, if I recall... Let me pop open the code to confirm

**Lars Wickman:** Software, hardware and settings used for encoding would be one.

**Jerold Santo:** So the ones that we are setting are: artists, title, subtitle, album, year, date, genre, publisher, and encoder.

**Lars Wickman:** So one of the good things about these frames is the frames you're not using, you don't add to the tag, at all. So there's no dead usage. And that way, they could take a stab at a bunch of frames that were maybe not realistically going to work. We tried to support them in our encoder and decoder regardless, but...

**Jerold Santo:** You were going for 100% coverage on that? Do you have a commercial frame?

**Lars Wickman:** I believe we have the commercial frame. There are some frames that I don't think we've merged yet, or added yet. But the tricky thing is we haven't been able to test these frames, because there's no other implementations that I know of that do these.

**Jerold Santo:** Right. Well, even with the chapters, I guess - some of that we did talk through on Ship It, so for those who are curious, Ship It 70 has some more details on more of the chapters and Changelog side of things... But we definitely did hit -- I guess that's where I came back in, was like you were kind of building this thing in a vacuum, an Elixir vacuum, where you would encode it in Elixir and decode it in Elixir, and test it with your encode and decode, doing your best, but it actually hit the reality of "Will other tools parse this? Will podcast apps parse this?" That's when we actually had to do some QA, and some bug fixes, and realize that I guess maybe the test suite wasn't quite as comprehensive, or would you describe it as rigorous as it needed to be?

**Lars Wickman:** Yeah. So when we implement the test, which are we use the library to encode this, and then we check that it's the binary we expect - in the end, that just means that we read the spec twice, and ideally, those two readings match up with our implementation. The problem is, we could introduce the same bug twice, and that can fairly trivially happen. Most of the issues we've had to track down to fix have been one stray null byte.

**Jerold Santo:** Those are the easiest ones to find, right? The one stray null byte. At least it's easy to see... How would you go about finding one straight null byte? What were you actually -- were you going frame by frame? Were you reading -- was it like The Matrix, where everything merges into one to you now?

**Lars Wickman:** \[54:01\] Yeah, so I just look at the hex and just feel it. No...

**Jerold Santo:** Yeah, just kind of feel where the -- like in Severance, you can just feel where the bad ones are.

**Lars Wickman:** I don't have a ton of experience with hex editors, and sort of staring at that and figuring it out... So what I ended up doing was typically trying to figure out, trying to drill down to "Okay, this is the problem area where our encoding differs from, for example, whatever forecast has encoded this episode of ATP", that we used a lot for comparison; because they have chapters. So in some cases, I decoded their implementation, re-encoded the results with ours, and checked the differences. After a while, I started building out a whole slew of small functions that just stepped through the binary and gave me the differences, and helped me sort through them... And sort of "Oh, I know it's after the first thousand bytes, so let's hop to that."

There's a lot of drilling down and just figuring out "Oh, this is the problem frame", and then finding, "Oh, the only difference in this one is that we encoded correctly, with UTF-16, and they encoded correctly with ISO-88591." It should support both, according to spec. But if you do it this way, Overcast just won't show it, at all, and then your chapters don't exist.

**Jerold Santo:** Yeah... Thankfully, we didn't run into any sort of mutually exclusive encodings, where one app would support this, and not the other, and vice versa. Like, what if Apple Podcasts requires UTF-16 in that particular frame? We didn't run into any of those, thankfully. And then we tested it in probably half a dozen or so actual apps, to make sure that it was working...

**Lars Wickman:** Yeah. After we had it working in Overcast and Pocket Casts, I haven't seen any others that had issues now.

**Jerold Santo:** No. And I've been asking people to report if it doesn't render in their particular podcast app, and no one has said that. One person confirmed it worked in Pod verse... I'm going from memory now. But nobody has confirmed it doesn't work in theirs.

**Lars Wickman:** And after this process, we also introduced a tool called ID3v2 - that's a command-line tool - and FFmpeg into the test suite. Now, both of those cover a subset of the frames, so we still don't have a comprehensive test suite, because there's simply no implementations that I know of, that we can rely on. But for example, FFmpeg covers chapters pretty well, and ID3v2 covers a lot of things that are not chapters quite well, at least decently... So yeah, that's about what we can do to ensure that we're doing the thing. If you know of reference implementations or good test suites, please do chime in the issues, because it would be sweet to have more reference.

**Jerold Santo:** Or if you do build that cross-platform AI-based mp3 player app, that'd be a great reference, because you're going to implement all these features. Maybe if it has like a command line, we can shell out to it. And also have a command line, please.

**Break:** \[57:17\]

**Adam Staravia:** How does any of this change, as we look at like podcasting 2.0 initiatives - does any of this current or future stuff play into that?

**Lars Wickman:** So they jam most of their stuff into the RSS feed, right?

**Jerold Santo:** Yeah. Yeah, so they have chapters in the RSS feed.

**Lars Wickman:** And that's probably a good approach, honestly. I don't think they want to extend ID3 or hack things into ID3. Now, I think ID3 has absolutely served many more purposes than they intended building it in the late '90s. I mean, many of the frames that are currently used with great success by podcasts were established in the late '90s; like album art, and all that. Chapters are later. But still, it has served podcasting well... But not everything needs to live in the file.

**Jerold Santo:** \[laughs\]

**Adam Staravia:** I mean, for me - I watch a lot of YouTube stuff, and I absolutely love when they have chaptering in YouTube videos, especially when it's at least 10 minutes or more. Like, who wants to listen to the whole thing? Just let me go to the thing that is the point. I use YouTube in a lot of cases for awareness, reviews, how to be... So knowledge-based, you know, gathering... Whether it's financial, whether it's software, whether it's tech, or hardware, or networking, whatever it might be. I'm always thankful.

So having this in our -- I personally have enjoyed it tremendously. And the one thing -- I'm not sure if this is a byproduct, Jerold, of us doing start and ends for our chapters... You remember how we speculated, "Should we just put the start time with the chapter, and never worry about the end?" Because obviously, the beginning of the next chapter is theoretically the end of the previous one.

**Jerold Santo:** Mm-hm.

**Adam Staravia:** In at least Overcast, I like the visual of knowing how long a chapter is. I don't know, is that a byproduct of the start and end or is it just assuming that based on the start of every chapter? What do you know about that?

**Jerold Santo:** \[01:01:54.01\] I haven't actually tested it. I assume it's there every time. So start times to chapters are required, end times are not required... Which makes sense. We include both. And I would assume, if I was writing that app, I would say, "Okay, if I have the metadata that shows me the start and the end time, I'm going to use that for my calculations. But if I don't, I'm going to use the start time, and I'm going to use the start time for the next chapter, and use that for my calculation." So I would use the end time if it was there and fall back.

**Adam Staravia:** Yeah.

**Jerold Santo:** I don't know if that's how it's doing it... But that's how I would do it.

**Adam Staravia:** But I've been appreciating that; like, just going back to some of the conversations we have on our shows, and just knowing "Okay, this segment is two minutes and 32 seconds." That's pretty interesting, how we can break it down... And then it also is a feedback loop for us as creators, I think. Because like when you think about respecting your listeners' time, being concise in your thinking, conducting a good show - it's evident in the length of a segment. If you've got one that's six minutes, it doesn't mean it's bad. But when you're listening to it, you're like, "Is all those six minutes pretty good signal? Or was there a lot of like side tangent stuff, that really didn't belong?" Maybe it's the culture and love of our show, who knows, but it just makes you look at your production differently when you know the length of each segment or chapter. At least this is what it's been for me, it's like "How long is this intro? How long is that ad spot? How long are all these parts? Does it really make sense to be that length? Could we be more concise? Could we be more? Listener-first aware of time?"

**Jerold Santo:** "How long are they gonna talk about HBO's Silicon Valley? When are they going to change subjects here?"

**Adam Staravia:** That's right! Please...

**Jerold Santo:** "Why does Jerold keep bringing up Star Wars? It doesn't make any sense." No, I think it does -- as creators, it is a signal back to us, I guess, to tighten things up maybe, and to also realize that some shows are way different from other shows. This one's, I would say, meandering for me in a good way, but it's going to be hard to chapter this, because we just kind of talk about stuff... And other shows it's like "There's this part, then there's this part, then there's this part." And so the actual chapter creation process, which I do write about somewhat in the announcement blog posts - because it's interesting if you're into the inside baseball; and if not, then it's not. But it's a challenge, and it's an interesting part of it. It's like, you can't just add chapters, and then it's good. You have to actually make them good chapters, otherwise they're not worth anything. In fact, I haven't added the chapters into Practical AI yet, just because of the way our production flow works. We don't have good contextual chapters there. They're just kind of like "Here's the first segment, here's the second segment, here's the third." And for me, it's like, that's not even good enough to be worth putting them in. And so as of today, that's our only show that does not have chapters, just because we've got to get it to a place where our editor can actually put those in there in a way that's meaningful.

So the creation process for chapters is an interesting one as a creator. I don't know -- as a listener, I appreciate being able to skip down to that one part I was curious about, and not listen to the part about Silicon Valley, or whatever. I don't know, Lars, do you use chapters? You're a podcast listener...

**Lars Wickman:** Not very often, because most of the podcasts I listen to, I both want to hear what everyone's saying. Some of them are straight up conversational, and some are more sort of guest interview... But then it's still -- I feel like I lose track if I skip around. If it's a multi-guest podcast, then I wouldn't mind skipping, probably. I actually listen to a sort of mainstream podcast today, non-tech nerdy - or I guess cyber; I guess it's tech-nerdy, but I think it's targeted at the mainstream.

**Jerold Santo:** Okay...

**Lars Wickman:** And this is the first time in ages that I heard dynamic ad insertion. So jarring...

**Jerold Santo:** Oh, yeah...

**Lars Wickman:** It switched to Swedish and started talking about a local electronics chain...

**Jerold Santo:** Oh, wow.

**Lars Wickman:** Or a Swedish electronics chain. Not that local.

**Jerold Santo:** That would be jarring, if it switches languages on you.

**Lars Wickman:** Yeah. That was so weird. I was like, "Ah, is this what podcasts are to people?" Because I just listened to this artisanal silliness...

**Jerold Santo:** \[01:06:07.06\] Right. We're definitely in that same bubble with you. I think there's one or two podcasts where I listen to them and I know they're doing dynamic ad insertion...

**Lars Wickman:** But I assume your ad rates are going to go up now that you can add a link and a logo to the ad read.

**Adam Staravia:** We haven't added the logo yet, but we've done, obviously, the link and the chapter for it.

**Lars Wickman:** They're credible cash flow options...

**Jerold Santo:** Yeah. I don't know if the ad rate's going up, but it's definitely a value-add. I mean, I think it definitely is something that our advertisers would like to have, especially if you're sitting there listening to it, and you can click over and check it out there while you're listening. Furthermore, I mean, I do that all the time when people put the links in.

**Lars Wickman:** It's nice. I don't think anyone thinks it'll move the needle much, but...

**Jerold Santo:** No.

**Adam Staravia:** This is definitely a sweat-the-details kind of move... We've wanted this for years. It's one thing you said Jerold, to put non-useful chapters in, and Practical AI is example... Like, it's just challenging now to get that in there workflow-wise and editor-wise and context-wise. But this to me is like a sweat-the-details move. And I think more than anything, one, getting a chance to buddy up with Lars and have this kind of feedback loop, and open source out there, and then this conversation from it, and then finally get to having chapters, and then executing on those chapters... Like, I've enjoyed the process of chaptering our shows, even though as part of the process of creating these podcasts, there's that, you know, "Here's the record time." We're all here an nourish; there's that time involved. Then there's the mastering time, and putting the show together, and telling the episode online... A lot of moving parts. And then to bolt on or add on one more, highly visible to a listener, and a UX factor, really, to a listener, to the listener, to us and to the listeners, is this chaptering part... You know, at first -- I've always wanted, but I thought, "Man, when we get there, it's one more thing to do in all the process to get to an ending artifact of producing a show and shipping it around the world. Wow, it's going to be a lot of work getting there."

But now I've really enjoyed that process, because we truly are a -- I would say, not just because we say this, but we actually follow through on it, is we sweat the details. And this to me is one of those details where like when we're doing the chaptering of a show - at least for me, and you could speak to your process, Jerold, and how you do it, and how you feel about what you do... Like, I really enjoy it, because I feel like I'm giving a listener a superpower into listening to our shows; like a secret key. Should their client just support the feature into the good parts of the show, if they want to just jump around, or jump to their favourite part of that episode? Because there's a lot of shows people go back to and listen to again, and again, at least maybe twice or three times. Like, if you do that, then here's these perfect waypoints. Hopefully, we've done our job good, and give us feedback if you don't think we have... But I think it's a sweat-the-details kind of move.

**Jerold Santo:** Yeah, and because we implemented them in the admin versus only in the mp3s and WAV files. Because we could have done this as just one step in post-production, and use a tool like Forecast or something, to write those tags and then upload the file from there, and be done. But because we do it in the admin, it's a centralized source of truth for the chaptering information for an episode, and so we can emit that in multiple places. And why that's cool is that you have the exact same chapters on the website.

So if you want to deep link to a chapter - like, you really liked this conversation we had, or this thing this person said was interesting, and you want to link to that, there are deep links on the web page directly into that chapter, that you can share. So now chapters are shareable... Which is just a neat little byproduct of having it there, versus having it somewhere else, is we can put it there, we can do the podcasting 2.0 RSS feed style, which we support as well, we can put it in the mp3 via Lars' library, which we do as well, and we can also put it in our email as it goes out, as we do... So it's just like, that's cool.

\[01:10:14.20\] Yeah. So it's a cool thing, and we couldn't have done it without you, man. We really appreciate the work you've put in on it, and the quality that came out of it, the fact that it works... And for you putting up with me as a customer... Do you have any comments on me as a client? You know, I did client work for a decade, so I know what a client should be like.

**Lars Wickman:** Your description about going away and showing up checks out... But it's also weirdly that you reach out about these projects... So the last time we worked together on some projects was also when I was just heading into parental leave; I was this time as well... And when you get really, really busy, so you surface like once a week at best... And usually, you're quite responsive in general... But yeah, during these projects, that's also during your crunch time. I think Adam was on leave, and you were handling a lot of production, and all that... So ideal client in the sense that not particularly hanging over my shoulder, or getting too involved... But also maybe not the quickest turnaround on responses... Which has been fine.

**Jerold Santo:** Yeah, which was fine. That's my luxury, that's my prerogative as the customer, is to be less concerned with your time and more concerned with mine... Even though I don't want to be like that. But I think the only feedback I gave you code-wise was at one point I said, "I would like this to be a little bit higher-level API." That was pretty much all I ever said in terms of the end product. And then obviously, I tried to use it, and it was like "Hey, how do I use this? It's not working." I'd say stuff like that. But I tried to provide as much information as I could, as like a good technical client.

**Lars Wickman:** Yeah. I think once you were available, and actually trying to use the thing - which took a little bit, but I think we were both quite busy, so I was happy not to get too much feedback too early, because I had a one-month-old kid then, and it was easier when he was two.

**Jerold Santo:** Yeah. So you got the bulk of the work done by mid-July, maybe early July, and I literally didn't touch it until the first or second week in August. I just was like "Cool, I'll take a look", and I just never took a look. And I was building out the backend, too. I really wanted to be able to have the data in there, so we can start capturing it... And we actually captured the chapter data for a month and a half or so before we had the feature, so that we could go back and just like retrofit... Which I've done now, Adam; that's all those old mp3... Old as in going back to June. They all have chapters in them.

So I wanted to get that done fast, so we can start adding the chapters and figure out the workflow, and then I wanted to actually get around to your tool, and so I sat on my hands for a while doing that. And then I was like -- Ship It was coming up, Kaiden 70, and I'm like "We've got to have this sucker done, so we have something to talk about." And then I was like "Lars, where are you? I have questions. I have problems. Answer me immediately." Hopefully, it wasn't too bad...

**Lars Wickman:** \[laughs\] No, no. It was all good. Now, it shows that you've dealt with clients, because the information I get out of you is much, much better than the average level of a non-technical client.

**Jerold Santo:** I even submitted a pull request at one point...

**Lars Wickman:** Yeah. Pull requests, GitHub issues...

**Jerold Santo:** I actually fixed a bug, but then you didn't like it. You did it yourself anyway.

**Lars Wickman:** I think I rewrote most of what you had touched at that point, yeah.

**Jerold Santo:** Yeah, you already touched that. But I was like "You know what - I'm sick of just complaining. I'm going to actually contribute a fix", and I did. And then the--

**Lars Wickman:** The spirit of it has been merged.

**Jerold Santo:** The spirit of it has been merged. Is that like a non-code contribution? Do I get any credit for that in the README? "The spirit of Jerold's code exists."

**Lars Wickman:** I mean, you're listed as the maintainer...

**Jerold Santo:** \[01:14:04.08\] \[laughs\] That's only nominal, you know? You're going to have to sign up for my GitHub Sponsors if you want any bug fixes. Just kidding...

**Adam Staravia:** Will this become a /the changelog library? What's the plan for the actual code long-term?

**Lars Wickman:** It's going on the Changelog repos that's already owned by the Changelog org on hex. Pm, which is the Elixir package repository.

**Adam Staravia:** We have tried, listeners, to get /changelog on GitHub...

**Jerold Santo:** We've talked to all the people...

**Adam Staravia:** Sadly, it's probably never going to happen, so we have to be /THE changelog on GitHub, sadly. It is a hard life, and you can't get just /changelog somewhere, like -- we've got it on YouTube, you know... We almost have it on Instagram...

**Jerold Santo:** Yeah. If you want to check out all the new stuff on YouTube, go to youtube.com/changelog; you can check out there Changelog highlights... Well, anything left uncovered? Anything we should say before we call it a show?

**Lars Wickman:** I think I can and just add that we are planning a bit of a technical dive into the structure of ID3 tags and how we tackle the parsing and encoding of them... So there should be another Changelog blog post covering that. If you want to read the blog post we're talking about, that's a lot fluffier, and mostly about the thoughts that we've discussed here, which were awoken in me while I was reading the spec.

**Jerold Santo:** \[laughs\] Well, it was a fun, nostalgic, deep-dive into some ID3 esoterica, as I called it in the working title... Lots of fun chatting with you, Lars. Like I said before, I appreciate your work you've done on this. Really cool. It's got to feel good, at least as a listener of our shows, to -- or at least when you glance at the chapters in your app, even if not using them, and be like "Hey, my code. My code does that." It always feels nice.

**Adam Staravia:** Not just a listener, but a Plus-Plus subscriber.

**Jerold Santo:** That's true.

**Lars Wickman:** Of course. I want to be closer to the metal.

**Jerold Santo:** And a fellow podcaster. Give a quick shout-out to your podcast, Lars.

**Lars Wickman:** Yeah, so the one I should shout-out is Beam Radio. So beamrad.io. I came up with the domain, and I'm slightly proud of it. That covers Elixir and Erlang and the ecosystem overall, and it's me and a number of much, much more fantastic co-hosts.

And then I have a podcast, Regular Programming, but that one (RegProg.com) is currently sort of on hiatus... But if you want to hear me talk about programming in the very general sense, there's a bit of a backlog that you can go through. Otherwise, it's blogging and newsletters and the YouTube channel right now popping off.

**Jerold Santo:** Oh, yeah.

**Adam Staravia:** What's the handle? How do you search for -- is it Underlord?

**Lars Wickman:** Yeah, I go by Underjord.io.

**Jerold Santo:** Underlord... Say it again?

**Lars Wickman:** Underlord.

**Jerold Santo:** I won't try. I like it though.

**Lars Wickman:** It means "underground" in Swedish.

**Jerold Santo:** Oh, okay.

**Lars Wickman:** Very suspicious... My mother had notes on my company name...

**Jerold Santo:** Hah! Who's going to trust you...?

**Lars Wickman:** Yeah, exactly. "Mom, I'm being cool on the internet!"

**Jerold Santo:** \[01:17:11.25\] \[laughs\] Classic, classic...

**Adam Staravia:** Well, speaking of the Plus-plus subscribers, I do want to mention something... So we often ship bonuses to our shows. And so what I love most about this new feature is it lets us give you a direct click - or tap, depending upon your platform - right into those bonuses. So we have a chapter called out for the bonus, and then for the more recent episode there's an another chapter after the bonus, which is a thank-you chapter. So if you want to go find that one, the most recent episode that I'm talking about is episode \#506. So special chapters just for Plus-Plus members, directly to the bonus and the good stuff.

**Jerold Santo:** And a personal thank you do you... Did you embed each person's name into their own mp3 file, by way of dynamic thank you insertion?

**Adam Staravia:** That would be amazing, honestly.

**Jerold Santo:** Yes, dynamic thank you insertions.

**Adam Staravia:** I'll do a thank you in my voice, and then Stable Diffusion other voices, because that's the thing coming for each -- and I can do it, you know, accent, or dialect or language... That'd be--

**Jerold Santo:** Oh, and if you fill out your language of choice in your profile, we could send you via Open API's Whisper library, we can send you a thank you in your own language.

**Adam Staravia:** That's right. Yes, more...

**Jerold Santo:** More fun stuff to hire Lars to build for us.

**Lars Wickman:** Yeah, so I'll clear my calendar...

**Adam Staravia:** Anything else, Lars. Anything left unturned/unsaid?

**Lars Wickman:** No, I think we'll, we've thoroughly covered what needs to be covered about ID3 tags. I'm also sure that there will be people who spend their whole lives focusing on the perfect curated mp3 collection, that are like "You've missed the most important part!!" But that's okay. I really only care about the podcast thing.

1:If people are interested in hiring you, should we send them to - pronounce in English terms - underjord.io? Is that the best place to send folks?

**Lars Wickman:** Yeah, sure. And probably the most appropriate thing to send my way right now is companies that are looking to hire Elixir developers. Not necessarily to hire me, but hire others. I have been helping a number of companies recruit, which is an interesting thing to do as a developer rather than a recruiter... Because many developers don't like recruiters.

**Jerold Santo:** Right. So you're saying you're a recruiter now?

**Lars Wickman:** Technically, yes.

**Jerold Santo:** \[laughs\] Technically...

**Lars Wickman:** Technically yes, which is the worst kind of yes...

**Jerold Santo:** Yeah. You started off trying to be cool on the internet, and you ended up a recruiter. So maybe your mom was right the whole time.

**Lars Wickman:** But I seem to have a decent approach to it, because the developers come to me. I don't actually hunt people down on LinkedIn. It's more that I post a job posting, and then people reach out, and then I talk to them.

**Jerold Santo:** Okay. So on the other side of the coin then, if you are an Elixirs who wants some work, maybe reach out to you as well.

**Lars Wickman:** Yeah. You can also check out the site. There are postings under the Jobs section.

**Adam Staravia:** Very cool. We'll link all that up. Check the show notes for those links, for jobs, or for hiring Lars and team for consulting... But Lars - hey, thank you so much for working with us. I've been mainly on air support for Jerold and the rest of everybody involved in this; the desire, I suppose, of this feature for many years now... But it's nice to see it actually in production, in use, using it every single week to deliver chapters to our listeners, and we couldn't have done it without you. Thank you so much. It's been awesome talking through what could have been with ID3v2...

**Lars Wickman:** It's been a pleasure.

**Adam Staravia:** Thanks, Lars.
