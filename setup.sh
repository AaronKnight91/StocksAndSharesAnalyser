startdir=$(pwd)

if [ -z $FINANCIALROOT ]; then
    scriptdir=$(dirname $(readlink -f ${BASH_SOURCE[0]:-$0}));
    financialdir=$(readlink -f $scriptdir);
    export FINANCIALROOT="${financialdir}"
fi

FINANCIAL_SRC_DIR=${FINANCIALROOT}

export PYTHONPATH=${FINANCIAL_SRC_DIR}
