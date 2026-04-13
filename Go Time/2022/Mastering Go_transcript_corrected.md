**Johnny Tourniquet:** Yes, yes, it is indeed Go Time. I will be your host today. I'm Johnny Tourniquet, and joining me is the author of the book "Mastering Go", Mr. Michaelis Touracos. Hopefully, I've done your name justice...

**Michaelis Touracos:** Yes.

**Johnny Tourniquet:** Awesome, awesome. So I became aware of your book - or rather the first edition of your book, maybe a year or two ago. And then it seemed like one of those very thick reference manuals. I was like, "Okay, this is one of those things you've got to get on your shelves", like old-school, those giant tomes that you'd put on your shelves, and you'd use them as reference every once in a while... Because nobody reads a book front to back these days. So I'm thinking, "Okay, maybe I'll put this book on my shelf."

Lo and behold, I never happened to do that, and then the publisher reaches out to me and says "Hey, would you like a review copy of this book? And I'm like "Sure, yeah. It's not like I don't have a dozen other things to do", but hey, I'm a sucker for reviewing Go books, and I was looking forward to this one as well... And I got the book in the mail, started going through it, and I was basically nodding in few places, I'm like, "Yup, yup, that's how I would explain that." In other places I'm like, "Okay, yeah, that's a different way of explaining it." But the thing is, as I was flipping through the book - and I certainly looked at different areas of the book to see how you explain things, and see "Are there some tricks and tips and things that I can steal from you to explain certain things as well in teaching people Go?" And when the opportunity came up for -- I think I was talking about it on Twitter or something, and you chimed in... I'm like, "Okay, so he seems friendly enough. Why don't I just have him on the show, so we can actually talk about the book?" But not just about the book, but really -- the title, basically, I find intriguing, and I wanted to talk about what it is like to master Go. We've got to go meta with this, right?

\[04:09\] But yeah, for those who don't know who you are, who you are on Twitter, the Twitter handle is @mactsouk, and you're a systems engineer and technical writer. So obviously, the writing is important. You're writing books, and everything. This is the third edition of your book. I wanted to start out with basically -- well, I'll give you a chance to sort of add any flavour you want to your intro. Like, what else have you been up to?

**Michaelis Touracos:** Okay, so hello everyone, thanks for listening to us, and Johnny, thanks for the opportunity to come to your podcast. I'm a Unix passionate, I like Unix. I don't know why, but I like Unix, so you know... And systems stuff. I used to be an Oracle DBA, and I used to work with Cisco IOS... You know, the operating system of Cisco, not the Apple version of iOS. And Unix, and setting up Sendmail DNS, with BIND, all these things that some people find miserable, but I really like them.

**Johnny Tourniquet:** Yeah, it used to be a rite of passage, you know? Set up your own mail server, and everything, your own DNS...

**Michaelis Touracos:** Yeah, Sendmail with m4 configuration files, and those things. And working with versions of Unix other than Linux, like the IBM version AIX, or the Hewlett Packard version of Unix, HP-UX, and Polaris, my favourite one... So I'm a systems' person, I like Unix, and I like writing software... So every time I see a systems programming language, I like to try it. I like C very much, but C is not perfect. I don't like C++ though... It's too complex for me.

So the idea was to find something that I can write systems software, but without having to worry about C stuff. That's how I started getting interested in Go. And when I learned that Rob Pike was involved - that was a big plus.

So I started working more with Go, and learning Go more, and after some time I just wanted to write a book that I would like to read when I was learning Go. But the thing is that first I wrote a series of articles for Computer Magazine in the U.K. Ten, or maybe twelve, I don't remember... A series of articles that at the end became something like the table of contents of the book. Because you know, you have to prepare.

And that's how I started getting involved with Go. You know, you can't trust a programming language too early, but you have to work with it, see how it goes, and see if you want to keep working with it.

**Johnny Tourniquet:** Yeah, I definitely agree with that sentiment. The fact of the matter is when you say you want to write a book that you would have liked to learn Go with, the approach you took with the book - I definitely didn't think this was a beginner book. I think that's something that usually when I give references to people for learning material, I usually ask them "What level are you at? Are you an existing programmer who is learning to pick up a new language, or are you brand new to programming? Or are you basically a die-hard functional programming developer?" We analyze your preferences. And when I picked up this book, the first place I went - in the intro it basically says who this book is for. And right then and there, it says "Hey, this is an intermediate book."

