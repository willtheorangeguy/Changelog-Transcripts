**Johnny Tourniquet:** Hello, and welcome to Go Time - the show where a diverse panel and special guests discuss all things Go. My name it Johnny Tourniquet, and joining me today are Mat Ryder and Jon Calhoun, and our special guest, Rama Rao, to talk about the tool that developers are the most intimately familiar with - their editors. How is everybody doing today?

**Mat Ryder:** Hello. I'm very excited for today's show.

**Johnny Tourniquet:** Are you interested in starting wars, maybe?

**Mat Ryder:** No.

**Johnny Tourniquet:** We're not going to do that. There will be no such things on the show today.

**Mat Ryder:** Well, it's an interesting place to start maybe, because people are very opinionated about their editors, aren't they? And they get very tied to them emotionally... I think it's happened since we've had editors. And today, people still use Vim and Emacs for Go. I hear it all the time... So yeah, people love it. And it makes sense, because you spend so much of your time with this application, even though it's basically a text editor. It's hot...

**Johnny Tourniquet:** Whoa, whoa. Just a text editor?! Hang on, hang on; before we get into that, let us allow our special guests to say hi. Hi, Rama. It's good to have you back on the show. How are you doing?

**Rama Rao:** Hello. It's good to be back. I am doing great, and very I'm very interested to hear what Mat had to say... \[laughter\]

**Mat Ryder:** I was just trying to break the ice.

**Rama Rao:** Yeah, the minute he said "I'm so excited for this show..." and I'm like "Well, don't you have to say that for every episode?", because you know, you're here... \[laughter\]

**Johnny Tourniquet:** Oh, but this show... Hm, I don't know.

**Jon Calhoun:** I mean, the thing is he doesn't have to say it for every episode, because he can just not be on the episode.

**Mat Ryder:** I can just say whatever I like.

**Rama Rao:** Oh, right... Got it.

**Mat Ryder:** Yeah, it's awesome.

**Johnny Tourniquet:** \[laughs\] Jon, how have you been?

**Jon Calhoun:** Good, good. I'm excited about this one, too. I think editors are just something that -- I don't know, it shapes how you work on stuff so much that it's fun to talk about and explain how you use them.

**Johnny Tourniquet:** Indeed, indeed.

**Mat Ryder:** Hang on, so Jon can just say the same thing I said, and gets away with it? It was almost verbatim what I said... \[laughter\]

**Johnny Tourniquet:** \[03:53\] Kind of like Vim, and Emacs, you know... You know Vim's better, but you still need to allow Emacs -- hey, I'm kidding, I'm kidding. Let's not start this, let's not start this. Alright, Rama, we had you on the show previously to talk about Go support within VS Code, and [in that episode](https://changelog.com/gotime/49) - I'm blanking on the episode number, but I'm sure our listeners can find it - we talked a little bit about the history of Go support inside of VS Code, the plugin, the development process, how you manage the organization and the open source contributions around that stuff... That's all well and good, and we don't want to rehash that today. But what I would like to know is what have you been up to since then. Are you still doing anything editor-related, or Go-related at Microsoft?

**Rama Rao:** Yeah, sure. I think it's been like two years since that episode, I guess; it was in 2017. And yes, for almost two years (or one-and-a-half years) after that episode I have been very much heavily involved in the Go support and in the Go plugin. It's been a great one or two years after that... But you know, life happens, things change... Recently at Microsoft I moved out from the VS Code team, so the amount of time that I was spending on the Go extension has definitely changed, but my interest and passion and the hope to see it shine more is still the same.

**Johnny Tourniquet:** That's very cool. So who is now the person we bother on Twitter and social media with feature requests and all that good stuff? \[laughter\]

**Mat Ryder:** Great question.

**Rama Rao:** They're hiding, because they don't exist -- it's still me.

**Johnny Tourniquet:** Oh, my goodness... You are carrying that on your back as well. Wow.

**Jon Calhoun:** Do we need to put a Help Wanted ad out for you?

**Rama Rao:** Yes, definitely. I think that's definitely one of the topics we'll be talking about, of how the project and the management has changed over the years, how things are changing, either be it the number of contributors, the kind of contributors, the kind of contributions that have been coming in, the partnerships that I'd like to form moving forward... So yeah, I hope to get to that in the next hour.

**Johnny Tourniquet:** Yeah, we can actually start unpacking that a little bit right now, before we get too deeply into preferences, and things...

**Mat Ryder:** We're not going through all the preferences, are we? \[laughter\] We haven't got time for that.

**Rama Rao:** The last time I was on this call I think 20 minutes went into a customer support thing. I don't want to repeat that. \[laughter\]

**Johnny Tourniquet:** That's true. We were here troubleshooting and telling people how to do things. Okay, so hopefully one of the things that we're going to see land in VS Code - if it hasn't already - is the stable Goals integration inside of VS Code, inside the plugin. I've used it in the past, and it was kind of wonky a little bit, and with each release I saw it getting better and better, and the usability of it improving, and the errors started to go away. What is the state of that? And for those who don't know what Goals is, could you give a brief introduction of what that is and how it's going to make Go work better inside the VS Code plugin?

**Rama Rao:** Sure. The way the Go plugin has been built right now is it makes use of various Go tools that are already existing in the ecosystem. That's how it was originally built way back in November-December of 2015, when [Luke Oban](https://github.com/lukehoban) gave this a try. That's how all editors were providing Go support back then, because we had this rich ecosystem of tools like Gödel, Guru, Goode, for all your needs of code navigation, or code completion and all of those things.

So the way almost every Go plugin for most of the editors were written is it stands in-between the editor and the actual tool. So every time you form a request for "Hey, give me the definition for this symbol", it fires off a request to (say) Gödel, gets the results, parses the results, and then gives it back to the editor in a way it understands.

\[08:04\] So you can imagine this is like a big mishmash of about 5 to 6 different essential tools, and then for all the other fancy features that you want there are extra tools to fill up the gaps, like Go modify tags that will help you update your struct fields, fill struct, which would populate it with default values... So you have all of those things, again, powered by individual tools. And that worked great for the longest of time. And when it stopped working great was recently, in the past two years, because of the changes that were happening in the Go language and the Go command itself.

