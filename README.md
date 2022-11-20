# codeSW# 

Code challange for SW

## Getting Started

The process is very simple, if you wish you can create a virtual environment with the dependencies in requirements.txt file.

### Prerequisites

You can just create a virtualenv and execute the python script

```
virtualenv --python=python3 venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```
Script doesnt need any third party library for execution, only pytest for testing.

### Installing

Just get into the folder where script.py is and type:

```
python3 script.py <log file path or folder> <output .json with results> [options:--mflip,--eps,--efip,--bytes]
```

And thats it.

### Docker

There is a docker file with all the stuff needed for a sample run, just type inside the folder (same level as script.py)

```
docker build <image_name> .
docker run -t <image_name>
```
You will have a stdout with results and further instructions to retrieve the .json result from the container.

*Note: You will need to download and provide log file and name it: "access.log" and put it at the same level as script.py in order to dockerfile work.

## Considerations

* Consideration for mflip: only client-ip was evaluated for mflip, code was made such as including target ip would be easy to add to computation.
* Consideration for bytes: only response bytes sum, code was made such as including header bytes would be easy to add to computation.
* Consideration for efip: only client-ip was evaluated for efip, code was made such as including target ip would be easy to add to computation.

## Authors

* **Javier Moubayyed** - [ParserKnight](https://github.com/ParserKnight)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