So then I was like, okay, great. That means when I start going through that book, I'm not going to see things like "This is what a conditional is." It'll just say "This is how Go does conditionals." Or things of that nature.

\[07:56\] So when I went through the book, once I understood sort of the frame of reference that you were using to actually write the book, then the gripes I might have had with it, I started basically saying "Well, okay, so if Michaelis is making these assumptions about the reader, then this is the lens with which I have to look at this book and ingest some of this book." So I think definitely something I want to put out there - a lot of times folks just pick up a book, and they'll give a review, and not really understanding basically who the book was targeted for... If you're a beginner, and you've picked up this book - yeah, you'll still learn a lot. But there are some things that you're not going to go deep into. There's some language features that you already ran to without having to explain the background on them, because you assume that the reader is coming in with sort of basic understanding of at least what Go is, and what Go does.

So that was the approach I took with the book... And for those who are looking to pick it up as well, that's what they should expect. That said, I kind of wanted to give you a chance to narrate a little bit on -- yes, this is a book you would have liked to have had, but you've been working with Go for a while; obviously, you're going to have a biased answer for this, but do you believe a book like this - maybe not necessarily your book, but a book like this - is the right entry point for somebody whose maybe coming from another language and looking to get into Go? Is this a book for just learning Go, period, or are you targeting one level deeper? ...not just for the person who's starting to learn to pick up Go, but as you mentioned, you like systems programming, right? Will a systems programmer find this Go book in particular a lot more their speed, or should they look at something else more targeted at systems programming?

**Michaelis Touracos:** It depends. Generally speaking, if you have some experience with programming, you should pick up Mastering Go very quickly, because you have to have some experience. If you have the experience, then you can work with it very easily... Because programmers know that the key point to learning something is practice. Some things we find them difficult, and we have to look again, and other people find other things difficult, and they have to look at them multiple times to understand them.

With Go -- I mean, one thing that surprised me with Go is that you didn't have the tilde, and fork, and things that you do in C. It took me a while to understand it, and understand that I have to work with go routines instead. You have to practice understanding that, but in order to look for a fork, you have to know about fork. So if you know fork, then you can understand what is going on there.

Again, I think that the key point is practice. If you want to practice, then you will be okay. And the cool thing with the book is that even I use it as a reference sometimes, many times. Because you can't remember everything.

**Johnny Tourniquet:** God must give you some special kind of pride to be using your own book as a reference.

**Michaelis Touracos:** Yes, yes, yes. This is a good point, not as a pride, but as a thing that you can -- you know, it is useful. It's not pride, because I have read many books, and I have used them as a reference as well. Many people have done that. But it's good to find it useful, because you cannot remember everything. You can't have everything in your mind.

**Johnny Tourniquet:** Right, right. Yeah, Google-driven development is a thing... I partake in Google-driven development myself, so no shame in my game. Nobody can remember everything, and the nuance of everything. Every once in a while I'll still go to -- you know, my favourite resource in the Go community is gobyexample.com, for example... For example, for example. Gobyexample.com is a great resource that I regularly reference, even to this day, after having been doing Go for like five years, or something. I'll be like, "Okay, how do I initialize this again? What's the technique for doing this again?"

\[12:00\] One of the things I constantly refer to is "How do I properly seed for randomization?" I always have to go look up "Okay, what's the package Duran something?" These things, even though you use them frequently -- like, sometimes it's "Okay, what's the syntax? What is this type that I use all the time, that I need to learn a little bit more about? What is this package in the standard library that I have used a dozen times, and I've only ever tried one or two functions from this package? What else does it offer?"

So this is sort of a continuous journey of mastering Go, which is something I definitely want to get into and talk about in a bit... Sort of at the philosophical level, what does it mean to master Go. But this is a 750-page book, so it's a chunky book. Lots of topics covered. What do you think was the most interesting parts for you to research and write about?

**Michaelis Touracos:** The Go garbage collector.

**Johnny Tourniquet:** Ooh...

**Michaelis Touracos:** I really enjoyed reading about that and learning about it, and then writing about that. I really enjoyed it. And I also enjoyed lots of external libraries like Viper, and Cobra, and \[unintelligible 00:13:06.02\] and Gorilla. Because they extend the language in a good way. Especially Cobra and Viper are really helpful. As I'm working with some REST APIs, I use gorilla/mix, and I'm trying also to learn \[unintelligible 00:13:24.24\] to understand what their differences are, and which one is better for what job.