This has been very beautifully explained by Rebecca in this year's Gopher Con talk. If you've not seen it already, please, please do listen to the talk. I think it's named "[Go, pls stop breaking my editor](https://www.youtube.com/watch?v=EFJfdWzBHwE)."

**Johnny Tourniquet:** Something like that, yeah.

**Rama Rao:** It explains very well how this system of Go support has been, and why the language server can be the solution for most of the problems. The language server - the way it comes into play is it's like a single tool that can handle all of your language requests. So it's the same tool that can provide you navigation requests, the same tool can give you completions, the same tool can figure out if there's error in your code and give you diagnostics... So it's like one single tool for all your problems. But more than that, it is also a backend server, running in the background.

If you compare that to Gödel, which for every single request you try to figure out everything from scratch, versus this thing - the process that's running in your background is watching your files, it knows the state of your files, so there's no need to do all the operations all over again to figure out where is the symbol living, or what should be the completion.

All in all, the language server is Go's solution to most of the language support in editors. Other languages have already had this; that's how most of the VS Code support -- if you think about other languages, they already have a language server. Go is a little late in the game. Once we started figuring out that we can't keep up with the changes in the tooling system and in the Go tool itself, there were attempts at having a language server. Source graph was the first company that attempted to make a language server, and that worked for a while. We provided support to hook up to the Go language servers from Source graph. But then as time went on, as modules came in and that totally shifted the entire paradigm of tooling, they also noticed that they couldn't keep up.

So finally, we had the Go Tools team from Google itself stepping up and saying "Hey, we know, we understand things are breaking. We can provide a language server; this can be a one-place thing to solve most of the problems." That's how the language server started over the last year. Interestingly, it was in Gopher Con - not this year's Gopher Con, but last year's Gopher Con... I remember a group of us - either representing editors, or the Go Tools team, or people from the community - got together and were like "Hey, things are breaking. What do we need to do?" And from that came out this small working group, where we worked closely with Rebecca and Ian from the Go Tools team in getting this language server out.

**Jon Calhoun:** It's interesting hearing about that, because I think -- Sublime Text for a while is what I used with Go; this was a while back... And I think one of the reasons that one died out is I'm pretty sure the person who created that plugin tried to make their own language server... But there was one named Margo, I think -- or maybe that's what it is now. Basically, it ran some Go program in the background, that the actual plugin communicated with, and that's how it did a lot of figuring out with your code...

And I think because they were using their own thing, it became very hard for one person to maintain, and I think it sort of fell behind as a result... Which was disappointing for me, because I was a big fan of Sublime Text for the longest time, and it was what I was used to; I think that's what I liked it. So that led me to trying other stuff, and eventually settling on VS Code... But it'd be nice to have one universal Goals that everybody can integrate with, because that really makes it so that no matter what editor you like, you can still get great support.

**Rama Rao:** \[12:16\] Absolutely. That's one of the big selling points of the language server. You create one language server, and it can now cater to multiple editors... Because the language server protocol itself has been stable and has been onboarded to many, many editors already, so any editor that can support that protocol can hook up to Goals and give you the exact support that you would see in, say, VS Code, or any other editor.

So then, at the end of the day, you won't be judging an editor or choosing an editor for the particular language support it provides, but more for the inherent other features that the editor itself - the language-agnostic things that the editor provides. That would be a world I would love to be in, because if you get completions in a way in one editor, that should be the exact same thing you should get in the other editor. Everybody need not go and keep reinventing the wheel all over again.

**Jon Calhoun:** It's like a weird transition to see that, because I remember when I first started working professionally everybody had their preferred editor, and there were editors specific for whatever language you were using... That was the norm at the time, it felt like. Now, there were people who still used things like Vim and Emacs - I think that always existed - but there were a lot of people who use Eclipse and things like that for Java... And you kind of picked one, and you learned it, and you got so ingrained with it that it was hard to switch at that point. So it's cool that we're getting to a point that that's not the case.

**Johnny Tourniquet:** Well, I don't know about that... What I'm taking away from having that common layer underneath all these editors is that basically there's the undifferentiated heavy-lifting - to use terminology from AWS... Basically, the plumbing, the infrastructure is there, and the editors can just build on top of that. So you're going to get the same autocomplete features, for example, across editors, because that responsibility is sort of being delegated to the running server underneath. Things like "What keyboard shortcuts do you use to trigger certain actions? What does your editor look like? How do you theme it?"

