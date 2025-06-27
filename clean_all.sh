#!/bin/bash

echo "Stopping and removing containers..."
docker compose down

echo " Cleaning logs and reports..."
rm -rf logs/*
rm -rf crowdsourcing/ue_reports/*

echo "Cleanup complete."