I mean, that's the experience part. It's one thing to learn about something, but it's another thing to be able to choose based on facts. That's the difficult part.

**Break:** \[13:43\]

**Johnny Tourniquet:** Speaking of the research and writing process, how long did the -- at least the first edition; I'm assuming with each edition you're not rewriting everything, you're just updating a few parts, some things that have changed, maybe some idioms have changed and whatnot... Roughly how long did it take you to write and publish the first version?

**Michaelis Touracos:** Given the experience that I had with the articles, and another book that I have written for Pack is the Go Systems Programming, which helped a lot; it's one edition, it's the first book... It took me - and a lot of preparation though - six to eight months. But with a lot of preparation. You know, you cannot start from zero and expect to have the book ready in six months. But a lot of preparation, and a lot of code. You have to have some code ready.

**Johnny Tourniquet:** \[16:07\] So did you enjoy -- like, in my mind, having collaborated on book projects and things, in my mind there's the thing that I'm writing about, and then there's the writing about the thing that I'm writing about. Those are very different disciplines, very different skill sets. Writing about something you know and doing the thing you know are very different things. I can go all day and feel like I know what I'm doing, but the process of writing, even if I've written before, writing a book and working with an editor, working with people that are going to give you feedback on the writing process, the tools and resources that you use as a writer - these things are not your day-to-day typical programmer tool. There's always sort of a learning process that's also taking place in regard to the act of writing a book, or the act of creating a training, or a course, or the act of creating something for relaying and conveying information to another human being. That in itself is a separate skill set that you have to develop. I wonder how you feel about that skill set, having gone through it a few times. How do you feel about that?

**Michaelis Touracos:** For this skill set, the articles that I'm writing for Computer Magazine have helped me a lot, because for the article you have to present something, and you have a limited space. So you have to have a beginning, a middle and an end, and that helps a lot. So I'm trying to follow the same approach. As I've told you before, you cannot remember everything. If I read something afterwards, I try to be sure that it makes sense, at least to me, and then to the readers. Because you know what they say, "Write for your friends, but edit for your enemies."

**Johnny Tourniquet:** \[laughs\] I'd never heard of that one before. I'm going to use that.

**Michaelis Touracos:** So when I'm editing, I'm trying to edit and be a hard judge for my own writing. And I think that helped me a lot with magazines, but also for the books. But have in mind that I have written some articles for magazine that I'm not very proud of. \[laughs\] It's not perfect, it's a process.

**Johnny Tourniquet:** Right, right, right.

**Michaelis Touracos:** You don't begin perfect, it's a process. You learn, and you make mistakes, and then you make more mistakes, you correct something, and you try. We're not perfect, we're just -- you know, work in progress.

**Johnny Tourniquet:** Don't expect to have something good, ready to ship the first time around, the first go-around, right?

**Michaelis Touracos:** Yeah.

**Johnny Tourniquet:** ...which sounds very much like the engineering process as well. You never quite get something right the first time. That's why we have even idioms around the act of writing software. You write a test, you get a failure, we make the test pass, and rinse and repeat. We often have mnemonics and things around these things, so I think we shouldn't expect any different from a different kind of creative process. It's just ones that you're not writing code. Although, I must say, I'm envious a bit, because -- I'm sort of picking your brain in this whole thing, because I too want to write books on Go and whatnot, and I'm picking your brain and saying "Okay, what should I run away from?" \[laughs\] If I were to take on such a project, what should I run away from, or watch out for? What are the pitfalls to taking on a writing project? ...not necessarily exclusively about Go, but really about any task of this nature. Basically, you're teaching people about how to use a tool, this tool being a programming language. What do you think the biggest takeaways for you were about writing this book and creating this project?

**Michaelis Touracos:** The key to writing the book is to enjoy the process first. Because if you don't enjoy the process, it's difficult. The second is that you have to think of the reader as a friend; not as money, but as something that you're trying to help... You know, just help. Try to explain and don't assume that something that is easy for you should be easy for the other people, and vice versa. Sometimes you have to explain something twice maybe... It's a process. You have to enjoy the process. Once you enjoy the process, then everything becomes easier.