All these extra things that some might consider important, some might consider frivolous (it doesn't matter), these things are left to the implementers/creators of those editors, be they VS Code, or JetBrains-flavoured tools, or whatever you prefer... But that underlying -- this is what the language exposes, this is what the language does, and that's ubiquitous across editors, that's the stuff that drops to the language server.

**Jon Calhoun:** What I meant was -- so I agree with you there, that every editor is going to have some differences; I think that's part of why I don't use Poland - it's not because it's not a good editor, it's because some of the assumptions about your workflow and things like that they make aren't ones that go well with my workflow. So it's not that it's bad, it's that some of the things outside of Go support just aren't what I prefer.

But for a while, I felt like whatever language you went with, you had to go find an editor for that language, one that supported it well. That was more important than half of the other stuff. So you kind of got stuck learning some new setup for the editor, whereas now we're getting to the point where if you're a Vim user, you can pretty much count on most languages having a language server, and you can switch between languages pretty easy because that's there. But if it wasn't, then that becomes much more challenging.

**Rama Rao:** \[15:43\] And I believe that is still the case for certain languages... Because I have heard from people who've been using C\# forever that they'd much rather stick to Visual Studio than go to VS Code, because they still find a big gap. Now, that can be attributed maybe to different things. One, you're used to a particular way of doing things... Now, just because a lightweight editor gives you -- you have to relearn a lot of things, and it's not related to the language, but just workflow, just like what we were just talking about.

So workflows would definitely be tied to the editors. If it just comes to the language support, then language servers can step in and remove that gap for you. The way I tell it to certain people is like, if you think of what you're seeing in your editor, and if you divide it into data versus behaviour, behaviours and interactions are your editors; like what comes directly out of your editors. Data can come from the language server. So it's the data part we would like to reach a world where all editors give you the same set of completions, take you to the same file when you do F12 to try to go to Navigation... And how they do it, how fast they are, or what keyboard shortcut comes out of the box by default, how it looks like, how does the peek window look like - all that is interactions, behaviours, UI. That goes into the editor land, and that's where different editors can do things differently, and you judge editors based on that.

**Jon Calhoun:** Yeah, I can definitely see, like you said, about people not wanting to switch with C\#. I had an exchange with somebody on Twitter at one time when we were basically just coming up with ideas of "This is something I might do with Vim, or Emacs, or something", and they'd be like "This is the problem I'm solving. Here's how I do it in Vim. How would you do this in VS Code, or something else?" And it was funny looking at some of these examples, because I think it really changed -- like, you can either present a problem, and if you get too specific, like "This is exactly what I want to do", then yeah, one might chime better than the other.

But if you just say like "This is the general problem I am solving; I have this text, and I need to change the case of all these certain words", then what I've found was that in Vim a lot of times they think in -- sorry, I guess I'm quiet... But in Vim, a lot of times people think in macros, so they record themselves doing the action once, and then they reapply those macros. But in VS Code, a lot of the times - at least a lot of developers who I'd consider power developers - they think in multi-select. So they select everything they want to edit, and then they just do it all at once. So they're not applying a macro or recording one, because they're just doing it to everything at once.

So it's interesting seeing how those flows differentiate, and then if you try to get somebody to switch from one or the other, it's a complete change in how you think about the problem and tackling it, so it'd be very hard to even compare "Is one better than the other?" It's more just "Which process are you better with?"

**Break:** \[18:37\]

**Johnny Tourniquet:** I find it incredibly hard to - I think you touched on this - to switch to different editors... But I think some of the reasons why I've switched editors... Sometimes I feel like peer pressure has been a part of that process... \[laughter\]

**Rama Rao:** Of all the reasons, I wouldn't have imagined peer pressure to be the reason to switch editors, Johnny, honestly...

**Johnny Tourniquet:** \[19:58\] I mean, seriously... I remember when VS Code was coming out... Back then I was a Sublime user as well, and I think I even tried Atom for a little bit... And those editors had their problems, but I'm like "You know what, I don't want to switch..." And before that I was all Vim, all the time. I'm still Vim, just not all the time.

Anyway, to me there's a switching cost. But what tipped me over the edge - I'd always go to the website, look at the list of features... I'm like, "I'm gonna stick with my editor. Oh, it has that? That's kind of nice though..." You know, I'm pining over these other features, and I'm like "Oh, that'd be nice to be able to do." Then I'd go search within the plugin directory for my editor, and I'm like "Can I do that? Is there something for me to do that in my editor?"

I think a huge part of it - and maybe some developers out there will also agree to that as well - a lot of it is "Okay, what are all my team members using?", or folks that are out there talking about it, what stuff do they use... So you kind of want to feel like you belong a little bit. I think we shouldn't underestimate the impact that peer pressure has on which editor you end up using.

**Jon Calhoun:** Is it peer pressure though? Sorry, I'll let Mat talk in a second...

**Mat Ryder:** No, that's alright.

**Jon Calhoun:** I say that in the sense that yes, you might do it because somebody else is doing it, but it's also beneficial to be able to walk over and ask somebody on your team "How do I do this?" And if you're the only Vim user on your team, and you're just learning it, you're probably going to have a rough time.

**Mat Ryder:** Yeah, it could work the other way as well, where a Vim user might say "How can I get it so that when I press a key it goes into the file?"

**Johnny Tourniquet:** \[laughs\]

**Mat Ryder:** "That's what I really would love. How do I get that?" And then, of course, you see "Oh, VS Code has that feature, so I might switch over." I use VS Code, actually. Rama, I guess I've said this before. Thank you very much for all the work that's been done on it... But genuinely, every time there are updates that have noticeable improvements, it's such a great feeling, and that's multiplied to everyone using it. I get really excited when it's time to update it.

**Rama Rao:** Back when I was in the VS Code team, one of the things -- after every release, we collect feedback, either via email or Twitter, and we see the top things... And it always makes us feel warm and fuzzy inside when we see appreciation for the release notes and all the new features that are coming out... And for a lot of people, it's just pure joy, just reading the release notes every month when it comes out, like "UUP, shiny feature! UUP, I have to try that!" So... Yeah, sorry, but it just reminded me of that.

**Mat Ryder:** Yeah.

**Johnny Tourniquet:** So here's the thing though - if I'm being honest, I've sort of started lagging on reading the release notes, because I found out I just can't keep up with the features anymore. Literally, there are so many things you can do now that I'm like "Okay, I'm going to settle on the 12 keyboard shortcuts that I really use every day", and try to master those. Because to me there's just simply way too much going on. It's all good, and some people are going to find different things more useful than others, but I'm at the point where I'm like "Okay, these are the things I use regularly, on a daily basis. As long as the new stuff doesn't break the things that I use, then I'm good."

**Mat Ryder:** I could do with like a workshop, or something like a Gopher Con you could image, of just -- and you could do it for different editors, but yeah, "Here's VS Code." Do the proper research. Figure out those features, and show them off. Because I'm the same - it does a lot more than I even... I actually asked on Twitter what people's favourite plugins were, and there are some amazing ones... Everything from rainbow brackets, which is when the brackets line up clockwise...

**Johnny Tourniquet:** I've got that one, I've got that one. \[laughter\]

**Jon Calhoun:** That one is fantastic.

**Mat Ryder:** Yeah. So that's why I ask that. There are a few others, too. They're brilliant. And I love the fact that any of us can extend this, as well. We can contribute too if there's something specific. Sometimes you might need something just for your team, and it's not worth sharing, but often I bet if you solve a problem for yourself, you need other people to do it. Do you have to do it in JavaScript though, if you want to write an extension for VS Code?

**Rama Rao:** \[24:14\] Yes. An extension for VS Code has to be in JavaScript, because that's how it can talk to VS Code. So yeah... You can get around that, but... JavaScript is pretty easy, and most of our Getting Started guides, especially around extension authoring - we spent quite some time last year in improving the docs, especially around how to extend VS Code. So we have a lot of samples targeting different parts of the editor on how would you extend it. How would you extend the file explorer? How would you add a new view on the left side, the activity bar? How would you add a status bar item down below? How would you do this, how would you that...? So there are tons of examples already out there.

So if you're someone who's thinking of trying to extend VS Code and might feel that "Oh, but I don't know JavaScript", there are a lot of starting points you can jump off of. There's a lot of scaffolding already involved. So we hope that the time we spent last year \[unintelligible 00:25:11.18\] from the team definitely lowers the barrier into getting an extension for VS Code.

**Jon Calhoun:** I can say from personal experience that it definitely has... Just from what I've seen. Because there was a time period where I felt like you had to be a full-time extension developer to do something more complicated... And it's gotten to the point where you can actually find an example that is close enough to what you want to do that you can start moving in the right direction and actually making progress, and you aren't feeling like "Oh, I have to learn this whole thing all over from the ground up." And it's at that point, which -- or at least the last I checked, it seemed, for the things that I wanted to do, it was... Which was really cool.

**Rama Rao:** Yeah. And even if you don't want to spend too much time on JavaScript, you can always write things in your own language and shell it out... Exactly how the Go extension does. It creates a new child process called Gödel, and it gets back the results, parses it and give it back to VS Code. So you can also choose to keep your JavaScript middle person very light, and do all your heavy-lifting maybe if you want to do it in Go, or any other language that can provide you a command line tool, so you can just shell it out.

**Mat Ryder:** That's a nice idea. That's probably what I'd do if I was going to build that. And I like JavaScript... I just want to say, I like JavaScript. It's common in the Go community to poke fun at it, but I don't. I like it.

**Jon Calhoun:** See, the only thing I dislike about JavaScript is I don't like writing JavaScript the way that I probably should. I write JavaScript more like I write Go code.

**Mat Ryder:** Hm... That's okay.

**Jon Calhoun:** So as long as you're okay with that, I like JavaScript just fine.

**Rama Rao:** Hey, as long as your extension works, I don't think anybody cares... \[laughs\]

**Mat Ryder:** Yeah... But Jon, if you write it in a Go style, then you'll be using a subset probably of JavaScript, I suppose.

**Jon Calhoun:** Oh yeah, I don't use the arrow functions and stuff like that nearly as much as other people do, but I think it's just because it's not what I'm familiar with. I haven't messed with it enough to really get comfortable with all those.

Earlier, Johnny had said that there's like 12 shortcuts that he uses in the editor, and I'm kind of curious if that rings true for you too as well, because I feel like that's -- most people, when I talk with them or watch them actually use their editor, there's all these crazy things the editor can do, and then they use seven of them frequently. That covers 90% of their use case. And I think that's normal, because you're probably not doing weird things all the time... So do you guys think you fall into that category?

**Rama Rao:** When I started in the VS Code team I used to see everybody around me use all the fancy shortcuts, and I just couldn't bring myself to learn them... Because historically, I've never been a keyboard-heavy person. I didn't mind using my mouse, I didn't mind losing out on whatever the 10%-20% speed that you would get by not removing your hand, and moving it two inches... But over time, I did familiarize myself with certain shortcuts, and they've remained with me.

\[28:17\] But since I've changed teams and I now see other people trying to do things, and when I tell them "Hey, you know there's a shortcut, right?" and it just blows their mind... "I didn't know we could do this!" So if I had to share, first I would share those. Symbol search in the current file that you're on, Ctrl+Shift+O. It gives you a dropdown of all the methods and variables in your file.

**Jon Calhoun:** Is that Cmd+R on Mac?

**Rama Rao:** No, it's Cmd+Shift+O.

**Jon Calhoun:** Because CMD+R does something similar, where like if you're in a Go file, it'll show you all the types you've declared.

**Mat Ryder:** I don't have that...

**Jon Calhoun:** Although it's very possible that I've changed the key binding at this point... \[laughter\]

**Mat Ryder:** Great...!

**Jon Calhoun:** So I'm sorry.

**Mat Ryder:** Listeners of this podcast are also going to need your settings file in the show notes then, please.

**Jon Calhoun:** Well, here's the thing... I actually have videos of me setting everything up, and I have exports of all my settings files, so I can actually give that to people.

**Mat Ryder:** That sounds riveting. I'd love to watch that.

**Rama Rao:** Yeah. So I do use Ctrl+Shift+O very often, just to navigate to another method on a very large file... And if you want to do this across file, you have Ctrl’T. That's your entire project, if you want to do a symbol search. Now, based on the language you're using, that might be slow; just a fair warning.

Other than that, I have found Zen mode to be interesting, especially when you're presenting; if you don't want all the clutter showing up on your presentation, you could always go to Zen mode.

Ctrl+B - it was hilarious when the other day I told someone "You know you can use Ctrl+B to just hide that thing?" Because once you're sharing, and then you zoom it, because people who are remote can't see the very small font, and then suddenly you are left with a very big site explorer, and half of your screen is actual text. So Ctrl+B hides that thing for you.

**Mat Ryder:** It's Cmd+B for me, and it's whatever Jon has mapped it to for him. \[laughter\]

**Jon Calhoun:** Are you talking about the entire sidebar, or...?

**Rama Rao:** Yes.

**Jon Calhoun:** I think the very far left little skinny one is Cmd+B for me, and then Cmd+KB is the text files part, which that comes from Sublime Text.

**Rama Rao:** Okay, nobody should listen to Jon.

**Jon Calhoun:** If you install the Sublime text key bindings, you'll probably get something similar to mine, because that's what it was there, and I ported a lot of stuff over.

**Rama Rao:** Oh, okay.

**Mat Ryder:** \[unintelligible 00:30:32.26\]

**Rama Rao:** Yeah, that is an interesting point to keep in mind. I think I talked about this the last time I was here... There are extensions just for key bindings, especially if you're migrating from another editor. We really wanted to make sure that people coming from other editors feel at home, and the keyboard shortcuts that they were so familiar with all over the years, that they didn't have to relearn those things... So we published extensions with the updated key bindings that would match whatever you were using before. I mean, no whatever exactly YOU were using before, but typically in those editors...

**Mat Ryder:** It'd be impossible to know what Jon was using, for example, so... Yeah.

**Rama Rao:** Yeah. Maybe we need an extension called "Jon's key bindings", or something... \[laughter\]

**Mat Ryder:** No.

**Rama Rao:** But yeah... And then I think the last, Ctrl+Backtick, to toggle your terminal is also pretty helpful, because I think most of us do go to the terminal on and off for whatever reason that we want to, and I think Ctrl+Backtick is something that I often use to just slip into the terminal and start working there.

**Johnny Tourniquet:** I have a weird question... Has anybody ever put the terminal in VS Code full-screen, and used Vim inside of it? \[laughter\] Or is that just me?

**Rama Rao:** Is that your confession? \[laughs\]

**Mat Ryder:** \[32:06\] Yeah, it sounded like a confession, didn't it?

**Johnny Tourniquet:** Yeah, I've done that... It wasn't a bad experience at all. It felt wasteful, but...

**Mat Ryder:** And you could fit in with all these peers giving you this pressure to switch...

**Johnny Tourniquet:** I know, "I'm using it though..." \[laughter\]

**Jon Calhoun:** I've got Johnny here doing Vim inside the terminal, and I'm trying to get rid of my terminal altogether inside of VS Code...

**Rama Rao:** Ohh...!

**Jon Calhoun:** The problem is -- so I use iTerm2, and I have a global key binding, so no matter what space I'm on my computer, I can just press the binding and my terminal pops up on my screen... So I've gotten so used to that at this point that it's nearly impossible to break that muscle memory and stop using it... And it's just set up with everything I want, and I don't have to mess around with it at this point. So I could probably learn to like the one in VS Code, but it's one of those... It's probably not worth the effort to learn it.

One of the shortcuts I know is Cmd+Shift+U... It shows one of those windows down at the bottom, but I know if you press it twice it will make that whole window disappear... Because when it pops up randomly, and I don't want it, I have to press it twice to get rid of it real quick...

**Mat Ryder:** Yeah.

**Jon Calhoun:** So it's just weird bindings like that, or ones that I've picked up over time.

**Mat Ryder:** This is what happens... People end up being really superstitious. That's a superstition, Jon, pressing -- what was it? Cmd+Something and U twice? \[laughter\] I don't think it works...

**Jon Calhoun:** Okay, Cmd+Shift+U brings up Output. If you press it again, it gets rid of it. So if the console pops up for some reason, if you press that once, it will switch to that tab, and if you press it a second time, it gets rid of that whole box.

**Rama Rao:** It behaves, I think, as a focus plus toggle. So if it's not already in focus, it gets you to focus, and then once you're in focus, it kind of toggles.

**Jon Calhoun:** It was one of those where I didn't want to learn the key binding for every single tab, I just needed to get rid of it sometimes, and that's just kind of... Because even Rama talks about Zen mode, and it's interesting to me that -- I never use Zen mode. I basically just get rid of my left sidebars with key bindings, and then I use different stuff with my -- basically, I have a window manager tiling, or whatever... And I move things around based on what I'm doing. So what I use more often than that is I'll actually Cmd+Shift+N; that basically gets you a brand new VS Code window. So instead of a new tab, it will get you a whole new window... And then I'll throw that wherever I want it.

Then there's some other key bindings that I tend to use a lot that people probably don't, and this is where the context of what you do matters a lot... So since I record stuff, or I show people what I'm coding a lot, Cmd+Plus and Cmd+Minus, and then I have Cmd+Shift+Plus/Minus... One will just change the text size in my editor, and then the editor (I think it's through an extension) will actually change it so it changes the sidebars, and all the tab menus, and stuff like that... But I think by default all of that zooms with Cmd+Plus/Minus, and you have to use an extension to change it.

