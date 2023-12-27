from src.rec_system.commands.other_cmds.hello_command import (
    HelloCommandContructor,
)
from src.rec_system.commands.other_cmds.unknown_command import (
    UnknownCommandContructor,
)
from src.rec_system.commands.other_cmds.sos_command import (
    SosCommandContructor,
)
from src.rec_system.commands.other_cmds.for_pleasure_command import (
    ForPleasureCommandContructor,
)

from src.rec_system.commands.strategy_measure_cmds.change_measure_command import (
    ChangeMeasureCommandContructor,
)
from src.rec_system.commands.strategy_measure_cmds.change_strategy_command import (
    ChangeStrategyCommandContructor,
)
from src.rec_system.commands.strategy_measure_cmds.show_measure_command import (
    ShowMeasureCommandContructor,
)
from src.rec_system.commands.strategy_measure_cmds.show_strategy_command import (
    ShowStrategyCommandContructor,
)
from src.rec_system.commands.strategy_measure_cmds.show_possible_measures_command import (
    ShowPossibleMeasuresCommandContructor
)
from src.rec_system.commands.strategy_measure_cmds.show_possible_strategies_command import (
    ShowPossibleStrategiesCommandContructor
)

from src.rec_system.commands.filter_cmds.add_filter_command import (
    AddFilterCommandContructor,
)
from src.rec_system.commands.filter_cmds.add_filter_with_value_command import (
    AddFilterWithValueCommandContructor,
)
from src.rec_system.commands.filter_cmds.filter_value_eq_command import (
    FilterValueEqCommandContructor,
)
from src.rec_system.commands.filter_cmds.reset_filter_command import (
    ResetFilterCommandContructor,
)
from src.rec_system.commands.filter_cmds.show_filters_command import (
    ShowFiltersCommandContructor,
)

from src.rec_system.commands.likes_cmds.hate_only_command import (
    HateOnlyCommandContructor,
)
from src.rec_system.commands.likes_cmds.hate_picturers_command import (
    HatePicturersCommandContructor,
)
from src.rec_system.commands.likes_cmds.hate_writer_command import (
    HateWriterCommandContructor,
)
from src.rec_system.commands.likes_cmds.like_only_command import (
    LikeOnlyCommandContructor,
)
from src.rec_system.commands.likes_cmds.like_writer_command import (
    LikeWriterCommandContructor,
)
from src.rec_system.commands.likes_cmds.not_hate_only_command import (
    NotHateOnlyCommandContructor,
)
from src.rec_system.commands.likes_cmds.not_hate_picturers_command import (
    NotHatePicturersCommandContructor,
)
from src.rec_system.commands.likes_cmds.not_hate_writer_command import (
    NotHateWriterCommandContructor,
)
from src.rec_system.commands.likes_cmds.not_like_only_command import (
    NotLikeOnlyCommandContructor,
)
from src.rec_system.commands.likes_cmds.not_like_writer_command import (
    NotLikeWriterCommandContructor,
)
from src.rec_system.commands.likes_cmds.show_likes_command import (
    ShowLikesCommandContructor,
)
from src.rec_system.commands.likes_cmds.show_dislikes_command import (
    ShowDislikesCommandContructor,
)

from src.rec_system.commands.suggestion_cmds.suggest_something_command import (
    SuggestSomethingCommandContructor,
)
from src.rec_system.commands.suggestion_cmds.show_something_verbose_command import (
    ShowSomethingVerboseCommandContructor
)

from src.rec_system.commands.reset_cmds.reset_history_command import (
    ResetHistoryCommandContructor,
)
from src.rec_system.commands.reset_cmds.reset_session_command import (
    ResetSessionCommandContructor,
)