\[20:22\] The other thing that I told you before - write for your friends, edit for your enemies. You should be edited hard, for your own good. That's the way to do -- you have the skeleton, you have the text, but you have to edit hard. I'm still learning that. I really enjoy books like The C Programming Language, or The Unix Programming Environment - they have the necessary thing only.

**Johnny Tourniquet:** Right, right. Everything you need, nothing you don't.

**Michaelis Touracos:** Yeah. And they have written these books with trough and Unix tools, and that's really amazing. \[laughter\]

**Johnny Tourniquet:** Yeah...

**Michaelis Touracos:** Not even latex

**Johnny Tourniquet:** Yeah, not even modern tools that we have. That is amazing.

**Michaelis Touracos:** And they have created classic books, just for the love of it.

**Johnny Tourniquet:** Indeed, indeed. Yeah, I always tell folks that based on all the publishers that I talk to, and having been part of book projects and everything else, I'm like, "Okay, people who do this - it's not done for money." This is definitely a labour of love, the advance that you get really is not -- if you were to map that to your hourly wage, whatever you're getting out with your employer or consulting, whatever it is, the amount of time you put in, it wouldn't even come close. When you do this because it's a labour of love, it's not something that -- unless you have a book that's immensely popular, whatever it is, and you make bank, and that's fine... But the vast majority of people writing technical books like this - you're really just sharing something with the community, for the love of it. I can definitely appreciate that.

So again, the book is called Mastering Go, and I wanted to talk about what we believe mastering Go today looks like. If somebody started out saying, "Hey, you know what - I'm going to pick up this language, and I want to master it." What does that journey look like for somebody who's basically starting today and saying "I want to master this language." What are the things they need to look out for? What are the approaches that they should have? What should they expect?

**Michaelis Touracos:** Look, my book is here to help people - not master Go, but like Go. If you like Go and you use it, you're going to master it. The thing that mastered everything is the marketing stuff mainly. You cannot master something, but...

**Johnny Tourniquet:** Right, right, right.

**Michaelis Touracos:** No book will help you master anything.

**Johnny Tourniquet:** Right. \[laughs\]

**Michaelis Touracos:** It's like swimming. You cannot master swimming by reading about swimming. You have to swim. So I just try to make people love Go, understand what they can do and what they can't do with Go, and where Go is -- what are the advantages and disadvantages of Go, and then Go out and write software. That's the key. Without practice, you won't do anything. I have been inspired by The C Programming Language book, I have been inspired by the book The Unix Programming Environment, by the Stevens books, the Advanced Programming in the Unix Environment series of books, or the TCP/IP, network programming books by Stevens... These books were my inspiration. They didn't teach me everything, but they inspired me to write things. I have written an FTP client in C a long time ago, which was -- it was pretty challenging, but rewarding. I mean, that's the idea.

**Johnny Tourniquet:** Yeah. You're going to learn by bumping your head against things, and researching, and figuring out how it's done... Yeah. That's really key to mastering anything, right? You have to keep doing it.

**Michaelis Touracos:** Yes.

**Johnny Tourniquet:** \[23:59\] For me, whenever I hear the term "master this, master that", I'm like -- yeah, like you said, this is marketing. I get it. But to me, at some point I believe you can reach what we can consider the realm of mastery. When somebody can present a problem and say "Hey, how would you approach this in Go?" and immediately ideas start popping in your head, and you're like "Oh yeah, I could use a buffer for this, I could use some go routines for that, I'm going to communicate over these channels..." So immediately in your head you start thinking "How can I approach this?" So I think sort of getting to these ideas flowing into your mind at a rapid pace - to me, I think that is what shows a sign of mastery.

**Michaelis Touracos:** Exactly.

**Johnny Tourniquet:** As you become so comfortable with the language that it's no longer a matter of "Okay, how do I piece together this syntax?" but I have a problem that I want to solve. I want to go from problem statement to possible solution and something that I can test, and not having to worry about the actual writing of the syntax. You can't type fast enough, because the language at this point becomes your pen. You're writing it down. So you have the idea in your mind, and you're basically just trying to get your physical hand to keep up with your mind.

**Michaelis Touracos:** Yes, exactly.