I've found that for me, that worked way better, and that was one of the things that I tried Poland for a while and there wasn't an easy way to change the font size, which was kind of rough... Because when you're recording a video and teaching something, you want a big font, so it's easy to watch no matter if they're in standard dev, or something... But then when you go try to code, you don't want size 24 font up on your screen, while you're coding regularly; it's just unbearable sometimes... So it's just little things like that... They're interesting to see.

**Mat Ryder:** Yeah, I've got one... Can I do my ones? So you all know about copy and paste, right? \[laughter\] Because it's brilliant. The other one though, the real one - Ctrl+Minus, where you navigate through the history of where you've been... So if you're clicking around, trying to debug something, and you're going through different files, and you're going through all sorts of rabbit holes, when you then want to go back to where you're being previously, you can do Ctrl and then every time you hit Minus, it jumps back to the last history position, or whatever... I find that to be extremely useful.

**Johnny Tourniquet:** That is neat... I usually just search for a word for where I was...

**Jon Calhoun:** That's a good one. I know one that's Go-specific, that I absolutely love, is go to definition, which for me is Cmd+Option+Down. I think that's the same for everybody...

**Johnny Tourniquet:** \[36:13\] If you had Vim bindings, that's just GD. I'm just saying...

**Jon Calhoun:** Okay... Well, one of the reasons I love that one - and it depends on the language you're in, but in Go I love it because everything is documented in source code... So it's an instant way to jump to documentation, which is absolutely fantastic when you're coding.

