say-hello:
	echo "Hello, World!"

lint:
	uv run ruff check .

lint-fix:
	uv run ruff --fix check .
