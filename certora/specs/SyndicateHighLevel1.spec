using MocksETH as sETHToken

methods {
    //// Regular methods
    totalETHReceived() returns (uint256) envfree
    isKnotRegistered(bytes32) returns (bool) envfree

    //// Resolving external calls
	// stakeHouseUniverse
	stakeHouseKnotInfo(bytes32) returns (address,address,address,uint256,uint256,bool) => DISPATCHER(true)
    memberKnotToStakeHouse(bytes32) returns (address) => DISPATCHER(true) // not used directly by Syndicate
    // stakeHouseRegistry
    getMemberInfo(bytes32) returns (address,uint256,uint16,bool) => DISPATCHER(true) // not used directly by Syndicate
    // slotSettlementRegistry
	stakeHouseShareTokens(address) returns (address)  => DISPATCHER(true)
	currentSlashedAmountOfSLOTForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	numberOfCollateralisedSlotOwnersForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	getCollateralisedOwnerAtIndex(bytes32, uint256) returns (address) => DISPATCHER(true)
	totalUserCollateralisedSLOTBalanceForKnot(address, address, bytes32) returns (uint256) => DISPATCHER(true)
    // sETH
    sETHToken.balanceOf(address) returns (uint256) envfree
    // ERC20
    name()                                returns (string)  => DISPATCHER(true)
    symbol()                              returns (string)  => DISPATCHER(true)
    decimals()                            returns (string) envfree => DISPATCHER(true)
    totalSupply()                         returns (uint256) => DISPATCHER(true)
    balanceOf(address)                    returns (uint256) => DISPATCHER(true)
    allowance(address,address)            returns (uint)    => DISPATCHER(true)
    approve(address,uint256)              returns (bool)    => DISPATCHER(true)
    transfer(address,uint256)             returns (bool)    => DISPATCHER(true)
    transferFrom(address,address,uint256) returns (bool)    => DISPATCHER(true)

    //// Harnessing
    // harnessed variables
    accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32,address) returns (uint256) envfree
    totalETHProcessedPerCollateralizedKnot(bytes32) returns (uint256) envfree
    sETHStakedBalanceForKnot(bytes32,address) returns (uint256) envfree
    sETHTotalStakeForKnot(bytes32) returns (uint256) envfree
    // harnessed functions
    deRegisterKnots(bytes32) 
    deRegisterKnots(bytes32,bytes32)
    stake(bytes32,uint256,address)
    stake(bytes32,bytes32,uint256,uint256,address)
    unstake(address,address,bytes32,uint256)
    unstake(address,address,bytes32,bytes32,uint256,uint256)
    claimAsStaker(address,bytes32)
    claimAsStaker(address,bytes32,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32,bytes32)
    registerKnotsToSyndicate(bytes32)
    registerKnotsToSyndicate(bytes32,bytes32)
    addPriorityStakers(address)
    addPriorityStakers(address,address)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32)

    // added by neumo
    getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32) returns(uint256) envfree
    sETHUserClaimForKnot(bytes32, address) returns(uint256) envfree
    PRECISION() returns(uint256) envfree
    lastAccumulatedETHPerFreeFloatingShare(bytes32) returns(uint256) envfree
    owner() returns (address) envfree
    updatePriorityStakingBlock(uint256)
    accumulatedETHPerFreeFloatingShare() returns(uint256) envfree
    accumulatedETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    isNoLongerPartOfSyndicate(bytes32) returns (bool) envfree
    priorityStakingEndBlock() returns (uint256) envfree
    isPriorityStaker(address) returns (bool) envfree
    lastSeenETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    lastSeenETHPerFreeFloating() returns(uint256) envfree
    calculateETHForFreeFloatingOrCollateralizedHolders() returns(uint256) envfree
    calculateUnclaimedFreeFloatingETHShare(bytes32, address) returns(uint256) envfree
    previewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    getETHBalance(address) returns(uint256) envfree
    batchPreviewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    calculateNewAccumulatedETHPerFreeFloatingShare() returns (uint256) envfree
    batchPreviewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    previewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    getUnprocessedETHForAllFreeFloatingSlot() returns (uint256) envfree
    getUnprocessedETHForAllCollateralizedSlot() returns (uint256) envfree
    numberOfRegisteredKnots() returns (uint256) envfree
    totalFreeFloatingShares() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedSharePerKnot() returns (uint256) envfree
    totalClaimed() returns (uint256) envfree
    calculateCollateralizedETHOwedPerKnot() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedShare(uint256) returns (uint256) envfree
    updateAccruedETHPerShares()
    updateCollateralizedSlotOwnersAccruedETH(bytes32)
    initialize(address, uint256, address, bytes32)
    isInitialized() returns(bool) envfree
}