And then the second thing I love about it is if you ever want to build an interface, you just jump straight to the function definition of whatever you want to build an interface around, and you just copy it real quick, and then you quickly can build your interface, and you don't have to worry about what are these arguments named; you can actually copy them exactly. So it just makes that type of thing much easier in Go.

**Mat Ryder:** Yeah, that's great.

**Rama Rao:** I have a feeling we're going to confuse all the listeners with all the key bindings...

**Mat Ryder:** Jon will.

**Jon Calhoun:** I will. \[laughter\]

**Rama Rao:** ...especially because each person here has their own extension. Not me, I'm using a default one...

**Mat Ryder:** Me too.

**Jon Calhoun:** So that's why I tried to go with go to definition. That's what it is.

**Rama Rao:** \[laughs\]

**Mat Ryder:** Yeah, and I like when you hover over symbols as well, you get the little pop-up of documentation... I do anyway. Any of that stuff is quite helpful. It's interesting -- Rama, you were talking about the language server having a consistent API. Does that mean that all the languages are similar enough that you can actually represent it in this abstract way?

**Rama Rao:** They are. It's not about whether the languages are similar enough; it's what one would expect out of a language when working in an editor. Any language user would want to go to a definition of a symbol; we go to definition, that Jon just talked about. Any language person would want to hover on a symbol and try to get more information on that symbol, whether it is "What's the signature?" or the documentation on it. Anybody who is typing would like to get some kind of completions based on what they're typing and where that word is in the file... So on and so forth.