**Johnny Tourniquet:** So to me, when you've mastered Go or when you're reaching a level of mastery, I think that's when you know; when the language sort of fades away, it gets out of your way, and it's just about now communicating your design or your idea, you're communicating that a bringing something to life. That's where I think -- if somebody's looking for that signal that you can recognize in your own self, "How good am I with this thing?", I think you have to ask yourself "How often do I have to reference basic concepts? How often do I have to look up some documentation on something I use often enough?" So that's how I know I still have a lot to learn about Go, because I'm still looking up some basic stuff sometimes.

**Michaelis Touracos:** Me too, yes.

**Johnny Tourniquet:** I'm like, "Okay, yeah, I've been doing it for a while, but I expect - hopefully, if I'm lucky, I'll still be doing it for years and years to come, so I expect that ease of just using the language and it kind of fading away as a tool, and not really thinking about it too much... I expect that to come in another 5, 6, 7 years." So I expect it to be a long journey.

Personally, that's why I love Go, because - can I stick with this language for a decade? Can I use this language and be happy using it for a decade or more? To me, that's going to give me enough time to get to the mastery level, and that's the journey that I'm on... Like, "Can I spend a decade on this language?"

**Michaelis Touracos:** And the most important point is that a master knows when not to use it.

**Johnny Tourniquet:** Mm-hm, mm-hm...

**Michaelis Touracos:** You cannot solve everything with a tool. You have to know when not to use it. It's equally important.

**Johnny Tourniquet:** Yeah, agreed. So obviously, you've been a part of the Go community for a while... Personally, I'm big on the Go community overall; I think technology is technology, but the people is what makes it fun. I'm interested in knowing - do you have any stories about the community, or people, some of your favourite gophers, or anything like that? Do you have anybody in the community you want to give a shout-out to? ...however you want to do that, but I just wanted to ask, at the very least.

**Michaelis Touracos:** \[laughs\] Lots of people's writings have helped me a lot, and especially the official Go Blog is really helpful. I have read many things from Mat, who's not here with us today, and Bill Kennedy has helped me a lot... His writings are very good, and he's always ready to help and willing to help people, and the community is really -- I mean, I don't know if other programming languages have such an active and helpful community.

**Johnny Tourniquet:** \[27:52\] Yeah, I totally agree. These are definitely some of my favourite people as well. I happened to also have the distinct pleasure of co-hosting this podcast with Mat every once in a while, along with my fantastic other co-hosts that grace the mic here every once in a while... And again, for me that's part of the joy; I get to hang out with people that share this love, and basically we want the community to be a welcoming one, a friendly one, a helpful one... So we try to live that, and hopefully as people new to the community come in, and they feel that love, they feel that welcome, they stick around.

I usually say -- pretty much every year we have a Gopher Con, which is the big, official, I'd say the biggest Go conference we have year-round. And over the years we've gotten a lot more conferences spread throughout the world as well, but Gopher Con is sort of the big one, and the one that usually gets a lot of people showing up on-site, and everything. During the pandemic we had to do it online the last couple of years, but it's going to be in-person again this year...

**Michaelis Touracos:** Oh yes, that's great.

**Johnny Tourniquet:** So I am looking forward to that. I can't tell you how much I'm looking forward to that, to see people I haven't seen in quite some time, or only online here and there... But yeah, at Gopher Con I usually see the makeup of the audience; it's usually, consistently, there are more newbie Go developers, brand-new folks in the Go community than there are veterans. This means that there are more people coming into the community than there are people that have been doing it for a while. Every year, consistently.

So that means Go still has a lot of time, a lot of growth in front of it. We're just going to continue to attract a ton of new people into the community, and to me, it's important that with every layer of growth, right? Every ring in the tree if you will, people that come in and that we add to the community, that we continue to carry on that kindness, and be nice to people...

**Michaelis Touracos:** Exactly, exactly.

**Johnny Tourniquet:** ...be helpful... All of these things that basically this community has as core values. So we definitely want that to keep growing, along with the number of people that we have coming into the community. So to me, that's huge. Obviously, you play your own role in that, in creating learning materials and interacting with people online, so definitely you're part of that... So on behalf of the community, I say thank you.

**Michaelis Touracos:** Thank you. \[laughs\]

**Johnny Tourniquet:** I did want to ask a couple more questions, and then we're going to switch it over to unpopular opinions. I hope you brought an unpopular opinion...

**Michaelis Touracos:** Yes.

**Johnny Tourniquet:** Nice, nice. Obviously. Go is not the only language you've used; obviously, you've done some C, and whatnot; you even built an FTP client in C. Who knows, you should do that in Go and compare notes, and see "Okay, what was that experience like?" But anything else that you're actively using and learning about today beyond just Go and old-school C?

