{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOT/6zpmxsUvOOlaUe13Om/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Rehan8894/python-tasks01/blob/main/TASK01.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Task 1: Perform Basic Mathematical Operations\n",
        "# prompt: Problem Statement: Write a Python program that does the following:\n",
        "# 1.  Takes two numbers as input from the user.\n",
        "# 2.  Performs the basic mathematical operations on these two numbers:\n",
        "# o\tAddition\n",
        "# o\tSubtraction\n",
        "# o\tMultiplication\n",
        "# o\tDivision\n",
        "# 3.  Displays the results of each operation on the screen.\n",
        "\n",
        "def calculator():\n",
        "    try:\n",
        "        num1 = float(input(\"Enter the first number: \"))\n",
        "        num2 = float(input(\"Enter the second number: \"))\n",
        "\n",
        "        addition = num1 + num2\n",
        "        subtraction = num1 - num2\n",
        "        multiplication = num1 * num2\n",
        "\n",
        "        if num2 != 0:\n",
        "            division = num1 / num2\n",
        "        else:\n",
        "            division = \"Undefined (division by zero)\"\n",
        "\n",
        "        print(f\"Addition: {num1} + {num2} = {addition}\")\n",
        "        print(f\"Subtraction: {num1} - {num2} = {subtraction}\")\n",
        "        print(f\"Multiplication: {num1} * {num2} = {multiplication}\")\n",
        "        print(f\"Division: {num1} / {num2} = {division}\")\n",
        "\n",
        "    except ValueError:\n",
        "        print(\"Invalid input. Please enter valid numbers.\")\n",
        "\n",
        "calculator()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UtoyiLQjDmYc",
        "outputId": "b11ff42c-704b-4566-fa3f-c7f93025def7"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number: 5\n",
            "Enter the second number: 10\n",
            "Addition: 5.0 + 10.0 = 15.0\n",
            "Subtraction: 5.0 - 10.0 = -5.0\n",
            "Multiplication: 5.0 * 10.0 = 50.0\n",
            "Division: 5.0 / 10.0 = 0.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "b9A-bBAuEZSd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