There's this whole range of language support features which are applicable to all languages... Which is why we were able to come up with the API, which we called the language server protocol, which has hooks for almost all of such requests and all of such features. We could provide a link in the notes later, but if you look at the protocol, you will see there are a lot. You wouldn't think that there are so many hooks that you could play with, but there are a lot of things which are applicable across languages.

Now, there might be some languages for which something might not be applicable... Then just skip it. But any language, we should be able to be in a state to have a language server that can provide those features for you. Exactly, `go to definition`, `hover`, `completion` - applies to all languages; why shouldn't they?

**Jon Calhoun:** Another one I can think of is viewing where something has been used. I think the references... I don't remember what the shortcut is.

**Rama Rao:** Yes.

**Jon Calhoun:** But seeing that type of thing, like "Where has this class been used?" or "Where is it referenced?" is pretty much universal across any language.

**Rama Rao:** Yeah, finding references, or even giving an interface - well, what implements this interface? Not just where is it referenced, but what implements this interface? The symbol search that I talked about - every file, every language has a particular shape defined to it; there are functions, there are classes, there are interfaces... Everybody has a way of defining them, and the editor gives you a way to show them in a structured format... Whether you call them interface or something else, it's up to the language. But the fact that there is a structure, and you'd like to see the structure is common, regardless of what language you're using.

**Mat Ryder:** \[39:47\] Yeah, it makes sense. I love also some of the features in VC Code that surprise people when you're new to programming, or they're not programmers. Sometimes people look over your shoulder, like "What do you do?" and then they're like "Oh yeah, that's awful. I'm going to go." But before that, what they see are things like Cmd+D for me, which is that select, where you select all the occurrences of a particular piece of text throughout a file. That for me is extremely useful, and it is a variant that selects all within the file as well. That as a trick for just quickly selecting a load of things that you want to do some work on at the same time - I find that to be very useful. I thought it was going to be one of those features that just looks cool, and is a bit of a gimmick, but practically it's not very useful, but it turns out to be very useful... But it does blow people away when they see -- for some reason they think you're smart because you're doing more programming at the same time, you know? \[laughter\]

**Rama Rao:** Yeah... And Cmd+D reminds me of -- I've used it in a slightly... I've extended that. I mean, "extend" is the wrong word to use when there are extensions being talked about. Sorry... So what I've done is in big log files when I want to get rid of noise, and when I know that the noise is in certain lines, having certain words, then I've used Cmd+D or changed all occurrences to select them, and then there's another command that can take you to the end of the line. There's a command that tells "Just move the cursor to the end of the line." And then I could do Shift+Home, or whatever it is, based on whether you're on Windows or Mac, and then just select the entire line and just backspace, and it's gone.

**Mat Ryder:** Yeah.

**Rama Rao:** Of course, there are other ways to do it. You could use regular expressions, and things... But somehow for my lizard brain that's the easiest for me to just get rid of those lines.

**Jon Calhoun:** There are a lot of cool things you can do with that. If you bundle that with extensions, you're going to get an extension that will change case. And then you can, all of a sudden, take your Go fields and turn them into JSON struct tags really easily, and do things like that where you're just changing it to snake case or something... Because for the longest time, I didn't even know about some of the ways you can -- like, I know there are built-in features to make struct tags for you, but I didn't know about them because I was so used to using multiselect that it didn't slow me down enough to actually go learn that other thing.

**Rama Rao:** Yeah. I would definitely recommend trying out the add tags/remove tags command. They are powered by the tool gomodifytags by faith. They're pretty neat, and you could change the setting so that if you prefer camel case versus snake case versus anything, just change the setting for that and you could go to town with that command.

**Johnny Tourniquet:** I have a feeling my next question might take us off this path of shortcuts...

**Mat Ryder:** Oh, I thought \[unintelligible 00:42:39.28\]

**Jon Calhoun:** Let me say one thing then... I will say, Mat, you were saying that it seemed like a gimmick, the multiselect...

**Mat Ryder:** Yeah.

**Jon Calhoun:** And I'll definitely say that you know it's not a gimmick when you're like "I can tell you in Chrome that Cmd+D is the bookmark shortcut." Not because I ever want to bookmark anything; it's because I want a multiselect, and it doesn't work. \[laughter\]

**Mat Ryder:** Yes.

**Johnny Tourniquet:** Funny enough, I think I ran across a Chrome extension which used Vim bindings to navigate Chrome. I tried it, and I was like "Okay, that's a bit much." You'd have to be a really huge fan of Vim to be navigating the web with it.

**Break:** \[43:19\]

**Johnny Tourniquet:** So for the longest time I basically would tell myself that "Okay, you are not a true (to use poor terminology from the recruiting industry) ninja or rock star developer blah-blah-blah until you can completely navigate your editor, gained mastery of it, with Cmd/Ctrl keys, you're just flying through the text...", kind of like how Hollywood tends to portray programmers and "hackers." The screen is just flying by, a 3D cube floating up in the air, and that kind of nonsense... But basically, I used to associate mastery of your craft, your language, whatever you happen to be working on, with how well you're able to navigate your editor, how quick your fingers are. Is it fair to tie your rise of competency as a developer to how fluidly you're able to navigate and get things done in your editor?