**Michaelis Touracos:** I'm using Python a lot nowadays, because I'm doing some excess things with time series and stuff, and Python is perfect at that. Big data, and things.

**Johnny Tourniquet:** Okay.

**Michaelis Touracos:** For the first time I wrote Java last year.

**Johnny Tourniquet:** Oh. \[laughs\]

**Michaelis Touracos:** I don't like Java, but I had to...

**Johnny Tourniquet:** Well, I'm sorry... \[laughter\]

**Michaelis Touracos:** It's not a bad programming language, but it's not my favourite.

**Johnny Tourniquet:** I'm kidding, I'm kidding. Yeah, no shade to the Java developers out there. We love you, too.

**Michaelis Touracos:** I don't like the syntax. It's not a bad programming language, but I don't like the syntax. I never liked the syntax. But as we said before, it's a common secret that a good programmer can write in any programming language. You can pick up a programming language really easily, especially when you don't have to deal with graphics, and that stuff; if it's command line utilities...

**Johnny Tourniquet:** Except Haskell. Man, every time I pick up Haskell, I'm like "I don't know what the heck is going on..." \[laughter\] I digress...

**Michaelis Touracos:** Yes. I have tried to learn Elixir and Erlang, but... You know, they require a different kind of thinking. They are good, especially Erlang; Erlang was used for telephone initially, but it's high availability, and all these things; it's very powerful. But you know, you have to like it. Or you have to read it again, and like it in the process.

\[32:14\] So I mainly write Python and Go, and I'm learning other languages. I'm going to write a tutorial about the V programming language. I haven't heard of it before, but... You know, it's a good way of learning it.

**Johnny Tourniquet:** Yeah, yeah.

**Michaelis Touracos:** And I like Rust, but the syntax of Rust is really bizarre, I don't know... Have you tried Rust?

**Johnny Tourniquet:** You know, I've played around in some playgrounds, and actually I've read in the early days, when Rust was in pre-1.0, I tried to get into it... And since then there's been some improvements in terms of some things that were kind of weird in the beginning; they've refined those things. So I need to give it another go, I have to give it another try. A lot of things have been sort of smoothed out...

But if I add one more thing on my plate, I'll probably just fall apart. There are so many balls in here right now; that's my excuse right now, and it is a legitimate one. I have so many projects going on, I'm like "Okay, before I can add one more thing to my plate, I have to take one off." I have to be done with one project before I take on another one. So that's how I'm keeping myself honest. But yeah, definitely, Rust is on my to-learn list. Basically, I try to pick up a new language every 2–3 years. The last one I picked was Go, and I've stuck with that for the last 4–5 years or so... And now it's time to pick up something new. Definitely not leaving behind Go, for sure; not by a long shot. Go is still my daily bread, it's still what I use for work every day, it's still what I use for my side-projects... It's my thing. But yeah, it's always good to learn something new; it brings in a different lens with which to look at problems. So definitely, Rust is on my list.

Before diving into Go, I had actually started picking up Elixir as well, only because some of the same few folks that were in the Ruby community basically were either working on Elixir, or somehow were involved in that community as well... I did a ton of Ruby back then, so naturally, I heard about Elixir and everything else, and started to learn about Erlang, and the BEAM virtual machine, and all that stuff. I learned a good deal about that stuff.

And then I met Go, and pretty much all others were cast aside once I learned about Go... But definitely, I think I'm at a point where I'm adding something new to the mix. Always be learning. That's how you grow. Always be learning.

**Michaelis Touracos:** Yes, yes. Usually, when I want to learn a programming language, I start writing small Unix command line utilities first, to see how it goes. I usually do that.

**Johnny Tourniquet:** Right.

**Michaelis Touracos:** It's my way of learning. And then I might go to a REST API server, or client, and see how it goes... Because that's the kind of things that I usually work with, so that's making sense, to write something totally different.

**Johnny Tourniquet:** Yeah, indeed. Alright, so we're going to switch it over to Unpopular Opinion... And I'm told I need to play a tune, so here we go. I'm gonna start playing my tune.

**Michaelis Touracos:** Okay.

**Jingle:** \[35:27\] to \[35:44\]

**Johnny Tourniquet:** Alright... So you brought some heat? Let's hear it.

