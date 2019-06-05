Command Skill
=====================

A Simple mycroft skill for running shell scripts and other commands. The commands will run quietly without any confirmation from Mycroft.

## Usage

*Hey Mycroft, launch command echo TEST*

*Hey Mycroft, run script generate report*

## Configuration

This is a very old skill so it uses the now depricated skill config in mycroft.conf. 
The skill can be configured to run scripts from easily pronouncable human utterances, such as "generate report" by adding the following to the `~/.mycroft/mycroft.conf`

```json
  "CmdSkill": {
      "alias": {
        "generate report": "/home/forslund/scripts/generate_report.sh"
      }
  }
```

(The config needs to be valid json so be careful). The config usually contains a 

The configuration above will launch `/home/forslund/scripts/generate_report.sh` when the second utterance under usage is invoked.