**Jon Calhoun:** Before we answer that, can I ask you -- you don't have the 3D City plugin for VS Code?

**Johnny Tourniquet:** No, I -- \[laughter\]

**Rama Rao:** Whoa... What is that?

**Jon Calhoun:** There's none, I don't think, but... If somebody made one that I could fly through a 3D City to find my stuff, my definitions, I'd be like "This is awesome."

**Mat Ryder:** Yeah, we can definitely make that happen. That's a great idea. That's what we want for whenever Go turns up in a movie.

**Johnny Tourniquet:** Right, yeah. 3D navigable city.

**Jon Calhoun:** I mean, I would definitely say that I don't think you're less of a developer if you aren't mastering your tools and memorizing shortcuts... But I think that as you use them, you will just gradually find -- like you said, there's some six or so that you use, and you'll just use them so much that eventually they just start to stick. You don't even have to think about it, you're just pressing those keyboard shortcuts... And I think over time that will happen, but it doesn't make you less of a developer or a junior just because you don't know a bunch of them... Because I've seen very smart people that just program slower, but they can think about hard problems much better than other people, and as a result it doesn't matter if they program slower, they're still going to get the thing done sooner because they're doing all the other stuff better.

**Rama Rao:** Yeah, I totally agree with that... Because I believe our industry, and as software engineers and as problem solvers, there's much more to it than just typing and using an editor. So yeah, I don't believe it makes you any less of a developer, and I totally agree with everything that Jon said. But I would like to also compare this with another analogy, which is personal to me because I have seen it apply to me...

Remember back when you were using either computers or typewriters for the first time, and you had to always look at the keyboard to be able to type?

**Mat Ryder:** Mm-hm...

**Rama Rao:** Right? And you eventually - some of us - are reaching a stage where we don't have to look down at the keyboard to type. Now, this is a very simple thing, but it does give you speed in some shape or way, and then it does take away some of the cognitive efforts you have to put in to see which finger is typing which letter... So I would say knowing keyboard shortcuts and all of these fancy things might give you a small edge, there's no doubt about it, but if you don't have it, it's absolutely fine as well.

**Mat Ryder:** Yeah. The only exception to that is if you don't know how to save a file, you are going to struggle. \[laughter\]

**Rama Rao:** Hey, that's why we have autosaved, right?

**Mat Ryder:** \[48:09\] Oh, we don't even need to. Brilliant. \[laughter\]

**Rama Rao:** So yeah, I would compare that to that. If you feel like typing without looking at the keyboard gives you an advantage, then maybe knowing some shortcuts will give you some advantage as well.

**Mat Ryder:** Yeah, I remember being intimidated in the past when I saw somebody... And I think it was Vim, or one of these. Because I started kind of basic in VS, and I remember ASP.NET and things... And I used to use Notepad to do it, because I was learning it before the tooling was ready, so the only way you could do it that I knew of was Notepad.

**Johnny Tourniquet:** I'm not sure if I should pity you, or be impressed by that... \[laughs\]

**Mat Ryder:** Pity... Pity. And then I saw somebody using Vim, and they were just doing all kinds of stuff that was just mind-blowing, and very intimidating. It did feel like "Okay, so I'm using Notepad here..." I got eight spaces every time I pressed Tab, do you know what I mean? And it's like "Oh, that's too far... It's miles away. Why are you going over there?"

**Johnny Tourniquet:** \[laughs\]

**Mat Ryder:** But yeah... So yes, anyone that feels that, I encourage you, don't worry about that at all, because like Rama said, there's more to it than just typing.

**Rama Rao:** Yes.

**Jon Calhoun:** I mean, there are definitely some things that come with it, but that's definitely -- because I did Java in EDIT, which is like Notepad on Linux, and... Anybody who's done Java knows that you import a lot of stuff, and I basically had to import everything that I needed at the start, so I just had a blanket list of "This is what I import..." And this was for small programs, it was in school, it didn't matter that much... But it was still one of those things that over time you learn better ways to do this stuff. But you still can learn so much and improve as a developer so much without actually needing all that.

**Rama Rao:** So should we move on from keyboard shortcuts?

**Johnny Tourniquet:** Yes, I thought we were-- yeah, let's do that... Okay, fine...

**Jon Calhoun:** Am I allowed to bring up a controversial subject?

**Johnny Tourniquet:** Sure, you've got like five minutes.

**Mat Ryder:** It's not the Middle East again, is it, Jon? \[laughter\]

**Jon Calhoun:** No.

**Mat Ryder:** Good. Because it's really not the right podcast for that.

**Johnny Tourniquet:** \[laughs\]

**Jon Calhoun:** So... Syntax highlighting in colours. What are your opinions on those? And I only say that might be controversial here, because I think Rob Pike is known for not caring for colours... And I don't mean to poke fun at that - everybody has their own preference - but for me at least, I find colours really useful in certain specific situations... Having the keyword fun or some of those colour-coded usually doesn't make a difference to me. But one of the ones that really stands out is if I have a string and all of a sudden part of the string changes colour, I'm like "I did something wrong. I didn't escape a quotation mark, or something." So it's a very clear indicator of "My code is wrong", and that removes that cognitive load of thinking about "Am I doing this right?"

So I'm curious if there are other cases like that you guys can think of, where if you care for colour, syntax highlighting in colours, and stuff like that.

**Rama Rao:** Honestly, I've never thought about it. Whatever the default set of colours are there, they're good. I don't think I ever gave a thought to "Should I go to black and white?"

**Mat Ryder:** Well, Rob Pike also doesn't use a fixed width font, as well. He uses just any font he wants... I assume a good font, not Comic Sans...

**Jon Calhoun:** Not Comic Sans. \[laughs\]

**Mat Ryder:** I doubt it. I'd be impressed if he's written Go in Comic Sans...

**Jon Calhoun:** Maybe it depends on the program he's writing. He's like "This is going to be a fun one. We need a good time." \[laughter\]

