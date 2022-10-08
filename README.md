# Command Skill

A Simple mycroft skill for running shell scripts and other commands. The commands will run quietly without any confirmation from Mycroft.

## Usage

*Hey Mycroft, launch command echo TEST*

*Hey Mycroft, run script generate report*

## Configuration

This is a very old skill so it uses the now depricated skill config in mycroft.conf. 
The skill can be configured to run scripts from easily pronouncable human utterances, such as "generate report" by adding the following to the `~/.config/mycroft/mycroft.conf`

```json
  "CmdSkill": {
    "alias": {
      "generate report": "/home/forslund/scripts/generate_report.sh",
      "mines": "gnome-mines"
    }
  }
```

The configuration above will launch `/home/forslund/scripts/generate_report.sh` when the an utterance like "run generate report" is heard and lunch the application "gnome-mines" when "run mines" is heard.

(The config needs to be valid json so be careful). The config usually contains a max_allowed_core_version field so make sure commas are placed correctly:
```json
{
  "max_allowed_core_version": 21.2,
  "CmdSkill": {
    [...]
  }
}
```