/// We defined additional functions to get around the complexity of defining dynamic arrays in cvl. We filter them in 
/// normal rules and invariants as they serve no purpose.
definition notHarnessCall(method f) returns bool = 
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    && f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32).selector
    && f.selector != deRegisterKnots(bytes32).selector
    && f.selector != deRegisterKnots(bytes32,bytes32).selector
    && f.selector != stake(bytes32,uint256,address).selector
    && f.selector != stake(bytes32,bytes32,uint256,uint256,address).selector
    && f.selector != unstake(address,address,bytes32,uint256).selector
    && f.selector != unstake(address,address,bytes32,bytes32,uint256,uint256).selector
    && f.selector != claimAsStaker(address,bytes32).selector
    && f.selector != claimAsStaker(address,bytes32,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32,bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32,bytes32).selector
    && f.selector != addPriorityStakers(address).selector
    && f.selector != addPriorityStakers(address,address).selector
    && f.selector != batchPreviewUnclaimedETHAsFreeFloatingStaker(address,bytes32).selector
    && f.selector != getETHBalance(address).selector
    && f.selector != calculateCollateralizedETHOwedPerKnot().selector
    && f.selector != calculateNewAccumulatedETHPerCollateralizedShare(uint256).selector
    && f.selector != getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32).selector
    && f.selector != isInitialized().selector
    && f.selector != initialize(address,uint256,address,bytes32).selector
    && f.selector != getETHBalance(address).selector;


/// Functions with onlyOwner modifier.
definition onlyOwnerFunctions(method f) returns bool = 
    f.selector == deRegisterKnots(bytes32[]).selector
    || f.selector == registerKnotsToSyndicate(bytes32[]).selector
    || f.selector == addPriorityStakers(address[]).selector
    || f.selector == updatePriorityStakingBlock(uint256).selector;


/// Corrollary that can be used as requirement after sETH solvency is proven.
function sETHSolvencyCorrollary(address user1, address user2, bytes32 knot) returns bool {
    return sETHStakedBalanceForKnot(knot,user1) + sETHStakedBalanceForKnot(knot,user2) <= sETHTotalStakeForKnot(knot);
}


/*-------------------------------------------------
|               High level rules                   |
--------------------------------------------------*/

/**
 * Total ETH received must not decrease.
 */
rule totalEthReceivedMonotonicallyIncreases(method f) filtered {
    f -> notHarnessCall(f)
}{
    
    uint256 totalEthReceivedBefore = totalETHReceived();

    env e; calldataarg args;
    f(e, args);

    uint256 totalEthReceivedAfter = totalETHReceived();

    assert totalEthReceivedAfter >= totalEthReceivedBefore, "total ether received must not decrease";
}

/**
 * accumulatedETHPerFreeFloatingShare must not decrease.
 */