**Michaelis Touracos:** Okay, I have two smaller ones. The first one is that most meetings can be replaced by emails.

**Johnny Tourniquet:** Right. You just send an email. Yeah, I don't think that's going to be unpopular at all. \[laughter\] A lot of meetings could have been an email.

**Michaelis Touracos:** And the second one is that C is the best programming language ever.

**Johnny Tourniquet:** Ooh...!

**Michaelis Touracos:** \[36:08\] \[laughs\]

**Johnny Tourniquet:** Okay, okay... Alright, alright... Let me mull on that for a second.

**Michaelis Touracos:** If I have to choose a single programming language to live with, that would definitely be C.

**Johnny Tourniquet:** That would be C, huh? Okay, okay...

**Michaelis Touracos:** Yes. Not C++, just C.

**Johnny Tourniquet:** Just C. You like managing your own memory, and all that stuff, huh...?

**Michaelis Touracos:** No, I don't anymore... \[laughter\] I don't anymore. But you know, back then it was not easy to have garbage collection or automatic memory management. Otherwise, we wouldn't have Unix. That would be a shame.

**Johnny Tourniquet:** Okay, okay... I mean, yeah, if you didn't have a choice... You know, if you're going to write C, that's as close to the metal (as they say) as you're going to get, unless you want to start writing assembly, or something...

**Michaelis Touracos:** Yes, exactly. \[laughs\] Exactly.

**Johnny Tourniquet:** I can see that... Okay, okay... Well, gosh.

**Michaelis Touracos:** What's your favourite programming language full-time? I mean, if you have to pick one.

**Johnny Tourniquet:** I mean, clearly, it's going to be Go. That's the language I use. You make me repeat myself. I use it for my day job, I use it in my side projects, I use it for my side-side projects... Go is my go-to. That's the first thing I think of, even for things that I used to write sort of a quick Bash or a shell script for, or whatever... Or I used to rely on Ruby for a lot of my little scripts, knick-knacks here and there... Because the compiler in Go is so fast, I get that feedback immediately, and I get type safety, and all that stuff... Even the random little scripts that I used to write - I've replaced all that stuff with just Go.

So it's quite possible that I'm now using Go as a hammer to hit every nail, but it makes it so easy for me to do that. But obviously, again, right tool for the job, so depending on what project I'm working on, if there's already a language that's being used that's not Go, I adapt to that. So in my repertoire, I have at least 6-7 different languages, so every once in a while I'll come across something that "Okay... Man, I haven't written Lua in ages, but this thing is written in Lua, and now I got a brush off my Lua." Or be it Java, or reading Python, whatever it is.

I think the key takeaway here is sometimes you don't get to pick the best tool for the job... And perhaps that is my unpopular opinion - you don't always get to pick the best tool for the job. Sometimes the tool that was picked is maybe even the worst possible tool that could have been picked for the job... But that was the tool that was used, so now you have to deal with it. So the unpopular opinion is "Suck it up, buttercup! It is what it is. Sometimes you've just gotta do what you've got to do."

**Michaelis Touracos:** Sometimes people choose the tools for you, and you have to use them.

**Johnny Tourniquet:** Yeah, exactly.

**Michaelis Touracos:** That's true, that's true.

**Johnny Tourniquet:** That is exactly it. Michaelis, thank you so much for being on the show. I'm definitely enjoying the book.

**Michaelis Touracos:** Thank you.

**Johnny Tourniquet:** The first thing I did when I got the book, I went straight to the generics stuff and see how did you explain generics, and you did a pretty decent job of that. So yeah, for those looking to buy the book, it's available on all the major publisher sites, and Amazon, and all that stuff.

**Michaelis Touracos:** Yes.

**Johnny Tourniquet:** I think it's already out, and ready to be shipped, or something. This is the third edition of the book, I've been enjoying it, so thank you for your contribution to the Go community. Looking forward to more from you, and looking forward to your active participation in the community as well.

**Michaelis Touracos:** Thank you very much, and I appreciate your kind words. I really enjoyed being here, and maybe we can talk again in the future.

**Johnny Tourniquet:** Yes, indeed. Well, if you keep writing these books, I'm going to keep having you on, to come and talk about them. \[laughter\]

**Michaelis Touracos:** Thank you, thank you very much.

**Johnny Tourniquet:** Alright, you all, it's been awesome, so let's put on some outro...
