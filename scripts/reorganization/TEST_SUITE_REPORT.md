# Full Test Suite Report

**Timestamp:** 2025-10-22T10:13:54.565294

**Return Code:** 3

## Test Statistics

- Passed: 0
- Failed: 0
- Skipped: 0
- Errors: 0

## Test Output

```
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0 -- C:\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\JAMES\bedrock-agentcore-starter-toolkit
configfile: pyproject.toml
plugins: anyio-4.11.0, asyncio-1.2.0, cov-7.0.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 102 items
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 164, in startup
INTERNALERROR>     server = await loop.create_server(
INTERNALERROR>              ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>     ...<5 lines>...
INTERNALERROR>     )
INTERNALERROR>     ^
INTERNALERROR>   File "C:\Python313\Lib\asyncio\base_events.py", line 1622, in create_server
INTERNALERROR>     raise OSError(err.errno, msg) from None
INTERNALERROR> OSError: [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8080): [winerror 10048] only one usage of each socket address (protocol/network address/port) is normally permitted
INTERNALERROR> 
INTERNALERROR> During handling of the above exception, another exception occurred:
INTERNALERROR> 
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 289, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>                          ~~~~^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 342, in _main
INTERNALERROR>     config.hook.pytest_collection(session=session)
INTERNALERROR>     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>     ~~~~~~~~~~~~~~^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\logging.py", line 788, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>     ~~~~~~~~~~~~~~^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\warnings.py", line 99, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>     ~~~~~~~~~~~~~~^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\config\__init__.py", line 1450, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 353, in pytest_collection
INTERNALERROR>     session.perform_collect()
INTERNALERROR>     ~~~~~~~~~~~~~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 813, in perform_collect
INTERNALERROR>     self.items.extend(self.genitems(node))
INTERNALERROR>     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 979, in genitems
INTERNALERROR>     yield from self.genitems(subnode)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 979, in genitems
INTERNALERROR>     yield from self.genitems(subnode)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 979, in genitems
INTERNALERROR>     yield from self.genitems(subnode)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 974, in genitems
INTERNALERROR>     rep, duplicate = self._collect_one_node(node, handle_dupes)
INTERNALERROR>                      ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\main.py", line 839, in _collect_one_node
INTERNALERROR>     rep = collect_one_node(node)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\runner.py", line 567, in collect_one_node
INTERNALERROR>     rep: CollectReport = ihook.pytest_make_collect_report(collector=collector)
INTERNALERROR>                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>     ~~~~~~~~~~~~~~^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\capture.py", line 880, in pytest_make_collect_report
INTERNALERROR>     rep = yield
INTERNALERROR>           ^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\pluggy\_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\runner.py", line 391, in pytest_make_collect_report
INTERNALERROR>     call = CallInfo.from_call(
INTERNALERROR>         collect, "collect", reraise=(KeyboardInterrupt, SystemExit)
INTERNALERROR>     )
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\runner.py", line 344, in from_call
INTERNALERROR>     result: TResult | None = func()
INTERNALERROR>                              ~~~~^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\runner.py", line 389, in collect
INTERNALERROR>     return list(collector.collect())
INTERNALERROR>                 ~~~~~~~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\python.py", line 554, in collect
INTERNALERROR>     self._register_setup_module_fixture()
INTERNALERROR>     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\python.py", line 567, in _register_setup_module_fixture
INTERNALERROR>     self.obj, ("setUpModule", "setup_module")
INTERNALERROR>     ^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\python.py", line 280, in obj
INTERNALERROR>     self._obj = obj = self._getobj()
INTERNALERROR>                       ~~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\python.py", line 551, in _getobj
INTERNALERROR>     return importtestmodule(self.path, self.config)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\python.py", line 498, in importtestmodule
INTERNALERROR>     mod = import_path(
INTERNALERROR>         path,
INTERNALERROR>     ...<2 lines>...
INTERNALERROR>         consider_namespace_packages=config.getini("consider_namespace_packages"),
INTERNALERROR>     )
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\pathlib.py", line 587, in import_path
INTERNALERROR>     importlib.import_module(module_name)
INTERNALERROR>     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Python313\Lib\importlib\__init__.py", line 88, in import_module
INTERNALERROR>     return _bootstrap._gcd_import(name[level:], package, level)
INTERNALERROR>            ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\_pytest\assertion\rewrite.py", line 186, in exec_module
INTERNALERROR>     exec(co, module.__dict__)
INTERNALERROR>     ~~~~^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\bedrock-agentcore-starter-toolkit\tests_integ\memory\test_create_memory.py", line 33, in <module>
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\bedrock_agentcore\runtime\app.py", line 370, in run
INTERNALERROR>     uvicorn.run(self, host=host, port=port, access_log=self.debug, log_level="info" if self.debug else "warning")
INTERNALERROR>     ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\uvicorn\main.py", line 593, in run
INTERNALERROR>     server.run()
INTERNALERROR>     ~~~~~~~~~~^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 67, in run
INTERNALERROR>     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
INTERNALERROR>   File "C:\Python313\Lib\asyncio\runners.py", line 195, in run
INTERNALERROR>     return runner.run(main)
INTERNALERROR>            ~~~~~~~~~~^^^^^^
INTERNALERROR>   File "C:\Python313\Lib\asyncio\runners.py", line 118, in run
INTERNALERROR>     return self._loop.run_until_complete(task)
INTERNALERROR>            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
INTERNALERROR>   File "C:\Python313\Lib\asyncio\base_events.py", line 712, in run_until_complete
INTERNALERROR>     self.run_forever()
INTERNALERROR>     ~~~~~~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Python313\Lib\asyncio\base_events.py", line 683, in run_forever
INTERNALERROR>     self._run_once()
INTERNALERROR>     ~~~~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Python313\Lib\asyncio\base_events.py", line 2042, in _run_once
INTERNALERROR>     handle._run()
INTERNALERROR>     ~~~~~~~~~~~^^
INTERNALERROR>   File "C:\Python313\Lib\asyncio\events.py", line 89, in _run
INTERNALERROR>     self._context.run(self._callback, *self._args)
INTERNALERROR>     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 71, in serve
INTERNALERROR>     await self._serve(sockets)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 86, in _serve
INTERNALERROR>     await self.startup(sockets=sockets)
INTERNALERROR>   File "C:\Users\JAMES\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 174, in startup
INTERNALERROR>     sys.exit(1)
INTERNALERROR>     ~~~~~~~~^^^
INTERNALERROR> SystemExit: 1

============================ 2 warnings in 31.85s =============================


STDERR:
ERROR:    [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8080): [winerror 10048] only one usage of each socket address (protocol/network address/port) is normally permitted
mainloop: caught unexpected SystemExit!

```
