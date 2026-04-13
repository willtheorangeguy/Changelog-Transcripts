• Creation of asciinema, a service for recording and playing back terminal sessions
• Early development, initially as a jQuery-based proof of concept
• Recording terminals on different computers, hosting, and embedding playback
• Avoiding screencast limitations, focusing on animating HTML elements to display terminal output
• Terminal emulator development, initially in Ruby, later in Rust, compiled to WebAssembly and embedded in JavaScript player
• Recording process intercepts standard output, not visually recording terminal
• Player reconstructs terminal display from bytes stream, creating a video-like experience
• Resolution independence allows for dynamic scaling of fonts and text in asciinema recordings
• Asciinema uses a JSON-based text format called asciicast to record terminal interactions, which is small in size (around 10 kilobytes per minute)
• The recorder works by creating a pseudoterminal, which intercepts all output and input from the terminal, including keystrokes and mouse events
• Asciinema can record most terminal applications, including Vim, but does not capture images or graphics
• The player mimics the cursor blinking and other visual effects to create a realistic playback experience
• Asciinema files can be copied and pasted from, making it easy to share and reuse terminal interactions
• The recording is optimized to capture only the active interaction, resulting in small file sizes and efficient recording
• Discussion of ascii cinema vs asciinema as a tool for teaching and documenting terminal interactions
• Ability to adjust playback speed and idle time to improve user experience
• Feature to remove pauses and idle moments in recorded sessions
• Possibility to change terminal theme and font after recording
• Potential for further development and expansion of asciinema capabilities
• Discussion of project maintenance and financial stability, including the use of GitHub Sponsors
• Vision for the future of the project and its potential capabilities
• The asciinema project has been a hobby project for 12 years, and while the creator has considered turning it into a business, they've chosen to keep it free and open-source, with support from the community.
• The creator has set up a GitHub Sponsors program to support the project and offers consulting services around it.
• The project's niche audience and the creator's desire to maintain its purity and simplicity have contributed to its decision to remain free and open-source.
• Adding audio support to the project could make it more sustainable, but would also require significant changes and might compromise the project's lean aspect.
• Currently, users can record audio separately and use the project's player with it, but this requires additional coding and hosting.
• Discussion of Blinkenlights, a retro online hack that played Star Wars in a terminal
• Marcin's blog post "Blast from the past" on asciinema's new parser features
• Jerod's suggestion to add audio support to asciinema
• Marcin's response that asciinema can already handle custom parsers for Star Wars asciimation
• Jerod's idea to also add caption/subtitle support to asciinema
• Adam's question about embedding and sharing asciinema recordings, including options for self-hosting and embedding
• Marcin's explanation of asciinema's embedding and sharing options
• Discussion of converting asciicast files to GIF files using AGG, the Asciinema GIF Generator
• AGG (Asciinema GIF Generator) is a tool that converts asciicast files to GIF files in a matter of seconds, with minimal memory usage.
• The tool was written in Rust and is a separate project from asciinema.
• Users can install AGG using Homebrew, Docker, or Podman.
• AGG's functionality is useful for sharing terminal sessions, but it's not built into asciinema by default due to historical and technical reasons.
• AGG can be used as a library in other Rust code, and a web service using AGG as a library generates social media preview cards.
• The asciinema recorder is written in Python and would require significant work to integrate with AGG's Rust code.
• Asciinema and AGG integration
• Recording and replaying terminal sessions
• Exporting recordings as GIFs or MP4s
• Configuration options for recording and playback
• Possibility of a transcript view in the player for a text-based alternative
• Potential feature request for AGG to add a feature for recording stdin
• Marcin Kulik's Agg tool can now accept asciinema.org URLs and automatically download and convert the content to a GIF
• Jerod Santo and Adam Stacoviak test the feature and provide feedback
• The need for updated installation instructions and help documentation for Agg is discussed
• Jerod Santo offers to modify the help message for Agg
• The conversation diverges to discuss Hacktoberfest and the effectiveness of digital rewards
• Marcin Kulik shares his vision for the future of Agg, including obtaining sponsorships to focus on the project full-time
• Marcin Kulik teases an upcoming feature, a live streaming capability for terminal nerds, which will be implemented using Elixir and Rust
• Marcin Kulik discusses the codebase of Asciinema, a tool for live streaming terminal sessions, and mentions that he rewrote it in Go but later returned to Python due to issues with Go packaging.
• Marcin mentions that he is considering rewriting the code in Rust and would need additional resources to dedicate to the project.
• He discusses the importance of corporate sponsors to help fund his work on Asciinema and mentions that individual donations are also welcome.
• Marcin mentions plans to add full-text search to the Asciinema website, which currently hosts over half a million recordings.
• The idea of live streaming terminal sessions to help users discover new concepts and ideas is discussed, and Marcin mentions the need for more time and focus to develop the tool further.
• Adam Stacoviak offers to introduce Marcin to TypeSense, a full-text search solution that may be able to help with the project.
• Discussion of the Pokey Rule and how it was created
• Invitation to join the Matrix room community for further discussion
• Promotion of the project and encouragement to share thoughts and feedback
• Conclusion and thank you from Marcin and the hosts