**Mat Ryder:** And I suppose if methods are a different colour to functions, and things like that, you could get some of the glues. The strings one is a great example, Jon... Because you're right - if you accidentally escape something, or you're trying to escape it, and it's not changing, it is a clue, and that feedback is dead useful. But otherwise - yeah, it's just what looks good for me. I just want my eyes to be happy while I've got work.

**Johnny Tourniquet:** \[52:07\] I've gone back and forth, but mostly I've stayed with the colour stuff. Honestly, it's really what value you get out of it. I think Jon has a pretty good reason for liking them. For me, I'm at the point where -- I don't know, maybe that's age... I've been looking at code for a long time, and if they're there by default, it's great; I'm okay with them. But if they're not there, I'm still able to navigate the code and whatnot. So yeah, it doesn't say anything about you as a developer if you like them or not...

What I do want to do though, before we start to wrap up the show, is to kind of get an idea from Rama, since she's still pretty much in charge of the direction of Go support inside of VS Code - what's next? Are you just looking for stability at this point, or are you still thinking that there are some significant things that could be added to make the experience better? What are you thinking about, what's next?

**Rama Rao:** I think before modules came into the picture, if somebody had asked me what's next, my answer was always the debugging support. So over the last year we've been chipping apart -- like, adding small improvements here and there. Lots of things have improved in the last year for debugging. My this year's lightning talk at Gopher Con was exactly about that. But generally, that is one area where, as the extension, I would like to put more thought on.

And then, of course, modules came in, and the language server came in, and Rebecca and Ian's team is doing a great job on improving those and making it work really well. So for me, these two would be the two parts to focus on. Since I personally don't do much of the language server work, because it's in Go and there's a whole team behind it, and they know it better than me, I focus more on what I can help to improve the debugging side of things.

There are a couple of partners who are interested in that area, so I work more closely with them, and then I do whatever I can to help Rebecca to get the language server support in. But most of the time I think it is in looking at incoming issues and feature requests, and knowing what makes sense for the extension and what can live as a separate extension.

Initially, in my first year, I would pick up -- anything that can be done, I would do it. I mean, it's programming; you could figure out a way to hack things in and get things done, right? But over time, I also learned "Maybe this can live in a separate extension, and it need not be bundled within this."

So yeah, at the moment it's more about do whatever needs to be done to help the language server gain traction, and help people get onboarded to that, help people report issues, so that it can be fixed... Because that is going to be the future. And on the other hand, see what can be done on the debugging side of things to help out debugging.

**Johnny Tourniquet:** Super. So if somebody wanted to help, perhaps with those initiatives, or others, the best way is to check out the GitHub repository, where all the action happens? ...or is there a better way? Or is that still the primary--

**Rama Rao:** Yes, [the GitHub repo](https://github.com/Microsoft/vscode-go) is the place to go. From the language server perspective I would say everybody please do give it a try. If that doesn't work, for any reason, for your day-to-day work, or your large projects, maybe if you can spend some time of the week or day just trying it out sometimes... Because it's an easy setting to turn it on and off. It's not like you're signing over your life to using the language server.

So give it a try and report - report issues, report what's working, what's not working... Because feedback is the way we can improve things. Especially this Gopher Con, I met so many people who came up to me and said "We love VS Code, but in the last year things have not been that great, things are breaking because of..." "Of course, we understand." "Can you let us know when it'll get back to the way it used to be?"

\[56:09\] So getting back to the way it used to be is by helping the language server become better... And you can do that by trying it out. Even if you don't want to do it five days a week, try it out one day a week, report issues, and together we can make that better. And that will take us back to the lovely place VS Code used to be for Go developers, and then we can focus on other things, like debugging, or snippets... Or even VS Code itself.

The one thing I mentioned last time was VS Code itself is going so fast. We talked about it. Release notes... Every single month so many new things coming out. Part of those new things are also new APIs for language extensions to use and onboard. So once we get off of this basic language support that we are working on with the language server, we can start looking into those fancy things, like code actions, and refactorings; how best to hook into those hooks that VS Code provides. We can focus on that once we get out of the basic language server issues. So there's lots to do, but I think the more immediate step is driving more usage to the language server and reporting issues.

**Mat Ryder:** How do we turn on Goals then, if we use VS Code today? ...for anyone that doesn't know.

**Rama Rao:** Yeah. I'll tell you how, but just in case, if you forget... \[laughs\]

**Mat Ryder:** Google it. Go on Google.

**Rama Rao:** No... \[laughter\] The README on the extension, either on the VS Code Go repo, or even in your extensions; in your extensions view, when you click on the extension, it shows you the README. So that talks about how do you turn it on, why should you turn it on, and all those details. So if you ever want to go back, that has more details.

But in a single line, there's a setting called `use language server` It's a basic true or false setting; so turning it true or false would, of course, turn the language server on and off.

**Mat Ryder:** Is that the same for you, Jon, or have you switched yours around to false and true? \[laughter\]

**Johnny Tourniquet:** Wow...

**Jon Calhoun:** I prefer on and off. They're strings.

**Johnny Tourniquet:** The shade, the shade... \[laughs\]

**Rama Rao:** Yeah... So it will prompt you to reload, because once the extension is activated, it either chooses to use a language server or not. When you make that decision to switch it, it'll ask you to reload the window. But that's how you opt in and opt out There are other settings that can help you diagnose things better. Everything is recorded in the README. We also have a wiki on the repo, so that has a little more interesting facts, if you want to try it out...

So that would be the next thing... If anybody wants to help out, try out the language server, and tell us how it goes.

**Johnny Tourniquet:** Awesome. Thank you so much, Rama, for coming on the show again. It's always a pleasure to have you, and my thanks to my co-hosts, Jon Calhoun, and Mat Ryder. Hopefully, we've sufficiently covered all of Jon's keyboard shortcuts... Or shortcomings... Whatever they may be... \[laughter\]

**Rama Rao:** We have to change the title of this episode...

**Johnny Tourniquet:** To just shortcuts?

**Rama Rao:** It will be like "Shortcuts, and then something about what Rama had to say." \[laughter\]

**Johnny Tourniquet:** Awesome, awesome. Alright, listeners, thank you so much for listening to this show, and we invite you to come back for our next episode. With that, we bid you goodbye.
