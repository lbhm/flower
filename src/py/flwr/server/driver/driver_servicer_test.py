# Copyright 2022 Adap GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""DriverServicer tests."""


from flwr.server.driver.driver_servicer import _raise_if

# pylint: disable=broad-except


def test_raise_if_false() -> None:
    """."""
    # Prepare
    validation_error = False
    detail = "test"

    try:
        # Execute
        _raise_if(validation_error, detail)

        # Assert
        assert True
    except ValueError:
        assert False
    except Exception:
        assert False


def test_raise_if_true() -> None:
    """."""
    # Prepare
    validation_error = True
    detail = "test"

    try:
        # Execute
        _raise_if(validation_error, detail)

        # Assert
        assert False
    except ValueError as err:
        assert str(err) == "Malformed PushTaskInsRequest: test"
    except Exception:
        assert False