rule accumulatedETHPerFreeFloatingShareMonotonicallyIncreases(method f) filtered {
    f -> notHarnessCall(f)
}{
    
    uint256 accumulatedETHPerFreeFloatingShareBefore = accumulatedETHPerFreeFloatingShare();

    env e; calldataarg args;
    f(e, args);

    uint256 accumulatedETHPerFreeFloatingShareAfter = accumulatedETHPerFreeFloatingShare();

    assert accumulatedETHPerFreeFloatingShareAfter >= accumulatedETHPerFreeFloatingShareBefore, "accumulatedETHPerFreeFloatingShare must not decrease";
}

/**
 * accumulatedETHPerCollateralizedSlotPerKnot must not decrease.
 */
rule accumulatedETHPerCollateralizedSlotPerKnotMonotonicallyIncreases(method f) filtered {
    f -> notHarnessCall(f)
}{
    
    uint256 accumulatedETHPerCollateralizedSlotPerKnotBefore = accumulatedETHPerCollateralizedSlotPerKnot();

    env e; calldataarg args;
    f(e, args);

    uint256 accumulatedETHPerCollateralizedSlotPerKnotAfter = accumulatedETHPerCollateralizedSlotPerKnot();

    assert accumulatedETHPerCollateralizedSlotPerKnotAfter >= accumulatedETHPerCollateralizedSlotPerKnotBefore, "accumulatedETHPerCollateralizedSlotPerKnot must not decrease";
}

/**
 * lastSeenETHPerCollateralizedSlotPerKnot must not decrease.
 */
rule lastSeenETHPerCollateralizedSlotPerKnotMonotonicallyIncreases(method f) filtered {
    f -> notHarnessCall(f)
}{
    
    uint256 lastSeenETHPerCollateralizedSlotPerKnotBefore = lastSeenETHPerCollateralizedSlotPerKnot();

    env e; calldataarg args;
    f(e, args);

    uint256 lastSeenETHPerCollateralizedSlotPerKnotAfter = lastSeenETHPerCollateralizedSlotPerKnot();

    assert lastSeenETHPerCollateralizedSlotPerKnotAfter >= lastSeenETHPerCollateralizedSlotPerKnotBefore, "lastSeenETHPerCollateralizedSlotPerKnot must not decrease";
}

/**
 * calculateETHForFreeFloatingOrCollateralizedHolders must be always greater or equal than lastSeenETHPerCollateralizedSlotPerKnot.
 */
rule calculatedETHGTElastSeenETHPerCollateralizedSlotPerKnot(method f) filtered {
    f -> notHarnessCall(f)
}{
    
    uint256 calculateETHForFreeFloatingOrCollateralizedHoldersBefore = calculateETHForFreeFloatingOrCollateralizedHolders();
    uint256 lastSeenETHPerCollateralizedSlotPerKnotBefore = lastSeenETHPerCollateralizedSlotPerKnot();

    require calculateETHForFreeFloatingOrCollateralizedHoldersBefore > lastSeenETHPerCollateralizedSlotPerKnotBefore;

    env e; calldataarg args;
    f(e, args);

    uint256 calculateETHForFreeFloatingOrCollateralizedHoldersAfter = calculateETHForFreeFloatingOrCollateralizedHolders();
    uint256 lastSeenETHPerCollateralizedSlotPerKnotAfter = lastSeenETHPerCollateralizedSlotPerKnot();

    assert calculateETHForFreeFloatingOrCollateralizedHoldersAfter >= lastSeenETHPerCollateralizedSlotPerKnotAfter, "calculateETHForFreeFloatingOrCollateralizedHolders be always greater or equal than lastSeenETHPerCollateralizedSlotPerKnot";
}



/*-------------------------------------------------
|         Invariants, ghosts and hooks             |
--------------------------------------------------*/

/**
 * Address 0 must have zero sETH balance.
 */
invariant addressZeroHasNoBalance()
    sETHToken.balanceOf(0) == 0

/**
 * If knot is no longer part of syndicate, it must be registered
 */
invariant noLongerPartOfSyndicateImpliesRegistered(bytes32 blsPubKey)
    isNoLongerPartOfSyndicate(blsPubKey) => isKnotRegistered(blsPubKey)