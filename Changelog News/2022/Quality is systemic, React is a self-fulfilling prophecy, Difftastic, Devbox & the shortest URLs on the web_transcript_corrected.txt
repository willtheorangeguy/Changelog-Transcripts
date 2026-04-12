**Jerold Santo:**

Top of the muffin to ya

**Elaine Benes:**

[Top of the muffin to you?](https://www.youtube.com/watch?v=_z9NyQnDdz4)

**Jerold Santo:**

I'm Jerold and this is Changelog News for the week of Monday, September 12th 2022.

We have two quick bits of Changelog News before we get to the rest of what's new.

First, I just booked my flight to Raleigh, North Carolina for All Things Open this Fall. Yes, Adam and I will be there in the flesh helping celebrate one of our favourite conference's ten-year anniversary. More info on our involvement coming soon. If you were thinking about attending, now you have one more good reason to do it.

**Ben Still:**

Do it. DO IT!

**Jerold Santo:**

Second, last month I announced we added chapters to each episode page on changelog.com. As promised, we have now brought those same chapters into your podcast app. In fact, you're in a chapter right now. We'll call it: "The chapter about chapters"

**Dom Cobb:**

[Dreams... they feel real while we're in them, right? It's only when we wake up that we realize something was actually strange.](https://youtu.be/KZWxPWa8xOs)

**Jerold Santo:**

Now, if you don't see any chapters in your podcast app of choice, it's possible that app doesn't support the feature. In that case, maybe contact the developers and ask them to add it. Or, try out some other podcast apps that do support chapters. It's a great feature, worth switching.

If your app does support chapters, but you're still not seeing them. There is a chance that we have a bug in our ID3v2 frame generation code. And since I didn't write that code, I'm emotionally OK with that being a real possibility. In that case, please let us know in the comments.

OK, enough Changelog-gazing for now, let's get into the news.

**Break:**

**Jerold Santo:**

First up, Jacob Kaplan-Moss dropped a hot take on software quality. And we picked it up.

**Lil Wayne:**

[Drop it like it's hot, drop it like it's hot.](https://www.youtube.com/watch?v=WpQrAbkM3dI)

**Jerold Santo:**

Jacob says, "Software quality is more the result of a system designed to produce quality, and not so much the result of individual performance. That is: a group of mediocre programmers working with a structure designed to produce quality will produce better software than a group of fantastic programmers working in a system designed with other goals."

He goes on to list out what he means when he says 'software quality', then describes the virtuous cycle between the human and technical factors involved. I'll jump you to the end for two quick conclusions, but you should definitely read Jacob's full post for yourself.

One: "If your team is producing defective code, consider that it may not be because they all suck at their jobs. It’s probably because the environment isn’t allowing them to produce quality software."

Two: "Instead of spending tons of time and effort on hiring because you believe that you can “only hire the best”, direct that effort towards building a system that produces great results out of a wider spectrum of individual performance.""

**Break:**

**Jerold Santo:**

If you don't know Jacob Kaplan-Moss from the Django project, perhaps you remember him from his appearance on The Changelog #479 where we talked principles for hiring engineers. This was one of the most listened to episodes of the year. Here's a clip, in case you missed it:

**Jacob Kaplan-Moss:**

**Jerold Santo:**

If you did miss that one, or you just want to give it another listen, head to changelog.fm/479

**Break:**

**Jerold Santo:**

Fantastic is, the "Fantastic Diff"! Wilfred Hughes always wanted a structural diff tool, so he built fantastic. And he calls it the most fascinating, most frustrating, and most challenging program he's ever written.

How does it differ (see what I did there) from other diff tools? Instead of diffing files line-by-line or character-by-character, fantastic is aware of the syntax of the actual programming languages involved, so it can be much more accurate. For example, fantastic understands nesting, indentation, and line-wrapping. What results are much cleaner results, which are easier for humans to read.

**Scuba Steve:**

[Be nice to the delivery guy, would ya? It's not his fault he can't read!](https://www.youtube.com/watch?v=3PhwiJHnbdM)

**Jerold Santo:**

We will link to Wilfred's blog post where he goes deep on the process of building fantastic, which got a lot of attention last week.

A side-note of interest: we first linked to fantastic back in July 2021, but this blog post was published over a year later and garnered a bunch of attention for the tool. Two takeaways from this fact:

One, follow Changelog News for the freshens. We find cool stuff before it blows up.

Two, if you release something and nobody seems to care, maybe try writing more about it as you have inspiration. Or, as Carl Lange put it years ago when he was writing about having success: "Do things, tell people."

**Christopher Miller:**

"That's a great idea I'm glad I thought of it."

**Break:**

**Jerold Santo:**

Josh Collinsworth knows how to start a flame war. Are you ready? Josh says, "React isn’t great at anything except being popular."

**Russell Crowe:**

[Are you not entertained? Is this not why you are here?](https://www.youtube.com/watch?v=Of_jyeDZ3Sg)

**Jerold Santo:**

OK, let's balance that out before moving on, he also says, "React is good. Even I, a noted and unapologetic React non-fan, readily admit that. Give me a choice between React and no frontend framework at all, and given any project of sufficient size or complexity, I will happily take React, thank you very much."

Now, you've already heard his hot take, so I'm sure you can predict the big "BUT" that follows. Actually, there are a bunch of "buts" that follow.

**Cable Guy:**

**Jerold Santo:**

There’s a lot to unpack in this post. Josh got into the details on the best choice for the job, covering: performance, learning curve, bundle size, scalability, community and support, financial backing, hireability, and developer experience. This post isn't merely a React hater hating on React. There's a lot of thoughtfulness here. Worth a read.

**Break:**

**Jerold Santo:**

Dev box is a command-line tool that lets you easily create isolated shells and containers. You define a list of packages required by your development environment, and Dev box uses that definition to create an isolated environment just for your app. It's built on top of Nix and Docker. But the README assures use we don't have to learn Nix and Docker is only required if you want to create containers. The shell functionality works without it.

Getting started seems pretty easy. After installing Nix, Docker (if you need it), and Dev box itself, run: `dev box unit`

That creates a `dev box.Jason` (sorry jigsawn) in the current directory.

**Douglas Crockford:**

I think you should probably pronounce it 'jigsawn'

**Jerold Santo:**

Then you can add command-line tools from Nix packages, such as `python310`. When you're done, run `dev box shell` and you'll be in a brand-new shell with Python 3.10 installed. Just `exit` when you're finished and you're back to your regular shell.

This tool was first shared by Hammer Sale in the #shipit channel of Changelog's community slack. If you haven't joined our community yet, let's fix that bug. It's high-signal, low-noise, full of nice people, and 100% free. Join today at changelog.com/community. Why not, right?

**Break:**

**Jerold Santo:**

Let's finish up with a fun one, shall we? James Williams set out to find the shortest URLs on the internet. Can you guess what they are?

If you're thinking Google's `g.co` or Facebook's `m.me`, you're close but no cigar. How do you get shorter than that? James says, "there’s nothing stopping TLD registry operators serving A records at the apexes of their TLD zones. For example, if VeriSign (the operator of the com TLD registry) wished, they could add an A record at the apex of the `com` TLD zone – `com` would then resolve to that IP, and your browser would connect to that IP when you visited `https://com`"

With that knowledge in hand, James scanned the internet to see if any registry operators actually do this. And the answer is: yes

One example, if you visit `http://ai` you will hit a retro landing page for "Offshore Information Services", who maintain the `.ai` TLD. Crazy, huh.

**Break:**

**Jerold Santo:**

That's the news for now. We hope you enjoy our new chapters feature. We'll dive into all the details behind it, including the new open source library we had to build to make it a reality, on this week's Kaiden episode of Ship It! That episode will drop into the Ship It! Feed as well as our Master feed on Wednesday.

Have a great week! We'll talk to you again real soon.
