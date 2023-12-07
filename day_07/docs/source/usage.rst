Quick Start
=============

- To use tests, you need json file of the next format:

.. code-block:: python

    {
      "question": "question",
      "answers": [
        {
          "answer": "first possible answer",
          "value": first value
        },
        {
          "answer": "second possible answer",
          "value": second value
        }
      ]
    }

The **value** is the level of similarity of the answer to human behaviour

- Next step is to write in main function max/min values met in question

.. code-block:: python

    MAX_POINT = 3
    MIN_POINT = 1

Then in the main function define parameters which will be evaluated during answers.
For example:

.. code-block:: python

    etalon = {
      "respiration" : 16,
      "heart rate" : 60,
      "blushing level" : 2,
      "pupillary dilation" : 4
    }

- And then load them into **Params** class:

.. code-block:: python

    params_asker.set_etalon_params(etalon)

Theese params will be filled after each answer and the value related to answer will be corrected in accordance with coefficients.
For this certain task some organism reactions and metrics are choosen. If Reaction is presented and it is more than standart human
state, then answer value increased slightly, otherwise - decreased.

- You can adjust correction to increase impact of reactions on final decision by changing:

.. code-block:: python

    UP_C = 1.1
    DOWN_C = 0.7